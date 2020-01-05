441. Arranging Coins

You have a total of `n` coins that you want to form in a staircase shape, where every `k`-th row must have exactly `k` coins.

Given `n`, find the total number of **full** staircase rows that can be formed.

`n` is a non-negative integer and fits within the range of a 32-bit signed integer.

**Example 1:**
```
n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
```

**Example 2:**
```
n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.
```

# Submissions
---
**Solution 1:**
```
Runtime: 28 ms
Memory Usage: 12.6 MB
```
```python
class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 0:
            return 0
        
        lo, hi = 1, n
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            area = (1 + mid) * mid // 2
            if area == n:
                return mid
            elif area < n:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo - 1
```