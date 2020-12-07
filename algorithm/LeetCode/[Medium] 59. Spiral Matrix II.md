59. Spiral Matrix II

Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

**Example:**
```
Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
```

# Submissions
---
**Solution 1: (Math)**
```
Runtime: 40 ms
Memory Usage: 13.7 MB
```
```python
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        counter = 1
        m = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n//2):
            for j in range(i,n-i-1):
                m[i][j] = counter
                m[j][n-i-1] = counter + n-1-(i*2)
                m[n-1-i][n-j-1] = counter + 2 * (n-1-(i*2))
                m[n-j-1][i] = counter + 3 * (n-1-(i*2))
                counter +=1
            counter = counter + 3 * (n-1-(i*2))
        if n %2 == 1:
            m[n//2][n//2] = n*n
        return m
```

**Solution 2: (DFS)**
```
Runtime: 28 ms
Memory Usage: 14.6 MB
```
```python
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0]*n for _ in range(n)]
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        
        def dfs(x, y, d, k):
            ans[x][y] = k
            nx, ny = x+dx[d], y+dy[d]
            if 0 <= nx < n and  0 <= ny < n and ans[nx][ny] == 0:
                dfs(nx, ny, d, k+1)
            else:
                d = (d+1)%4
                nx, ny = x+dx[d], y+dy[d]
                if 0 <= nx < n and  0 <= ny < n and ans[nx][ny] == 0:
                    dfs(nx, ny, d, k+1)
            
        dfs(0, 0, 0, 1)
        return ans
```