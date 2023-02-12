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

**Solution 2: (BFS)**
```
Runtime: 77 ms
Memory: 19.8 MB
```
```c++
class Solution {
public:
    int maxDistance(vector<vector<int>>& grid) {
        int N = grid.size(), sz, nr, nc, ans = -1;
        int diff[] = {0, 1, 0, -1};
        queue<tuple<int, int>> q;
        for (int r = 0; r < N; r ++)
            for (int c = 0; c < N; c ++)
                if (grid[r][c]) {
                    q.push({r, c});
                }
        if (q.size() == 0 || q.size() == N*N) {
            return -1;
        }
        while (!q.empty()) {
            sz = q.size();
            for (int i = 0; i < sz; i ++) {
                auto [r, c] = q.front();
                q.pop();
                for (int d = 0; d < 4; d ++) {
                    nr = r + diff[d];
                    nc = c + diff[(d+1)%4];
                    if (0 <= nr && nr < N && 0 <= nc && nc < N) {
                        if (grid[nr][nc] == 0) {
                            grid[nr][nc] = 1;
                            q.push({nr, nc});
                        }
                    }
                }
            }
            ans += 1;
        }
        return ans;
    }
};
```

**Solution 3: (DP)**
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
