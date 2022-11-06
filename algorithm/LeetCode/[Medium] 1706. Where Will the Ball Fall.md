1706. Where Will the Ball Fall

You have a 2-D grid of size `m x n` representing a box, and you have `n` balls. The box is open on the top and bottom sides.

Each cell in the box has a diagonal board spanning two corners of the cell that can redirect a ball to the right or to the left.

* A board that redirects the ball to the right spans the top-left corner to the bottom-right corner and is represented in the grid as `1`.
* A board that redirects the ball to the left spans the top-right corner to the bottom-left corner and is represented in the grid as `-1`.

We drop one ball at the top of each column of the box. Each ball can get stuck in the box or fall out of the bottom. A ball gets stuck if it hits a "V" shaped pattern between two boards or if a board redirects the ball into either wall of the box.

Return an array `answer` of size `n` where `answer[i]` is the column that the ball falls out of at the bottom after dropping the ball from the `i`th column at the top, or `-1` if the ball gets stuck in the box.

 

**Example 1:**

![1706_ball.jpg](img/1706_ball.jpg)
```
Input: grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
Output: [1,-1,-1,-1,-1]
Explanation: This example is shown in the photo.
Ball b0 is dropped at column 0 and falls out of the box at column 1.
Ball b1 is dropped at column 1 and will get stuck in the box between column 2 and 3 and row 1.
Ball b2 is dropped at column 2 and will get stuck on the box between column 2 and 3 and row 0.
Ball b3 is dropped at column 3 and will get stuck on the box between column 2 and 3 and row 0.
Ball b4 is dropped at column 4 and will get stuck on the box between column 2 and 3 and row 1.
```

**Example 2:**

Input: grid = [[-1]]
Output: [-1]
Explanation: The ball gets stuck against the left wall.

**Example 3:**
```
Input: grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
Output: [0,1,2,3,4,-1]
```

**Constraints:**

* `m == grid.length`
* `n == grid[i].length`
* `1 <= m, n <= 100`
* `grid[i][j]` is `1` or `-1`.

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 50 ms
Memory: 13.1 MB
```
```c++
class Solution {
    int findBallDropColumn(int row, int col, vector<vector<int>>& grid) {
        // base case; ball reached the last row
        if (row == grid.size()) return col;
        int nextColumn = col + grid[row][col];
        if (nextColumn < 0 || nextColumn > grid[0].size() - 1 ||
            grid[row][col] != grid[row][nextColumn]) {
            return -1;
        }
        return findBallDropColumn(row + 1, nextColumn, grid);
    }
public:
    vector<int> findBall(vector<vector<int>>& grid) {
        vector<int> result(grid[0].size(), 0);
        for (int i = 0; i < grid[0].size(); i++) {
            result[i] = findBallDropColumn(0, i, grid);
        }
        return result;
    }
};
```

**Solution 2: (DP)**
```
Runtime: 25 ms
Memory: 14.1 MB
```
```c++
class Solution {
public:
    vector<int> findBall(vector<vector<int>>& grid) {
        vector<int> result(grid[0].size(), 0);
        vector<vector<int>> memo(grid.size() + 1, vector<int>(grid[0].size(), 0));

        for (int row = int(grid.size()); row >= 0; row--) {
            for (int col = 0; col < grid[0].size(); col++) {
                if (row == grid.size()) {
                    memo[row][col] = col;
                    continue;
                }
                int nextColumn = col + grid[row][col];
                if (nextColumn < 0 || nextColumn > grid[0].size() - 1 ||
                    grid[row][col] != grid[row][nextColumn])
                    memo[row][col] = -1;
                else
                    memo[row][col] = memo[row + 1][nextColumn];
                if (row == 0) {
                    result[col] = memo[row][col];
                }
            }
        }
        return result;
    }
};
```

**Solution 3: (Iterative Approach, Simulation)**
```
Runtime: 69 ms
Memory: 13.1 MB
```
```c++
class Solution {
public:
    vector<int> findBall(vector<vector<int>>& grid) {
        vector<int> result(grid[0].size(), 0);

        for (int col = 0; col < grid[0].size(); col++) {
            int currentCol = col;
            for (int row = 0; row < grid.size(); row++) {
                int nextColumn = currentCol + grid[row][currentCol];
                if (nextColumn < 0 || nextColumn > grid[0].size() - 1 ||
                    grid[row][currentCol] != grid[row][nextColumn]) {
                    result[col] = -1;
                    break;
                }
                result[col] = nextColumn;
                currentCol = nextColumn;
            }
        }
        return result;
    }
};
```
