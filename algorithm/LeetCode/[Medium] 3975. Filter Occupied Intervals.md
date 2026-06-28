3975. Filter Occupied Intervals

You are given a 2D integer array `occupiedIntervals`, where `occupiedIntervals[i] = [starti, endi]` represents a time interval during which you are occupied. Each interval starts at `starti` and ends at `endi`, inclusive. These intervals may overlap.

You are also given two integers `freeStart` and `freeEnd`, which define a free time interval from `freeStart` to `freeEnd`, inclusive.

Your task is to merge **all** occupied intervals that overlap or touch, then remove **all** integer points in the free interval from the merged occupied intervals.

Two intervals touch if the second interval starts **immediately** after the first one ends. For example, `[1, 1]` and `[2, 2]` touch and should be merged into `[1, 2`].

Return the **remaining** occupied intervals in **sorted** order. The returned intervals must be **non-overlapping** and must contain the **minimum** number of intervals possible. If there are no remaining occupied points, return an empty list.

 

**Example 1:**
```
Input: occupiedIntervals = [[2,6],[4,8],[10,10],[10,12],[14,16]], freeStart = 7, freeEnd = 11

Output: [[2,6],[12,12],[14,16]]

Explanation:

After merging, the occupied intervals are [2, 8], [10, 12], and [14, 16].
Excluding the free interval [7, 11] results in [2, 6], [12, 12], and [14, 16].
```

**Example 2:**
```
Input: occupiedIntervals = [[1,5],[2,3]], freeStart = 3, freeEnd = 8

Output: [[1,2]]

Explanation:

After merging, the occupied interval is [1, 5].
Excluding the free interval [3, 8] results in [1, 2].
```

**Constraints:**

* `1 <= occupiedIntervals.length <= 5 * 10^4`
* `occupiedIntervals[i].length == 2`
* `1 <= starti <= endi <= 10^9`
* `1 <= freeStart <= freeEnd <= 10^9`

# Submissions
---
**Solution 1: (Hash Table, Sort, open close event)**
```
Runtime: 325 ms, Beats 5.09%
Memory: 241.47 MB, Beats 5.02%
```
```c++
class Solution {
public:
    vector<vector<int>> filterOccupiedIntervals(vector<vector<int>>& occupiedIntervals, int freeStart, int freeEnd) {
        map<int, int> cnt;
        for (const auto &interval: occupiedIntervals) {
            auto start = interval[0];
            auto end = interval[1];
            cnt[start] += 1;
            cnt[end + 1] -= 1;
        }
        cnt[freeStart] -= 1e5;
        cnt[freeEnd + 1] += 1e5;
        int pre = 0;
        int a = 0;
        vector<vector<int>> ans;
        for (const auto &[x, k]: cnt) {
            a += k;
            if (a > 0) {
                if (pre <= 0) {
                    ans.push_back({x, INT_MAX});
                }
            } else {
                if (ans.size() && ans.back()[1] == INT_MAX) {
                    ans.back()[1] = x - 1;
                }
            }
            pre = a;
        }
        return ans;
    }
};
```

**Solution 2: (Sort)**
```
Runtime: 83 ms, Beats 93.11%
Memory: 192.59 MB, Beats 49.59%
```
```c++
class Solution {
public:
    vector<vector<int>> filterOccupiedIntervals(vector<vector<int>>& occupiedIntervals, int freeStart, int freeEnd) {
        int n = occupiedIntervals.size();
        sort(occupiedIntervals.begin(), occupiedIntervals.end());
        vector<vector<int>> dp;
        dp.push_back(occupiedIntervals[0]);
        int pre = occupiedIntervals[0][1];
        for (int i = 1; i < n; i ++) {
            if (occupiedIntervals[i][0] <= pre + 1) {
                pre = max(pre, occupiedIntervals[i][1]);
            } else {
                dp.back()[1] = pre;
                dp.push_back(occupiedIntervals[i]);
                pre = dp.back()[1];
            }
            if (i == n - 1) {
                dp.back()[1] = pre;
            }
        }
        n = dp.size();
        vector<vector<int>> ans;
        for (int i = 0; i < n; i ++) {
            if (dp[i][1] < freeStart || dp[i][0] > freeEnd) {
                ans.push_back(dp[i]);
            } else {
                if (dp[i][0] < freeStart && dp[i][1] > freeEnd) {
                    ans.push_back({dp[i][0], freeStart - 1});
                    ans.push_back({freeEnd + 1, dp[i][1]});
                } else if (dp[i][0] < freeStart && dp[i][1] >= freeStart) {
                    ans.push_back({dp[i][0], freeStart - 1});
                } else if (dp[i][0] <= freeEnd && dp[i][1] > freeEnd) {
                    ans.push_back({freeEnd + 1, dp[i][1]});
                }
            }
        }
        return ans;
    }
};
```

**Solution 3: (Sort)**
```
Runtime: 96 ms, Beats 56.45%
Memory: 192.34 MB, Beats 85.36%
```
```c++
class Solution {
public:
    vector<vector<int>> filterOccupiedIntervals(vector<vector<int>>& occupiedIntervals, int freeStart, int freeEnd) {
         int n = occupiedIntervals.size();
        sort(occupiedIntervals.begin(), occupiedIntervals.end());
        vector<vector<int>> dp;
        dp.push_back(occupiedIntervals[0]);
        int pre = occupiedIntervals[0][1];
        for (int i = 1; i < n; i ++) {
            if (occupiedIntervals[i][0] <= pre + 1) {
                pre = max(pre, occupiedIntervals[i][1]);
            } else {
                dp.back()[1] = pre;
                dp.push_back(occupiedIntervals[i]);
                pre = dp.back()[1];
            }
            if (i == n - 1) {
                dp.back()[1] = pre;
            }
        }
        n = dp.size();
        vector<vector<int>> ans;
        for (int i = 0; i < n; i ++) {
            if (dp[i][1] < freeStart || dp[i][0] > freeEnd) {
                ans.push_back(dp[i]);
            } else {
                if (dp[i][0] < freeStart) {
                    ans.push_back({dp[i][0], freeStart - 1});
                }
                if (dp[i][1] > freeEnd) {
                    ans.push_back({freeEnd + 1, dp[i][1]});
                }
            }
        }
        return ans;
    }
};
```
