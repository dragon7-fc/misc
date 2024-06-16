807. Max Increase to Keep City Skyline

In a 2 dimensional array `grid`, each value `grid[i][j]` represents the height of a building located there. We are allowed to increase the height of any number of buildings, by any amount (the amounts can be different for different buildings). Height 0 is considered to be a building as well. 

At the end, the "skyline" when viewed from all four directions of the grid, i.e. top, bottom, left, and right, must be the same as the skyline of the original grid. A city's skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance. See the following example.

What is the maximum total sum that the height of the buildings can be increased?

**Example:**
```
Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
Output: 35
Explanation: 
The grid is:
[ [3, 0, 8, 4], 
  [2, 4, 5, 7],
  [9, 2, 6, 3],
  [0, 3, 1, 0] ]

The skyline viewed from top or bottom is: [9, 4, 8, 7]
The skyline viewed from left or right is: [8, 7, 9, 3]

The grid after increasing the height of buildings without affecting skylines is:

gridNew = [ [8, 4, 8, 7],
            [7, 4, 7, 7],
            [9, 4, 8, 7],
            [3, 3, 3, 3] ]
```

**Notes:**

* `1 < grid.length = grid[0].length <= 50`.
* All heights `grid[i][j]` are in the range `[0, 100]`.
* All buildings in `grid[i][j]` occupy the entire `grid` cell: that is, they are a 1 x 1 x `grid[i][j]` rectangular prism.

# Solution
---
## Approach #1: Row and Column Maximums [Accepted]
**Intuition and Algorithm**

The skyline looking from the top is `col_maxes = [max(column_0), max(column_1), ...]`. Similarly, the skyline from the left is `row_maxes [max(row_0), max(row_1), ...]`

In particular, each building `grid[r][c]` could become height `min(max(row_r), max(col_c))`, and this is the largest such height. If it were larger, say `grid[r][c] > max(row_r)`, then the part of the skyline `row_maxes = [..., max(row_r), ...]` would change.

These increases are also independent (none of them change the skyline), so we can perform them independently.

```python
class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        row_maxes = [max(row) for row in grid]
        col_maxes = [max(col) for col in zip(*grid)]

        return sum(min(row_maxes[r], col_maxes[c]) - val
                   for r, row in enumerate(grid)
                   for c, val in enumerate(row))
```

**Complexity Analysis**

* Time Complexity: $O(N^2)$, where $N$ is the number of rows (and columns) of the `grid`. We iterate through every cell of the `grid`.

* Space Complexity: $O(N)$, the space used by `row_maxes` and `col_maxes`.

# Submissions
---
**Solution 1: (Row and Column Maximums, Array)**
```
Runtime: 60 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_maxes = [max(row) for row in grid]
        col_maxes = [max(col) for col in zip(*grid)]

        return sum(min(row_maxes[r], col_maxes[c]) - val
                   for r, row in enumerate(grid)
                   for c, val in enumerate(row))
```

**Solution 2: (Prefix sum)**
```
Runtime: 5 ms
Memory: 12.54 MB
```
```c++
class Solution {
public:
    int maxIncreaseKeepingSkyline(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<int> dp(n*n);
        for (int i = 0; i < n; i ++) {
            for (int j = 0; j < n; j ++) {
                dp[i] = max(dp[i], grid[i][j]);
                dp[n+j] = max(dp[n+j], grid[i][j]);
            }
        }
        int ans = 0;
        for (int i = 0; i < n; i ++) {
            for (int j = 0; j < n; j ++) {
                ans += min(dp[i], dp[n+j]) - grid[i][j];
            }
        }
        return ans;
    }
};
```
