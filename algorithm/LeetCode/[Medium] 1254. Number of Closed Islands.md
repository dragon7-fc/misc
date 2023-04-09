1254. Number of Closed Islands

Given a 2D `grid` consists of `0s` (land) and `1s` (water).  An island is a maximal 4-directionally connected group of `0s` and a closed island is an island totally (all left, top, right, bottom) surrounded by `1s`.

Return the number of closed islands.

 

**Example 1:**

![1254_sample_3_1610](img/1254_sample_3_1610.png)

```
Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).
```

**Example 2:**

![1254_sample_4_1610](img/1254_sample_4_1610.png)

```
Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1
```

**Example 3:**

```
Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2
```

**Constraints:**

* `1 <= grid.length, grid[0].length <= 100`
* `0 <= grid[i][j] <=1`

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 144 ms
Memory Usage: 13 MB
```
```python
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        R, C = len(grid), len(grid[0])

        def neighbours(r, c):
            for nr,nc in ((r-1, c),(r+1, c),(r, c-1),(r, c+1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr,nc
        
        def dfs(r, c):
            grid[r][c] = 1
            for nr, nc in neighbours(r, c):
                if grid[nr][nc] == 0:
                    dfs(nr, nc)

        for r in range(R):
            for c in range(C):
                if (r == 0 or c == 0 or r == R-1 or c == C-1) and grid[r][c] == 0:
                    dfs(r, c)

        res = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    dfs(r, c)
                    res += 1

        return res
```

**Solution 2: (DFS)**
```
Runtime: 11 ms
Memory: 9.5 MB
```
```c++
class Solution {
    int d[5] = {0, 1, 0, -1, 0};
    void dfs(int r, int c, bool& is_contour, vector<vector<int>>& grid) {
        grid[r][c] = 1;
        if (r == 0 || r == grid.size()-1 || c == 0 || c == grid[0].size()-1) {
            is_contour = true;
        }
        int nr, nc;
        for (int i = 0; i < 4; i ++) {
            nr = r + d[i];
            nc = c + d[i+1];
            if (0 <= nr && nr < grid.size() && 0 <= nc && nc < grid[0].size() && grid[nr][nc] == 0) {
                dfs(nr, nc, is_contour, grid);
            }
        }
    }
public:
    int closedIsland(vector<vector<int>>& grid) {
        int ans = 0;
        bool is_contour;
        for (int r = 0; r < grid.size(); r ++) {
            for (int c = 0; c < grid[0].size(); c++) {
                if (grid[r][c] == 0) {
                    is_contour = false;
                    dfs(r, c, is_contour, grid);
                    if (!is_contour) {
                        ans += 1;
                    }
                }
            }
        }
        return ans;
    }
};
```
