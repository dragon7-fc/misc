790. Domino and Tromino Tiling

We have two types of tiles: a 2x1 domino shape, and an "L" tromino shape. These shapes may be rotated.

```
XX  <- domino

XX  <- "L" tromino
X
```

Given `N`, how many ways are there to tile a `2 x N` board? **Return your answer modulo 10^9 + 7**.

(In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.)

**Example:**

```
Input: 3
Output: 5
Explanation: 
The five different ways are listed below, different letters indicates different tiles:
XYZ XXZ XYY XXY XYY
XYZ YYZ XZZ XYY XXY
```

**Note:**

* `N` will be in range `[1, 1000]`.

# Submissions
---
**Solution 1:**

Tiles can end at column `i` with one of the three ending states:

```
Ending state A:
      x
...   x
      i
Ending state B:
      x
...   xx
       i
Ending state C:
      xx
...   x
       i
```

Let `S[i]` be the number of ways to get to state `S` at `i`'th column, where `S` can be `A`, `B` or `C`. Then, we just need to write down all posiible transitions between the states.

```
Runtime: 28 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def numTilings(self, N: int) -> int:
        MOD = 10**9 + 7
        A = [0 for i in range(N+1)]
        B = [0 for i in range(N+1)]
        C = [0 for i in range(N+1)]
        A[0] = 1
        for i in range(1, N+1):
            A[i] = (B[i-1] + C[i-1] + A[i-1] + (A[i-2] if i >=2 else 0)) % MOD
            B[i] = (C[i-1] + (A[i-2] if i >=2 else 0)) % MOD
            C[i] = (B[i-1] + (A[i-2] if i >=2 else 0)) % MOD
        return A[-1]
```