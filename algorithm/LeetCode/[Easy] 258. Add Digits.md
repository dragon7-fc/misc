258. Add Digits

Given a non-negative integer `num`, repeatedly add all its digits until the result has only one digit.

**Example:**
```
Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.
```

**Follow up:**

Could you do it without any loop/recursion in O(1) runtime?

# Submissions
---
**Solution 1:**
```
Runtime: 28 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def addDigits(self, num: int) -> int:
        def dfs(num):
            digits = [int(d) for d in str(num)]
            if len(digits) == 1:
                return digits[0]
            return dfs(str(sum(digits)))
        
        return dfs(num)
```