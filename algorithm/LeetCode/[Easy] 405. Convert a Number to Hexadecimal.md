405. Convert a Number to Hexadecimal

Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.

**Note:**

1. All letters in hexadecimal (a-f) must be in lowercase.
1. The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
1. The given number is guaranteed to fit within the range of a 32-bit signed integer.
1. You **must not use any method provided by the library** which converts/formats the number to hex directly.

**Example 1:**
```
Input:
26

Output:
"1a"
```

**Example 2:**
```
Input:
-1

Output:
"ffffffff"
```

# Submissions
---
**Solution 1: (Bit Manipulation)**
```
Runtime: 20 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        if num <0:
            num = num&0xffffffff
        ans = ''
        while num:
            a = num&15
            num >>= 4
            ans = (str(a) if a<10 else chr(a+ ord('a') - 10)) + ans
        return ans
```