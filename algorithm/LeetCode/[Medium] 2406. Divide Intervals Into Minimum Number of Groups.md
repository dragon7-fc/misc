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

interval   [5,10],[6,8],[1,5],[2,3],[1,10]
sort       [1,5],[1,10],[2,3],[5,10],[6,8]
pq         {-5}
                 {-5,-10}
                        {-3,-5,-10}
                              {-5,-10,-10}
                                     {-8,-10,-10} 

```
Runtime: 328 ms
Memory: 104.59 MB
```
```c++
class Solution {
public:
    int minGroups(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        priority_queue<int> pq;
        int ans = 0, a, b;
        for (auto interval: intervals) {
            a = interval[0];
            b = interval[1];
            while (pq.size() && pq.top() > -a) {
                pq.pop();
            }
            pq.push(-b);
            ans = max(ans, (int)pq.size());
        }
        return ans;
    }
};
```

**Solution 1: (bucket sort, start end event)**

interval   [5,10],[6,8],[1,5],[2,3],[1,10]
dp   0 1 2 3 4  5 6 7 8  9 10 11
       2 1   -1 1 0     -1    -2
cur  0 2 3 3 2  3 3 3 3  2     0 

```
Runtime: 264 ms
Memory: 107.02 MB
```
```c++
class Solution {
public:
    int minGroups(vector<vector<int>>& intervals) {
        int a, b, cur = 0, ans = 0, dp[1000002] = {0};
        for (auto interval: intervals) {
            a = interval[0];
            b = interval[1];
            dp[a] += 1;
            dp[b+1] -= 1;
        }
        for (int i = 0; i <= 1000001; i ++) {
            cur += dp[i];
            ans = max(ans, cur);
        }
        return ans;
    }
};
```
