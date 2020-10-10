452. Minimum Number of Arrows to Burst Balloons

There are a number of spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter and hence the x-coordinates of start and end of the diameter suffice. Start is always smaller than end. There will be at most 104 balloons.

An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with x_start and x_end bursts by an arrow shot at x if x_start ≤ x ≤ x_end. There is no limit to the number of arrows that can be shot. An arrow once shot keeps travelling up infinitely. The problem is to find the minimum number of arrows that must be shot to burst all balloons.

**Example:**
```
Input:
[[10,16], [2,8], [1,6], [7,12]]

Output:
2

Explanation:
One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).
```

# Submissions
---
**Solution 1: (Greedy, Sort by end and filter by start)**
```
Runtime: 448 ms
Memory Usage: 18 MB
```
```python
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        prev_end = float('inf')
        ans = 0
        for start, end in sorted(points, key=lambda x: x[1]):
            if start <= prev_end <= end:
                continue
            else:
                prev_end = end
                ans += 1
        return ans
```

**Solution2 : (Greedy, Sort by start and filter by end)**
```
Runtime: 464 ms
Memory Usage: 19.2 MB
```
```python
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        s = []
        ans = 0
        for start, end in points:
            if not s or s and s[-1][1] < start:
                ans += len(s)
                s = [[start, end]]
            elif s and s[-1][1] >= start:
                s += [[start, min(end, s[-1][1])]]
                s.pop(-2)
        ans += len(s)
        
        return ans
```