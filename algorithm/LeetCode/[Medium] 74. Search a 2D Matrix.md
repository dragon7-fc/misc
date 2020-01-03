74. Search a 2D Matrix

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

* Integers in each row are sorted from left to right.
* The first integer of each row is greater than the last integer of the previous row.

**Example 1:**
```
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
```

**Example 2:**
```
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
```

# Submissions
---
**Solution 1:**
```
Runtime: 40 ms
Memory Usage: N/A
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
        for row in matrix:
            if target in row:
                return True
        return False
```

**Solution 2:**
```
Runtime: 64 ms
Memory Usage: 14.8 MB
```
```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search_1d(row, target):
            lo = 0
            hi = len(row) - 1

            while lo <= hi:
                mid = lo + (hi - lo) // 2

                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1

            return False
        
        def binary_search_2d(matrix, target):
            lo = 0
            hi = len(matrix) - 1

            while lo <= hi:
                mid = lo + (hi - lo) // 2

                if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                    return binary_search_1d(matrix[mid], target)
                elif matrix[mid][0] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
        
            return False
        
        if not matrix:
            return False
        elif len(matrix) == 1:
            return binary_search_1d(matrix[0], target)
        else:
            return binary_search_2d(matrix, target)
```