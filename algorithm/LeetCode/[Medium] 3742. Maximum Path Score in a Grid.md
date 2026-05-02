3742. Maximum Path Score in a Grid

You are given an `m x n` grid where each cell contains one of the values `0`, `1`, or `2`. You are also given an integer `k`.

You start from the top-left corner `(0, 0)` and want to reach the bottom-right corner `(m - 1, n - 1)` by moving only **right** or **down**.

Each cell contributes a specific score and incurs an associated cost, according to their cell values:

* 0: adds 0 to your score and costs 0.
* 1: adds 1 to your score and costs 1.
* 2: adds 2 to your score and costs 1.

Return the **maximum** score achievable without exceeding a total cost of `k`, or `-1` if no valid path exists.

Note: If you reach the last cell but the total cost exceeds `k`, the path is invalid.

 

**Example 1:**
```
Input: grid = [[0, 1],[2, 0]], k = 1

Output: 2

Explanation:

The optimal path is:

Cell	grid[i][j]	Score	Total
Score	Cost	Total
Cost
(0, 0)	0	0	0	0	0
(1, 0)	2	2	2	1	1
(1, 1)	0	0	2	0	1
Thus, the maximum possible score is 2.
```

**Example 2:**
```
Input: grid = [[0, 1],[1, 2]], k = 1

Output: -1

Explanation:

There is no path that reaches cell (1, 1) without exceeding cost k. Thus, the answer is -1.
```
 

**Constraints:**

* `1 <= m, n <= 200`
* `0 <= k <= 10^3`
* `grid[0][0] == 0`
* `0 <= grid[i][j] <= 2`

# Submissions
---
**Solution 1: (DP Bottom-Up)**
```
Runtime: 759 ms, Beats 33.33%
Memory: 499.59 MB, Beats 0.00%
```
```c++
class Solution {
public:
    int maxPathScore(vector<vector<int>>& grid, int k) {
        int m = grid.size();
        int n = grid[0].size();

        vector<int> score_add = {0, 1, 2};
        vector<int> cost_add  = {0, 1, 1};

        vector<vector<vector<int>>> dp(m, vector<vector<int>>(n, vector<int>(k + 1, -1)));
        dp[0][0][0] = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                for (int cost_used = 0; cost_used <= k; cost_used++) {
                    if (dp[i][j][cost_used] == -1) continue;

                    int cur_score = dp[i][j][cost_used];

                    // Move DOWN
                    if (i + 1 < m) {
                        int new_cost = cost_used + cost_add[grid[i + 1][j]];
                        if (new_cost <= k) {
                            int new_score = cur_score + score_add[grid[i + 1][j]];
                            dp[i + 1][j][new_cost] = max(dp[i + 1][j][new_cost], new_score);
                        }
                    }

                    // Move RIGHT
                    if (j + 1 < n) {
                        int new_cost = cost_used + cost_add[grid[i][j + 1]];
                        if (new_cost <= k) {
                            int new_score = cur_score + score_add[grid[i][j + 1]];
                            dp[i][j + 1][new_cost] = max(dp[i][j + 1][new_cost], new_score);
                        }
                    }
                }
            }
        }

        int best = -1;
        for (int c = 0; c <= k; c++) {
            best = max(best, dp[m - 1][n - 1][c]);
        }
        return best;
    }
};
```

**Solution 2: (DP Bottom-Up, pruning, O(m * n * k), k <= m + n - 2)**
```
Runtime: 739 ms, Beats 82.06%
Memory: 499.32 MB, Beats 62.72%
```
```c++
class Solution {
public:
    int maxPathScore(vector<vector<int>>& grid, int k) {
        int m = grid.size(), n = grid[0].size(), val, cost;
        vector<vector<vector<int>>> dp(
            m, vector<vector<int>>(n, vector<int>(k + 1, -1)));
        dp[0][0][0] = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                for (int c = 0; c <= k; c++) {
                    if (dp[i][j][c] == -1) {  // pruning
                        continue;
                    }
                    if (i + 1 < m) {
                        val = grid[i + 1][j];
                        cost = (val == 0 ? 0 : 1);
                        if (c + cost <= k) {
                            dp[i + 1][j][c + cost] =
                                max(dp[i + 1][j][c + cost], dp[i][j][c] + val);
                        }
                    }
                    if (j + 1 < n) {
                        val = grid[i][j + 1];
                        cost = (val == 0 ? 0 : 1);
                        if (c + cost <= k) {
                            dp[i][j + 1][c + cost] =
                                max(dp[i][j + 1][c + cost], dp[i][j][c] + val);
                        }
                    }
                }
            }
        }
        int ans = -1;
        for (int c = 0; c <= k; c++) {
            ans = max(ans, dp[m - 1][n - 1][c]);
        }
        return ans < 0 ? -1 : ans;
    }
};
```

**Solution 3: (DP Bottom-Up, 1-D, try max score for every cost of every cell)**
```
Runtime: 574 ms, Beats 90.07%
Memory: 119.85 MB, Beats 90.94%
```
```c++
class Solution {
public:
    int maxPathScore(vector<vector<int>>& grid, int k) {
        int m = grid.size(), n = grid[0].size(), i, j, c, nc;
        vector<vector<int>> pre(n, vector<int>(k + 1, -1)), dp(n, vector<int>(k + 1, -1));
        pre[0][0] = 0;
        for (j = 1; j < n; j ++) {
            for (c = 0; c <= k; c ++) {
                if (pre[j - 1][c] >= 0) {
                    nc = c + (grid[0][j] > 0);
                    if (nc <= k) {
                        pre[j][nc] = pre[j - 1][c] + grid[0][j];
                    }
                }
            }
        }
        for (i = 1; i < m; i ++) {
            for (j = 0; j < n; j ++) {
                for (c = 0; c <= k; c ++) {
                    if (pre[j][c] >= 0) {
                        nc = c + (grid[i][j] > 0);
                        if (nc <= k) {
                            dp[j][nc] = max(dp[j][nc], pre[j][c] + grid[i][j]);
                        }
                    }
                    if (j && dp[j - 1][c] >= 0) {
                        nc = c + (grid[i][j] > 0);
                        if (nc <= k) {
                            dp[j][nc] = max(dp[j][nc], dp[j - 1][c] + grid[i][j]);
                        }
                    }
                }
            }
            pre = dp;
            fill(dp.begin(), dp.end(), vector<int>(k + 1, -1));
        }
        int ans = -1;
        for (c = 0; c <= k; c ++) {
            ans = max(ans, pre[n - 1][c]);
        }
        return ans < 0 ? -1 : ans;
    }
};
```
