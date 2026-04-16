"""
装饰器工具集 - Week 3 核心知识点
================================
装饰器(Decorator)是Python最强大的特性之一，本质上是：
  一个函数，接收一个函数作为参数，返回一个新函数
  
语法糖 @decorator 让代码更优雅

本文件包含4个实用的装饰器，每个都展示不同的应用场景和实现技巧：

📚 知识点覆盖:
  ✓ 基础装饰器 (log_execution)
  ✓ 带参数装饰器 (timer)
  ✓ 带参数+保留元信息 (validate_input)
  ✓ 重试机制装饰器 (retry)
  ✓ functools.wraps 的作用
  ✓ *args, **kwargs 的通用包装
"""
import time
import functools
from typing import Any, Callable, Optional, Type


def log_execution(func: Callable) -> Callable:
    """
    🔍 装饰器1：基础日志装饰器（无参数）
    
    功能：在函数执行前后打印日志，记录调用信息
    
    知识点：
      1. 装饰器 = 接收函数 → 定义内部函数(wrapper) → 返回wrapper
      2. *args, **kwargs：接收任意位置参数和关键字参数（通用包装）
      3. functools.wraps：复制原函数的名称、文档字符串等元信息
      
    使用方法：
        @log_execution
        def add_student(name):
            ...
            
    执行效果：
        [LOG] 正在调用 add_student('张三')...
        [LOG] add_student('张三') 执行完毕，耗时 0.001s
    """
    @functools.wraps(func)   # 关键！保留原函数的元信息
    def wrapper(*args, **kwargs):
        # 构建参数显示字符串（用于日志）
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        
        print(f"📝 [LOG] 正在调用 {func.__name__}({signature})...")
        
        start_time = time.time()
        result = func(*args, **kwargs)   # 调用被装饰的原函数
        elapsed = time.time() - start_time
        
        print(f"✅ [LOG] {func.__name__}() 执行完毕，耗时 {elapsed:.4f}s")
        return result
    
    return wrapper


