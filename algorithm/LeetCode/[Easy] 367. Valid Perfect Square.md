367. Valid Perfect Square

Given a positive integer `num`, write a function which returns `True` if `num` is a perfect square else `False`.

**Note:** Do not use any built-in library function such as sqrt.

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
Runtime: 28 ms
Memory Usage: 13.7 MB
```
```python
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1: return True
        lo, hi = 1, num
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            val = mid ** 2
            if val == num: return True
            elif val < num: lo = mid + 1
            else: hi = mid - 1
        return False
```