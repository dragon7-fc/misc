""" 
Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

"""


""" Solution: 60 ms """
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        mps = [[0 for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if i == 0 and j == 0:
                    mps[i][j] = grid[i][j]
                elif i == 0:
                    mps[i][j] = mps[i][j-1] + grid[i][j]
                elif j == 0:
                    mps[i][j] = mps[i-1][j] + grid[i][j]
                else:
                    mps[i][j] = min(mps[i-1][j], mps[i][j-1]) + grid[i][j]
        return mps[-1][-1]