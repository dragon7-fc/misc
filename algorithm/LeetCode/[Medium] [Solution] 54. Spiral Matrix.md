54. Spiral Matrix

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

**Example 1:**
```
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
```

**Example 2:**
```
Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

# Solution
---
## Approach 1: Simulation
**Intuition**

Draw the path that the spiral makes. We know that the path should turn clockwise whenever it would go out of bounds or into a cell that was previously visited.

**Algorithm**

Let the array have $\text{R}$ rows and $\text{C}$ columns. $\text{seen[r][c]}$ denotes that the cell on the $\text{r}$-th row and $\text{c}$-th column was previously visited. Our current position is $\text{(r, c)}$, facing direction $\text{di}$, and we want to visit $\text{R} x \text{C}$ total cells.

As we move through the matrix, our candidate next position is $\text{(cr, cc)}$. If the candidate is in the bounds of the matrix and unseen, then it becomes our next position; otherwise, our next position is the one after performing a clockwise turn.

```python
class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix: return []
        R, C = len(matrix), len(matrix[0])
        seen = [[False] * C for _ in matrix]
        ans = []
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0
        for _ in range(R * C):
            ans.append(matrix[r][c])
            seen[r][c] = True
            cr, $c$ = r + dr[di], c + dc[di]
            if 0 <= cr < R and 0 <= $c$ < C and not seen[cr][cc]:
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the total number of elements in the input matrix. We add every element in the matrix to our final answer.

* Space Complexity: $O(N)$, the information stored in `seen` and in `ans`.

## Approach 2: Layer-by-Layer
**Intuition**

The answer will be all the elements in clockwise order from the first-outer layer, followed by the elements from the second-outer layer, and so on.

**Algorithm**

We define the $\text{k}$-th outer layer of a matrix as all elements that have minimum distance to some border equal to $\text{k}$. For example, the following matrix has all elements in the first-outer layer equal to 1, all elements in the second-outer layer equal to 2, and all elements in the third-outer layer equal to 3.

```
[[1, 1, 1, 1, 1, 1, 1],
 [1, 2, 2, 2, 2, 2, 1],
 [1, 2, 3, 3, 3, 2, 1],
 [1, 2, 2, 2, 2, 2, 1],
 [1, 1, 1, 1, 1, 1, 1]]
```

For each outer layer, we want to iterate through its elements in clockwise order starting from the top left corner. Suppose the current outer layer has top-left coordinates $\text{(r1, c1)}$ and bottom-right coordinates $\text{(r2, c2)}$.

