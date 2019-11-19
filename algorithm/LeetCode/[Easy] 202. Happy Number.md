202. Happy Number

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

**Example:** 
```
Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
```

# Submissions
---
**Solution 1:**
```
Runtime: 32 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        v = n
        while True:
            v = sum([int(i)**2 for i in str(v)])
            if v == 1:
                return True
            elif v in seen:
                return False
            else:
                seen.add(v)
```