def timer(show_args: bool = True, precision: int = 4) -> Callable:
    """
    ⏱️ 装饰器2：带参数的性能计时器
    
    与 log_execution 不同的是：这个装饰器可以接收参数！
    
    知识点 - 带参数装饰器的"三层嵌套"结构：
        def decorator_factory(parameters):     # 第1层：接收装饰器参数
            def decorator(func):               # 第2层：接收被装饰函数
                @functools.wraps(func)
                def wrapper(*args, **kwargs): # 第3层：接收函数调用参数
                    ...实际逻辑...
                    return result
                return wrapper
            return decorator
        return decorator_factory
    
    当你写 @timer(precision=6) 时，Python 实际执行的是：
        timer(precision=6)(your_function)
    
    参数:
        show_args: 是否在输出中显示调用参数
        precision: 时间精度（小数位数）
        
    使用示例：
        @timer(precision=6)          # 自定义精度
        def slow_function():
            ...
            
        @timer()                     # 使用默认参数
        def fast_function():
            ...
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()  # perf_counter 比 time.time() 更精确
            
            # 调用原函数并计时
            result = func(*args, **kwargs)
            
            elapsed = time.perf_counter() - start_time
            
            # 格式化输出
            if show_args:
                args_str = ", ".join(repr(a) for a in args[:3])  # 只显示前3个参数
                if len(args) > 3 or kwargs:
                    args_str += "..."
                print(f"⏱️ [{func.__name__}({args_str})] 耗时: {elapsed:.{precision}f}s")
            else:
                print(f"⏱️ [{func.__name__}] 耗时: {elapsed:.{precision}f}s")
            
            return result
        return wrapper
    return decorator


def validate_input(**validators) -> Callable:
    """
    ✅ 装饰器3：输入验证装饰器（带动态参数）
    
    最复杂的装饰器之一！根据传入的验证规则自动校验函数参数。
    
    工作原理：
      1. validators 是关键字参数字典，key=参数名, value=验证函数
      2. 调用原函数前，逐个检查指定参数是否通过验证
      3. 任一验证失败则抛出异常，阻止函数执行
    
    知识点：
      - 动态关键字参数 **validators 可以接受任意数量的验证规则
      - 验证函数应该返回 (bool, str) 元组：(是否通过, 错误消息)
      - 结合 inspect 模块可以获取更多参数信息
    
    使用示例：
        # 定义验证函数
        def check_positive(value):
            return (value > 0, f"值必须为正数，当前: {value}")
            
        # 应用装饰器
        @validate_input(score=check_positive, name=lambda v: (len(v)>0, "名字不能为空"))
        def set_score(name, score):
            ...
    
    高级用法 - 用 lambda 快速定义简单验证规则：
        @validate_input(
            student_id=lambda v: bool(re.match(r'^2026\d{4}$', v))),  # noqa
        )
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """
            将位置参数和关键字参数合并后进行验证
            
            知识点：inspect.signature 可以获取函数签名，
                  从而将 args 映射到对应的参数名
            """
            import inspect
            sig = inspect.signature(func)
            bound = sig.bind(*args, **kwargs)   # 将参数绑定到函数签名
            bound.apply_defaults()              # 填充默认值
            
            errors = []
            for param_name, validator in validators.items():
                if param_name in bound.arguments:
                    value = bound.arguments[param_name]
                    
                    # 调用验证函数
                    try:
                        if callable(validator):
                            result = validator(value)
                            
                            # 支持两种验证结果格式：
                            # 格式1: 直接返回 bool
                            # 格式2: 返回 (bool, error_message) 元组
                            if isinstance(result, tuple):
                                is_valid, msg = result
                                if not is_valid:
                                    errors.append(f"  • {param_name}: {msg}")
                            elif not result:
                                errors.append(f"  • {param_name}: 验证失败")
                    except Exception as e:
                        errors.append(f"  • {param_name}: 验证异常 - {e}")
            
            if errors:
                error_msg = f"\n❌ 输入验证未通过 ({func.__name__}):\n" + "\n".join(errors)
                raise ValueError(error_msg)
            
            # 所有验证通过，调用原函数
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry(max_attempts: int = 3, 
           delay: float = 1.0,
           exceptions: tuple = (Exception,),
           on_retry: Optional[Callable] = None) -> Callable:
    """
    🔄 装饰器4：自动重试装饰器
    
    当函数可能因网络/IO等原因临时失败时，自动重试指定次数。
    
    参数:
        max_attempts: 最大尝试次数（含首次）
        delay: 每次重试之间的等待时间（秒）
        exceptions: 需要捕获并重试的异常类型（元组）
        on_retry: 每次重试时的回调函数 retry_num, error → None
        
    知识点：
      - time.sleep(): 让程序暂停指定秒数
      - 异常类型的元组匹配：except (TypeError, ValueError) as e
      - 回调模式：将额外逻辑通过函数参数注入
      
    典型应用场景：
      - 网络请求（可能超时）
      - 文件操作（文件可能被占用）
      - 数据库连接（可能断开）
      
    注意事项：
      - 重试不适用于所有错误（如参数错误、权限不足）
      - 应该只对"可恢复的临时性错误"使用重试
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            
            for attempt in range(1, max_attempts + 1):
                try:
                    if attempt > 1:
                        print(f"🔄 第 {attempt}/{max_attempts} 次重试 {func.__name__}()...")
                        
                    return func(*args, **kwargs)
                    
                except exceptions as e:
                    last_exception = e
                    
                    if attempt < max_attempts:  # 还有剩余重试次数
                        if on_retry:
                            on_retry(attempt, e)
                        time.sleep(delay)
                    else:
                        print(f"❌ {func.__name__}() 在 {max_attempts} 次尝试后仍然失败")
                
            raise last_exception
        return wrapper
    return decorator


# ========== 实际应用示例 ==========

class PermissionManager:
    """权限管理器 - 演示带状态的装饰器"""
    
    def __init__(self):
        self.current_user = "guest"
        self.permissions = {
            "admin": ["add", "delete", "modify", "view", "export"],
            "teacher": ["add", "modify", "view"],
            "student": ["view"],
        }
    
    def require_permission(self, *required_perms: str) -> Callable:
        """
        权限验证装饰器（工厂方法模式）
        
        知识点：装饰器也可以作为类的方法，这样可以使用实例的状态
        """
        def decorator(func: Callable) -> Callable:
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                user_perms = self.permissions.get(self.current_user, [])
                
                missing = [p for p in required_perms if p not in user_perms]
                if missing:
                    print(f"🔒 权限不足！用户 '{self.current_user}' 缺少权限: {missing}")
                    return None
                
                return func(*args, **kwargs)
            return wrapper
        return decorator


# ========== 装饰器组合演示 ==========
def deprecated(reason: str = "", since: str = "") -> Callable:
    """标记已弃用的函数"""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            msg = f"⚠️ 函数 '{func.__name__}' 已弃用"
            if since:
                msg += f" (自版本 {since})"
            if reason:
                msg += f"，原因: {reason}"
            print(msg)
            return func(*args, **kwargs)
        return wrapper
    return decorator


def cache_result(max_size: int = 128) -> Callable:
    """
    简易缓存装饰器（手动实现版）
    
    知识点：闭包 + 字典缓存
    Python标准库中已存在更完善的版本：functools.lru_cache
    这里手动实现是为了理解原理！
    """
    def decorator(func: Callable) -> Callable:
        cache = {}  # 缓存字典（闭包变量）
        cache_info = {"hits": 0, "misses": 0}
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 生成缓存键：参数的不可变表示
            key = (args, frozenset(kwargs.items()))
            
            if key in cache:
                cache_info["hits"] += 1
                return cache[key]
            
            cache_info["misses"] += 1
            result = func(*args, **kwargs)
            
            # LRU淘汰策略（简化版）：超过最大容量则清空
            if len(cache) >= max_size:
                oldest_key = next(iter(cache))
                del cache[oldest_key]
            
            cache[key] = result
            return result
        
        # 暴露缓存统计信息
        wrapper.cache_info = lambda: cache_info.copy()
        wrapper.cache_clear = lambda: cache.clear()
        
        return wrapper
    return decorator
