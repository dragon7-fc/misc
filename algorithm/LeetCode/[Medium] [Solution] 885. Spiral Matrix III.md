885. Spiral Matrix III

On a 2 dimensional grid with `R` rows and `C` columns, we start at `(r0, c0)` facing east.

Here, the north-west corner of the grid is at the first row and column, and the south-east corner of the grid is at the last row and column.

Now, we walk in a clockwise spiral shape to visit every position in this grid. 

Whenever we would move outside the boundary of the grid, we continue our walk outside the grid (but may return to the grid boundary later.) 

Eventually, we reach all `R * C` spaces of the grid.

Return a list of coordinates representing the positions of the grid in the order they were visited.

 

**Example 1:**
```
Input: R = 1, C = 4, r0 = 0, c0 = 0
Output: [[0,0],[0,1],[0,2],[0,3]]
```

![885_example_1.png](img/885_example_1.png) 

**Example 2:**
```
Input: R = 5, C = 6, r0 = 1, c0 = 4
Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
```

![885_example_2.png](img/885_example_2.png)

**Note:**

1. `1 <= R <= 100`
1. `1 <= C <= 100`
1. `0 <= r0 < R`
1. `0 <= c0 < C`

# Solution
---
## Approach 1: Walk in a Spiral
**Intuition**

We can walk in a spiral shape from the starting square, ignoring whether we stay in the grid or not. Eventually, we must have reached every square in the grid.

**Algorithm**

Examining the lengths of our walk in each direction, we find the following pattern: 1, 1, 2, 2, 3, 3, 4, 4, ... That is, we walk 1 unit east, then 1 unit south, then 2 units west, then 2 units north, then 3 units east, etc. Because our walk is self-similar, this pattern repeats in the way we expect.

After, the algorithm is straightforward: perform the walk and record positions of the grid in the order we visit them. Please read the inline comments for more details.

```python
class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        ans = [(r0, c0)]
        if R * C == 1: return ans

        # For walk length k = 1, 3, 5 ...
        for k in xrange(1, 2*(R+C), 2):

            # For direction (dr, dc) = east, south, west, north;
            # and walk length dk...
            for dr, dc, dk in ((0, 1, k), (1, 0, k), (0, -1, k+1), (-1, 0, k+1)):

                # For each of dk units in the current direction ...
                for _ in xrange(dk):

                    # Step in that direction
                    r0 += dr
                    c0 += dc

                    # If on the grid ...
                    if 0 <= r0 < R and 0 <= c0 < C:
                        ans.append((r0, c0))
                        if len(ans) == R * C:
                            return ans
```

**Complexity Analysis**

* Time Complexity: $O((\max(R, C))^2)$. Potentially, our walk needs to spiral until we move $R$ in one direction, and $C$ in another direction, so as to reach every cell of the grid.

* Space Complexity: $O(R * C)$, the space used by the answer.

# Submissions
---
**Solution 1:**
```
Runtime: 116 ms
Memory Usage: 13.6 MB
```
```python
class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        ans = [(r0, c0)]
        if R * C == 1: return ans

        # For walk length k = 1, 3, 5 ...
        for k in range(1, 2*(R+C), 2):

            # For direction (dr, dc) = east, south, west, north;
            # and walk length dk...
            for dr, dc, dk in ((0, 1, k), (1, 0, k), (0, -1, k+1), (-1, 0, k+1)):

                # For each of dk units in the current direction ...
                for _ in range(dk):

                    # Step in that direction
                    r0 += dr
                    c0 += dc

                    # If on the grid ...
                    if 0 <= r0 < R and 0 <= c0 < C:
                        ans.append((r0, c0))
                        if len(ans) == R * C:
                            return ans
```