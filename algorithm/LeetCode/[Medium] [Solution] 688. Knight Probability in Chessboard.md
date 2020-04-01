688. Knight Probability in Chessboard

On an `NxN` chessboard, a knight starts at the `r`-th row and `c`-th column and attempts to make exactly `K` moves. The rows and columns are `0 indexed`, so the top-left square is `(0, 0)`, and the bottom-right square is `(N-1, N-1)`.

A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

![688_knight](img/688_knight.png)

Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

The knight continues moving until it has made exactly `K` moves or has moved off the chessboard. Return the probability that the knight remains on the board after it has stopped moving.

**ample:**

```
Input: 3, 2, 0, 0
Output: 0.0625
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.
```

**Note:**

* `N` will be between `1` and `25`.
* `K` will be between `0` and `100`.
* The knight always initially starts on the board.

## Approach #1: Dynamic Programming [Accepted]
**Intuition and Algorithm**

Let `f[r][c][steps]` be the probability of being on square `(r, c)` after steps `steps`. Based on how a knight moves, we have the following recursion:

$f[r][c][steps] = \sum_{dr, dc} f[r+dr][c+dc][steps-1] / 8.0$

where the sum is taken over the eight $(dr, dc)$ pairs $(2, 1)$, $(2, -1)$, $(-2, 1)$, $(-2, -1)$, $(1, 2)$, $(1, -2)$, $(-1, 2)$, $(-1, -2)$.

Instead of using a three-dimensional array `f`, we will use two two-dimensional ones `dp` and `dp2`, storing the result of the two most recent layers we are working on. `dp2` will represent `f[][][steps]`, and `dp` will represent `f[][][steps-1]`.

```python
class Solution(object):
    def knightProbability(self, N, K, r, c):
        dp = [[0] * N for _ in xrange(N)]
        dp[r][c] = 1
        for _ in xrange(K):
            dp2 = [[0] * N for _ in xrange(N)]
            for r, row in enumerate(dp):
                for c, val in enumerate(row):
                    for dr, dc in ((2,1),(2,-1),(-2,1),(-2,-1),
                                   (1,2),(1,-2),(-1,2),(-1,-2)):
                        if 0 <= r + dr < N and 0 <= c + dc < N:
                            dp2[r+dr][c+dc] += val / 8.0
            dp = dp2

        return sum(map(sum, dp))
```

**Complexity Analysis**

* Time Complexity: $O(N^2 K)$ where $N, K$ are defined as in the problem. We do $O(1)$ work on each layer `dp` of $N^2$ elements, and there are $K$ layers considered.

* Space Complexity: $O(N^2)$, the size of `dp` and `dp2`.

## Approach #2: Matrix Exponentiation [Accepted]
**Intuition**

The recurrence expressed in Approach #1 expressed states that transitioned to a linear combination of other states. Any time this happens, we can represent the entire transition as a matrix of those linear combinations. Then, the $n$-th power of this matrix represents the transition of $n$ moves, and thus we can reduce the problem to a problem of matrix exponentiation.

**Algorithm**

First, there is a lot of symmetry on the board that we can exploit. Naively, there are $N^2$ possible states the knight can be in (assuming it is on the board). Because of symmetry through the horizontal, vertical, and diagonal axes, we can assume that the knight is in the top-left quadrant of the board, and that the column number is equal to or larger than the row number. For any square, the square that is found by reflecting about these axes to satisfy these conditions will be the canonical index of that square.

This will reduce the number of states from $N^2$ to approximately $\frac{N^2}{8}$, which makes the following (cubic) matrix exponentiation on this $O(\frac{N^2}{8}) \times O(\frac{N^2}{8})$ matrix approximately $8^3$ times faster.

Now, if we know that every state becomes some linear combination of states after one move, then let's write a transition matrix $\mathcal{T}$ of them, where the $i$-th row of $\mathcal{T}$ represents the linear combination of states that the $i$-th state goes to. Then, $\mathcal{T}^n$ represents a transition of $n$ moves, for which we want the sum of the $i$-th row, where $i$ is the index of the starting square.

```python
class Solution(object):
    def knightProbability(self, N, K, sr, sc):
        def canonical(r, c):
            if 2 * r > N: r = N - 1 - r
            if 2 * c > N: c = N - 1 - c
            if r > c: r, c = c, r
            return r*N + c

        def matrix_mult(A, B):
            ZB = zip(*B)
            return [[sum(a * b for a, b in zip(row, col))
                     for col in ZB] for row in A]

        def matrix_expo(A, K):
            if K == 0:
                return [[+(i==j) for j in xrange(len(A))]
                        for i in xrange(len(A))]
            if K == 1:
                return A
            elif K % 2:
                return matrix_mult(matrix_expo(A, K-1), A)
            B = matrix_expo(A, K/2)
            return matrix_mult(B, B)

        index = [0] * (N*N)
        t = 0
        for r in xrange(N):
            for c in xrange(N):
                if r*N + c == canonical(r, c):
                    index[r*N + c] = t
                    t += 1
                else:
                    index[r*N + c] = index[canonical(r, c)]

        T = []
        for r in xrange(N):
            for c in xrange(N):
                if r*N + c == canonical(r, c):
                    row = [0] * t
                    for dr, dc in ((2,1),(2,-1),(-2,1),(-2,-1),
                                    (1,2),(1,-2),(-1,2),(-1,-2)):
                        if 0 <= r+dr < N and 0 <= c+dc < N:
                            row[index[(r+dr)*N + c+dc]] += 0.125
                    T.append(row)

        Tk = matrix_expo(T, K)
        i = index[sr * N + sc]
        return sum(Tk[i])
```

**Complexity Analysis**

* Time Complexity: $O(N^6 \log(K))$ where $N, K$ are defined as in the problem. There are approximately $\frac{N^2}{8}$ canonical states, which makes our matrix multiplication $O(N^6)$. To find the $K$-th power of this matrix, we make $O(\log(K))$ matrix multiplications.

* Space Complexity: $O(N^4)$. The matrix has approximately $\frac{N^4}{64}$ elements.

# Submissions
----
**Solution 1: (Dynamic Programming Bottom-Up)**
```
Runtime: 264 ms
Memory Usage: 13.6 MB
```
```python
class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        dp = [[0] * N for _ in range(N)]
        dp[r][c] = 1
        for _ in range(K):
            dp2 = [[0] * N for _ in range(N)]
            for r, row in enumerate(dp):
                for c, val in enumerate(row):
                    for dr, dc in ((2,1),(2,-1),(-2,1),(-2,-1),
                                   (1,2),(1,-2),(-1,2),(-1,-2)):
                        if 0 <= r + dr < N and 0 <= c + dc < N:
                            dp2[r+dr][c+dc] += val / 8.0
            dp = dp2

        return sum(map(sum, dp))
```