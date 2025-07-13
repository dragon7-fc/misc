733. Flood Fill

An `image` is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate `(sr, sc)` representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the `newColor`.

At the end, return the modified image.

**Example 1:**
```
Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
```

**Note:**

* The length of image and image[0] will be in the range `[1, 50]`.
* The given starting pixel will satisfy `0 <= sr < image.length` and `0 <= sc < image[0].length`.
* The value of each color in `image[i][j]` and `newColor` will be an integer in `[0, 65535]`.

# Solution
---
## Approach #1: Depth-First Search [Accepted]
**Intuition**

We perform the algorithm explained in the problem description: paint the starting pixels, plus adjacent pixels of the same color, and so on.

**Algorithm**

Say `color` is the color of the starting pixel. Let's floodfill the starting pixel: we change the color of that pixel to the new color, then check the 4 neighboring pixels to make sure they are valid pixels of the same `color`, and of the valid ones, we floodfill those, and so on.

We can use a function `dfs` to perform a floodfill on a target pixel.

```python
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: return image
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1: dfs(r-1, c)
                if r+1 < R: dfs(r+1, c)
                if c >= 1: dfs(r, c-1)
                if c+1 < C: dfs(r, c+1)

        dfs(sr, sc)
        return image
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the number of pixels in the `image`. We might process every pixel.

* Space Complexity: $O(N)$, the size of the implicit call stack when calling `dfs`.

# Submissions
---
**Solution: (Depth-First Search)**
```
Runtime: 80 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: return image
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1: dfs(r-1, c)
                if r+1 < R: dfs(r+1, c)
                if c >= 1: dfs(r, c-1)
                if c+1 < C: dfs(r, c+1)

        dfs(sr, sc)
        return image
```

**Solution 2: (BFS)**
```
Runtime: 76 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: return image
        q = collections.deque([[sr, sc]])
        while q:
            r, c = q.popleft()
            image[r][c] = newColor
            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0 <= nr < R and 0 <= nc < C:
                    if image[nr][nc] == color:
                        q.append([nr, nc])

        return image
```
 
**Solution 3: (DFS)**
```
Runtime: 16 ms
Memory Usage: 8.3 MB
```
```c
void paint(int** image, int imageSize, int* imageColSize,
          int sr, int sc, int newColor, int oldColor)
{
    if (sr < 0 || sr >= imageSize)
        return;
    if (sc < 0 || sc >= imageColSize[0])
        return;
    
    if (image[sr][sc] == oldColor) {
        image[sr][sc] = newColor;
        paint(image, imageSize, imageColSize, sr - 1, sc, newColor, oldColor);
        paint(image, imageSize, imageColSize, sr + 1, sc, newColor, oldColor);
        paint(image, imageSize, imageColSize, sr, sc - 1, newColor, oldColor);
        paint(image, imageSize, imageColSize, sr, sc + 1, newColor, oldColor);
    }
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** floodFill(int** image, int imageSize, int* imageColSize, int sr, int sc, int newColor, int* returnSize, int** returnColumnSizes){
    int i;
    *returnSize = imageSize;
    *returnColumnSizes = malloc(sizeof(int) * imageSize);
    for (i = 0; i < imageSize; i++)
        (*returnColumnSizes)[i] = imageColSize[i];

    if (newColor != image[sr][sc])
        paint(image, imageSize, imageColSize,
              sr, sc, newColor, image[sr][sc]);
    
    return image;
}
```

**Solution 4: (DFS)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 18.04 MB, Beats 77.73%
```
```c++
class Solution {
    int dd[5] = {0, 1, 0, -1, 0};
    void dfs(int i, int j, int ac, int bc, vector<vector<int>> &ans) {
        ans[i][j] = bc;
        int m = ans.size(), n = ans[0].size(), d, ni, nj;
        for (d = 0; d < 4; d ++) {
            ni = i + dd[d];
            nj = j + dd[d+1];
            if (0 <= ni && ni < m && 0 <= nj && nj < n && ans[ni][nj] == ac) {
                dfs(ni, nj, ac, bc, ans);
            }
        } 
    }
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        vector<vector<int>> ans = image;
        if (ans[sr][sc] == color) {
            return ans;
        }
        dfs(sr, sc, ans[sr][sc], color, ans);
        return ans;
    }
};
```
