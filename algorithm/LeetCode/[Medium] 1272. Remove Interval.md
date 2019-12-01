1272. Remove Interval

Given a **sorted** list of disjoint `intervals`, each interval `intervals[i] = [a, b]` represents the set of real numbers `x` such that `a <= x < b`.

We remove the intersections between any interval in `intervals` and the interval `toBeRemoved`.

Return a **sorted** list of intervals after all such removals.

 

**Example 1:**
```
Input: intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]
Output: [[0,1],[6,7]]
```

**Example 2:**
```
Input: intervals = [[0,5]], toBeRemoved = [2,3]
Output: [[0,2],[3,5]]
```

**Constraints:**

* `1 <= intervals.length <= 10^4`
* ``-10^9 <= intervals[i][0] < intervals[i][1] <= 10^9`

# Submissions
---
**Solution 1:**
```
Runtime: 428 ms
Memory Usage: 19.3 MB
```
```python
class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        ans = []
        for lo, hi in intervals:
            remove_lo, remove_hi = toBeRemoved
            if hi <= remove_lo or lo >= remove_hi:
                ans.append([lo, hi])
            else:
                if lo < remove_lo:
                    ans.append([lo, remove_lo])
                if hi > remove_hi:
                    ans.append([remove_hi, hi])
        return ans
```