1905. Count Sub Islands

You are given two `m x n` binary matrices `grid1` and `grid2` containing only `0`'s (representing water) and `1`'s (representing land). An **island** is a group of `1`'s connected **4-directionally** (horizontal or vertical). Any cells outside of the grid are considered water cells.

An island in `grid2` is considered a **sub-island** if there is an island in `grid1` that contains **all** the cells that make up **this** island in `grid2`.

Return the **number** of islands in `grid2` that are considered **sub-islands**.

 

**Example 1:**

![1905_test1.png](img/1905_test1.png)
```
Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
Output: 3
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.
```

**Example 2:**

![1905_testcasex2.png](img/1905_testcasex2.png)
```
Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
Output: 2 
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are two sub-islands.
```

**Constraints:**

* `m == grid1.length == grid2.length`
* `n == grid1[i].length == grid2[i].length`
* `1 <= m, n <= 500`
* `grid1[i][j]` and `grid2[i][j]` are either `0` or `1`.

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 3544 ms
Memory Usage: 122 MB
```
```python
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        n, m = len(grid2), len(grid2[0])

        def dfs(i, j):
            if not (0 <= i < n and 0 <= j < m and grid2[i][j] == 1): return 1
            grid2[i][j] = 0
            res = grid1[i][j]
            for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                res &= dfs(i + di, j + dj)
            return res
            
        return sum(dfs(i, j) for i in range(n) for j in range(m) if grid2[i][j])
```

**Solution 2: (DFS)**
```
Runtime: 206 ms
Memory: 91.69 MB
```
```c++
class Solution {
    int dd[5] = {0, 1, 0, -1, 0};
    bool dfs(int i, int j, vector<vector<int>> &grid1, vector<vector<int>> &grid2) {
        bool rst = grid1[i][j] == 0;
        grid2[i][j] = 0;
        int ni, nj;
        for (int d = 0; d < 4; d ++) {
            ni = i + dd[d];
            nj = j + dd[d+1];
            if (0 <= ni && ni < grid1.size() && 0 <= nj && nj < grid1[0].size() && grid2[ni][nj] == 1) {
                rst |= dfs(ni, nj, grid1, grid2);
            }
        }
        return rst;
    }
public:
    int countSubIslands(vector<vector<int>>& grid1, vector<vector<int>>& grid2) {
        int ans = 0;
        for (int i = 0; i < grid1.size(); i ++) {
            for (int j = 0; j < grid1[0].size(); j ++) {
                if (grid2[i][j] == 1) {
                    if (!dfs(i, j, grid1, grid2)) {
                        ans += 1;
                    }
                }
            }
        }
        return ans;
    }
};
```
