2406. Divide Intervals Into Minimum Number of Groups

You are given a 2D integer array `intervals` where `intervals[i] = [lefti, righti]` represents the **inclusive** interval `[lefti, righti]`.

You have to divide the intervals into one or more **groups** such that each interval is in **exactly** one group, and no two intervals that are in the same group **intersect** each other.

Return the **minimum** number of groups you need to make.

Two intervals **intersect** if there is at least one common number between them. For example, the intervals `[1, 5]` and `[5, 8]` intersect.

 

**Example 1:**
```
Input: intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
Output: 3
Explanation: We can divide the intervals into the following groups:
- Group 1: [1, 5], [6, 8].
- Group 2: [2, 3], [5, 10].
- Group 3: [1, 10].
It can be proven that it is not possible to divide the intervals into fewer than 3 groups.
```

**Example 2:**
```
Input: intervals = [[1,3],[5,6],[8,10],[11,13]]
Output: 1
Explanation: None of the intervals overlap, so we can put all of them in one group.
```

**Constraints:**

* `1 <= intervals.length <= 10^5`
* `intervals[i].length == 2`
* `1 <= lefti <= righti <= 10^6`

# Submissions
---
**Solution 1: (start end event)**
```
Runtime: 3532 ms
Memory Usage: 56.8 MB
```
```python
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        A = []
        for a,b in intervals:
            A.append([a, 1])
            A.append([b + 1, -1])
        res = cur = 0
        for a, diff in sorted(A):
            cur += diff
            res = max(res, cur)
        return res
```

**Solution 2: (Heap)**
```
Runtime: 1078 ms
Memory Usage: 89 MB
```
```c++
class Solution {
public:
    int minGroups(vector<vector<int>>& intervals) {
        sort(begin(intervals), end(intervals));
        priority_queue<int, vector<int>, greater<int>> pq;
        for (const auto &i : intervals) {
            if (!pq.empty() && pq.top() < i[0])
                pq.pop();
            pq.push(i[1]);
        }
        return pq.size();
    }
};
```
