463. Island Perimeter

You are given a map in form of a two-dimensional integer `grid` where `1` represents land and `0` represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

**Example:**

```
Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:
```

![463_island](img/463_island.png)

# Submissions
---
**Solution 1: (Brute Force)**
```
Runtime: 276 ms
Memory Usage: N/A
```
```python
class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        num = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    if r == 0 or grid[r-1][c] == 0:
                        num += 1
                    if r == m-1 or grid[r+1][c] == 0:
                        num += 1
                    if c == 0 or grid[r][c-1] == 0:
                        num += 1
                    if c == n-1 or grid[r][c+1] == 0:
                        num += 1
        return num
```

**Solution 2: (Groupby)**
```
Runtime: 476 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        h = sum(k for row in grid for k, _ in itertools.groupby(row))
        v = sum(k for col in zip(*grid) for k, _ in itertools.groupby(col))
        return 2*(h+v)
```

**Solution 3: (Brute Force)**
```
Runtime: 212 ms
Memory Usage: 96 MB
```
```c++
class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        if(grid.empty())    return 0;
        int m = grid.size(), n = grid[0].size(), peri = 0;
        
        auto borderLines = [&](int i, int j) -> int {
            int cnt = 0;
            if(i-1 < 0 || grid[i-1][j] == 0)    cnt++;
            if(j+1 >= n || grid[i][j+1] == 0)   cnt++;
            if(i+1 >= m || grid[i+1][j] == 0)   cnt++;
            if(j-1 < 0 || grid[i][j-1] == 0)    cnt++;
            return cnt;
        };
        
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(grid[i][j] == 1)    peri += borderLines(i, j);
            }
        }
        return peri;
    }
};
```