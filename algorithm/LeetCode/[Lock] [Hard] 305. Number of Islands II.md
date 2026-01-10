305. Number of Islands II

You are given an empty 2D binary grid `grid` of size `m x n`. The grid represents a map where `0`'s represent water and `1`'s represent land. Initially, all the cells of grid are water cells (i.e., all the cells are `0`'s).

We may perform an add land operation which turns the water at position into a land. You are given an array `positions` where `positions[i] = [ri, ci]` is the position `(ri, ci)` at which we should operate the `i`th operation.

Return an array of integers `answer` where `answer[i]` is the number of islands after turning the cell `(ri, ci)` into a land.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

**Example 1:**

![305_tmp-grid.jpg](img/305_tmp-grid.jpg)
```
Input: m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]]
Output: [1,1,2,3]
Explanation:
Initially, the 2d grid is filled with water.
- Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land. We have 1 island.
- Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land. We still have 1 island.
- Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land. We have 2 islands.
- Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land. We have 3 islands.
```

**Example 2:**
```
Input: m = 1, n = 1, positions = [[0,0]]
Output: [1]
```

**Constraints:**

* `1 <= m, n, positions.length <= 10^4`
* `1 <= m * n <= 10^4`
* `positions[i].length == 2`
* `0 <= ri < m`
* `0 <= ci < n`
 

**Follow up:** Could you solve it in time complexity `O(k log(mn))`, where `k == positions.length`?

# Submissions
---
**Solution 1: (Union Find)**

     m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]]
pre                              0      1     1     2
cur                              1      1     2     3
         0  1  2  3  4  5  6  7  9
p        0  1  2  3  4  5  6  7  8
         1           
visited  1  1           1     1

```
Runtime: 4 ms, Beats 87.70%
Memory: 41.52 MB, Beats 74.94%
```
```c++
class Solution {
    vector<int> p;
    vector<int> rk;
    int find (int x) {
        if (p[x] != x) {
            p[x] = find(p[x]);
        }
        return p[x];
    }
    bool uni(int x, int y) {
        int xr = find(x), yr = find(y);
        if (xr == yr) {
            return false;
        }
        if (rk[xr] > rk[yr]) {
            p[yr] = xr;
        } else if (rk[xr] < rk[yr]) {
            p[xr] = yr;
        } else {
            p[yr] = xr;
            rk[xr] += 1;
        }
        return true;
    }
public:
    vector<int> numIslands2(int m, int n, vector<vector<int>>& positions) {
        int i, r, c, nr, nc, pre = 0, cur, dd[5] = {0,1,0,-1,0}, d;
        p.resize(m * n);
        for (i = 0; i < m * n; i ++) {
            p[i] = i;
        }
        rk.resize(m * n);
        vector<int> ans;
        vector<vector<bool>> visited(m, vector<bool>(n)); 
        for (auto &p: positions) {
            r = p[0];
            c = p[1];
            if (visited[r][c]) {
                ans.push_back(pre);
                continue;
            }
            visited[r][c] = true;
            cur = pre + 1;
            for (d = 0; d < 4; d ++) {
                nr = r + dd[d];
                nc = c + dd[d + 1];
                if (0 <= nr && nr < m && 0 <= nc && nc < n && visited[nr][nc]) {
                    if (uni(r * n + c, nr * n + nc)) {
                        cur -= 1;
                    }
                }
            }
            ans.push_back(cur);
            pre = cur;
        }
        return ans;
    }
};
```
