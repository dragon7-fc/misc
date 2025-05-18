3552. Grid Teleportation Traversal

You are given a 2D character grid matrix of size `m x n`, represented as an array of strings, where `matrix[i][j]` represents the cell at the intersection of the `i`th row and `j`th column. Each cell is one of the following:

* `'.'` representing an empty cell.
* `'#'` representing an obstacle.
* An uppercase letter ('A'-'Z') representing a teleportation portal.

You start at the top-left cell `(0, 0)`, and your goal is to reach the bottom-right cell `(m - 1, n - 1)`. You can move from the current cell to any adjacent cell (up, down, left, right) as long as the destination cell is within the grid bounds and is not an obstacle.

If you step on a cell containing a portal letter and you haven't used that portal letter before, you may instantly teleport to any other cell in the grid with the same letter. This teleportation does not count as a move, but each portal letter can be used **at most** once during your journey.

Return the **minimum** number of moves required to reach the bottom-right cell. If it is not possible to reach the destination, return `-1`.

 

**Example 1:**
```
Input: matrix = ["A..",".A.","..."]

Output: 2

Explanation:
```
![3552_example04140](img/3552_example04140.png)
```
Before the first move, teleport from (0, 0) to (1, 1).
In the first move, move from (1, 1) to (1, 2).
In the second move, move from (1, 2) to (2, 2).
```

**Example 2:**
```
Input: matrix = [".#...",".#.#.",".#.#.","...#."]

Output: 13

Explanation:
```
![3552_ezgifcom-animated-gif-maker.gif](img/3552_ezgifcom-animated-gif-maker.gif)
 

**onstraints:**

* `1 <= m == matrix.length <= 10^3`
* `1 <= n == matrix[i].length <= 10^3`
* `matrix[i][j]` is either `'#'`, `'.'`, or an uppercase English letter.
* `matrix[0][0]` is not an obstacle.

# Submissions
---
**Solution 1: (BFS)**
```
Runtime: 242 ms, Beats 97.21%
Memory: 138.33 MB, Beats 93.40%
```
```c++
class Solution {
    int dd[5] = {0, 1, 0, -1, 0};
public:
    int minMoves(vector<string>& matrix) {
        int m = matrix.size(), n = matrix[0].size(), i, j, d, nr, nc;
        vector<vector<pair<int,int>>> dp(26);
        for (i = 0; i < m; i ++) {
            for (j = 0; j < n; j ++) {
                if (matrix[i][j] != '.' && matrix[i][j] != '#') {
                    dp[matrix[i][j] - 'A'].push_back({i, j});
                }
            }
        }
        queue<tuple<int,int,int>> q;
        if (matrix[0][0] != '.') {
            for (auto [tr, tc]: dp[matrix[0][0] - 'A']) {
                q.push({tr, tc, 0});
                matrix[tr][tc] = '#';
            }
        } else {
            q.push({0, 0, 0});
            matrix[0][0] = '#';
        }
        matrix[0][0] = '#';
        while (q.size()) {
            auto [r, c, s] = q.front();
            q.pop();
            if (r == m-1 && c == n-1) {
                return s;
            }
            for (d = 0; d < 4; d ++) {
                nr = r + dd[d];
                nc = c + dd[d+1];
                if (0 <= nr && nr < m && 0 <= nc && nc < n && matrix[nr][nc] != '#') {
                    if (matrix[nr][nc] != '.') {
                        for (auto [tr, tc]: dp[matrix[nr][nc] - 'A']) {
                            if (matrix[tr][tc] != '#') {
                                q.push({tr, tc, s + 1});
                                matrix[tr][tc] = '#';
                            }
                        }
                    } else {
                        q.push({nr, nc, s + 1});
                        matrix[nr][nc] = '#';
                    }
                }
            }
        }
        return -1;
    }
};
```
