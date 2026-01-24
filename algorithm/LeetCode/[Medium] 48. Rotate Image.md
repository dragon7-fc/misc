48. Rotate Image

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

**Note:**

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. **DO NOT** allocate another 2D matrix and do the rotation.

**Example 1:**
```
Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
```

**Example 2:**
```
Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
```

# Submissions
---
**Solution 1: (Rotate Groups of Four Cells)**
```
Runtime: 36 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp
```

**Solution 2: (Transpose on Diagonal and then Reverse Left to Right)**
```
Runtime: 36 ms
Memory Usage: 14.1 MB
```
```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        self.reflect(matrix)
    
    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]
```

**Solution 3: (Rotate Groups of Four Cells)**
```
Runtime: 4 ms
Memory Usage: 6.5 MB
```
```c
void rotate(int** matrix, int matrixSize, int* matrixColSize){
    int tmp;
    for (int i = 0; i < matrixSize/2 + matrixSize%2; i ++) {
        for (int j = 0; j < *matrixColSize/2; j ++) {
            tmp = matrix[*matrixColSize - 1 - j][i];
            matrix[matrixSize - 1 - j][i] = matrix[matrixSize - 1 - i][*matrixColSize - 1 -j];
            matrix[matrixSize - 1 - i][*matrixColSize - 1 - j] = matrix[j][matrixSize - 1 -i];
            matrix[j][matrixSize - 1 - i] = matrix[i][j];
            matrix[i][j] = tmp;
        }
    }
}
```

**Solution 4: (Rotate Groups of Four Cells)**


           r         |  
           |         |   
    ----c--x         c  
                     | 
    r-x              x-r
      | 
      c         x--c----
      |         |      
      |         r     

```
Runtime: 0 ms
Memory Usage: 7.1 MB
```
```c++
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        int tmp;
        for (int r = 0; r < n/2; r++) {
            for (int c = 0; c < (n+1)/2; c++) {
                tmp = matrix[r][c];
                matrix[r][c] = matrix[n-1-c][r];
                matrix[n-1-c][r] = matrix[n-1-r][n-1-c];
                matrix[n-1-r][n-1-c] = matrix[c][n-1-r];
                matrix[c][n-1-r] = tmp;
            }
        }
    }
};
```

**Solution 5: (Array)**
        
      i              |  
      |              |-i 
    ----j---x        j  
                     | 
    i-x              x
      | 
      j   x------j------
      |              | 
      |              i

    0,1 -> 2,0   -> 3,2       -> 1,3      i = 0, j = 1
    i,j    n-1-j,i  n-1-i,n-1-j  j,n-1-i

```
Runtime: 0 ms, Beats 100.00%
Memory: 10.28 MB, Beats 34.99%
```
```c++
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size(), i = 0, j, a, b;
        while (i < n-1-i) {
            for (j = i; j < n-1-i; j ++) {
                a = matrix[i][j];
                matrix[i][j] = matrix[n-1-j][i];
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j];
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i];
                matrix[j][n-1-i] = a;
            }
            i += 1;
        }
    }
};

```
