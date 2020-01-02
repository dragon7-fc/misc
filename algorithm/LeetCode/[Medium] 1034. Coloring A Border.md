1034. Coloring A Border

Given a 2-dimensional `grid` of integers, each value in the grid represents the color of the grid square at that location.

Two squares belong to the same connected component if and only if they have the same color and are next to each other in any of the 4 directions.

The border of a connected component is all the squares in the connected component that are either 4-directionally adjacent to a square not in the component, or on the boundary of the grid (the first or last row or column).

Given a square at location `(r0, c0)` in the grid and a `color`, color the border of the connected component of that square with the given `color`, and return the final `grid`.

 

**Example 1:**
```
Input: grid = [[1,1],[1,2]], r0 = 0, c0 = 0, color = 3
Output: [[3, 3], [3, 2]]
```

**Example 2:**
```
Input: grid = [[1,2,2],[2,3,2]], r0 = 0, c0 = 1, color = 3
Output: [[1, 3, 3], [2, 3, 3]]
```

**Example 3:**
```
Input: grid = [[1,1,1],[1,1,1],[1,1,1]], r0 = 1, c0 = 1, color = 2
Output: [[2, 2, 2], [2, 1, 2], [2, 2, 2]]
```

**Note:**

* `1 <= grid.length <= 50`
* `1 <= grid[0].length <= 50`
* `1 <= grid[i][j] <= 1000`
* `0 <= r0 < grid.length`
* `0 <= c0 < grid[0].length`
* `1 <= color <= 1000`

# Submissions
---
**Solution 1:**
```
Runtime: 140 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        R,C = len(grid),len(grid[0])
        
        seen = set()
        ans = [row[:] for row in grid]
        
        def neighbours(r, c):
            for nr,nc in ((r, c+1),(r, c-1),(r-1, c),(r+1, c)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc
                
        def dfs(r, c):
            if (r,c) in seen:
                return 
            if grid[r][c] == orig:
                seen.add((r, c))
                if r in (0, R-1) or c in (0, C-1):
                    ans[r][c] = color
                for nr, nc in neighbours(r, c):
                    if grid[nr][nc] != orig:
                        ans[r][c] = color
                        break
            else:
                return 
            
            for nr, nc in neighbours(r,c):
                dfs(nr, nc)
                
        orig = grid[r0][c0]
        dfs(r0, c0)
        return ans
```