2128. Remove All Ones With Row and Column Flips

You are given an `m x n` binary matrix `grid`.

In one operation, you can choose **any** row or column and flip each value in that row or column (i.e., changing all `0`'s to `1`'s, and all `1`'s to `0`'s).

Return `true` if it is possible to remove all `1`'s from grid using any number of operations or `false` otherwise.

 

**Example 1:**

```
Input: grid = [[0,1,0],[1,0,1],[0,1,0]]
Output: true
Explanation: One possible way to remove all 1's from grid is to:
- Flip the middle row
- Flip the middle column
```

**Example 2:**

```
Input: grid = [[1,1,0],[0,0,0],[0,0,0]]
Output: false
Explanation: It is impossible to remove all 1's from grid.
```

**Example 3:**

```
Input: grid = [[0]]
Output: true
Explanation: There are no 1's in grid.
```

**Constraints:**

* `m == grid.length`
* `n == grid[i].length`
* `1 <= m, n <= 300`
* `grid[i][j`] is either `0` or `1`.

# Submissions
---
**Solution 1: (Marker)**
```
Runtime: 440 ms
Memory Usage: 16.6 MB
```
```python
class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        reverse = [1 - x for x in grid[0]]
        return all(grid[row] == grid[0] or grid[row] == reverse for row in range(1, len(grid)))
```

**Solution 2: (Marker)**
```
Runtime: 63 ms
Memory Usage: 24.5 MB
```
```c++
class Solution {
public:
    bool removeOnes(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        
        for(int row = 1; row < m; row++) {
            bool flip = grid[0][0] != grid[row][0];
            
            for(int col = 0; col < n; col++) {
                int cell = grid[row][col];
                
                if(flip) cell = 1 - cell;
                if(grid[0][col] != cell) return false;
            }
        }
        
        return true;
    }
};
```
