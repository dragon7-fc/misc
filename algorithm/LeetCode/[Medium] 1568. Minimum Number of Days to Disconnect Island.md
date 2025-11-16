1568. Minimum Number of Days to Disconnect Island

Given a 2D `grid` consisting of `1`s (land) and `0`s (water).  An island is a maximal 4-directionally (horizontal or vertical) connected group of 1s.

The `grid` is said to be **connected** if we have **exactly one island**, otherwise is said **disconnected**.

In one day, we are allowed to change any single land cell (`1`) into a water cell (`0`).

Return the minimum number of days to disconnect the grid.

 

**Example 1:**

![1568_1926_island.png](img/1568_1926_island.png)
```
Input: grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
Output: 2
Explanation: We need at least 2 days to get a disconnected grid.
Change land grid[1][1] and grid[0][2] to water and get 2 disconnected island.
```

**Example 2:**
```
Input: grid = [[1,1]]
Output: 2
Explanation: Grid of full water is also disconnected ([[1,1]] -> [[0,0]]), 0 islands.
```

**Example 3:**
```
Input: grid = [[1,0,1,0]]
Output: 0
```

**Example 4:**
```
Input: grid = [[1,1,0,1,1],
               [1,1,1,1,1],
               [1,1,0,1,1],
               [1,1,0,1,1]]
Output: 1
```

**Example 5:**
```
Input: grid = [[1,1,0,1,1],
               [1,1,1,1,1],
               [1,1,0,1,1],
               [1,1,1,1,1]]
Output: 2
```

**Constraints:**

* `1 <= grid.length, grid[i].length <= 30`
* `grid[i][j] is 0 or 1`.

# Submissions
---
**Solution 1: (Union-Find)**

**Idea**

* How to make the grid disconnected?

    We can tell from the first official example that, the worst situation we may get into is to take 2 steps and separate a single island out.
    More specifically, there are 3 situation.

    1. The number of island on the grid is not 1.
        
        return 0
    1. The number of island on the grid is 1, and we can break them into 2 islands within 1 step.
        
        return 1
    1. The number of island on the grid is 1, and we cannot break them into 2 islands within 1 step.
        
        return 2, because no matter what, we can always separate 1 island out within 2 steps
* How to count the number of islands on the grid

    There are many different ways like DFS, Union Find. I use union find here.

**Complexity**

* Time: O(n^4)
* Space: O(n^2)

```
Runtime: 5784 ms
Memory Usage: 21.8 MB
```
```python
class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def countIsland():
            roots = {(i,j):(i,j) for i in range(m) for j in range(n)}
            def find(x):
                if roots[x] != x: roots[x] = find(roots[x])
                return roots[x]                    
            
            def unite(x, y):
                roots[find(x)] = find(y)
                
            for i in range(m):
                for j in range(n):
                    if grid[i][j]:
                        if i < m - 1 and grid[i + 1][j]:
                            unite((i, j), (i + 1, j))
                        if j < n - 1 and grid[i][j + 1]:
                            unite((i, j), (i, j + 1))
            return len(set(find((i, j)) for i in range(m) for j in range(n) if grid[i][j]))                            
        
        if countIsland() != 1:
            return 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    grid[i][j] = 0
                    if countIsland() != 1:
                        return 1
                    grid[i][j] = 1
        return 2
```

**Solution 2: (Brute Force, O((m * n)^2))**
```
Runtime: 159 ms
Memory: 20.37 MB
```
```c++
class Solution {
    // Directions for adjacent cells: right, left, down, up
    const vector<vector<int>> DIRECTIONS = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};



    int countIslands(vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();
        vector<vector<bool>> visited(rows, vector<bool>(cols, false));
        int islandCount = 0;

        // Iterate through all cells
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                // Found new island
                if (!visited[row][col] && grid[row][col] == 1) {
                    exploreIsland(grid, row, col, visited);
                    islandCount++;
                }
            }
        }
        return islandCount;
    }

    // Helper method to explore all cells of an island
    void exploreIsland(vector<vector<int>>& grid, int row, int col,
                       vector<vector<bool>>& visited) {
        visited[row][col] = true;

        // Check all adjacent cells
        for (const auto& direction : DIRECTIONS) {
            int newRow = row + direction[0];
            int newCol = col + direction[1];
            // Explore if valid land cell
            if (isValidLandCell(grid, newRow, newCol, visited)) {
                exploreIsland(grid, newRow, newCol, visited);
            }
        }
    }

    bool isValidLandCell(const vector<vector<int>>& grid, int row, int col,
                         const vector<vector<bool>>& visited) {
        int rows = grid.size();
        int cols = grid[0].size();
        // Check bounds, land, and not visited
        return row >= 0 && col >= 0 && row < rows && col < cols &&
               grid[row][col] == 1 && !visited[row][col];
    }
public:
    int minDays(vector<vector<int>>& grid) {
         int rows = grid.size();
        int cols = grid[0].size();

        // Count initial islands
        int initialIslandCount = countIslands(grid);

        // Already disconnected or no land
        if (initialIslandCount != 1) {
            return 0;
        }

        // Try removing each land cell
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                if (grid[row][col] == 0) continue;  // Skip water

                // Temporarily change to water
                grid[row][col] = 0;
                int newIslandCount = countIslands(grid);

                // Check if disconnected
                if (newIslandCount != 1) return 1;

                // Revert change
                grid[row][col] = 1;
            }
        }

        return 2;
    }
};
```