Then, the top row is the set of elements $\text{(r1, c)}$ for $\text{c = c1,...,c2}$, in that order. The rest of the right side is the set of elements $\text{(r, c2)}$ for $\text{r = r1+1,...,r2}$, in that order. Then, if there are four sides to this layer (ie., $\text{r1 < r2}$ and $\text{c1 < c2}$, we iterate through the bottom side and left side as shown in the solutions below.

![spiralmatrix](img/54_spiralmatrix.png)

```python
class Solution(object):
    def spiralOrder(self, matrix):
        def spiral_coords(r1, c1, r2, c2):
            for c in range(c1, c2 + 1):
                yield r1, c
            for r in range(r1 + 1, r2 + 1):
                yield r, c2
            if r1 < r2 and c1 < c2:
                for c in range(c2 - 1, c1, -1):
                    yield r2, c
                for r in range(r2, r1, -1):
                    yield r, c1

        if not matrix: return []
        ans = []
        r1, r2 = 0, len(matrix) - 1
        c1, c2 = 0, len(matrix[0]) - 1
        while r1 <= r2 and c1 <= c2:
            for r, c in spiral_coords(r1, c1, r2, c2):
                ans.append(matrix[r][c])
            r1 += 1; r2 -= 1
            c1 += 1; c2 -= 1
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the total number of elements in the input matrix. We add every element in the matrix to our final answer.

* Space Complexity: $O(N)$, the information stored in `ans`.

# Submissions
---
**Solution 1: (Simulation)**
```
Runtime: 32 ms
Memory Usage: 13.7 MB
```
```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        R, C = len(matrix), len(matrix[0])
        seen = [[False] * C for _ in matrix]
        ans = []
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0
        for _ in range(R * C):
            ans.append(matrix[r][c])
            seen[r][c] = True
            cr, cc = r + dr[di], c + dc[di]
            if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        return ans
```

**Solution 2: (Simulation)**
```
Runtime: 2 ms
Memory Usage: 6.8 MB
```
```c++
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> result;
        int rowBegin, colBegin, rowEnd, colEnd;
        rowBegin = colBegin = 0, rowEnd = matrix.size() - 1, colEnd = matrix[0].size() - 1;
        while (rowBegin <= rowEnd && colBegin <= colEnd) {
            for (int j = colBegin; j <= colEnd; j++)  // Traverse Right
                result.push_back(matrix[rowBegin][j]);
            
            for (int i = ++rowBegin; i <= rowEnd; i++) // Traverse Down
                result.push_back(matrix[i][colEnd]);
            
            for (int j = --colEnd; rowBegin <= rowEnd && j >= colBegin; j--) // Traverse Left
                result.push_back(matrix[rowEnd][j]);
            
            for (int i = --rowEnd; colBegin <= colEnd && i >= rowBegin; i--) // Traver Up
                result.push_back(matrix[i][colBegin]);
            
            colBegin++;
        }
        return result;
    }
};
```

**Solution 3: (DFS)**
```
Runtime: 0 ms
Memory: 6.9 MB
```
```c++
class Solution {
    int d[4] = {0, 1, 0, -1};
    void dfs(int r, int c, int dd, vector<int> &ans, vector<vector<int>> &matrix) {
        ans.push_back(matrix[r][c]);
        matrix[r][c] = INT_MAX;
        int nr = r + d[dd], nc = c + d[(dd+1)%4];
        if (!(0 <= nr) || !(nr < matrix.size()) || !(0 <= nc) || !(nc < matrix[0].size()) || matrix[nr][nc] == INT_MAX) {
            dd = (dd+1) % 4;
            nr = r + d[dd];
            nc = c + d[(dd+1)%4];
            if (!(0 <= nr) || !(nr < matrix.size()) || !(0 <= nc) || !(nc < matrix[0].size()) || matrix[nr][nc] == INT_MAX) {
            return;
            }
        }
        dfs(nr, nc, dd, ans, matrix);
    }
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> ans;
        dfs(0, 0, 0, ans, matrix);
        return ans;
    }
};
```

**Solution 4: Mark Visited Elements()**
```
Runtime: 3 ms
Memory: 8.04 MB
```
```c++
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        const int VISITED = 101;
        int rows = matrix.size(), columns = matrix[0].size();
        // Four directions that we will move: right, down, left, up.
        vector<vector<int>> directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        // Initial direction: moving right.
        int currentDirection = 0;
        // The number of times we change the direction.
        int changeDirection = 0;
        // Current place that we are at is (row, col).
        // row is the row index; col is the column index.
        int row = 0, col = 0;
        // Store the first element and mark it as visited.
        vector<int> result = {matrix[0][0]};
        matrix[0][0] = VISITED;
        while (changeDirection < 2) {
            while (0 <= row + directions[currentDirection][0] &&
                   row + directions[currentDirection][0] < rows &&
                   0 <= col + directions[currentDirection][1] &&
                   col + directions[currentDirection][1] < columns &&
                   matrix[row + directions[currentDirection][0]]
                         [col + directions[currentDirection][1]] != VISITED) {
                // Reset this to 0 since we did not break and change the
                // direction.
                changeDirection = 0;
                // Calculate the next place that we will move to.
                row += directions[currentDirection][0];
                col += directions[currentDirection][1];
                result.push_back(matrix[row][col]);
                matrix[row][col] = VISITED;
            }
            // Change our direction.
            currentDirection = (currentDirection + 1) % 4;
            // Increment change_direction because we changed our direction.
            changeDirection++;
        }
        return result;
    }
};
```

**Solution 5: (Set Up Boundaries)**
```
Runtime: 0 ms
Memory: 8.20 MB
```
```c++
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> result;
        int rows = matrix.size();
        int columns = matrix[0].size();
        int up = 0;
        int left = 0;
        int right = columns - 1;
        int down = rows - 1;
        while (result.size() < rows * columns) {
            // Traverse from left to right.
            for (int col = left; col <= right; col++) {
                result.push_back(matrix[up][col]);
            }
            // Traverse downwards.
            for (int row = up + 1; row <= down; row++) {
                result.push_back(matrix[row][right]);
            }
            // Make sure we are now on a different row.
            if (up != down) {
                // Traverse from right to left.
                for (int col = right - 1; col >= left; col--) {
                    result.push_back(matrix[down][col]);
                }
            }
            // Make sure we are now on a different column.
            if (left != right) {
                // Traverse upwards.
                for (int row = down - 1; row > up; row--) {
                    result.push_back(matrix[row][left]);
                }
            }
            left++;
            right--;
            up++;
            down--;
        }
        return result;
    }
};
```

**Solution 6: (Set Up Boundaries)**
```
Runtime: 0 ms
Memory: 8.10 MB
```
```c++
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int top = 0, bottom = matrix.size()-1, left = 0, right = matrix[0].size()-1;
        vector<int> ans;
        while (top <= bottom && left <= right) {
            for (int i = left; i <= right; i ++) {
                ans.push_back(matrix[top][i]);
            }
            top += 1;
            if (top > bottom) {
                break;
            }
            for (int i = top; i <= bottom; i ++) {
                ans.push_back(matrix[i][right]);
            }
            right -= 1;
            if (right < left) {
                break;
            }
            for (int i = right; i >= left; i --) {
                ans.push_back(matrix[bottom][i]);
            }
            bottom -= 1;
            for (int i = bottom; i >= top; i --) {
                ans.push_back(matrix[i][left]);
            }
            left += 1;
        }
        return ans;
    }
};
```
