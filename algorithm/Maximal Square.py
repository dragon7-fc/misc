''' 
Maximal Square

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4

'''


''' Solution: 176 ms '''
class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == []:
            return 0
        m, n, cur, pre = len(matrix), len(matrix[0]), 0, 0
        dp = [0 for _ in range(n+1)]
        for i in range(1,m+1) :
            for j in range(1,n+1) :
                temp = dp[j]
                if(matrix[i-1][j-1] == "1"):
                    dp[j] = min(dp[j - 1], pre,dp[j]) + 1
                    cur = max(cur,dp[j])
                else:
                    dp[j] = 0
                pre = temp
        return cur*cur


''' Solution2: 64 ms '''
class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or len(matrix) == 0:
            return 0
        lrow = len(matrix)
        lcol = len(matrix[0])
        
        # dp array stores max length of edge of the square ends at this point
        dp_row = matrix[0] 
        for index in range(lcol): 
            dp_row[index]=int(dp_row[index])
        maxArea = max(dp_row) # to counter corner case that there is only one row

        for row in range(1, lrow):
            dp_row2 = [int(matrix[row][0])]+[0 for _ in range(1, lcol)]
            for col in range(1, lcol):
                if matrix[row][col] == "1":
                    dp_row2[col] = min(dp_row[col], dp_row2[col-1], dp_row[col-1]) + 1
            maxArea = max(maxArea, max(dp_row2))
            dp_row = list(dp_row2)
                    
        return maxArea**2
        