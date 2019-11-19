67. Add Binary

Given two binary strings, return their sum (also a binary string).

The input strings are both **non-empty** and contains only characters `1` or `0`.

**Example 1:**
```
Input: a = "11", b = "1"
Output: "100"
```

**Example 2:**
```
Input: a = "1010", b = "1011"
Output: "10101"
```

# Submissions
---
**Solution 1:**
```
Runtime: 40 ms
Memory Usage: N/A
```
```python
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        num_a = int(a, 2)
        num_b = int(b, 2)
        return str("{0:b}".format((num_a+num_b)))
```