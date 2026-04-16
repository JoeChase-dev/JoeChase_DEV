"""
单元测试 - 验证系统各模块的正确性
================================
测试框架：Python内置 unittest 模块

📚 知识点覆盖:
  ✓ unittest 框架基础 (TestCase, setUp, tearDown)
  ✓ 断言方法 (assertEqual, assertTrue, assertRaises, etc.)
  ✓ 测试用例的组织和命名规范
  ✓ 测试数据准备与清理
  ✓ 异常场景的测试

运行方式:
    python -m pytest tests/test_system.py -v   # 使用pytest（推荐）
    python -m unittest tests.test_system -v     # 使用标准库unittest
"""
import unittest
import sys
import os
import json
import tempfile

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models import (
    Student, Gender, GradeLevel,
    StudentNotFoundError, DuplicateStudentError,
    InvalidScoreError, DataValidationError,
)
from services import GradeManager
from utils.validators import (
    validate_student_id, validate_name, validate_score,
    validate_phone, validate_email, validate_gender,
)
from utils.decorators import timer, log_execution, cache_result
from utils.formatters import format_table, paginate


class TestStudentModel(unittest.TestCase):
    """学生模型单元测试"""
    
    def test_create_student(self):
        """测试创建学生对象"""
        student = Student(
            student_id="20260001",
            name="张三",
            gender=Gender.MALE,
            scores={"Python": 95, "数学": 88, "英语": 92}
        )
        self.assertEqual(student.student_id, "20260001")
        self.assertEqual(student.name, "张三")
        self.assertEqual(student.gender, Gender.MALE)
        self.assertEqual(student.scores["Python"], 95)
    
    def test_total_and_average(self):
        """测试总分和平均分计算"""
        student = Student(
            student_id="20260002",
            name="李四",
            gender=Gender.FEMALE,
            scores={"Python": 80, "数学": 90, "英语": 70}
        )
        self.assertEqual(student.total_score, 240)  # 80+90+70
        self.assertAlmostEqual(student.average_score, 80.0, places=2)
    
    def test_grade_level(self):
        """测试成绩等级判定"""
        # 优秀
        s1 = Student("20260001", "A", Gender.MALE, scores={"Python": 95})
        self.assertEqual(s1.grade_level, GradeLevel.A)
        
        # 良好
        s2 = Student("20260002", "B", Gender.FEMALE, scores={"Python": 85})
        self.assertEqual(s2.grade_level, GradeLevel.B)
        
        # 中等
        s3 = Student("20260003", "C", Gender.MALE, scores={"Python": 75})
        self.assertEqual(s3.grade_level, GradeLevel.C)
        
        # 及格
        s4 = Student("20260004", "D", Gender.FEMALE, scores={"Python": 65})
        self.assertEqual(s4.grade_level, GradeLevel.D)
        
        # 不及格
        s5 = Student("20260005", "F", Gender.MALE, scores={"Python": 45})
        self.assertEqual(s5.grade_level, GradeLevel.F)
    
    def test_invalid_student_id(self):
        """测试无效学号异常"""
        with self.assertRaises(DataValidationError):
            Student(student_id="abc123", name="测试", gender=Gender.MALE)
        
        with self.assertRaises(DataValidationError):
            Student(student_id="20250001", name="测试", gender=Gender.MALE)  # 错误年份
    
    def test_invalid_scores(self):
        """测试无效成绩异常"""
        with self.assertRaises(InvalidScoreError):
            Student(
                student_id="20260001",
                name="测试",
                gender=Gender.MALE,
                scores={"Python": 150}  # 超过100
            )
        
        with self.assertRaises(InvalidScoreError):
            Student(
                student_id="20260002",
                name="测试",
                gender=Gender.FEMALE,
                scores={"数学": -5}  # 负数
            )
    
    def test_magic_methods(self):
        """测试魔术方法"""
        s1 = Student("20260001", "张三", Gender.MALE, scores={"Python": 90})
        s2 = Student("20260002", "李四", Gender.FEMALE, scores={"Python": 95})
        s1_dup = Student("20260001", "重复", Gender.MALE)
        
        # __eq__: 学号相同则相等
        self.assertEqual(s1, s1_dup)
        
        # __lt__: 总分排序
        self.assertTrue(s1 < s2)  # 90 < 95
        
        # __contains__: 科目存在检查
        self.assertTrue("Python" in s1)
        self.assertFalse("数学" in s1)
    
    def test_set_score_with_validation(self):
        """测试带验证的成绩设置"""
        student = Student("20260001", "测试", Gender.MALE)
        
        # 正常设置
        student.set_score("Python", 85)
        self.assertEqual(student.scores["Python"], 85.0)
        
        # 边界值: 0
        student.set_score("数学", 0)
        self.assertEqual(student.scores["数学"], 0.0)
        
        # 边界值: 100
        student.set_score("英语", 100)
        self.assertEqual(student.scores["英语"], 100.0)
        
        # 超范围应抛出异常
        with self.assertRaises(InvalidScoreError):
            student.set_score("物理", 101)


