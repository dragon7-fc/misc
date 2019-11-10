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
**Solution 1:**
```
Runtime: 112 ms
Memory Usage: N/A
```
```python
class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        def chk_island(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                   and grid[r][c] == '1'):
                return
            grid[r][c] = '0'
            chk_island(r-1, c)
            chk_island(r+1, c)
            chk_island(r, c-1)
            chk_island(r, c+1)
        
        island = 0
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    island += 1
                    chk_island(r, c)
        
        return island
```