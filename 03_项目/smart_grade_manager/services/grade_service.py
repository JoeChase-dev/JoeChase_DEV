"""
成绩管理服务 - 核心业务逻辑层
=============================
这是整个系统的"大脑"，协调所有模块完成业务功能。

📚 知识点覆盖:
  ✓ 类的设计与封装（管理器模式）
  ✓ 列表/字典/集合的综合运用
  ✓ 排序算法（内置sorted + 自定义key）
  ✓ 过滤/搜索/统计（列表推导 + lambda）
  ✓ 异常处理的分层设计
  ✓ 生成器（yield 实现流式数据）
  ✓ 迭代器协议（__iter__, __next__)
  
设计原则：
  - 单一职责：每个方法只做一件事
  - 开放封闭：通过装饰器扩展行为，不改原有代码
  - 错误早发现：输入验证在操作前完成
"""
from typing import List, Optional, Iterator, Callable
import time

# 导入项目内部模块
from models import Student, Gender, GradeLevel, StudentNotFoundError, DuplicateStudentError
from utils.decorators import log_execution, timer, retry
from utils.validators import validate_student_id, validate_name, validate_score
from utils.file_io import save_to_json, load_from_json
from utils.formatters import format_table, format_progress_bar


class StudentIterator:
    """
    自定义迭代器 - 遍历学生集合
    
    知识点：迭代器协议 = __iter__() + __next__()
          实现 __iter__ 让对象可用于 for 循环
    
    Python的for循环本质：
      for student in iterator:
          等价于：
      it = iter(iterator)
      while True:
          try:
              student = next(it)
          except StopIteration:
              break
    """
    
    def __init__(self, students: List[Student]):
        self._students = students
        self._index = 0
    
    def __iter__(self) -> "StudentIterator":
        """迭代器必须返回自身"""
        return self
    
    def __next__(self) -> Student:
        """返回下一个学生，没有则抛出StopIteration"""
        if self._index >= len(self._students):
            raise StopIteration
        student = self._students[self._index]
        self._index += 1
        return student