class TestValidators(unittest.TestCase):
    """输入验证模块测试"""
    
    def test_valid_student_ids(self):
        """有效学号"""
        valid_ids = ["20260001", "20269999", "20260000"]
        for sid in valid_ids:
            ok, _ = validate_student_id(sid)
            self.assertTrue(ok, f"{sid} 应该是有效学号")
    
    def test_invalid_student_ids(self):
        """无效学号"""
        invalid_cases = [
            ("", "空字符串"),
            ("abc", "非数字"),
            ("20256001", "错误年份"),
            ("2026001", "长度不足"),
            ("202600001", "超长"),
            ("20260a01", "含字母"),
        ]
        for value, reason in invalid_cases:
            ok, msg = validate_student_id(value)
            self.assertFalse(ok, f"'{value}' ({reason}) 应该是无效学号")
    
    def test_valid_names(self):
        """有效姓名"""
        ok, _ = validate_name("张三")
        self.assertTrue(ok)
        
        ok, _ = validate_name("Alice")
        self.assertTrue(ok)
    
    def test_valid_scores(self):
        """有效成绩"""
        for score in [0, 50, 99.9, 100]:
            ok, _ = validate_score(score)
            self.assertTrue(ok, f"{score} 应该是有效成绩")
    
    def test_invalid_scores(self):
        """无效成绩"""
        for score in [-1, 101, 150, "abc"]:
            ok, msg = validate_score(score)
            self.assertFalse(ok, f"{score} 应该是无效成绩")


class TestGradeManager(unittest.TestCase):
    """成绩管理器集成测试"""
    
    def setUp(self):
        """
        每个测试前执行 - 准备测试数据
        
        知识点：setUp() 用于创建每个测试共享的初始环境
               对应的是 tearDown() 在测试后清理资源
        """
        # 使用临时文件避免影响真实数据
        self.temp_file = tempfile.mktemp(suffix=".json")
        self.manager = GradeManager(data_file=self.temp_file)
        
        # 添加测试数据
        self.manager.add_student("20260001", "张三", "M", Python=95, 数学=88, 英语=92)
        self.manager.add_student("20260002", "李四", "F", Python=82, 数学=95, 英语=78)
        self.manager.add_student("20260003", "王五", "M", Python=55, 数学=48, 英语=52)
    
    def tearDown(self):
        """测试后清理"""
        if os.path.exists(self.temp_file):
            os.remove(self.temp_file)
    
    def test_add_and_count(self):
        """测试添加和计数"""
        self.assertEqual(self.manager.count, 3)
        
        self.manager.add_student("20260004", "赵六", "F", Python=76)
        self.assertEqual(self.manager.count, 4)
    
    def test_duplicate_prevention(self):
        """测试重复学号检测"""
        with self.assertRaises(DuplicateStudentError):
            self.manager.add_student("20260001", "张小三", "M")
    
    def test_find_by_id(self):
        """测试按学号查找"""
        found = self.manager.find_by_id("20260001")
        self.assertIsNotNone(found)
        self.assertEqual(found.name, "张三")
        
        not_found = self.manager.find_by_id("99999999")
        self.assertIsNone(not_found)
    
    def test_search(self):
        """测试搜索功能"""
        results = self.manager.search("张")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "张三")
    
    def test_remove(self):
        """测试删除"""
        initial_count = self.manager.count
        self.manager.remove_student("20260001")
        self.assertEqual(self.manager.count, initial_count - 1)
        
        # 删除不存在的学生应抛出异常
        with self.assertRaises(StudentNotFoundError):
            self.manager.remove_student("99999999")
    
    def test_update_scores(self):
        """测试修改成绩"""
        updated = self.manager.update_scores("20260001", Python=100)
        self.assertEqual(updated.get_score("Python"), 100.0)
        self.assertAlmostEqual(updated.average_score, 93.33, places=2)
    
    def test_ranking(self):
        """测试排名功能"""
        ranked = self.manager.get_ranking(by="total", reverse=True)
        
        # 第一名应该是张三（总分最高：275）
        self.assertEqual(ranked[0].name, "张三")
        self.assertEqual(ranked[-1].name, "王五")  # 最后一名
    
    def test_statistics(self):
        """测试统计功能"""
        stats = self.manager.get_statistics()
        
        self.assertEqual(stats["total_students"], 3)
        self.assertIn("subject_stats", stats)
        self.assertIn("grade_distribution", stats)
        self.assertGreater(stats["overall_average"], 0)
    
    def test_iterator(self):
        """测试迭代器协议"""
        collected = list(self.manager)
        self.assertEqual(len(collected), 3)
    
    def test_generator(self):
        """测试生成器"""
        top_students = list(self.manager.iter_top_students(n=2))
        self.assertEqual(len(top_students), 2)
        
        # 验证返回格式是 (rank, student) 元组
        rank, student = top_students[0]
        self.assertIsInstance(rank, int)
        self.assertIsInstance(student, Student)


