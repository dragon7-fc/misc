1314. Matrix Block Sum

Given a `m * n` matrix `mat` and an integer `K`, return a matrix answer where each `answer[i][j]` is the sum of all elements `mat[r][c]` for `i - K <= r` <= `i + K, j - K <= c <= j + K`, and `(r, c)` is a valid position in the matrix.
 

**Example 1:**
```
Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
Output: [[12,21,16],[27,45,33],[24,39,28]]
```

**Example 2:**
```
Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2
Output: [[45,45,45],[45,45,45],[45,45,45]]
```

**Constraints:**

* `m == mat.length`
* `n == mat[i].length`
* `1 <= m, n, K <= 100`
* `1 <= mat[i][j] <= 100`

# Submissions
---
**Solution 1:**

To calculate `rangeSum`, the ideas are as below - credit to @haoel
```
+-----+-+-------+     +--------+-----+     +-----+---------+     +-----+--------+
|     | |       |     |        |     |     |     |         |     |     |        |
|     | |       |     |        |     |     |     |         |     |     |        |
+-----+-+       |     +--------+     |     |     |         |     +-----+        |
|     | |       |  =  |              |  +  |     |         |  -  |              |
+-----+-+       |     |              |     +-----+         |     |              |
|               |     |              |     |               |     |              |
|               |     |              |     |               |     |              |
+---------------+     +--------------+     +---------------+     +--------------+
```
`rangeSum[i+1][j+1] =  rangeSum[i][j+1] + rangeSum[i+1][j]    -   rangeSum[i][j]   + mat[i][j]`
So, we use the same idea to find the specific block's sum. - credit to @haoel
```
+---------------+   +--------------+   +---------------+   +--------------+   +--------------+
|               |   |         |    |   |   |           |   |         |    |   |   |          |
|   (r1,c1)     |   |         |    |   |   |           |   |         |    |   |   |          |
|   +------+    |   |         |    |   |   |           |   +---------+    |   +---+          |
|   |      |    | = |         |    | - |   |           | - |      (r1,c2) | + |   (r1,c1)    |
|   |      |    |   |         |    |   |   |           |   |              |   |              |
|   +------+    |   +---------+    |   +---+           |   |              |   |              |
|        (r2,c2)|   |       (r2,c2)|   |   (r2,c1)     |   |              |   |              |
+---------------+   +--------------+   +---------------+   +--------------+   +--------------+
```

```
Runtime: 100 ms
Memory Usage: 13.7 MB
```
```python
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        R, C = len(mat), len(mat[0])
        rangeSum = [[0] * (C + 1) for _ in range(R + 1)]
        for r in range(R):
            for c in range(C):
                rangeSum[r + 1][c + 1] = rangeSum[r + 1][c] + rangeSum[r][c + 1] - rangeSum[r][c] + mat[r][c]
        ans = [[0] * C for _ in range(R)]        
        for r in range(R):
            for c in range(C):
                r1, c1, r2, c2 = max(0, r - K), max(0, c - K), min(R, r + K + 1), min(C, c + K + 1)
                ans[r][c] = rangeSum[r2][c2] - rangeSum[r1][c2] - rangeSum[r2][c1] + rangeSum[r1][c1]
        return ans
```