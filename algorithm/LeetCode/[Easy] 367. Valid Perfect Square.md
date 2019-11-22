367. Valid Perfect Square

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

**Example 1:**
```
Input: 16
Output: true
```

**Example 2:**
```
Input: 14
Output: false
```

# Submissions
---
**Solution 1:**
```
Runtime: 36 ms
Memory Usage: 12.7 MB
```
```python
Runtime: 36 ms
Memory Usage: 12.7 MB
```
```
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, num
        while l < r:
            mid = l + (r - l) // 2
            val = mid ** 2
            if val == num: return True
            elif val < num: l = mid + 1
            else: r = mid
        return l ** 2 == num
```