class TestDecorators(unittest.TestCase):
    """装饰器模块测试"""
    
    def test_timer_decorator(self):
        """测试计时装饰器"""
        @timer(show_args=False)
        def slow_func():
            import time
            time.sleep(0.05)
            return 42
        
        result = slow_func()
        self.assertEqual(result, 42)
    
    def test_cache_decorator(self):
        """测试缓存装饰器"""
        call_count = [0]
        
        @cache_result(max_size=10)
        def expensive_computation(x):
            call_count[0] += 1
            return x * x
        
        # 第一次调用应该执行函数
        r1 = expensive_computation(5)
        self.assertEqual(call_count[0], 1)
        self.assertEqual(r1, 25)
        
        # 第二次调用相同参数应该命中缓存
        r2 = expensive_computation(5)
        self.assertEqual(call_count[0], 1)  # 不应增加
        self.assertEqual(r2, 25)
        
        # 不同参数应该重新计算
        r3 = expensive_computation(10)
        self.assertEqual(call_count[0], 2)
        self.assertEqual(r3, 100)


class TestFormatters(unittest.TestCase):
    """格式化工具测试"""
    
    def test_format_table(self):
        """测试表格生成"""
        headers = ["Name", "Score"]
        rows = [["Alice", 95], ["Bob", 87]]
        
        table = format_table(headers, rows)
        self.assertIn("Alice", table)
        self.assertIn("Bob", table)
        self.assertIn("95", table)
    
    def test_paginate(self):
        """测试分页"""
        items = list(range(25))  # 25个项目
        
        p1 = paginate(items, page=1, per_page=10)
        self.assertEqual(len(p1["items"]), 10)
        self.assertTrue(p1["has_next"])
        self.assertFalse(p1["has_prev"])
        
        p3 = paginate(items, page=3, per_page=10)
        self.assertEqual(len(p3["items"]), 5)
        self.assertFalse(p3["has_next"])
        self.assertTrue(p3["has_prev"])


class TestEnum(unittest.TestCase):
    """枚举类测试"""
    
    def test_gender_enum(self):
        """性别枚举"""
        male = Gender.from_str("M")
        self.assertEqual(male, Gender.MALE)
        
        female = Gender.from_str("f")  # 大小写不敏感
        self.assertEqual(female, Gender.FEMALE)
        
        with self.assertRaises(ValueError):
            Gender.from_str("X")  # 无效值
    
    def test_gender_str(self):
        """性别字符串表示"""
        self.assertEqual(str(Gender.MALE), "男")
        self.assertEqual(str(Gender.FEMALE), "女")
    
    def test_grade_level_passing(self):
        """等级是否及格"""
        self.assertTrue(GradeLevel.A.is_passing)
        self.assertTrue(GradeLevel.B.is_passing)
        self.assertTrue(GradeLevel.C.is_passing)
        self.assertTrue(GradeLevel.D.is_passing)
        self.assertFalse(GradeLevel.F.is_passing)


class TestSerialization(unittest.TestCase):
    """序列化/反序列化测试"""
    
    def test_to_dict_roundtrip(self):
        """测试字典转换往返一致性"""
        original = Student(
            student_id="20260042",
            name="序列化测试",
            gender=Gender.FEMALE,
            scores={"Python": 88, "数学": 77}
        )
        
        # 序列化为字典
        data_dict = original.to_dict()
        self.assertEqual(data_dict["student_id"], "20260042")
        self.assertEqual(data_dict["gender"], "F")  # 枚举转value
        
        # 反序列化为对象
        restored = Student.from_dict(data_dict)
        self.assertEqual(restored, original)  # __eq__ 比较
        self.assertEqual(restored.total_score, original.total_score)


# ========== 运行测试 ==========

if __name__ == "__main__":
    print("=" * 60)
    print("🧪 运行智能学生成绩管理系统 - 单元测试")
    print("=" * 60)
    unittest.main(verbosity=2)