**Solution 3: (Tarjan's Algorithm, O(m * n))**
```
Runtime: 5 ms
Memory: 12.48 MB
```
```c++
class Solution {
    // Directions for adjacent cells: right, down, left, up
    const vector<vector<int>> DIRECTIONS = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

    struct ArticulationPointInfo {
        bool hasArticulationPoint;
        int time;

        ArticulationPointInfo(bool hasArticulationPoint, int time)
            : hasArticulationPoint(hasArticulationPoint), time(time) {}
    };
    void findArticulationPoints(vector<vector<int>>& grid, int row, int col,
                                vector<vector<int>>& discoveryTime,
                                vector<vector<int>>& lowestReachable,
                                vector<vector<int>>& parentCell,
                                ArticulationPointInfo& apInfo) {
        int rows = grid.size(), cols = grid[0].size();
        discoveryTime[row][col] = apInfo.time;
        apInfo.time++;
        lowestReachable[row][col] = discoveryTime[row][col];
        int children = 0;

        // Explore all adjacent cells
        for (const auto& direction : DIRECTIONS) {
            int newRow = row + direction[0];
            int newCol = col + direction[1];
            if (isValidLandCell(grid, newRow, newCol)) {
                if (discoveryTime[newRow][newCol] == -1) {
                    children++;
                    parentCell[newRow][newCol] =
                        row * cols + col;  // Set parent
                    findArticulationPoints(grid, newRow, newCol, discoveryTime,
                                           lowestReachable, parentCell, apInfo);

                    // Update lowest reachable time
                    lowestReachable[row][col] =
                        min(lowestReachable[row][col],
                            lowestReachable[newRow][newCol]);

                    // Check for articulation point condition
                    if (lowestReachable[newRow][newCol] >=
                            discoveryTime[row][col] &&
                        parentCell[row][col] != -1) {
                        apInfo.hasArticulationPoint = true;
                    }
                } else if (newRow * cols + newCol != parentCell[row][col]) {
                    // Update lowest reachable time for back edge
                    lowestReachable[row][col] =
                        min(lowestReachable[row][col],
                            discoveryTime[newRow][newCol]);
                }
            }
        }

        // Root of DFS tree is an articulation point if it has more than one
        // child
        if (parentCell[row][col] == -1 && children > 1) {
            apInfo.hasArticulationPoint = true;
        }
    }

    // Check if the given cell is a valid land cell
    bool isValidLandCell(const vector<vector<int>>& grid, int row, int col) {
        int rows = grid.size(), cols = grid[0].size();
        return row >= 0 && col >= 0 && row < rows && col < cols &&
               grid[row][col] == 1;
    }
public:
    int minDays(vector<vector<int>>& grid) {
        int rows = grid.size(), cols = grid[0].size();
        ArticulationPointInfo apInfo(false, 0);
        int landCells = 0, islandCount = 0;

        // Arrays to store information for each cell
        vector<vector<int>> discoveryTime(
            rows,
            vector<int>(cols, -1));  // Time when a cell is first discovered
        vector<vector<int>> lowestReachable(
            rows,
            vector<int>(cols, -1));  // Lowest discovery time reachable from the
                                     // subtree rooted at this cell
        vector<vector<int>> parentCell(
            rows, vector<int>(cols, -1));  // Parent of each cell in DFS tree

        // Traverse the grid to find islands and articulation points
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 1) {
                    landCells++;
                    if (discoveryTime[i][j] == -1) {  // If not yet visited
                        // Start DFS for a new island
                        findArticulationPoints(grid, i, j, discoveryTime,
                                               lowestReachable, parentCell,
                                               apInfo);
                        islandCount++;
                    }
                }
            }
        }
        
        // Determine the minimum number of days to disconnect the grid
        if (islandCount == 0 || islandCount >= 2)
            return 0;                  // Already disconnected or no land
        if (landCells == 1) return 1;  // Only one land cell
        if (apInfo.hasArticulationPoint)
            return 1;  // An articulation point exists
        return 2;      // Need to remove any two land cells
    }
};
```

**Solution 4: (BFS, Brute Force)**
```
Runtime: 95 ms, Beats 21.19%
Memory: 35.52 MB, Beats 18.81%
```
```c++
class Solution {
    int dd[5] = {0, 1, 0, -1, 0};
    int bfs(vector<vector<int>> &grid) {
        int m = grid.size(), n = grid[0].size(), i, j, d, ni, nj, rst = 0;
        vector<vector<bool>> visited(m, vector<bool>(n));
        for (i = 0; i < m; i ++) {
            for (j = 0; j < n; j ++) {
                if (grid[i][j] == 1 && !visited[i][j]) {
                    rst += 1;
                    visited[i][j] = true;
                    queue<array<int, 2>> q;
                    q.push({i, j});
                    while (q.size()) {
                        auto [ci, cj] = q.front();
                        q.pop();
                        for (d = 0; d < 4; d ++) {
                            ni = ci + dd[d];
                            nj = cj + dd[d + 1];
                            if (0 <= ni && ni < m && 0 <= nj && nj < n && grid[ni][nj] == 1 && !visited[ni][nj]) {
                                visited[ni][nj] = true;
                                q.push({ni, nj});
                            }
                        }
                    }
                }
            }
        }
        return rst;
    }
public:
    int minDays(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size(), i, j, k;
        k = bfs(grid);
        if (k != 1) {
            return 0;
        }
        for (i = 0; i < m; i ++) {
            for (j = 0; j < n; j ++) {
                if (grid[i][j] == 1) {
                    grid[i][j] = 0;
                    k = bfs(grid);
                    if (k != 1) {
                        return 1;
                    }
                    grid[i][j] = 1;
                }
            }
        }
        return 2;
    }
};
```
