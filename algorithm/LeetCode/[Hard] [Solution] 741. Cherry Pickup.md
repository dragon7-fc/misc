741. Cherry Pickup

In a N x N `grid` representing a field of cherries, each cell is one of three possible integers.

* 0 means the cell is empty, so you can pass through;
* 1 means the cell contains a cherry, that you can pick up and pass through;
* -1 means the cell contains a thorn that blocks your way.
 

Your task is to collect maximum number of cherries possible by following the rules below:

* Starting at the position (0, 0) and reaching (N-1, N-1) by moving right or down through valid path cells (cells with value 0 or 1);
* After reaching (N-1, N-1), returning to (0, 0) by moving left or up through valid path cells;
* When passing through a path cell containing a cherry, you pick it up and the cell becomes an empty cell (0);
* If there is no valid path between (0, 0) and (N-1, N-1), then no cherries can be collected.

**Example 1:**
```
Input: grid =
[[0, 1, -1],
 [1, 0, -1],
 [1, 1,  1]]
Output: 5
Explanation: 
The player started at (0, 0) and went down, down, right right to reach (2, 2).
4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
Then, the player went left, up, up, left to return home, picking up one more cherry.
The total number of cherries picked up is 5, and this is the maximum possible.
```

**Note:**

* `grid` is an N by N 2D array, with `1 <= N <= 50`.
* Each `grid[i][j]` is an integer in the set `{-1, 0, 1}`.
* It is guaranteed that `grid[0][0]` and `grid[N-1][N-1]` are not `-1`.

# Solution
---
## Approach #1: Greedy [Wrong Answer]
**Intuition**

Let's find the most cherries we can pick up with one path, pick them up, then find the most cherries we can pick up with a second path on the remaining field.

Though a counter example might be hard to think of, this approach fails to find the best answer to this case:
```
11100
00101
10100
00100
00111
```

**Algorithm**

We can use dynamic programming to find the most number of cherries `dp[i][j]` that can be picked up from any location `(i, j)` to the bottom right corner. This is a classic question very similar to Minimum Path Sum, refer to the link if you are not familiar with this type of question.

After, we can find an first path that maximizes the number of cherries taken by using our completed `dp` as an oracle for deciding where to move. We'll choose the move that allows us to pick up more cherries (based on comparing `dp[i+1][j]` and `dp[i][j+1]`).

After taking the cherries from that path (and removing it from the `grid`), we'll take the cherries again.

