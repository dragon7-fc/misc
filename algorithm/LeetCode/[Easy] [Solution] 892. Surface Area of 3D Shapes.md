892. Surface Area of 3D Shapes

On a `N * N` grid, we place some 1 * 1 * 1 cubes.

Each value `v = grid[i][j]` represents a tower of `v` cubes placed on top of grid cell `(i, j)`.

Return the total surface area of the resulting shapes.

 

**Example 1:**
```
Input: [[2]]
Output: 10
```

**Example 2:**
```
Input: [[1,2],[3,4]]
Output: 34
```

**Example 3:**
```
Input: [[1,0],[0,2]]
Output: 16
```

**Example 4:**
```
Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: 32
```

**Example 5:**
```
Input: [[2,2,2],[2,1,2],[2,2,2]]
Output: 46
```

**Note:**

* `1 <= N <= 50`
* `0 <= grid[i][j] <= 50`

# Solution
---
## Approach 1: Square by Square
**Intuition**

Let's try to count the surface area contributed by `v = grid[i][j]`.

When `v > 0`, the top and bottom surface contributes an area of `2`.

Then, for each side (west side, north side, east side, south side) of the column at `grid[i][j]`, the neighboring cell with value `nv` means our square contributes `max(v - nv, 0)`.

For example, for `grid = [[1, 5]]`, the contribution at `grid[0][1]` is `2 + 5 + 5 + 5 + 4`. The `2` comes from the top and bottom side, the `5` comes from the north, east, and south side; and the `4` comes from the west side, of which `1` unit is covered by the adjacent column.

**Algorithm**

For each `v = grid[r][c] > 0`, count `ans += 2`, plus `ans += max(v - nv, 0)` for each neighboring value `nv` adjacent to `grid[r][c]`.

```python
class Solution(object):
    def surfaceArea(self, grid):
        N = len(grid)

        ans = 0
        for r in xrange(N):
            for c in xrange(N):
                if grid[r][c]:
                    ans += 2
                    for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r,c+1)):
                        if 0 <= nr < N and 0 <= nc < N:
                            nval = grid[nr][nc]
                        else:
                            nval = 0

                        ans += max(grid[r][c] - nval, 0)

        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N^2)$, where $N$ is the number of rows (and columns) in the grid.

* Space Complexity: $O(1)$.

# Submissions
---
**Solution:**
```
Runtime: 116 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        N = len(grid)

        ans = 0
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    ans += 2
                    for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r,c+1)):
                        if 0 <= nr < N and 0 <= nc < N:
                            nval = grid[nr][nc]
                        else:
                            nval = 0

                        ans += max(grid[r][c] - nval, 0)

        return ans
```