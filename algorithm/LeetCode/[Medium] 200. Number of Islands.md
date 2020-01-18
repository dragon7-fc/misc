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