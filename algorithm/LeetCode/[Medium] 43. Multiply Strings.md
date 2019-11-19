43. Multiply Strings

Given two non-negative integers `num1` and `num2` represented as strings, return the product of `num1` and `num2`, also represented as a string.

**Example 1:**
```
Input: num1 = "2", num2 = "3"
Output: "6"
```

**Example 2:**
```
Input: num1 = "123", num2 = "456"
Output: "56088"
```

**Note:**

1. The length of both `num1` and `num2` is `< 110`.
1. Both `num1` and `num2` contain only digits `0-9`.
1. Both `num1` and `num2` do not contain any leading zero, except the number `0` itself.
1. You **must not use any built-in BigInteger library** or **convert the inputs to integer** directly.

# Submissions
---
**Solution 1:**
```
Runtime: 24 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res1, res2 = 0, 0
        for i in num1:
            res1 = res1*10 + (ord(i)-ord("0"))
        for i in num2:
            res2= res2*10 + (ord(i)-ord("0"))
        return str(res1*res2)
```