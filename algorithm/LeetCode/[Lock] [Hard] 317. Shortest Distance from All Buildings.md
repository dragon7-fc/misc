317. Shortest Distance from All Buildings

You are given an `m x n` grid `grid` of values `0`, `1`, or `2`, where:

* each `0` marks an empty land that you can pass by freely,
* each `1` marks a building that you cannot pass through, and
* each `2` marks an obstacle that you cannot pass through.

You want to build a house on an empty land that reaches all buildings in the shortest total travel distance. You can only move up, down, left, and right.

Return the shortest travel distance for such a house. If it is not possible to build such a house according to the above rules, return `-1`.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

 

**Example 1:**

![317_buildings-grid.jpg](img/317_buildings-grid.jpg)
```
Input: grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
Output: 7
Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2).
The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal.
So return 7.
```

**Example 2:**
```
Input: grid = [[1,0]]
Output: 1
```

**Example 3:**
```
Input: grid = [[1]]
Output: -1
```

**Constraints:**

* `m == grid.length`
* `n == grid[i].length`
* 1` <= m, n <= 100`
* `grid[i][j]` is either `0`, `1`, or `2`.
* There will be at least one building in the `grid`.

# Submissions
---
**Solution 1: (BFS)**
```
Runtime: 1196 ms
Memory Usage: 14.7 MB
```
```python
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        # H: # of homes
        # N: x-axis length
        # M: y-axis length

        ROAD, HOME, OBSTACLE = 0, 1, 2
        COUNT, SUM = 0, 1
        
        xLimit, yLimit = len(grid), len(grid[0])
        # (count, sum)
        dp = [[[0, 0] for _ in range(yLimit)] for _ in range(xLimit)] # Space O(N * M)
        numOfHomes = 0
        for x in range(xLimit):
            for y in range(yLimit):
                if grid[x][y] == HOME: # Time O(H * N * M)
                    numOfHomes += 1
                    # Start BFS
                    visited, queue = set(), [(0, x, y)]
                    while len(queue) > 0:
                        curLevel, curX, curY = queue.pop(0)
                        if (curX, curY) in visited:
                            continue
                        visited.add((curX, curY))
                        dp[curX][curY][SUM] += curLevel
                        dp[curX][curY][COUNT] += 1
                        #Check up, down, left, right
                        for nextX, nextY in [(curX + 1, curY), (curX - 1, curY), (curX, curY - 1), (curX, curY + 1)]:
                            if 0 <= nextX < xLimit and 0 <= nextY < yLimit and grid[nextX][nextY] == ROAD and (nextX, nextY) not in visited:
                                queue.append((curLevel + 1, nextX, nextY))

        res = float('inf')
        for x in range(xLimit):
            for y in range(yLimit):
                if dp[x][y][COUNT] == numOfHomes and dp[x][y][SUM] > 0:
                    res = min(res, dp[x][y][SUM])
        return res if res != float('inf') else -1
```

**Solution 2: (BFS)**
```
Runtime: 2473 ms, Beats 13.67%
Memory: 468.22 MB, Beats 9.57%
```
```c++
class Solution {
    int dd[5] = {0, 1, 0, -1, 0};
public:
    int shortestDistance(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size(), i, j, k = 0, ii, nr, nc, cur, ans = INT_MAX;
        vector<vector<unordered_map<int,int>>> dp(m, vector<unordered_map<int,int>>(n));
        queue<tuple<int,int,int,int>> q;
        for (i = 0; i < m; i ++) {
            for (j = 0; j < n; j ++) {
                if (grid[i][j] == 1) {
                    q.push({i, j, k, 0});
                    dp[i][j][k] = 0;
                    k += 1;
                }
            }
        }
        if (k == m*n) {
            return -1;
        }
        while (q.size()) {
            auto [r, c, f, d] = q.front();
            q.pop();
            if (grid[r][c] == 0 && dp[r][c].size() == k) {
                cur = 0;
                for (auto [_, cd]: dp[r][c]) {
                    cur += cd;
                }
                ans = min(ans, cur);
            }
            for (ii = 0; ii < 4; ii ++) {
                nr = r + dd[ii];
                nc = c + dd[ii+1];
                if (0 <= nr && nr < m && 0 <= nc && nc < n && grid[nr][nc] == 0 && !dp[nr][nc].count(f)) {
                    dp[nr][nc][f] = d+1;
                    q.push({nr, nc, f, d+1});
                }
            }
        }
        return ans != INT_MAX ? ans : -1;
    }
};
```

**Solution 2: (BFS)**
```
Runtime: 151 ms, Beats 95.15%
Memory: 48.82 MB, Beats 86.69%
```
```c++
class Solution {
public:
    int shortestDistance(vector<vector<int>>& grid) {
        // Next four directions.
        int dirs[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        
        int rows = grid.size();
        int cols = grid[0].size();
        
        // Total Mtrix to store total distance sum for each empty cell.
        vector<vector<int>> total(rows, vector<int> (cols, 0));

        int emptyLandValue = 0;
        int minDist = INT_MAX;

        for (int row = 0; row < rows; ++row) {
            for (int col = 0; col < cols; ++col) {

                // Start a bfs from each house.
                if (grid[row][col] == 1) {
                    minDist = INT_MAX;

                    // Use a queue to perform a BFS, starting from the cell located at (row, col).
                    queue<pair<int, int>> q;
                    q.push({ row, col });
                    
                    int steps = 0;

                    while (!q.empty()) {
                        steps++;

                        for (int level = q.size(); level > 0; --level) {
                            auto curr = q.front();
                            q.pop();

                            for (auto& dir : dirs) {
                                int nextRow = curr.first + dir[0];
                                int nextCol = curr.second + dir[1];

                                // For each cell with the value equal to empty land value
                                // add distance and decrement the cell value by 1.
                                if (nextRow >= 0 && nextRow < rows &&
                                    nextCol >= 0 && nextCol < cols &&
                                    grid[nextRow][nextCol] == emptyLandValue) {
                                    grid[nextRow][nextCol]--;
                                    total[nextRow][nextCol] += steps;

                                    q.push({ nextRow, nextCol });
                                    minDist = min(minDist, total[nextRow][nextCol]);
                                }
                            }
                        }
                    }

                    // Decrement empty land value to be searched in next iteration.
                    emptyLandValue--;
                }
            }
        }

        return minDist == INT_MAX ? -1 : minDist;
    }
};
```
