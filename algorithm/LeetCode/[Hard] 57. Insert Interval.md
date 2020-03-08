57. Insert Interval

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

**Example 1:**
```
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
```

**Example 2:**
```
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
```

**NOTE:** input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

# Submissions
---
**Solution 1: (Sort, Greedy, Stack)**
```
Runtime: 80 ms
Memory Usage: 16.1 MB
```
```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals = sorted(intervals)
        res_stack = [intervals[0]]
        
        for i in range(1, len(intervals)):
            top = res_stack[-1]
            if top[1] >= intervals[i][0]:
                # tops' end is earlier than the start
                res_stack.pop()
                top[1] = max(intervals[i][1], top[1])
                res_stack.append(top)
            else:
                res_stack.append(intervals[i])
        
        return res_stack
```