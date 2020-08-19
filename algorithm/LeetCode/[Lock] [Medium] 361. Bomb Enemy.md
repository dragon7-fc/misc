361. Bomb Enemy

Given a 2D grid, each cell is either a wall `'W'`, an enemy `'E'` or empty `'0'` (the number zero), return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
Note: You can only put the bomb at an empty cell.

**Example:**
```
Input: [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
Output: 3 
Explanation: For the given grid,

0 E 0 0 
E 0 W E 
0 E 0 0

Placing a bomb at (1,1) kills 3 enemies.
```

# Submissions
---
**Solution 2: (Prefix Sum)**
```
Runtime: 480 ms
Memory Usage: 16 MB
```
```python
Runtime: 480 ms
Memory Usage: 16 MB
```
```python
class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        R, C = len(grid), len(grid[0])
        left, down = [[0]*(C+2) for _ in range(R+2)], [[0]*(C+2) for _ in range(R+1)]
        for r in range(R):
            for c in range(C):
                if grid[r][c] != 'W':
                    left[r+1][c+1] = left[r+1][c] + (1 if grid[r][c] == 'E' else 0)
                    down[r+1][c+1] = down[r][c+1] + (1 if grid[r][c] == 'E' else 0)
                else:
                    left[r+1][c+1] = down[r+1][c+1] =  0
        right, up = [[0]*(C+2) for _ in range(R+2)], [[0]*(C+2) for _ in range(R+2)]
        for r in range(R-1, -1, -1):
            for c in range(C-1, -1, -1):
                if grid[r][c] != 'W':
                    right[r+1][c+1] = right[r+1][c+2] + (1 if grid[r][c] == 'E' else 0)
                    up[r+1][c+1] = up[r+2][c+1] + (1 if grid[r][c] == 'E' else 0)
                else:
                    right[r+1][c+1] = up[r+1][c+1] = 0
        ans = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '0':
                    ans = max(ans, left[r+1][c] + right[r+1][c+2] + up[r+2][c+1] + down[r][c+1])
        
        return ans
        
                    
                    
```