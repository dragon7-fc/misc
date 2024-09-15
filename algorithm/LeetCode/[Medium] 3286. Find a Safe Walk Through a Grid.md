3286. Find a Safe Walk Through a Grid

You are given an `m x n` binary matrix `grid` and an integer `health`.

You start on the upper-left corner `(0, 0)` and would like to get to the lower-right corner `(m - 1, n - 1)`.

You can move up, down, left, or right from one cell to another adjacent cell as long as your health remains **positive**.

Cells `(i, j)` with `grid[i][j] = 1` are considered **unsafe** and reduce your health by 1.

Return `true` if you can reach the final cell with a health value of 1 or more, and `false` otherwise.

 

**Example 1:**
```
Input: grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], health = 1

Output: true

Explanation:

The final cell can be reached safely by walking along the gray cells below.
```
![3286_examples_1drawio.png](img/3286_examples_1drawio.png)

**Example 2:**
```
Input: grid = [[0,1,1,0,0,0],[1,0,1,0,0,0],[0,1,1,1,0,1],[0,0,1,0,1,0]], health = 3

Output: false

Explanation:

A minimum of 4 health points is needed to reach the final cell safely.
```
![3286_examples_2drawio.png](img/3286_examples_2drawio.png)


**Example 3:**
```
Input: grid = [[1,1,1],[1,0,1],[1,1,1]], health = 5

Output: true

Explanation:

The final cell can be reached safely by walking along the gray cells below.
```
![3286_examples_3drawio.png](img/3286_examples_3drawio.png)

```
Any path that does not go through the cell (1, 1) is unsafe since your health will drop to 0 when reaching the final cell.
```
 

**Constraints:**

* `m == grid.length`
* `n == grid[i].length`
* `1 <= m, n <= 50`
* `2 <= m * n`
* `1 <= health <= m + n`
* `grid[i][j]` is either `0` or `1`.

# Submissions
---
**Solution 1: (Dijkstra)**
```
Runtime: 21 ms
Memory: 30.24 MB
```
```c++
class Solution {
    int d[5] = {0, 1, 0, -1, 0};
public:
    bool findSafeWalk(vector<vector<int>>& grid, int health) {
        int m = grid.size(), n = grid[0].size(), nr, nc, nh;
        priority_queue<tuple<int,int,int>> pq;
        pq.push({health - (grid[0][0] == 1), 0, 0});
        vector<vector<int>> dist(m, vector<int>(n));
        dist[0][0] = health - (grid[0][0] == 1);
        while (pq.size()) {
            auto [h, r, c] = pq.top();
            pq.pop();
            if (r == m-1 && c == n-1 && h) {
                return true;
            }
            for (int i = 0; i < 4; i ++) {
                nr = r + d[i];
                nc = c + d[i+1];
                if (0 <= nr && nr < m && 0 <= nc && nc < n) {
                    nh = h - (grid[nr][nc] == 1);
                    if (nh > dist[nr][nc]) {
                        dist[nr][nc] = nh;
                        pq.push({nh, nr, nc});
                    }
                }
            }
        }
        return false;
    }
};
```
