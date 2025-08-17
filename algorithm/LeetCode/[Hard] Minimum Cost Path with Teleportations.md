Minimum Cost Path with Teleportations

You are given a `m x n` 2D integer array `grid` and an integer `k`. You start at the top-left cell `(0, 0)` and your goal is to reach the bottom‐right cell `(m - 1, n - 1)`.

There are two types of moves available:

**Normal move**: You can move right or down from your current cell `(i, j)`, i.e. you can move to `(i, j + 1)` (right) or `(i + 1, j)` (down). The cost is the value of the destination cell.

**Teleportation**: You can teleport from any cell `(i, j)`, to any cell `(x, y)` such that `grid[x][y] <= grid[i][j]`; the cost of this move is 0. You may teleport at most `k` times.

Return the **minimum** total cost to reach cell `(m - 1, n - 1)` from `(0, 0)`.

 

**Example 1:**
```
Input: grid = [[1,3,3],[2,5,4],[4,3,5]], k = 2

Output: 7

Explanation:

Initially we are at (0, 0) and cost is 0.

Current Position	Move	New Position	Total Cost
(0, 0)	Move Down	(1, 0)	0 + 2 = 2
(1, 0)	Move Right	(1, 1)	2 + 5 = 7
(1, 1)	Teleport to (2, 2)	(2, 2)	7 + 0 = 7
The minimum cost to reach bottom-right cell is 7.
```

**Example 2:**
```
Input: grid = [[1,2],[2,3],[3,4]], k = 1

Output: 9

Explanation:

Initially we are at (0, 0) and cost is 0.

Current Position	Move	New Position	Total Cost
(0, 0)	Move Down	(1, 0)	0 + 2 = 2
(1, 0)	Move Right	(1, 1)	2 + 3 = 5
(1, 1)	Move Down	(2, 1)	5 + 4 = 9
The minimum cost to reach bottom-right cell is 9.
```
 

**Constraints:**

* `2 <= m, n <= 80`
* `m == grid.length`
* `n == grid[i].length`
* `0 <= grid[i][j] <= 10^4`
* `0 <= k <= 10`

# Submissions
---
**Solution 1: (Dijkstra)**
```
Runtime: 1409 ms, Beats 41.94%
Memory: 359.47 MB, Beats 53.45%
```
```c++
class Solution {
public:
    int minCost(vector<vector<int>>& grid, int k) {
        int n = grid.size(), m = grid[0].size();
        vector<tuple<int, int, int>> vals(n * m);
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                vals[i * m + j] = {grid[i][j], i, j};
            }
        }
        sort(vals.rbegin(), vals.rend());
        vector available(k, vals);

        
        using tr = tuple<int, int, int, int>;
        priority_queue<tr, vector<tr>, greater<>> pq;
        vector shortest(n, vector(m, vector<int>(k + 1, INT_MAX/2)));
        pq.push({shortest[0][0][0] = 0, 0, 0, 0});

        while(!pq.empty()) {
            auto [cost, i, j, t] = pq.top();
            pq.pop();
            if(cost > shortest[i][j][t] || (t > 0 && cost >= shortest[i][j][t - 1])) continue;
            if(i == n - 1 && j == m - 1) return cost;

            if(i + 1 < n) {
                int newCost = cost + grid[i + 1][j];
                if(newCost < shortest[i + 1][j][t]) {
                    pq.push({shortest[i + 1][j][t] = newCost, i + 1, j, t});
                }
            }
            
            if(j + 1 < m) {
                int newCost = cost + grid[i][j + 1];
                if(newCost < shortest[i][j + 1][t]) {
                    pq.push({shortest[i][j + 1][t] = newCost, i, j + 1, t});
                }
            }

            if(t < k) {
                while(!available[t].empty() && get<0>(available[t].back()) <= grid[i][j]) {
                    auto& [_, ni, nj] = available[t].back();
                    if(cost < shortest[ni][nj][t + 1]) {
                        pq.push({shortest[ni][nj][t + 1] = cost, ni, nj, t + 1});
                    }
                    available[t].pop_back();
                }
                for(int p = t+1; p < k; p++) {
                    while(!available[p].empty() && get<0>(available[p].back()) <= grid[i][j]) {
                        available[p].pop_back();
                    }
                }
            }
        }
        unreachable();
    }
};
```
