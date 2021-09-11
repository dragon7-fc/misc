764. Largest Plus Sign

In a 2D grid from `(0, 0)` to `(N-1, N-1)`, every cell contains a `1`, except those cells in the given list `mines` which are `0`. What is the largest axis-aligned plus sign of `1`s contained in the grid? Return the order of the plus sign. If there is none, return `0`.

An "axis-aligned plus sign of `1`s of order **k**" has some center `grid[x][y] = 1` along with 4 arms of length `k-1` going up, down, left, and right, and made of 1s. This is demonstrated in the diagrams below. Note that there could be `0`s or `1`s beyond the arms of the plus sign, only the relevant area of the plus sign is checked for `1`s.

**Examples of Axis-Aligned Plus Signs of Order k:**

```
Order 1:
000
010
000

Order 2:
00000
00100
01110
00100
00000

Order 3:
0000000
0001000
0001000
0111110
0001000
0001000
0000000
```

**Example 1:**

```
Input: N = 5, mines = [[4, 2]]
Output: 2
Explanation:
11111
11111
11111
11111
11011
In the above grid, the largest plus sign can only be order 2.  One of them is marked in bold.
```

**Example 2:**

```
Input: N = 2, mines = []
Output: 1
Explanation:
There is no plus sign of order 2, but there is of order 1.
```

**Example 3:**

```
Input: N = 1, mines = [[0, 0]]
Output: 0
Explanation:
There is no plus sign, so return 0.
```

**Note:**

1. N will be an integer in the range `[1, 500]`.
1. `mines` will have length at most `5000`.
1. `mines[i]` will be length `2` and consist of integers in the range `[0, N-1]`.
1. (Additionally, programs submitted in C, C++, or C# will be judged with a slightly smaller time limit.)

# Solution
---
# Approach #1: Brute Force [Time Limit Exceeded]
**Intuition and Algorithm**

For each possible center, find the largest plus sign that could be placed by repeatedly expanding it. We expect this algorithm to be $O(N^3)$, and so take roughly $500^3 = (1.25) * 10^8$ operations. This is a little bit too big for us to expect it to run in time.

```python
class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        banned = {tuple(mine) for mine in mines}
        ans = 0
        for r in xrange(N):
            for c in xrange(N):
                k = 0
                while (k <= r < N-k and k <= c < N-k and
                        (r-k, c) not in banned and
                        (r+k, c) not in banned and
                        (r, c-k) not in banned and
                        (r, c+k) not in banned):
                    k += 1
                ans = max(ans, k)
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N^3)$, as we perform two outer loops $(O(N^2)$, plus the inner loop involving k is $O(N)$.

* Space Complexity: $O(\text{mines.length})$.

# Approach #2: Dynamic Programming [Accepted]
**Intuition**

How can we improve our bruteforce? One way is to try to speed up the inner loop involving `k`, the order of the candidate plus sign. If we knew the longest possible arm length $L_u$, $L_l$, $L_d$, $L_r$ in each direction from a center, we could know the order $\min(L_u, L_l, L_d, L_r)$ of a plus sign at that center. We could find these lengths separately using dynamic programming.

**Algorithm**

For each (cardinal) direction, and for each coordinate `(r, c)` let's compute the count of that coordinate: the longest line of '1's starting from `(r, c)` and going in that direction. With dynamic programming, it is either `0` if `grid[r][c]` is zero, else it is `1` plus the count of the coordinate in the same direction. For example, if the direction is left and we have a row like `01110110`, the corresponding count values are `01230120`, and the integers are either `1` more than their successor, or `0`. For each square, we want `dp[r][c]` to end up being the minimum of the 4 possible counts. At the end, we take the maximum value in `dp`.

```python
class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        banned = {tuple(mine) for mine in mines}
        dp = [[0] * N for _ in xrange(N)]
        ans = 0
        
        for r in xrange(N):
            count = 0
            for c in xrange(N):
                count = 0 if (r,c) in banned else count+1
                dp[r][c] = count
            
            count = 0
            for c in xrange(N-1, -1, -1):
                count = 0 if (r,c) in banned else count+1
                if count < dp[r][c]: dp[r][c] = count
        
        for c in xrange(N):
            count = 0
            for r in xrange(N):
                count = 0 if (r,c) in banned else count+1
                if count < dp[r][c]: dp[r][c] = count
            
            count = 0
            for r in xrange(N-1, -1, -1):
                count = 0 if (r, c) in banned else count+1
                if count < dp[r][c]: dp[r][c] = count
                if dp[r][c] > ans: ans = dp[r][c]
        
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N^2)$, as the work we do under two nested for loops is $O(1)$.

* Space Complexity: $O(N^2)$, the size of `dp`.

# Submissions
---
**Solution: (Dynamic Programming)**
```
Runtime: 1868 ms
Memory Usage: 16.8 MB
```
```python
class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        banned = {tuple(mine) for mine in mines}
        dp = [[0] * N for _ in range(N)]
        ans = 0
        
        for r in range(N):  # for every row
            count = 0
            for c in range(N):  # from left to right
                count = 0 if (r,c) in banned else count+1
                dp[r][c] = count
            
            count = 0
            for c in range(N-1, -1, -1):  # from right to left
                count = 0 if (r,c) in banned else count+1
                if count < dp[r][c]: dp[r][c] = count
        
        for c in range(N):  # for every column
            count = 0
            for r in range(N):  # from top - bottom
                count = 0 if (r,c) in banned else count+1
                if count < dp[r][c]: dp[r][c] = count
            
            count = 0
            for r in range(N-1, -1, -1):  # from bottom to up
                count = 0 if (r, c) in banned else count+1
                if count < dp[r][c]: dp[r][c] = count
                if dp[r][c] > ans: ans = dp[r][c]  # update an
        
        return ans
```
