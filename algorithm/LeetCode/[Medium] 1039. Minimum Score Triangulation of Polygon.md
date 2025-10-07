1039. Minimum Score Triangulation of Polygon

Given `N`, consider a convex `N`-sided polygon with vertices labelled `A[0], A[i], ..., A[N-1]` in clockwise order.

Suppose you triangulate the polygon into `N-2` triangles.  For each triangle, the value of that triangle is the **product** of the labels of the vertices, and the total score of the triangulation is the sum of these values over all `N-2` triangles in the triangulation.

Return the smallest possible total score that you can achieve with some triangulation of the polygon.

**Example 1:**

```
Input: [1,2,3]
Output: 6
Explanation: The polygon is already triangulated, and the score of the only triangle is 6.
```

**Example 2:**

![minimum-score-triangulation-of-polygon-1](img/minimum-score-triangulation-of-polygon-1.png)

```
Input: [3,7,4,5]
Output: 144
Explanation: There are two triangulations, with possible scores: 3*7*5 + 4*5*7 = 245, or 3*4*5 + 3*4*7 = 144.  The minimum score is 144.
```

**Example 3:**

```
Input: [1,3,1,4,1,5]
Output: 13
Explanation: The minimum score triangulation has score 1*1*3 + 1*1*4 + 1*1*5 + 1*1*1 = 13.
```

**Note:**

1. `3 <= A.length <= 50`
1. `1 <= A[i] <= 100`

# Submissions
---
**Solution 1: (DP Bottom-Up)**
```
Runtime: 116 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        n = len(A)
        dp = [[0]*n for i in range(n)]
        for l in range(2, n):
            for left in range(0, n - l):
                right = left + l
                dp[left][right] = float("Inf")
                for k in range(left + 1, right):
                    dp[left][right] = min(dp[left][right], dp[left][k] + dp[k][right] + A[left]*A[right]*A[k])
        return dp[0][-1]
```

**Solution 2: (DP Top-Down)**
```
Runtime: 124 ms
Memory Usage: 14.7 MB
```
```python
class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        
        @lru_cache(None)
        def dfs(left, right):
            if right - left + 1 < 3:
                return 0
            minnum = float("Inf")
            for k in range(left+1, right):
                minnum = min(minnum, A[left]*A[right]*A[k] + dfs(left, k) + dfs(k, right))
            return minnum

        return dfs(0, len(A) - 1)
```

**Solution 3: (DP Top-Down)**
```
Runtime: 3 ms, Beats 57.27%
Memory: 11.23 MB, Beats 44.38%
```
```c++
class Solution {
    int dfs(int i, int j, vector<vector<int>> &dp, vector<int> &values) {
        if (j - i == 1) {
            return 0;
        }
        if (j - i == 2) {
            return values[i] * values[i + 1] * values[j];
        }
        if (dp[i][j] != INT_MAX) {
            return dp[i][j];
        }
        int rst = INT_MAX;
        for (int k = i + 1; k < j; k ++) {
            rst = min(rst, values[i] * values[j] * values[k] + dfs(i, k, dp, values) + dfs(k, j, dp, values));
        }
        dp[i][j] = rst;
        return rst;
    }
public:
    int minScoreTriangulation(vector<int>& values) {
        int n = values.size();
        vector<vector<int>> dp(n, vector<int>(n, INT_MAX));
        return dfs(0, n - 1, dp, values);
    }
};
```

**Solution 4: (DP Bottom-Up)**
```
Runtime: 2 ms, Beats 66.77%
Memory: 11.35 MB, Beats 15.48%
```
```c++
class Solution {
public:
    int minScoreTriangulation(vector<int>& values) {
        int n = values.size(), i, j, k;
        vector<vector<int>> dp(n, vector<int>(n, INT_MAX));
        for (i = 0; i < n - 1; i ++) {
            dp[i][i + 1] = 0;
        }
        for (k = 2; k < n; k ++) {
            for (i = 0; i < n - k; i ++) {
                for (j = i + 1; j < i + k; j ++) {
                    dp[i][i + k] = min(dp[i][i + k], values[i] * values[j] * values[i + k] + dp[i][j] + dp[j][i + k]);
                }
            }
        }
        return dp[0][n - 1];
    }
};
```
