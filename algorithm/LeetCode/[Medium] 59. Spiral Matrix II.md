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
**Solution:**
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