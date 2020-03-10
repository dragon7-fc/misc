661. Image Smoother

Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.

**Example 1:**
```
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
```
**Note:**

1. The value in the given matrix is in the range of [0, 255].
1. The length and width of the given matrix are in the range of [1, 150].

# Solution
---
## Approach #1: Iterate Through Grid
**Intuition and Algorithm*

For each cell in the grid, look at the immediate neighbors - up to 9 of them, including the original cell.

Then, we will add the sum of the neighbors into ans[r][c] while recording count, the number of such neighbors. The final answer is the sum divided by the count.

```python
class Solution(object):
    def imageSmoother(self, M):
        R, C = len(M), len(M[0])
        ans = [[0] * C for _ in M]

        for r in xrange(R):
            for c in xrange(C):
                count = 0
                for nr in (r-1, r, r+1):
                    for nc in (c-1, c, c+1):
                        if 0 <= nr < R and 0 <= nc < C:
                            ans[r][c] += M[nr][nc]
                            count += 1
                ans[r][c] /= count

        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the number of pixels in our image. We iterate over every pixel.

* Space Complexity: $O(N)$, the size of our answer.

# Submissions
---
**Solution 1: (Iterate Through Grid)**
```
Runtime: 740 ms
Memory Usage: 14.2 MB
```
```python
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        R, C = len(M), len(M[0])
        ans = [[0] * C for _ in M]

        for r in range(R):
            for c in range(C):
                count = 0
                for nr in (r-1, r, r+1):
                    for nc in (c-1, c, c+1):
                        if 0 <= nr < R and 0 <= nc < C:
                            ans[r][c] += M[nr][nc]
                            count += 1
                ans[r][c] //= count

        return ans
```
