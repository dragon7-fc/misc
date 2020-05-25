1035. Uncrossed Lines

We write the integers of `A` and `B` (in the order they are given) on two separate horizontal lines.

Now, we may draw connecting lines: a straight line connecting two numbers `A[i]` and `B[j]` such that:

* `A[i]` == `B[j]`;
* The line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.

Return the maximum number of connecting lines we can draw in this way.

 

**Example 1:**

![1035_142](img/1035_142.png)

```
Input: A = [1,4,2], B = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will intersect the line from A[2]=2 to B[1]=2.
```

**Example 2:**
```
Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]
Output: 3
```

**Example 3:**
```
Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]
Output: 2
```

**Note:**

1. `1 <= A.length <= 500`
1. `1 <= B.length <= 500`
1. `1 <= A[i], B[i] <= 2000`

# Submissions
---
**Solution 1: (DP Bottom-Up)**
```
Runtime: 240 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        M, N = len(A), len(B)
        dp = [[0 for _ in range(N+1)] for _ in range(M+1)]
        for i in range(1, M+1):
            for j in range(1, N+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return dp[-1][-1]
```

**Solution 2: (DP Top-Down)**
```
Runtime: 352 ms
Memory Usage: 56.5 MB
```
```python
class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        M, N = len(A), len(B)
        
        @functools.lru_cache(None)
        def dp(i, j):
            if i == M or j == N:
                return 0
            if A[i] == B[j]:
                return dp(i+1, j+1) + 1
            else:
                return max(dp(i+1, j), dp(i, j+1))
            
        return dp(0, 0)
```