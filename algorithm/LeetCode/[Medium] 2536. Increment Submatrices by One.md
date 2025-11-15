2536. Increment Submatrices by One

You are given a positive integer `n`, indicating that we initially have an `n x n` **0-indexed** integer matrix `mat` filled with zeroes.

You are also given a 2D integer array `query`. For each `query[i] = [row1i, col1i, row2i, col2i]`, you should do the following operation:

* Add `1` to every element in the submatrix with the **top left** corner `(row1i, col1i)` and the **bottom right** corner `(row2i, col2i)`. That is, add `1` to `mat[x][y]` for for all `row1i <= x <= row2i` and `col1i <= y <= col2i`.

Return the matrix `mat` after performing every query.

 

**Example 1:**

```
Input: n = 3, queries = [[1,1,2,2],[0,0,1,1]]
Output: [[1,1,0],[1,2,1],[0,1,1]]
Explanation: The diagram above shows the initial matrix, the matrix after the first query, and the matrix after the second query.
- In the first query, we add 1 to every element in the submatrix with the top left corner (1, 1) and bottom right corner (2, 2).
- In the second query, we add 1 to every element in the submatrix with the top left corner (0, 0) and bottom right corner (1, 1).
```

**Example 2:**

```
Input: n = 2, queries = [[0,0,1,1]]
Output: [[1,1],[1,1]]
Explanation: The diagram above shows the initial matrix and the matrix after the first query.
- In the first query we add 1 to every element in the matrix.
```

**Constraints:**

* `1 <= n <= 500`
* `1 <= queries.length <= 10^4`
* `0 <= row1i <= row2i < n`
* `0 <= col1i <= col2i < n`

# Submissions
---
**Solution 1: (Prefix Sum)**
```
Runtime: 2646 ms
Memory: 37.5 MB
```
```python
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        dp = [[0]*(n+1) for _ in range(n)]
        for row1, col1, row2, col2 in queries:
            for r in range(row1, row2+1):
                dp[r][col1] += 1
                dp[r][col2+1] -= 1        
        return [list(accumulate(r))[:-1] for r in dp]
```

**Solution 2: (Prefix Sum, mask every row)**
```
Runtime: 51 ms, Beats 38.56%
Memory: 86.20 MB, Beats 100.00%
```
```c++
class Solution {
public:
    vector<vector<int>> rangeAddQueries(int n, vector<vector<int>>& queries) {
        int i, j, row1, col1, row2, col2;
        vector<vector<int>> ans(n, vector<int>(n));
        for (auto &q: queries) {
            row1 = q[0];
            col1 = q[1];
            row2 = q[2];
            col2 = q[3];
            for (i = row1; i <= row2; i ++) {
                ans[i][col1] += 1;
                if (col2 + 1 < n) {
                    ans[i][col2 + 1] -= 1;
                }
            }
        }
        for (i = 0; i < n; i ++) {
            for (j = 1; j < n; j ++) {
                ans[i][j] += ans[i][j - 1];
            }
        }
        return ans;
    }
};
```
