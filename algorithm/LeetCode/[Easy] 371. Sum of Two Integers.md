371. Sum of Two Integers

Calculate the sum of two integers a and b, but you are **not allowed** to use the operator `+` and `-`.

**Example 1:**
```
Input: a = 1, b = 2
Output: 3
```

**Example 2:**
```
Input: a = -2, b = 3
Output: 1
```

# Submissions
---
**Solution 1: (Array)**
```
Runtime: 28 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        return sum([a, b])
```