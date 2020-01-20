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
**Solution 1: (BFS)**
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