class GradeManager:
    """
    学生成绩管理器 - 核心业务类
    
    设计为单例使用方式：整个程序只创建一个实例
    负责所有CRUD操作和数据持久化
    """
    
    def __init__(self, data_file: str = None):
        """
        初始化管理器
        
        参数:
            data_file: 数据文件路径（可选，默认用默认路径）
        """
        self._students: List[Student] = []   # 学生列表（核心数据结构）
        self._data_file = data_file           # 数据文件路径
        self._modified = False                # 是否有未保存的修改
        
        # 启动时加载数据
        self._load_data()
    
    # ========== 属性 ==========
    
    @property
    def count(self) -> int:
        """当前学生总数 (只读属性)"""
        return len(self._students)
    
    @property
    def is_modified(self) -> bool:
        """是否有未保存的修改"""
        return self._modified
    
    @property
    def subjects(self) -> list:
        """获取支持的科目列表"""
        return Student._subjects
    
    # ========== 核心CRUD操作 ==========
    
    @log_execution
    def add_student(self, student_id: str, name: str, 
                    gender_str: str, **scores) -> Student:
        """
        添加新学生
        
        知识点：
          - **scores 接收任意关键字参数作为成绩
          - raise 抛出异常让调用者处理
          
        流程：
          1. 验证输入数据
          2. 检查学号是否重复
          3. 创建Student对象并加入列表
          4. 标记为已修改
        """
        # 步骤1：验证输入
        id_ok, id_err = validate_student_id(student_id)
        if not id_ok:
            raise ValueError(f"学号验证失败: {id_err}")
        
        name_ok, name_err = validate_name(name)
        if not name_ok:
            raise ValueError(f"姓名验证失败: {name_err}")
        
        # 验证各科成绩
        for subject, score in scores.items():
            score_ok, score_err = validate_score(score, subject)
            if not score_ok:
                raise ValueError(score_err)
        
        # 步骤2：检查学号唯一性
        # 知识点：any() 函数 + 生成器表达式做高效判断
        if any(s.student_id == student_id for s in self._students):
            existing = self.find_by_id(student_id)
            raise DuplicateStudentError(
                student_id=student_id,
                name=existing.name if existing else ""
            )
        
        # 步骤3：创建对象
        student = Student(
            student_id=student_id,
            name=name,
            gender=Gender.from_str(gender_str),
            scores={k: float(v) for k, v in scores.items()},
        )
        
        # 步骤4：添加到列表
        self._students.append(student)
        self._modified = True
        
        return student
    
    @log_execution
    def remove_student(self, student_id: str) -> bool:
        """
        按学号删除学生
        
        知识点：
          - enumerate() 同时获取索引和值
          - pop() 按索引删除列表元素
          - next() + 生成器查找目标
        """
        for i, student in enumerate(self._students):
            if student.student_id == student_id:
                removed = self._students.pop(i)
                self._modified = True
                print(f"🗑️ 已删除学生: {removed.name} ({removed.student_id})")
                return True
        
        raise StudentNotFoundError(student_id=student_id)
    
    @log_execution
    def update_scores(self, student_id: str, **new_scores) -> Student:
        """
        更新学生成绩
        
        知识点：
          - find_by_id() 复用已有方法
          - Student.set_score() 带验证的成绩设置
          - 字典解包 **new_scores
        """
        student = self.find_by_id(student_id)
        
        # 更新每科成绩
        for subject, score in new_scores.items():
            score_ok, score_err = validate_score(score, subject)
            if not score_ok:
                raise ValueError(score_err)
            student.set_score(subject, float(score))
        
        self._modified = True
        return student
    
    def find_by_id(self, student_id: str) -> Optional[Student]:
        """
        按学号查找学生
        
        知识点：next() + 生成器的短路求值
               找到第一个匹配项立即返回，不会遍历全部
               
        等价的写法对比：
          写法1（推荐）: next((s for s in students if s.id == target), None)
          写法2:         [s for s in students if s.id == target][0]  # 会遍历全部！
          写法3:         for s in students: if s.id == target: return s
        """
        return next(
            (s for s in self._students if s.student_id == student_id), 
            None
        )
    
    def find_by_name(self, name_keyword: str) -> List[Student]:
        """
        按姓名关键词搜索（模糊匹配）
        
        知识点：
          - in 运算符用于子字符串检查
          - 列表推导式过滤
        """
        keyword = name_keyword.strip().lower()
        return [
            s for s in self._students 
            if keyword in s.name.lower()
        ]
    
    def search(self, keyword: str, by_id: bool = False) -> List[Student]:
        """
        通用搜索接口
        
        知识点：
          - 条件表达式根据参数动态选择搜索策略
          - or 运算符组合两种结果
        """
        results = set()
        
        # 按学号精确匹配
        if by_id:
            student = self.find_by_id(keyword)
            if student:
                results.add(student)
        
        # 按姓名模糊匹配
        name_results = self.find_by_name(keyword)
        results.update(name_results)
        
        # 按科目名搜索（返回有该科目的学生）
        subject_matches = [
            s for s in self._students 
            if any(keyword.lower() in subj.lower() for subj in s.scores.keys())
        ]
        results.update(subject_matches)
        
        return list(results)
    
    # ========== 统计与分析 ==========
    
    @timer(show_args=False)
    def get_statistics(self) -> dict:
        """
        计算全体学生的统计数据
        
        返回包含以下信息的字典:
          - total_students: 总人数
          - subject_stats: 各科平均分、最高分、最低分
          - grade_distribution: 各等级人数分布
          - overall_average: 总体平均分
          
        知识点：
          - 多个列表推导式/生成器的综合运用
          - max/min/sum 内置函数配合 key 参数
          - dict.get() 提供默认值避免KeyError
          - 集合去重
        """
        if not self._students:
            return {"total_students": 0}
        
        # 有成绩的学生（过滤掉没有录入任何成绩的学生）
        active_students = [s for s in self._students if s.scores]
        
        if not active_students:
            return {
                "total_students": self.count,
                "active_students": 0,
                "message": "暂无已录入成绩的学生",
            }
        
        # 各科统计
        subject_stats = {}
        for subject in self.subjects:
            scores_for_subject = [
                s.get_score(subject) 
                for s in active_students 
                if subject in s
            ]
            
            if scores_for_subject:
                subject_stats[subject] = {
                    "average": round(sum(scores_for_subject) / len(scores_for_subject), 2),
                    "max": max(scores_for_subject),
                    "min": min(scores_for_subject),
                    "count": len(scores_for_subject),
                }
        
        # 等级分布 - 用Counter风格的字典计数
        grade_dist = {}
        for s in active_students:
            level = s.grade_level
            grade_dist[level] = grade_dist.get(level, 0) + 1
        
        # 总体平均分
        all_averages = [s.average_score for s in active_students]
        overall_avg = sum(all_averages) / len(all_averages) if all_averages else 0
        
        return {
            "total_students": self.count,
            "active_students": len(active_students),
            "overall_average": round(overall_avg, 2),
            "subject_stats": subject_stats,
            "grade_distribution": {str(k): v for k, v in sorted(grade_dist.items(), key=lambda x: x[0].value)},
            "highest_total": max(s.total_score for s in active_students),
            "lowest_total": min(s.total_score for s in active_students),
        }
    
    def get_ranking(self, by: str = "average", reverse: bool = True, limit: int = 0) -> list:
        """
        成绩排名
        
        参数:
            by: 排序依据 ("average"平均分 / "total"总分 / 某个科目名)
            reverse: True=降序(从高到低), False=升序
            limit: 返回前N名（0=全部）
            
        知识点：
          - sorted() 的 key 参数支持 lambda
          - attrgetter 作为 key（比 lambda 更快）
          - 切片 [:limit] 取前N个
        """
        from operator import attrgetter
        
        # 确定排序依据
        if by == "total":
            sort_key = attrgetter("total_score")
        elif by == "average":
            sort_key = attrgetter("average_score")
        elif by in self.subjects:
            sort_key = lambda s: s.get_score(by, 0)
        else:
            sort_key = attrgetter("average_score")
        
        # 过滤掉没有成绩的学生
        ranked = sorted(
            [s for s in self._students if s.scores],
            key=sort_key,
            reverse=reverse,
        )
        
        # 应用数量限制
        if limit > 0:
            ranked = ranked[:limit]
        
        return ranked
    
    # ========== 生成器与迭代器 ==========
    
    def iter_top_students(self, n: int = 5) -> Iterator[Student]:
        """
        生成器：惰性地逐个返回排名前N的学生
        
        知识点：
          - yield 关键字创建生成器函数
          - 生成器 vs 列表的区别：
            * 列表：一次性生成所有数据，占内存大
            * 生成器：每次yield一个值，按需生成，内存效率高
            
        使用场景：数据量极大时（如100万条记录），
                 用生成器可以逐条处理而不需要一次性加载到内存
        """
        ranking = self.get_ranking(limit=n)
        for i, student in enumerate(ranking, 1):
            # 可以在这里附加额外信息如排名
            yield i, student
    
    def iter_failing_students(self) -> Iterator[Student]:
        """
        生成器：遍历所有不及格学生
        """
        for student in self._students:
            if student.grade_level == GradeLevel.F:
                yield student
    
    def __iter__(self) -> StudentIterator:
        """
        魔术方法：让GradeManager本身可迭代
        
        用法：
          for student in manager:
              print(student.name)
        """
        return StudentIterator(self._students)
    
    # ========== 数据持久化 ==========
    
    def save(self, filepath: str = None) -> bool:
        """保存数据到JSON文件"""
        target_file = filepath or self._data_file
        if not target_file:
            target_file = None
        
        data = [s.to_dict() for s in self._students]
        
        if target_file:
            save_to_json(data, target_file)
        else:
            save_to_json(data)
        
        self._modified = False
        return True
    
    def _load_data(self):
        """启动时从文件加载历史数据"""
        try:
            data_list = load_from_json(self._data_file) if self._data_file else []
            self._students = [
                Student.from_dict(item) 
                for item in data_list
            ]
        except Exception as e:
            print(f"⚠️ 加载数据时出现问题: {e}")
            self._students = []
    
    def export_report(self) -> str:
        """
        导出文本格式的报告
        
        知识点：
          - 大量字符串拼接
          - join() 优化性能（比+号拼接更高效）
          - f-string 嵌套表达式
        """
        lines = []
        lines.append(format_title("📊 学生成绩报告"))
        lines.append("")
        lines.append(f"📅 生成时间: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append(f"📝 学生总数: {self.count}")
        lines.append("")
        
        # 统计摘要
        stats = self.get_statistics()
        if stats.get("total_students", 0) > 0:
            lines.append("--- 📈 统计摘要 ---")
            lines.append(f"  有效人数: {stats.get('active_students', 0)}")
            lines.append(f"  总体均分: {stats.get('overall_average', 0):.2f}")
            
            if stats.get("subject_stats"):
                lines.append("\n  各科情况:")
                for subj, info in stats["subject_stats"].items():
                    lines.append(
                        f"    • {subj}: "
                        f"均分 {info['average']:.1f} | "
                        f"最高 {info['max']:.0f} | "
                        f"最低 {info['min']:.0f}"
                    )
            
            if stats.get("grade_distribution"):
                lines.append("\n  等级分布:")
                for level, count in stats["grade_distribution"].items():
                    bar_len = count * 3  # 简单柱状图
                    lines.append(f"    {level}: {'█' * bar_len} ({count}人)")
        
        lines.append("")
        lines.append("--- 👨‍🎓 学生明细 ---")
        
        # 学生列表表格
        headers = ["学号", "姓名", "性别", "Python", "数学", "英语", "均分", "等级"]
        rows = []
        for student in self.get_ranking():
            rows.append([
                student.student_id,
                student.name,
                str(student.gender),
                str(student.get_score("Python", "--")),
                str(student.get_score("数学", "--")),
                str(student.get_score("英语", "--")),
                f"{student.average_score:.1f}",
                str(student.grade_level),
            ])
        
        lines.append(format_table(headers, rows))
        lines.append("")
        lines.append("=" * 50)
        
        return "\n".join(lines)
    
    # ========== 辅助方法 ==========
    
    def display_all(self, page: int = 1, per_page: int = 10) -> str:
        """分页显示所有学生"""
        from utils.formatters import paginate
        
        paged = paginate(self._students, page, per_page)
        
        result_lines = [
            format_title(f"👨‍🎓 学生列表 (第{paged['page']}/{paged['total_pages']}页)"),
            f"共 {paged['total_items']} 名学生",
            "",
        ]
        
        if paged["items"]:
            headers = ["序号", "学号", "姓名", "性别", "均分", "总分", "等级"]
            rows = []
            base_idx = (page - 1) * per_page
            for idx, student in enumerate(paged["items"], start=base_idx + 1):
                rows.append([
                    str(idx),
                    student.student_id,
                    student.name,
                    str(student.gender),
                    f"{student.average_score:.1f}",
                    f"{student.total_score:.0f}",
                    str(student.grade_level),
                ])
            result_lines.append(format_table(headers, rows))
        else:
            result_lines.append("(暂无学生数据)")
        
        result_lines.append("")
        if paged["has_prev"]:
            result_lines.append(f"  [p] 上一页 | 当前第{page}页")
        if paged["has_next"]:
            result_lines.append(f"  [n] 下一页 | 共{paged['total_pages']}页")
        
        return "\n".join(result_lines)
    
    def clear_all(self) -> int:
        """清空所有数据"""
        count = len(self._students)
        self._students.clear()
        self._modified = True
        return count
