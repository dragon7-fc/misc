861. Score After Flipping Matrix

We have a two dimensional matrix `A` where each value is `0` or `1`.

A move consists of choosing any row or column, and toggling each value in that row or column: changing all `0`s to `1`s, and all `1`s to `0`s.

After making any number of moves, every row of this matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score.

 

**Example 1:**
```
Input: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation:
Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]].
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
```

**Note:**

* `1 <= A.length <= 20`
* `1 <= A[0].length <= 20`
* `A[i][j] is 0 or 1`.

# Solution
---
## Approach 1: Brute Force
**Intuition**

Notice that a `1` in the iith column from the right, contributes $2^i$ to the score.

Say we are finished toggling the rows in some configuration. Then for each column, (to maximize the score), we'll toggle the column if it would increase the number of `1`s.

We can brute force over every possible way to toggle rows.

**Algorithm**

Say the matrix has `R` rows and `C` columns.

For each state, the transition `trans = state ^ (state-1)` represents the rows that must be toggled to get into the state of toggled rows represented by (the bits of) state.

We'll toggle them, and also maintain the correct column sums of the matrix on the side.

Afterwards, we'll calculate the score. If for example the last column has a column sum of `3`, then the score is `max(3, R-3)`, where `R-3` represents the score we get from toggling the last column.

In general, the score is increased by `max(col_sum, R - col_sum) * (1 << (C-1-c))`, where the factor `(1 << (C-1-c))` is the power of `2` that each `1` contributes.

Note that this approach may not run in the time allotted.

```python
class Solution(object):
    def matrixScore(self, A):
        R, C = len(A), len(A[0])

        colsums = [0] * C
        for r in xrange(R):
            for c in xrange(C):
                colsums[c] += A[r][c]

        ans = 0
        for r in xrange(1<<R):
            if r:
                trans = r ^ (r-1)
                for bit in xrange(R):
                    if (trans >> bit) & 1:
                        for c in xrange(C):
                            colsums[c] += -1 if A[bit][c] else +1
                            A[bit][c] ^= 1
            
            score = sum(max(x, R - x) * (1 << (C-1-c))
                        for c, x in enumerate(colsums))
            ans = max(ans, score)

        return ans
```

**Complexity Analysis**

* Time Complexity: $O(2^R * R * C)$, where $R, C$ is the number of rows and columns in the matrix.

* Space Complexity: $O(C)$ in additional space complexity.

## Approach 2: Greedy
**Intuition**

Notice that a `1` in the $i$th column from the right, contributes $2^i$ to the score.

Since $2^n > 2^{n-1} + 2^{n-2} + \cdots + 2^0$, maximizing the left-most digit is more important than any other digit. Thus, the rows should be toggled such that the left-most column is either all `0` or all `1` (so that after toggling the left-most column [if necessary], the left column is all `1`.)

**Algorithm**

If we toggle rows by the first column (`A[r][c] ^= A[r][0]`), then the first column will be all `0`.

Afterwards, the base score is `max(col, R - col)` where col is the column sum; and `(1 << (C-1-c))` is the power of `2` that each `1` in that column contributes to the score.

```python
class Solution(object):
    def matrixScore(self, A):
        R, C = len(A), len(A[0])
        ans = 0
        for c in xrange(C):
            col = 0
            for r in xrange(R):
                col += A[r][c] ^ A[r][0]
            ans += max(col, R - col) * 2 ** (C - 1 - c)
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(R * C)$, $R, C$ is the number of rows and columns in the matrix.

* Space Complexity: $O(1)$ in additional space complexity.

# Submissions
---
**Solution: (Greedy)**
```
Runtime: 32 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        R, C = len(A), len(A[0])
        ans = 0
        for c in range(C):
            col = 0
            for r in range(R):
                col += A[r][c] ^ A[r][0]
            ans += max(col, R - col) * 2 ** (C - 1 - c)
        return ans
```

**Solution 2: (Greedy)**

Assume A is M * N.

1. A[i][0] is worth 1 << (N - 1) points, more than the sum of (A[i][1] + .. + A[i][N-1]).
    We need to toggle all A[i][0] to 1, here I toggle all lines for A[i][0] = 0.
1. A[i][j] is worth 1 << (N - 1 - j)
    For every col, I count the current number of 1s.
    After step 1, A[i][j] becomes 1 if A[i][j] == A[i][0].
    if M - cur > cur, we can toggle this column to get more 1s.
    max(cur, M - cur) will be the maximum number of 1s that we can get.

```
Runtime: 0 ms
Memory: 10.24 MB
```
```c++
class Solution {
public:
    int matrixScore(vector<vector<int>>& grid) {
        int M = grid.size(), N = grid[0].size(), res = (1 << (N - 1)) * M;
        for (int j = 1; j < N; j++) {
            int cur = 0;
            for (int i = 0; i < M; i++) cur += grid[i][j] == grid[i][0];
            res += max(cur, M - cur) * (1 << (N - j - 1));
        }
        return res;
    }
};
```
