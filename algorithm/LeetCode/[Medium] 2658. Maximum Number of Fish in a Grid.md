2658. Maximum Number of Fish in a Grid

You are given a **0-indexed** 2D matrix `grid` of size `m x n`, where `(r, c)` represents:

* A **land** cell if `grid[r][c] = 0`, or
* A **water** cell containing `grid[r][c]` fish, if `grid[r][c] > 0`.

A fisher can start at any water cell `(r, c)` and can do the following operations any number of times:

* Catch all the fish at cell `(r, c)`, or
* Move to any adjacent **water** cell.

Return the **maximum** number of fish the fisher can catch if he chooses his starting cell optimally, or `0` if no water cell exists.

An **adjacent** cell of the cell `(r, c)`, is one of the cells `(r, c + 1)`, `(r, c - 1)`, `(r + 1, c)` or `(r - 1, c)` if it exists.

 

**Example 1:**

![2658_example.png](img/2658_example.png)
```
Input: grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
Output: 7
Explanation: The fisher can start at cell (1,3) and collect 3 fish, then move to cell (2,3) and collect 4 fish.
```

**Example 2:**

![2658_example2.png](img/2658_example2.png)
```
Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
Output: 1
Explanation: The fisher can start at cells (0,0) or (3,3) and collect a single fish. 
```

**Constraints:**

* `m == grid.length`
* `n == grid[i].length`
* `1 <= m, n <= 10`
* `0 <= grid[i][j] <= 10`

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 270 ms
Memory: 16.6 MB
```
```python
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        ans = 0
        
        def dfs(r, c):
            rst = grid[r][c]
            grid[r][c] = -1
            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] > 0:
                    rst += dfs(nr, nc)
            return rst
            
        for r in range(R):
            for c in range(C):
                if grid[r][c] > 0:
                    ans = max(ans, dfs(r, c))
        return ans
```

**Solution 2: (DFS)**
```
Runtime: 88 ms
Memory: 91.3 MB
```
```c++
class Solution {
public:
    int findMaxFish(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size(), dir[5] = {0, 1, 0, -1, 0};
        vector<vector<bool>> seen(m, vector<bool>(n, false));
        
        function<int(int, int)> dfs = [&](int i, int j) {
            seen[i][j] = true;
            int ans = grid[i][j];
            for(int d = 0; d < 4; d++) {
                int x = i + dir[d], y = j + dir[d+1];
                if(min(x, y) >= 0 && x < m && y < n && grid[x][y] && !seen[x][y]) 
                    ans += dfs(x, y);
            }
            return ans;
        };
        
        int ans = 0;
        for(int i = 0; i < m; i++) 
            for(int j = 0; j < n; j++) 
                if(grid[i][j] != 0 && !seen[i][j]) 
                    ans = max(ans, dfs(i, j));
        
        return ans;
    }
};
```
