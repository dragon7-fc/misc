3905. Multi Source Flood Fill

You are given two integers n and m representing the number of rows and columns of a grid, respectively.

You are also given a 2D integer array sources, where sources[i] = [ri, ci, color​​​​​​​i] indicates that the cell (ri, ci) is initially colored with colori. All other cells are initially uncolored and represented as 0.

At each time step, every currently colored cell spreads its color to all adjacent uncolored cells in the four directions: up, down, left, and right. All spreads happen simultaneously.

If multiple colors reach the same uncolored cell at the same time step, the cell takes the color with the maximum value.

The process continues until no more cells can be colored.

Return a 2D integer array representing the final state of the grid, where each cell contains its final color.

 

**Example 1:**

Input: n = 3, m = 3, sources = [[0,0,1],[2,2,2]]

Output: [[1,1,2],[1,2,2],[2,2,2]]

Explanation:

The grid at each time step is as follows:

![3905_g50new.png](img/3905_g50new.png)

At time step 2, cells (0, 2), (1, 1), and (2, 0) are reached by both colors, so they are assigned color 2 as it has the maximum value among them.

Example 2:

Input: n = 3, m = 3, sources = [[0,1,3],[1,1,5]]

Output: [[3,3,3],[5,5,5],[5,5,5]]

Explanation:

The grid at each time step is as follows:

![3905_g51new.png](img/3905_g51new.png)

Example 3:

Input: n = 2, m = 2, sources = [[1,1,5]]

Output: [[5,5],[5,5]]

Explanation:

The grid at each time step is as follows:

![3905_g52new.png](img/3905_g52new.png)

Since there is only one source, all cells are assigned the same color.

 

**Constraints:**

* `1 <= n, m <= 10^5`
* `1 <= n * m <= 10^5`
* `1 <= sources.length <= n * m`
* `sources[i] = [ri, ci, colori]`
* `0 <= ri <= n - 1`
* `0 <= ci <= m - 1`
* `1 <= colori <= 10^6`
* All `(ri, ci)` in `sources` are distinct.

# Submissions
---
**Solution 1: (BFS, sort then bfs from larger color)**
```
Runtime: 108 ms, Beats 71.43%
Memory: 201.47 MB, Beats 57.14%
```
```c++
class Solution {
    int dd[5] = {0, 1, 0, -1, 0};
public:
    vector<vector<int>> colorGrid(int n, int m, vector<vector<int>>& sources) {
        int i, sz, nr, nc, ncolor, d;
        vector<vector<int>> ans(n, vector<int>(m));
        queue<array<int, 3>> q;
        sort(sources.begin(), sources.end(), [](const auto &va, const auto &vb){
            return va[2] > vb[2];
        });
        for (i = 0; i < sources.size(); i ++) {
            auto &r = sources[i][0];
            auto &c = sources[i][1];
            auto &color = sources[i][2];
            q.push({r, c, color});
            ans[r][c] = color;
        }
        while (q.size()) {
            sz = q.size();
            for (i = 0; i < sz; i ++) {
                auto [r, c, color] = q.front();
                q.pop();
                for (d = 0; d < 4; d ++) {
                    nr = r + dd[d];
                    nc = c + dd[d + 1];
                    if (0 <= nr && nr < n && 0 <= nc && nc < m && ans[nr][nc] == 0) {
                        ans[nr][nc] = color;
                        q.push({nr, nc, color});
                    }
                }
            }
        }
        return ans;
    }
};
```
