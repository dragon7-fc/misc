4057. Number of Intersecting Interval Pairs II

You are given a 2D integer array `intervals` of `n` elements, where `intervals[i] = [starti, endi]` represents the closed interval from `starti` to `endi`.

Return the number of pairs of indices `(i, j)` such that `0 <= i < j < n` and `intervals[i]` and `intervals[j]` **intersect**.

Two intervals **intersect** if they have at least one point in common, including when they only share an endpoint.

 

**Example 1:**
```
Input: intervals = [[1,2],[2,3],[3,4]]

Output: 2

Explanation:

There are 2 intersecting interval pairs:

Intervals [1, 2] and [2, 3] intersect at the point 2.
Intervals [2, 3] and [3, 4] intersect at the point 3.
```

**Example 2:**
```
Input: intervals = [[1,5],[2,4],[3,6]]

Output: 3

Explanation:

There are 3 intersecting interval pairs:

The intersection of [1, 5] and [2, 4] is [2, 4].
The intersection of [1, 5] and [3, 6] is [3, 5].
The intersection of [2, 4] and [3, 6] is [3, 4].
```

**Example 3:**
```
Input: intervals = [[1,2],[3,4],[5,6]]

Output: 0

Explanation:

There are no intersecting interval pairs. Hence, the answer is 0.
```
 

**Constraints:**

* `2 <= n == intervals.length <= 10^5`
* `intervals[i] = [starti, endi]`
* `0 <= starti <= endi <= 10^9`

# Submissions
---
**Solution 1: (Sort, Heap, Greedy)**
```
Runtime: 119 ms, Beats 61.18%
Memory: 258.63 MB, Beats 76.41%
```
```c++
class Solution {
public:
    long long countIntersectingIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        priority_queue<int, vector<int>, greater<>> pq;
        int n = intervals.size();
        pq.push(intervals[0][1]);
        long long ans = 0;
        for (int i = 1; i < n; i ++) {
            while (pq.size() && pq.top() < intervals[i][0]) {
                pq.pop();
            }
            ans += pq.size();
            pq.push(intervals[i][1]);
        }
        return ans;
    }
};
```
