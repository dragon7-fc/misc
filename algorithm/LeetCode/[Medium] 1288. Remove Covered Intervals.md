1288. Remove Covered Intervals

Given a list of intervals, remove all intervals that are covered by another interval in the list. Interval `[a,b)` is covered by interval `[c,d)` if and only if `c <= a` and `b <= d`.

After doing so, return the number of remaining intervals.

 

**Example 1:**
```
Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
```

**Constraints:**

* `1 <= intervals.length <= 1000`
* `0 <= intervals[i][0] < intervals[i][1] <= 10^5`
* `intervals[i] != intervals[j] for all i != j`

# Submissions
---
**Solution 1:**
```
Runtime: 100 ms
Memory Usage: 13.1 MB
```
```python
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        res = right = 0
        for i, j in sorted(intervals, key=lambda a: [a[0], -a[1]]):
            res += j > right
            right = max(right, j)
        return res
```