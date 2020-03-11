840. Magic Squares In Grid

A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers **from 1 to 9** such that each row, column, and both diagonals all have the same sum.

Given an `grid` of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).

**Example 1:**
```
Input: [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]
Output: 1
Explanation: 
The following subgrid is a 3 x 3 magic square:
438
951
276

while this one is not:
384
519
762

In total, there is only one magic square inside the given grid.
```

**Note:**

1. 1 <= grid.length <= 10
1. 1 <= grid[0].length <= 10
1. 0 <= grid[i][j] <= 15

# Solution
---
## Approach #1: Brute Force [Accepted]
**Intuition and Algorithm**

Let's check every 3x3 grid individually. For each grid, all numbers must be unique and between 1 and 9; plus every row, column, and diagonal must have the same sum.

**Extra Credit**

We could also include an if `grid[r+1][c+1] != 5`: continue check into our code, helping us skip over our `for r... for c...` for loops faster. This is based on the following observations:

* The sum of the grid must be 45, as it is the sum of the distinct values from 1 to 9.
* Each horizontal and vertical line must add up to 15, as the sum of 3 of these lines equals the sum of the whole grid.
* The diagonal lines must also sum to 15, by definition of the problem statement.
* Adding the 12 values from the four lines that cross the center, these 4 lines add up to 60; but they also add up to the entire grid (45), plus 3 times the middle value. This implies the middle value is 5.

```python
class Solution(object):
    def numMagicSquaresInside(self, grid):
        R, C = len(grid), len(grid[0])

        def magic(a,b,c,d,e,f,g,h,i):
            return (sorted([a,b,c,d,e,f,g,h,i]) == range(1, 10) and
                (a+b+c == d+e+f == g+h+i == a+d+g ==
                 b+e+h == c+f+i == a+e+i == c+e+g == 15))

        ans = 0
        for r in xrange(R-2):
            for c in xrange(C-2):
                if grid[r+1][c+1] != 5: continue  # optional skip
                if magic(grid[r][c], grid[r][c+1], grid[r][c+2],
                         grid[r+1][c], grid[r+1][c+1], grid[r+1][c+2],
                         grid[r+2][c], grid[r+2][c+1], grid[r+2][c+2]):
                    ans += 1
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(R*C)$, where $R, C$ are the number of rows and columns in the given grid.

* Space Complexity: $O(1)$.

# Submissions
---
**Solution: (Brute Force)**
```
Runtime: 40 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        def magic(a,b,c,d,e,f,g,h,i):
            return (sorted([a,b,c,d,e,f,g,h,i]) == list(range(1, 10)) and
                (a+b+c == d+e+f == g+h+i == a+d+g ==
                 b+e+h == c+f+i == a+e+i == c+e+g == 15))

        ans = 0
        for r in range(R-2):
            for c in range(C-2):
                if grid[r+1][c+1] != 5: continue  # optional skip
                if magic(grid[r][c], grid[r][c+1], grid[r][c+2],
                         grid[r+1][c], grid[r+1][c+1], grid[r+1][c+2],
                         grid[r+2][c], grid[r+2][c+1], grid[r+2][c+2]):
                    ans += 1
        return ans
```