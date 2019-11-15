1139. Largest 1-Bordered Square

Given a 2D grid of `0`s and `1`s, return the number of elements in the largest **square** subgrid that has all `1`s on its **border**, or `0` if such a subgrid doesn't exist in the grid.

 

**Example 1:**

```
Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
Output: 9
```

**Example 2:**

```
Input: grid = [[1,1,0,0]]
Output: 1
```

**Constraints:**

* `1 <= grid.length <= 100`
* `1 <= grid[0].length <= 100`
* `grid[i][j]` is `0` or `1`

# Submissions
---
**Solution 1:**
```
Runtime: 184 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        R = len(grid)
        C = len(grid[0])
        dp_r = [[0] * C for _ in range(R)]
        dp_c = [[0] * C for _ in range(R)]

        maxlen = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] > 0:
                    dp_r[r][c] = (dp_r[r - 1][c] + 1) if r > 0 else 1
                    dp_c[r][c] = (dp_c[r][c - 1] + 1) if c > 0 else 1
                    maxedge = min(dp_r[r][c], dp_c[r][c])
                    res_max = 1
                    for i in range(maxedge, 0, -1):
                        if dp_r[r][c - i + 1] >= i and dp_c[r - i + 1][c] >= i:
                            res_max = i
                            break
                    maxlen = max(maxlen, res_max)

        return maxlen ** 2
```