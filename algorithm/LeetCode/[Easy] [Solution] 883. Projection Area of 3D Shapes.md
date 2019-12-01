883. Projection Area of 3D Shapes

On a `N * N` grid, we place some `1 * 1 * 1` cubes that are axis-aligned with the x, y, and z axes.

Each value `v = grid[i][j]` represents a tower of `v` cubes placed on top of grid cell `(i, j)`.

Now we view the projection of these cubes onto the xy, yz, and zx planes.

A projection is like a shadow, that maps our 3 dimensional figure to a 2 dimensional plane. 

Here, we are viewing the "shadow" when looking at the cubes from the top, the front, and the side.

Return the total area of all three projections.

**Example 1:**
```
Input: [[2]]
Output: 5
```

**Example 2:**
```
Input: [[1,2],[3,4]]
Output: 17
Explanation: 
Here are the three projections ("shadows") of the shape made with each axis-aligned plane.
```

![883_shadow.png](img/883_shadow.png)

**Example 3:**
```
Input: [[1,0],[0,2]]
Output: 8
```

**Example 4:**
```
Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: 14
```

**Example 5:**
```
Input: [[2,2,2],[2,1,2],[2,2,2]]
Output: 21
```

**Note:**

* 1 <= grid.length = grid[0].length <= 50
* 0 <= grid[i][j] <= 50

# Solution
---
## Approach 1: Mathematical
**Intuition and Algorithm**

From the top, the shadow made by the shape will be 1 square for each non-zero value.

From the side, the shadow made by the shape will be the largest value for each row in the grid.

From the front, the shadow made by the shape will be the largest value for each column in the grid.

**Example**

With the example `[[1,2],[3,4]]`:

* The shadow from the top will be `4`, since there are four non-zero values in the grid;

* The shadow from the side will be `2 + 4`, since the maximum value of the first row is `2`, and the maximum value of the second row is `4`;

* The shadow from the front will be `3 + 4`, since the maximum value of the first column is `3`, and the maximum value of the second column is `4`.

```python
class Solution:
    def projectionArea(self, grid):
        N = len(grid)
        ans = 0

        for i in xrange(N):
            best_row = 0  # max of grid[i][j]
            best_col = 0  # max of grid[j][i]
            for j in xrange(N):
                if grid[i][j]: ans += 1  # top shadow
                best_row = max(best_row, grid[i][j])
                best_col = max(best_col, grid[j][i])

            ans += best_row + best_col

        return ans

        """ Alternative solution:
        ans = sum(map(max, grid))
        ans += sum(map(max, zip(*grid)))
        ans += sum(v > 0 for row in grid for v in row)
        """
```

**Complexity Analysis**

* Time Complexity: $O(N^2)$, where $N$ is the length of grid.

* Space Complexity: $O(1)$.

# Submissions
---
**Solution 1:**
```
Runtime: 68 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        ans = sum(map(max, grid))
        ans += sum(map(max, zip(*grid)))
        ans += sum(v > 0 for row in grid for v in row)
        return ans
```