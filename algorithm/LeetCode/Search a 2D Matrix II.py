""" 
Search a 2D Matrix II

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

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

"""


""" Solution: 108 ms """
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


""" Solution2: 60 ms """
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        r = 0
        c = n - 1
        while r < m and c >= 0:
            if matrix[r][c] == target:
                return True
            if matrix[r][c] > target:
                c -= 1
            else: 
                r += 1
        return False


""" Solution3: 64 ms """
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if matrix:
            for i in range(m):
                if target in matrix[i][0:]:
                    return True
            return False
        else:
            return False


""" Solution4: 48 ms """
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix: return False
        if not matrix[0]: return False
        
        row = 0
        l = len(matrix)
        col = len(matrix[0])
        for i in range(l):
            if target > matrix[i][col-1]:
                continue
            if target < matrix[i][0]:
                return False
            if target in matrix[i]:
                return True
        return False
