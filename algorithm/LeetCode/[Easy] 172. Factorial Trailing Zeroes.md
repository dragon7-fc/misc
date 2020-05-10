172. Factorial Trailing Zeroes

Given an integer `n`, return the number of trailing zeroes in n!.

**Example 1:**
```
Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
```

**Example 2:**
```
Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
```

**Note:** Your solution should be in logarithmic time complexity.

# Submissions
---
**Solution 1: (Math)**
```
Runtime: 28 ms
Memory Usage: 12.6 MB
```
```python
class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeros = 0
        
        while n >= 5:
            q = n//5
            zeros += q
            n = q
            
        return zeros
```

**Solution 2: (Math, DFS)**
```
Runtime: 24 ms
Memory Usage: N/A
```
```python
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 0 if n == 0 else n // 5 + self.trailingZeroes(n // 5)
```