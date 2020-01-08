435. Non-overlapping Intervals

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

 

**Example 1:**
```
Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
```

**Example 2:**
```
Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
```

**Example 3:**
```
Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
```

**Note:**

* You may assume the interval's end point is always bigger than its start point.
* Intervals like `[1,2]` and `[2,3]` have borders "touching" but they don't overlap each other.

# Submissions
---
**Solution 1: (Greedy)**
```
Runtime: 60 ms
Memory Usage: 16 MB
```
```python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        sorted_intervals = sorted(intervals)
        curr_interval, dels = sorted_intervals[0], 0
        for i in range(1, len(sorted_intervals)):
            next_interval = sorted_intervals[i]
            if next_interval[0] >= curr_interval[1]:
                curr_interval = next_interval
            else:
                dels += 1
                if curr_interval[1] > next_interval[1]:
                    curr_interval = next_interval
        return dels
```