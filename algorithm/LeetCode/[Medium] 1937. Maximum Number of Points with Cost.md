1937. Maximum Number of Points with Cost

You are given an `m x n` integer matrix `points` (**0-indexed**). Starting with `0` points, you want to maximize the number of points you can get from the matrix.

To gain points, you must pick one cell in **each row**. Picking the cell at coordinates `(r, c)` will **add** `points[r][c]` to your score.

However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. For every two adjacent rows `r` and `r + 1` (where `0 <= r < m - 1`), picking cells at coordinates `(r, c1)` and `(r + 1, c2)` will **subtract** `abs(c1 - c2)` from your score.

Return the **maximum** number of points you can achieve.

`abs(x)` is defined as:

* `x` for `x >= 0`.
* `-x` for `x < 0`.
 

**Example 1:**

![1937_screenshot-2021-07-12-at-13-40-26-diagram-drawio-diagrams-net.png](img/1937_screenshot-2021-07-12-at-13-40-26-diagram-drawio-diagrams-net.png)
```
Input: points = [[1,2,3],[1,5,1],[3,1,1]]
Output: 9
Explanation:
The blue cells denote the optimal cells to pick, which have coordinates (0, 2), (1, 1), and (2, 0).
You add 3 + 5 + 3 = 11 to your score.
However, you must subtract abs(2 - 1) + abs(1 - 0) = 2 from your score.
Your final score is 11 - 2 = 9.
```

**Example 2:**

![1937_screenshot-2021-07-12-at-13-42-14-diagram-drawio-diagrams-net.png](img/1937_screenshot-2021-07-12-at-13-42-14-diagram-drawio-diagrams-net.png)
```
Input: points = [[1,5],[2,3],[4,2]]
Output: 11
Explanation:
The blue cells denote the optimal cells to pick, which have coordinates (0, 1), (1, 1), and (2, 0).
You add 5 + 3 + 4 = 12 to your score.
However, you must subtract abs(1 - 1) + abs(1 - 0) = 1 from your score.
Your final score is 12 - 1 = 11.
```

Constraints:

* `m == points.length`
* `n == points[r].length`
* `1 <= m, n <= 10^5`
* `1 <= m * n <= 10^5`
* `0 <= points[r][c] <= 10^5`

# Submissions
---
**Solution 1: (DP, Bottom-Up)**

Similar to 1014. Best Sightseeing Pair

```
Runtime: 207 ms
Memory: 85.2 MB
```
```c++
class Solution {
public:
    long long maxPoints(vector<vector<int>>& points) {
        const int n = int(points[0].size());
        vector<vector<long long>> dp(2, vector<long long>(n));
        for (int i = 0; i < n; ++i) {
            dp[0][i] = points[0][i];
        }
        int last = 0;
        for (int i = 1; i < points.size(); ++i) {
            int now = last ^ 1;
            long long temp = 0;
            for (int j = 0; j < n; ++j) {
                temp = max(temp, dp[last][j] + j);
                dp[now][j] = temp - j + points[i][j];
            }
            temp = -n;
            for (int j = n - 1; j >= 0; --j) {
                temp = max(temp, dp[last][j] - j);
                dp[now][j] = max(dp[now][j], temp + j + points[i][j]);
            }
            last = now;
        }
        return *max_element(dp[last].begin(), dp[last].end());
    }
};
```

**Solution 2: (DP Bottom-UP, left right)**
```
Runtime: 174 ms
Memory: 88.82 MB
```
```c++
class Solution {
public:
    long long maxPoints(vector<vector<int>>& points) {
        int m = points.size(), n = points[0].size();
        vector<long long> pre(n), right(n), cur(n);
        long long left;
        for (int j = 0; j < n; j ++) {
            pre[j] = points[0][j];
        }
        for (int i = 1; i < m; i ++) {
            right[n-1] = pre[n-1];
            for (int j = n-2; j >= 0; j--) {
                right[j] = max(pre[j], right[j+1] - 1);
            }
            left = 0;
            for (int j = 0; j < n; j ++) {
                cur[j] = points[i][j] + max(left-1, right[j]);
                left = max(left-1, pre[j]);
            }
            pre = cur;
        }
        return *max_element(pre.begin(), pre.end());
    }
};
```
