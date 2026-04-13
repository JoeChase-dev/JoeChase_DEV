"""
罗马数字转整数
LeetCode 13
"""


def roman_to_int(s: str) -> int:
    """
    将罗马数字转换为整数
    
    参数:
        s: 罗马数字字符串
        
    返回:
        对应的整数值
    """
    # 罗马数字字符映射表
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    result = 0
    n = len(s)
    
    for i in range(n):
        # 如果当前字符的值小于下一个字符的值，则减去当前值
        # 否则加上当前值
        if i < n - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
            result -= roman_map[s[i]]
        else:
            result += roman_map[s[i]]
    
    return result


def roman_to_int_v2(s: str) -> int:
    """
    另一种实现方式：从右向左遍历
    """
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    result = 0
    prev_value = 0
    
    # 从右向左遍历
    for char in reversed(s):
        current_value = roman_map[char]
        
        # 如果当前值小于前一个值，则减去
        if current_value < prev_value:
            result -= current_value
        else:
            result += current_value
        
        prev_value = current_value
    
    return result


# 测试代码
if __name__ == "__main__":
    # 测试用例
    test_cases = [
        ("III", 3),
        ("IV", 4),
        ("IX", 9),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
        ("XL", 40),
        ("XC", 90),
        ("CD", 400),
        ("CM", 900),
        ("MMMCMXCIX", 3999)  # 最大罗马数字
    ]
    
    print("方法一：从左向右遍历")
    print("=" * 50)
    for roman, expected in test_cases:
        result = roman_to_int(roman)
        status = "✓" if result == expected else "✗"
        print(f"{status} {roman:12} -> {result:4} (预期: {expected})")
    
    print("\n方法二：从右向左遍历")
    print("=" * 50)
    for roman, expected in test_cases:
        result = roman_to_int_v2(roman)
        status = "✓" if result == expected else "✗"
        print(f"{status} {roman:12} -> {result:4} (预期: {expected})")
