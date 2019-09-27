63. Unique Paths II

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

![robot_maze](img/63_robot_maze.png)

An obstacle and empty space is marked as `1` and `0` respectively in the grid.

**Note:** m and n will be at most 100.
```
Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
```

# Solution
---


# Submissions
---
## Approach 1: Dynamic Programming
**Intuition**

The robot can only move either down or right. Hence any cell in the first row can only be reached from the cell left to it.

![63_1_1](img/63_1_1.png)
![63_1_2](img/63_1_2.png)
![63_1_3](img/63_1_3.png)
![63_1_4](img/63_1_4.png)

And, any cell in the first column can only be reached from the cell above it.

![63_2_1](img/63_2_1.png)
![63_2_2](img/63_2_2.png)
![63_2_3](img/63_2_3.png)
![63_2_4](img/63_2_4.png)

For any other cell in the grid, we can reach it either from the cell to left of it or the cell above it.

If any cell has an obstacle, we won't let that cell contribute to any path.

We will be iterating the array from left-to-right and top-to-bottom. Thus, before reaching any cell we would have the number of ways of reaching the predecessor cells. This is what makes it a Dynamic Programming problem. We will be using the `obstacleGrid` array as the DP array thus not utilizing any additional space.

Note: As per the question, cell with an obstacle has a value 1. We would use this value to make sure if a cell needs to be included in the path or not. After that we can use the same cell to store the number of ways to reach that cell.

**Algorithm**
1. If the first cell i.e. `obstacleGrid[0,0]` contains `1`, this means there is an obstacle in the first cell. Hence the robot won't be able to make any move and we would return the number of ways as 0.
1. Otherwise, if `obstacleGrid[0,0]` has a 0 originally we set it to 1 and move ahead.
1. Iterate the first row. If a cell originally contains a 1, this means the current cell has an obstacle and shouldn't contribute to any path. Hence, set the value of that cell to 0. Otherwise, set it to the value of previous cell i.e. `obstacleGrid[i,j] = obstacleGrid[i,j-1]`
1. Iterate the first column. If a cell originally contains a 1, this means the current cell has an obstacle and shouldn't contribute to any path. Hence, set the value of that cell to 0. Otherwise, set it to the value of previous cell i.e. `obstacleGrid[i,j] = obstacleGrid[i-1,j]`
1. Now, iterate through the array starting from cell `obstacleGrid[1,1]`. If a cell originally doesn't contain any obstacle then the number of ways of reaching that cell would be the sum of number of ways of reaching the cell above it and number of ways of reaching the cell to the left of it.
`obstacleGrid[i,j] = obstacleGrid[i-1,j] + obstacleGrid[i,j-1]`
1. If a cell contains an obstacle set it to 0 and continue. This is done to make sure it doesn't contribute to any other path.

Following is the animation to explain the algorithm's steps:

![63_3_1](img/63_3_1.png)
![63_3_2](img/63_3_2.png)
![63_3_3](img/63_3_3.png)
![63_3_4](img/63_3_4.png)
![63_3_5](img/63_3_5.png)
![63_3_6](img/63_3_6.png)
![63_3_7](img/63_3_7.png)
![63_3_8](img/63_3_8.png)
![63_3_9](img/63_3_9.png)
![63_3_10](img/63_3_10.png)
![63_3_11](img/63_3_11.png)
![63_3_12](img/63_3_12.png)
![63_3_13](img/63_3_13.png)
![63_3_14](img/63_3_14.png)
![63_3_15](img/63_3_15.png)
![63_3_16](img/63_3_16.png)
![63_3_17](img/63_3_17.png)
![63_3_18](img/63_3_18.png)

```python
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # If the starting cell has an obstacle, then simply return as there would be
        # no paths to the destination.
        if obstacleGrid[0][0] == 1:
            return 0

        # Number of ways of reaching the starting cell = 1.
        obstacleGrid[0][0] = 1

        # Filling the values for the first column
        for i in range(1,m):
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1)

        # Filling the values for the first row        
        for j in range(1, n):
            obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] == 1)

        # Starting from cell(1,1) fill up the values
        # No. of ways of reaching cell[i][j] = cell[i - 1][j] + cell[i][j - 1]
        # i.e. From above and left.
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0

        # Return value stored in rightmost bottommost cell. That is the destination.            
        return obstacleGrid[m-1][n-1]
```

**Complexity Analysis**

* Time Complexity: $O(M \times N)$. The rectangular grid given to us is of size $M \times N$ and we process each cell just once.
* Space Complexity: $O(1)$. We are utilizing the obstacleGrid as the DP array. Hence, no extra space.

# Submissions
---
**Solution:**
```
Runtime: 48 ms
Memory Usage: 14 
```
```python
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # If the starting cell has an obstacle, then simply return as there would be
        # no paths to the destination.
        if obstacleGrid[0][0] == 1:
            return 0

        # Number of ways of reaching the starting cell = 1.
        obstacleGrid[0][0] = 1

        # Filling the values for the first column
        for i in range(1,m):
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1)

        # Filling the values for the first row        
        for j in range(1, n):
            obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] == 1)

        # Starting from cell(1,1) fill up the values
        # No. of ways of reaching cell[i][j] = cell[i - 1][j] + cell[i][j - 1]
        # i.e. From above and left.
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0

        # Return value stored in rightmost bottommost cell. That is the destination.            
        return obstacleGrid[m-1][n-1]
```