```python
class Solution(object):
    def cherryPickup(self, grid):
        def bestpath(grid):
            N = len(grid)
            NINF = float('-inf')
            dp = [[NINF] * N for _ in xrange(N)]
            dp[-1][-1] = grid[-1][-1]
            for i in xrange(N-1, -1, -1):
                for j in xrange(N-1, -1, -1):
                    if grid[i][j] >= 0 and (i != N-1 or j != N-1):
                        dp[i][j] = max(dp[i+1][j] if i+1 < N else NINF,
                                       dp[i][j+1] if j+1 < N else NINF)
                        dp[i][j] += grid[i][j]

            if dp[0][0] < 0: return None
            ans = [(0, 0)]
            i = j = 0
            while i != N-1 or j != N-1:
                if j+1 == N or i+1 < N and dp[i+1][j] >= dp[i][j+1]:
                    i += 1
                else:
                    j += 1
                ans.append((i, j))
            return ans

        ans = 0
        path = bestpath(grid)
        if path is None: return 0

        for i, j in path:
            ans += grid[i][j]
            grid[i][j] = 0

        for i, j in bestpath(grid):
            ans += grid[i][j]

        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N^2)$, where $N$ is the length of `grid`. Our dynamic programming consists of two for-loops of length `N`.

* Space Complexity: $O(N^2)$, the size of `dp`.

## Approach #2: Dynamic Programming (Top Down) [Accepted]
**Intuition**

Instead of walking from end to beginning, let's reverse the second leg of the path, so we are only considering two paths from the beginning to the end.

Notice after `t` steps, each position `(r, c)` we could be, is on the line `r + c = t`. So if we have two people at positions `(r1, c1)` and `(r2, c2)`, then `r2 = r1 + c1 - c2`. That means the variables `r1, c1, c2` uniquely determine `2` people who have walked the same `r1 + c1` number of steps. This sets us up for dynamic programming quite nicely.

**Algorithm**

Let `dp[r1][c1][c2]` be the most number of cherries obtained by two people starting at `(r1, c1)` and `(r2, c2)` and walking towards `(N-1, N-1)` picking up cherries, where `r2 = r1+c1-c2`.

If `grid[r1][c1]` and `grid[r2][c2]` are not thorns, then the value of `dp[r1][c1][c2]` is `(grid[r1][c1] + grid[r2][c2])`, plus the maximum of `dp[r1+1][c1][c2], dp[r1][c1+1][c2], dp[r1+1][c1][c2+1], dp[r1][c1+1][c2+1]` as appropriate. We should also be careful to not double count in case `(r1, c1) == (r2, c2)`.

Why did we say it was the maximum of `dp[r+1][c1][c2]` etc.? It corresponds to the 4 possibilities for person 1 and 2 moving down and right:

* Person 1 down and person 2 down: `dp[r1+1][c1][c2]`;
* Person 1 right and person 2 down: `dp[r1][c1+1][c2]`;
* Person 1 down and person 2 right: `dp[r1+1][c1][c2+1]`;
* Person 1 right and person 2 right: `dp[r1][c1+1][c2+1]`;

```python
class Solution(object):
    def cherryPickup(self, grid):
        N = len(grid)
        memo = [[[None] * N for _1 in xrange(N)] for _2 in xrange(N)]
        def dp(r1, c1, c2):
            r2 = r1 + c1 - c2
            if (N == r1 or N == r2 or N == c1 or N == c2 or
                    grid[r1][c1] == -1 or grid[r2][c2] == -1):
                return float('-inf')
            elif r1 == c1 == N-1:
                return grid[r1][c1]
            elif memo[r1][c1][c2] is not None:
                return memo[r1][c1][c2]
            else:
                ans = grid[r1][c1] + (c1 != c2) * grid[r2][c2]
                ans += max(dp(r1, c1+1, c2+1), dp(r1+1, c1, c2+1),
                           dp(r1, c1+1, c2), dp(r1+1, c1, c2))

            memo[r1][c1][c2] = ans
            return ans

        return max(0, dp(0, 0, 0))
```

**Complexity Analysis**

* Time Complexity: $O(N^3)$, where $N$ is the length of `grid`. Our dynamic programming has $O(N^3)$ states.

* Space Complexity: $O(N^3)$, the size of `memo`.

## Approach #3: Dynamic Programming (Bottom Up) [Accepted]
**Intuition**

Like in Approach #2, we have the idea of dynamic programming.

Say `r1 + c1 = t` is the `t`-th layer. Since our recursion only references the next layer, we only need to keep two layers in memory at a time.

**Algorithm**

At time `t`, let `dp[c1][c2]` be the most cherries that we can pick up for two people going from `(0, 0)` to `(r1, c1)` and `(0, 0)` to `(r2, c2)`, where `r1 = t-c1`, `r2 = t-c2`. Our dynamic program proceeds similarly to Approach #2.

```python
class Solution(object):
    def cherryPickup(self, grid):
        N = len(grid)
        dp = [[float('-inf')] * N for _ in xrange(N)]
        dp[0][0] = grid[0][0]
        for t in xrange(1, 2*N - 1):
            dp2 = [[float('-inf')] * N for _ in xrange(N)]
            for i in xrange(max(0, t-(N-1)), min(N-1, t) + 1):
                for j in xrange(max(0, t-(N-1)), min(N-1, t) + 1):
                    if grid[i][t-i] == -1 or grid[j][t-j] == -1:
                        continue
                    val = grid[i][t-i]
                    if i != j: val += grid[j][t-j]
                    dp2[i][j] = max(dp[pi][pj] + val
                                    for pi in (i-1, i) for pj in (j-1, j)
                                    if pi >= 0 and pj >= 0)
            dp = dp2
        return max(0, dp[N-1][N-1])
```

**Complexity Analysis**

* Time Complexity: $O(N^3)$, where $N$ is the length of `grid`. We have three for-loops of size $O(N)$.

* Space Complexity: $O(N^2)$, the sizes of `dp` and `dp2`.

# Submissions
---
