200. Number of Islands

Given a 2d grid map of `'1'`s (land) and `'0'`s (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

**Example 1:**

```
Input:
11110
11010
11000
00000

Output: 1
```

**Example 2:**

```
Input:
11000
11000
00100
00011

Output: 3
```

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 160 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        R, C = len(grid), len(grid[0])
        def neighbours(r, c):
            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc
        def dfs(r, c):
            grid[r][c] = '0'
            for nr, nc in neighbours(r, c):
                if grid[nr][nc] == '1':
                    dfs(nr, nc)
        island = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1':
                    island += 1
                    dfs(r, c)

        return island
```

**Solution 2: (BFS)**
```
Runtime: 160 ms
Memory Usage: 13.7 MB
```
```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def is_island(x, y):
            if x >= len(grid) or x < 0:
                return False
            if y >= len(grid[0]) or y < 0 :
                return False
            if grid[x][y] == '0':
                return False
            return True
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0':
                    continue
                else:
                    queue = collections.deque([(i, j)])
                    while queue:
                        x, y = queue.popleft()
                        for dx, dy in delta:
                            new_x, new_y = x + dx, y + dy
                            if is_island(new_x, new_y):
                                queue.append((new_x, new_y))
                                grid[new_x][new_y] = '0'
                    ans += 1 
        return ans
```

**Solution 3: (Union Find)**
```
Runtime: 248 ms
Memory Usage: 15.6 MB
```
```python
class DSU:
    def __init__(self, N):
        self.p = [_ for _ in range(N)]

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr
        
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        R, C = len(grid), len(grid[0])
        dsu = DSU(R*C)
        
        def neighbours(r, c):
            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc
        water = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1':
                    for nr, nc in neighbours(r, c):
                        if grid[nr][nc] == '1':
                            dsu.union(r*C + c, nr*C + nc)
        
        return len(set([dsu.find(r*C + c) for r in range(R) for c in range(C) if grid[r][c] == '1']))
```

**Solution 4: (DFS)**
```
Runtime: 12 ms
Memory Usage: 9.4 MB
```
```c++
class Solution {
private:
  void dfs(vector<vector<char>>& grid, int r, int c) {
    int nr = grid.size();
    int nc = grid[0].size();

    grid[r][c] = '0';
    if (r - 1 >= 0 && grid[r-1][c] == '1') dfs(grid, r - 1, c);
    if (r + 1 < nr && grid[r+1][c] == '1') dfs(grid, r + 1, c);
    if (c - 1 >= 0 && grid[r][c-1] == '1') dfs(grid, r, c - 1);
    if (c + 1 < nc && grid[r][c+1] == '1') dfs(grid, r, c + 1);
  }
    
public:
    int numIslands(vector<vector<char>>& grid) {
        int nr = grid.size();
        if (!nr) return 0;
        int nc = grid[0].size();

        int num_islands = 0;
        for (int r = 0; r < nr; ++r) {
          for (int c = 0; c < nc; ++c) {
            if (grid[r][c] == '1') {
              ++num_islands;
              dfs(grid, r, c);
            }
          }
        }

        return num_islands;
    }
};
```

**Solution 5: (BFS)**
```
Runtime: 8 ms
Memory Usage: 10.1 MB
```
```c++
class Solution {
    
public:
    int numIslands(vector<vector<char>>& grid) {
        int nr = grid.size();
        if (!nr) return 0;
        int nc = grid[0].size();

        int num_islands = 0;
        for (int r = 0; r < nr; ++r) {
          for (int c = 0; c < nc; ++c) {
            if (grid[r][c] == '1') {
              ++num_islands;
              grid[r][c] = '0'; // mark as visited
              queue<pair<int, int>> neighbors;
              neighbors.push({r, c});
              while (!neighbors.empty()) {
                auto rc = neighbors.front();
                neighbors.pop();
                int row = rc.first, col = rc.second;
                if (row - 1 >= 0 && grid[row-1][col] == '1') {
                  neighbors.push({row-1, col}); grid[row-1][col] = '0';
                }
                if (row + 1 < nr && grid[row+1][col] == '1') {
                  neighbors.push({row+1, col}); grid[row+1][col] = '0';
                }
                if (col - 1 >= 0 && grid[row][col-1] == '1') {
                  neighbors.push({row, col-1}); grid[row][col-1] = '0';
                }
                if (col + 1 < nc && grid[row][col+1] == '1') {
                  neighbors.push({row, col+1}); grid[row][col+1] = '0';
                }
              }
            }
          }
        }

        return num_islands;
    }
};
```