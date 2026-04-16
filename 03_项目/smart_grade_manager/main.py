"""
🎓 智能学生成绩管理系统 - 主程序入口
=====================================
这是整个项目的入口文件，负责：
  1. 初始化系统组件
  2. 显示主菜单和交互界面
  3. 分发用户操作到对应的处理函数
  4. 管理程序生命周期

📚 知识点覆盖 (Week 1-4 综合实战):
  ✓ 模块导入与项目结构组织
  ✓ 函数定义、调用与参数传递
  ✓ while 循环实现菜单系统
  ✓ if/elif/else 分支处理用户选择
  ✓ 字典映射 (命令分发)
  ✓ try/except 异常处理（用户体验）
  ✓ input() 用户输入获取
  ✓ print() 格式化输出
  ✓ sys.exit() 程序退出
  
运行方式:
    python main.py
"""

import sys
import os

# 确保可以导入同级包（无论从哪个目录运行）
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# 导入业务模块
from models import Student, Gender, StudentNotFoundError, DuplicateStudentError, InvalidScoreError
from services import GradeManager
from utils.formatters import format_title, separator
from utils.validators import validate_student_id, validate_name, validate_score, validate_gender


class Application:
    """
    应用程序类 - 管理整个系统的运行
    
    设计为类的目的是：
      1. 封装全局状态（管理器实例等）
      2. 方法分组（每个功能一个方法）
      3. 方便测试和扩展
    """
    
    # 菜单选项定义（常量，类级别）
    MENU_OPTIONS = [
        ("1", "添加学生", "add_student_ui"),
        ("2", "修改成绩", "modify_scores_ui"),
        ("3", "删除学生", "delete_student_ui"),
        ("4", "成绩统计", "statistics_ui"),
        ("5", "排名查询", "ranking_ui"),
        ("6", "显示全部", "list_all_ui"),
        ("7", "搜索学生", "search_ui"),
        ("8", "导出报告", "export_ui"),
        ("9", "批量导入", "batch_import_ui"),
        ("0", "退出系统", None),
    ]
    
    def __init__(self):
        """初始化应用：创建管理器实例"""
        self.manager = GradeManager()
        self.running = True
    
    # ========== 主循环 ==========
    
    def run(self):
        """应用主入口 - 启动菜单循环"""
        # 显示欢迎界面
        self.show_welcome()
        
        # 主循环
        while self.running:
            try:
                self.show_menu()
                choice = input("\n请选择操作: ").strip()
                self.dispatch(choice)
            except KeyboardInterrupt:
                # Ctrl+C 中断处理
                print("\n\n⚠️ 检测到中断请求...")
                self.handle_exit()
            except Exception as e:
                print(f"\n❌ 发生未预期的错误: {e}")
                print("   如果问题持续存在，请联系开发者")
                input("按回车继续...")
    
    def show_welcome(self):
        """显示欢迎界面"""
        os.system("cls" if os.name == "nt" else "clear")  # 清屏
        
        print(format_title("🎓 智能学生成绩管理系统 v1.0"))
        print("")
        print("  基于 Python 全知识点的实战学习项目")
        print(f"  当前数据: {self.manager.count} 名学生")
        print("")
        print(separator("-", 50))
        print("")
    
    def show_menu(self):
        """显示主菜单"""
        print("╔══════════════════════════════════════╗")
        print("║            📋 功能菜单               ║")
        print("╠══════════════════════════════════════╣")
        
        for code, name, _ in self.MENU_OPTIONS:
            if code == "0":
                print("╠══════════════════════════════════════╣")
            
            emoji = self._get_menu_emoji(code)
            print(f"║  [{code}] {emoji}{name}" + " " * max(0, 24 - len(name) - 2) + "║")
        
        print("╚══════════════════════════════════════╝")
    
    @staticmethod
    def _get_menu_emoji(code: str) -> str:
        """根据菜单项返回对应表情符号"""
        emojis = {
            "1": "➕ ", "2": "✏️  ", "3": "🗑️ ",
            "4": "📊 ", "5": "🏆 ", "6": "📋 ",
            "7": "🔍 ", "8": "💾 ", "9": "📥 ",
            "0": "🚪 ",
        }
        return emojis.get(code, "")
    
    def dispatch(self, choice: str):
        """
        命令分发器 - 根据用户选择调用对应功能
        
        知识点：
          - 字典映射替代大量if/elif
          - getattr() 动态调用方法
          - 默认处理未知命令
        """
        # 查找匹配的菜单项
        handler_name = None
        for code, _, method in self.MENU_OPTIONS:
            if code == choice:
                handler_name = method
                break
        
        if handler_name is None:  # 退出选项
            if choice == "0":
                self.handle_exit()
            else:
                print(f"\n⚠️ 无效的选择: '{choice}'，请输入 0-9 的数字")
        elif handler_name:
            # 动态调用方法
            handler = getattr(self, handler_name, None)
            if handler:
                handler()
            else:
                print(f"\n⚠️ 功能 '{choice}' 正在开发中...")
        else:
            print(f"\n⚠️ 未知命令: '{choice}'")
    
    # ========== 各功能的UI处理方法 ==========
    
    def add_student_ui(self):
        """UI: 添加学生"""
        print("\n" + "━" * 40)
        print("  ➕ 添加新学生")
        print("━" * 40)
        
        # 收集输入（带验证和重试）
        student_id = self._input_with_validation(
            prompt="请输入学号(如20260001): ",
            validator=validate_student_id,
            error_msg="学号格式错误，应为 2026 + 4位数字",
        )
        if not student_id:
            return
        
        name = self._input_with_validation(
            prompt="请输入姓名: ",
            validator=validate_name,
            error_msg="姓名格式错误，请输入2-4个汉字或英文名",
        )
        if not name:
            return
        
        gender_str = self._input_gender()
        if not gender_str:
            return
        
        # 输入各科成绩
        scores = {}
        for subject in ["Python", "数学", "英语"]:
            score_input = self._input_with_validation(
                prompt=f"请输入{subject}成绩(0-100，跳过直接回车): ",
                validator=lambda v: (True, "") if v.strip() == "" else validate_score(v, subject),
                allow_empty=True,
            )
            if score_input and score_input.strip():
                scores[subject] = float(score_input)
        
        # 执行添加
        try:
            student = self.manager.add_student(
                student_id=student_id,
                name=name,
                gender_str=gender_str,
                **scores
            )
            print(f"\n✅ 学生 {student.name}({student.student_id}) 添加成功！")
            print(f"   总分: {student.total_score} | 均分: {student.average_score:.2f} | 等级: {student.grade_level}")
        except DuplicateStudentError as e:
            print(f"\n{e}")
        except ValueError as e:
            print(f"\n❌ 数据验证失败: {e}")
        except Exception as e:
            print(f"\n❌ 添加失败: {e}")
        
        input("\n按回车返回菜单...")
    
    def modify_scores_ui(self):
        """UI: 修改成绩"""
        print("\n" + "━" * 40)
        print("  ✏️ 修改学生成绩")
        print("━" * 40)
        
        student_id = input("请输入要修改的学号: ").strip()
        if not student_id:
            print("已取消")
            return
        
        student = self.manager.find_by_id(student_id)
        if not student:
            print(f"\n❌ 学号 '{student_id}' 不存在")
            input("按回车返回...")
            return
        
        # 显示当前信息
        print(f"\n当前学生: {student.name} ({student.student_id})")
        print(f"当前成绩:")
        for subj in self.manager.subjects:
            current = student.get_score(subj, "--")
            print(f"  {subj}: {current}")
        
        print("\n输入新成绩（直接回车保持原值）:")
        new_scores = {}
        for subject in self.manager.subjects:
            new_val = input(f"  {subject}: ").strip()
            if new_val:
                try:
                    score = float(new_val)
                    ok, err = validate_score(score, subject)
                    if ok:
                        new_scores[subject] = score
                    else:
                        print(f"  ⚠️ {err}，保持原值")
                except ValueError:
                    print(f"  ⚠️ '{new_val}' 不是有效数字，保持原值")
        
        if new_scores:
            updated = self.manager.update_scores(student_id, **new_scores)
            print(f"\n✅ 成绩更新成功!")
            print(f"   新均分: {updated.average_score:.2f} | 新等级: {updated.grade_level}")
        else:
            print("\n未做任何修改")
        
        input("\n按回车返回菜单...")
    
    def delete_student_ui(self):
        """UI: 删除学生"""
        print("\n" + "━" * 40)
        print("  🗑️ 删除学生")
        print("━" * 40)
        
        student_id = input("请输入要删除的学号: ").strip()
        if not student_id:
            print("已取消")
            return
        
        confirm = input(f"确认删除学号为 [{student_id}] 的学生吗？(y/N): ").strip().lower()
        if confirm != "y":
            print("已取消删除")
            input("按回车返回...")
            return
        
        try:
            self.manager.remove_student(student_id)
            print("\n✅ 删除成功")
        except StudentNotFoundError as e:
            print(f"\n{e}")
        
        input("\n按回车返回菜单...")
    
    def statistics_ui(self):
        """UI: 成绩统计"""
        print("\n" + "━" * 40)
        print("  📊 成绩统计")
        print("━" * 40)
        
        stats = self.manager.get_statistics()
        
        if stats.get("total_students", 0) == 0:
            print("\n暂无数据，请先添加学生")
            input("\n按回车返回...")
            return
        
        print(f"\n📝 学生总数: {stats['total_students']} 人")
        print(f"📊 有效记录: {stats['active_students']} 人")
        
        if stats.get("overall_average"):
            print(f"\n📈 总体平均分: {stats['overall_average']:.2f}")
            print(f"🏆 最高总分: {stats['highest_total']:.0f}")
            print(f"📉 最低总分: {stats['lowest_total']:.0f}")
        
        # 各科统计
        if stats.get("subject_stats"):
            print("\n── 各科详情 ──")
            for subj, info in stats["subject_stats"].items():
                bar = self._score_bar(info["average"])
                print(f"  {subj:>6}: 均分{info['average']:6.1f} | "
                      f"最高{info['max']:5.0f} | 最低{info['min']:5.0f} | "
                      f"{info['count']}人 {bar}")
        
        # 等级分布
        if stats.get("grade_distribution"):
            print("\n── 等级分布 ──")
            for level, count in stats["grade_distribution"].items():
                pct = count / stats["active_students"] * 100
                bar = "█" * int(pct / 5) + "░" * (20 - int(pct / 5))
                print(f"  {level:>10}: {count:>3}人 ({pct:>5.1f}%) {bar}")
        
        input("\n按回车返回菜单...")
    
    def ranking_ui(self):
        """UI: 排名查询"""
        print("\n" + "━" * 40)
        print("  🏆 成绩排名")
        print("━" * 40)
        
        print("排序依据: [1]平均分  [2]总分  [3]Python  [4]数学  [5]英语")
        sort_choice = input("选择排序方式(默认=1): ").strip() or "1"
        
        sort_map = {"1": "average", "2": "total", "3": "Python", "4": "数学", "5": "英语"}
        by = sort_map.get(sort_choice, "average")
        
        reverse = input("排序顺序: [1]从高到低  [2]从低到高 (默认=1): ").strip()
        reverse = reverse != "2"
        
        limit_input = input("显示前N名(0=全部，默认=10): ").strip() or "10"
        limit = int(limit_input) if limit_input.isdigit() else 10
        
        ranked = self.manager.get_ranking(by=by, reverse=reverse, limit=limit)
        
        if not ranked:
            print("\n暂无排名数据")
            input("\n按回车返回...")
            return
        
        print(f"\n{'排名':>4} {'学号':>8} {'姓名':>8} {'性别':>4} {'均分':>7} {'总分':>7} {'等级'}")
        print("-" * 55)
        for rank, student in enumerate(ranked, 1):
            medal = self._get_medal(rank)
            print(f"{medal}{rank:>3} {student.student_id:>8} {student.name:>8} "
                  f"{str(student.gender):>4} {student.average_score:>7.2f} "
                  f"{student.total_score:>7.1f} {student.grade_level}")
        
        input("\n按回车返回菜单...")
    
    def list_all_ui(self):
        """UI: 显示所有学生"""
        page = 1
        while True:
            output = self.manager.display_all(page=page)
            print(f"\n{output}")
            
            action = input("\n操作 [n=下一页/p=上一页/q=返回]: ").strip().lower()
            if action == "n":
                page += 1
            elif action == "p":
                page = max(1, page - 1)
            elif action in ("q", ""):
                break
            else:
                break
    
    def search_ui(self):
        """UI: 搜索学生"""
        print("\n" + "━" * 40)
        print("  🔍 搜索学生")
        print("━" * 40)
        
        keyword = input("输入搜索关键词(学号/姓名/科目): ").strip()
        if not keyword:
            print("已取消")
            input("按回车返回...")
            return
        
        results = self.manager.search(keyword)
        
        if results:
            print(f"\n找到 {len(results)} 条结果:\n")
            for s in results:
                print(s.display_summary())
                print("-" * 40)
        else:
            print(f"\n未找到包含 '{keyword}' 的学生")
        
        input("\n按回车返回菜单...")
    
    def export_ui(self):
        """UI: 导出报告"""
        print("\n" + "━" * 40)
        print("  💾 导出报告")
        print("━" * 40)
        
        report = self.manager.export_report()
        print(report)
        
        save_choice = input("\n是否保存到文件？(y/N): ").strip().lower()
        if save_choice == "y":
            filename = input("保存文件名(默认=report.txt): ").strip() or "report.txt"
            filepath = os.path.join(os.path.dirname(__file__), "data", filename)
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(report)
            print(f"\n✅ 报告已保存到: {filepath}")
        
        input("\n按回车返回菜单...")
    
    def batch_import_ui(self):
        """UI: 批量导入示例数据"""
        print("\n" + "━" * 40)
        print("  📥 批量导入示例数据")
        print("━" * 40)
        
        sample_data = [
            {"student_id": "20260001", "name": "张三", "gender": "M", "scores": {"Python": 95, "数学": 88, "英语": 92}},
            {"student_id": "20260002", "name": "李四", "gender": "F", "scores": {"Python": 82, "数学": 95, "英语": 78}},
            {"student_id": "20260003", "name": "王五", "gender": "M", "scores": {"Python": 76, "数学": 62, "英语": 85}},
            {"student_id": "20260004", "name": "赵六", "gender": "F", "scores": {"Python": 91, "数学": 97, "英语": 94}},
            {"student_id": "20260005", "name": "孙七", "gender": "M", "scores": {"Python": 55, "数学": 48, "英语": 52}},
            {"student_id": "20260006", "name": "周八", "gender": "F", "scores": {"Python": 88, "数学": 76, "英语": 81}},
            {"student_id": "20260007", "name": "吴九", "gender": "M", "scores": {"Python": 93, "数学": 89, "英语": 96}},
            {"student_id": "20260008", "name": "郑十", "gender": "F", "scores": {"Python": 67, "数学": 71, "英语": 69}},
        ]
        
        print(f"\n准备导入 {len(sample_data)} 条示例数据...\n")
        
        success_count = 0
        fail_count = 0
        for item in sample_data:
            try:
                self.manager.add_student(**item)
                success_count += 1
                print(f"  ✅ {item['name']} ({item['student_id']})")
            except (DuplicateStudentError, ValueError) as e:
                fail_count += 1
                print(f"  ⚠️ {item.get('name', '?')}: {type(e).__name__}")
        
        print(f"\n导入完成: 成功 {success_count}, 失败 {fail_count}")
        input("\n按回车返回菜单...")
    
    def handle_exit(self):
        """处理退出操作"""
        if self.manager.is_modified:
            choice = input("\n💾 有未保存的更改是否保存? (Y/n): ").strip().lower()
            if choice != "n":
                try:
                    self.manager.save()
                    print("✅ 数据已保存")
                except Exception as e:
                    print(f"❌ 保存失败: {e}")
        
        print("\n感谢使用 🎓 智能学生成绩管理系统！")
        print("祝学习进步！\n")
        self.running = False
    
    # ========== UI辅助工具方法 ==========
    
    @staticmethod
    def _input_with_validation(prompt: str, validator, 
                               error_msg: str = "",
                               max_retries: int = 3,
                               allow_empty: bool = False) -> str:
        """
        带验证的输入函数 - 统一处理用户输入和验证逻辑
        
        参数:
            prompt: 提示文字
            validator: 验证函数，接收值返回 (bool, str) 元组
            error_msg: 自定义错误提示前缀
            max_retries: 最大重试次数
            allow_empty: 是否允许空值
            
        返回:
            验证通过的用户输入字符串，取消时返回 ""
        """
        for attempt in range(max_retries):
            value = input(prompt).strip()
            
            if allow_empty and not value:
                return value
            
            if not value and not allow_empty:
                print(f"  ⚠️ 输入不能为空 ({max_retries - attempt - 1}次机会剩余)")
                continue
            
            is_valid, msg = validator(value)
            if is_valid:
                return value
            else:
                detail = msg if msg else error_msg
                print(f"  ❌ {detail} ({max_retries - attempt - 1}次机会剩余)")
        
        print(f"  ❌ 达到最大尝试次数，已取消此操作")
        return ""
    
    @staticmethod
    def _input_gender() -> str:
        """输入性别并验证"""
        for attempt in range(3):
            value = input("请输入性别(M=男/F=女): ").strip()
            if not value:
                print("  ⚠️ 性别不能为空")
                continue
            
            is_valid, result = validate_gender(value)
            if is_valid:
                return result
            print(f"  ❌ {result}")
        
        return ""  # 默认返回男
    
    @staticmethod
    def _score_bar(average: float, width: int = 15) -> str:
        """生成分数可视化条形图"""
        ratio = min(average / 100, 1.0)
        filled = int(width * ratio)
        empty = width - filled
        
        # 根据分数选择颜色描述
        if average >= 90:
            char = "█"
        elif average >= 70:
            char = "▓"
        elif average >= 60:
            char = "▒"
        else:
            char = "░"
        
        return f"[{char * filled}{('░' * empty)}]"
    
    @staticmethod
    def _get_medal(rank: int) -> str:
        """根据排名返回奖牌表情"""
        if rank == 1:
            return "🥇"
        elif rank == 2:
            return "🥈"
        elif rank == 3:
            return "🥉"
        else:
            return "  "


# ========== 程序入口 ==========

def main():
    """
    程序主入口函数
    
    知识点：
      - if __name__ == "__main__": 的作用
        当文件被直接执行时 __name__ == "__main__"
        当文件被导入为模块时 __name__ == 文件名(不含.py)
      - 这样可以让模块既能被导入又能独立运行
    """
    app = Application()
    app.run()


if __name__ == "__main__":
    main()
