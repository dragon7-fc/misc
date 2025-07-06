1162. As Far from Land as Possible

Given an N x N `grid` containing only values `0` and `1`, where `0` represents water and `1` represents land, find a water cell such that its distance to the nearest land cell is maximized and return the distance.

The distance used in this problem is the Manhattan distance: the distance between two cells `(x0, y0)` and `(x1, y1)` is `|x0 - x1|` + `|y0 - y1|`.

If no land or water exists in the grid, return `-1`.

 

**Example 1:**

![1162_1336_ex1.jpg](img/1162_1336_ex1.jpg)
```
Input: [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: 
The cell (1, 1) is as far as possible from all the land with distance 2.
```

**Example 2:**

![1162_1336_ex2.jpg](img/1162_1336_ex2.jpg)
```
Input: [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: 
The cell (2, 2) is as far as possible from all the land with distance 4.
```

**Note:**

* `1 <= grid.length == grid[0].length <= 100`
* `grid[i][j]` is `0` or `1`

# Submissions
---
**Solution 1: (BFS, Graph)**
```
Runtime: 676 ms
Memory Usage: 13.7 MB
```
```python
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        q = collections.deque()
        q = [(r, c) for r in range(R) for c in range(C) if grid[r][c]]
        if len(q) == 0 or len(q) == R**2:
            return -1
        
        def neighbours(r, c):
            for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc
        
        dis = -1
        while q:
            qq = collections.deque()
            for r, c in q:
                for nr, nc in neighbours(r, c):
                    if not grid[nr][nc]:
                        grid[nr][nc] = 1
                        qq += [(nr, nc)]
            q = qq
            dis += 1
            
        return dis
                        
```

**Solution 2: (DP)**

    [1,0,1],
    [0,0,0],
    [1,0,1]

    ->
   |[0,1,0]
   v[1,2,3]
    [0,1,0]

    [0,1,0]
    [1,2,1]^
    [0,1,0]|
        <-
```
Runtime: 63 ms
Memory: 16.6 MB
```
```c++
public:
    int maxDistance(vector<vector<int>>& grid) {
        int rows = grid.size();
        // Although it's a square matrix, using different variable for readability.
        int cols = grid[0].size();

        // Maximum manhattan distance possible + 1.
        const int MAX_DISTANCE = rows + cols + 1;
        
        // First pass: check for left and top neighbours
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j]) {
                    // Distance of land cells will be 0.
                    grid[i][j] = 0;
                } else {
                    grid[i][j] = MAX_DISTANCE;
                    // Check left and top cell distances if they exist and update the current cell distance.
                    grid[i][j] = min(grid[i][j], min(i > 0 ? grid[i - 1][j] + 1 : MAX_DISTANCE,
                                                     j > 0 ? grid[i][j - 1] + 1 : MAX_DISTANCE));
                }
            }
        }

        // Second pass: check for right and bottom neighbours.
        int ans = INT_MIN;
        for (int i = rows - 1; i >= 0; i--) {
            for (int j = cols - 1; j >= 0; j--) {
                // Check the right and bottom cell distances if they exist and update the current cell distance.
                grid[i][j] = min(grid[i][j], min(i < rows - 1 ? grid[i + 1][j] + 1 : MAX_DISTANCE,
                                                 j < cols - 1 ? grid[i][j + 1] + 1 : MAX_DISTANCE));
                ans = max(ans, grid[i][j]);
            }
        }
        
        // If ans is 1, it means there is no water cell,
        // If ans is MAX_DISTANCE, it implies no land cell.
        return ans == 0 || ans == MAX_DISTANCE ? -1 : ans;
    }
};
```

**Solution 3: (BFS)**
```
Runtime: 23 ms, Beats 32.70%
Memory: 25.62 MB, Beats 41.50%
```
```c++
class Solution {
    int dd[5] = {0, 1, 0, -1, 0};
public:
    int maxDistance(vector<vector<int>>& grid) {
        int n = grid.size(), i, j, sz, d, nx, ny, k = 0;
        vector<vector<int>> visited(n, vector<int>(n));
        queue<array<int,2>> q;
        for (i = 0; i < n; i ++) {
            for (j = 0; j < n; j ++) {
                if (grid[i][j]) {
                    q.push({i, j});
                    visited[i][j] = 1;
                }
            }
        }
        while (q.size()) {
            sz = q.size();
            for (i = 0; i < sz; i ++) {
                auto [x, y] = q.front();
                q.pop();
                for (d = 0; d < 4; d ++) {
                    nx = x + dd[d];
                    ny = y + dd[d+1];
                    if (0 <= nx && nx < n && 0 <= ny && ny < n && grid[nx][ny] == 0 && !visited[nx][ny]) {
                        visited[nx][ny] = 1;
                        q.push({nx, ny});
                    }
                }
            }
            if (!q.size()) {
                break;
            }
            k += 1;
        }
        return k ? k : -1;
    }
};
```
