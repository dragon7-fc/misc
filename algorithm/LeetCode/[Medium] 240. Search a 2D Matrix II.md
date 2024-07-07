240. Search a 2D Matrix II

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

* Integers in each row are sorted in ascending from left to right.
* Integers in each column are sorted in ascending from top to bottom.

**Example:**
```
Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
```

**Solution 1:**
```
Runtime: 40 ms
Memory Usage: 17.4 MB
```
```python
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        return target in [matrix[r][c] for r in range(len(matrix)) for c in range(len(matrix[0]))]
```

**Solution 2: (DFS, Divide and Conquer)**
```
Runtime: 36 ms
Memory Usage: 17.5 MB
```
```python
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        def search(matrix, rows, cols):
            if rows >= len(matrix) or cols < 0:
                return False
            upper_right = matrix[rows][cols]
            if upper_right > target:
                return search(matrix, rows, cols - 1)
            elif upper_right < target:
                return search(matrix, rows + 1, cols)
            else:
                return True
        return search(matrix, 0, len(matrix[0]) - 1)
```

**Solution 3: (Iterative)**
```
Runtime: 36 ms
Memory Usage: 17.5 MB
```
```python
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        R, C = len(matrix), len(matrix[0])
        i, j = 0, C-1
        while i <= R - 1 and j >= 0:
            if matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1
            else:
                return True
        return False
```

**Solution 4: (Binary Search)**
```
Runtime: 32 ms
Memory Usage: 17.5 MB
```
```python
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows = len(matrix)
        cols = len(matrix[0]) if rows else 0
        pivot = cols - 1

        if cols == 0:
            return False
        
        for row in range(rows):  
            
            if target > matrix[row][pivot]:
                continue
                 
            pivot = bisect.bisect_left(matrix[row], target)
            
            if pivot != cols and matrix[row][pivot] == target:
                return True
            
        return False
```

**Solution 5: (Binary Search, two pointes)**
```
Runtime: 196 ms
Memory Usage: 14.8 MB
```
```c++
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size();
        int n = matrix[0].size();
        
        int i = m - 1;
        int j = 0;
        
        while (i>=0 && j<n){
            
            if (matrix[i][j] == target) return true;
            
            else if (matrix[i][j] < target) j++;
            
            else i--;
        }
        return false;
    }
};
```
