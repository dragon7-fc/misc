59. Spiral Matrix II

Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

**Example:**
```
Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
```

# Submissions
---
**Solution: (Traverse Layer by Layer in Spiral Form)**
```
Runtime: 0 ms
Memory Usage: 6.4 MB
```
```c++
class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> result (n, vector<int>(n));
        int cnt = 1;
        for (int layer = 0; layer < (n + 1) / 2; layer++) {
            // direction 1 - traverse from left to right
            for (int ptr = layer; ptr < n - layer; ptr++) {
                result[layer][ptr] = cnt++;
            }
            // direction 2 - traverse from top to bottom
            for (int ptr = layer + 1; ptr < n - layer; ptr++) {
                result[ptr][n - layer - 1] = cnt++;
            }
            // direction 3 - traverse from right to left
            for (int ptr = n - layer - 2; ptr >= layer; ptr--) {
                result[n - layer - 1][ptr] = cnt++;
            }
            // direction 4 - traverse from bottom to top
            for (int ptr = n - layer - 2; ptr > layer; ptr--) {
                result[ptr][layer] = cnt++;
            }
        }

        return result;
    }
};
```

**Solution: (Optimized spiral traversal)**
```
Runtime: 4 ms
Memory Usage: 6.6 MB
```
```c++
class Solution {
    int floorMod(int x, int y) {
        return ((x % y) + y) % y;
    }
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> result (n, vector<int>(n));
        int cnt = 1;
        int dir[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
       int d = 0;
        int row = 0;
        int col = 0;
        while (cnt <= n * n) {
            result[row][col] = cnt++;
            int r = floorMod(row + dir[d][0], n);
            int c = floorMod(col + dir[d][1], n);
            // change direction if next cell is non zero
            if (result[r][c] != 0) d = (d + 1) % 4;
            row += dir[d][0];
            col += dir[d][1];
        }
        return result;
    }
};
```

**Solution 1: (Math)**
```
Runtime: 40 ms
Memory Usage: 13.7 MB
```
```python
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        counter = 1
        m = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n//2):
            for j in range(i,n-i-1):
                m[i][j] = counter
                m[j][n-i-1] = counter + n-1-(i*2)
                m[n-1-i][n-j-1] = counter + 2 * (n-1-(i*2))
                m[n-j-1][i] = counter + 3 * (n-1-(i*2))
                counter +=1
            counter = counter + 3 * (n-1-(i*2))
        if n %2 == 1:
            m[n//2][n//2] = n*n
        return m
```

**Solution 2: (DFS)**
```
Runtime: 28 ms
Memory Usage: 14.6 MB
```
```python
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0]*n for _ in range(n)]
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        
        def dfs(x, y, d, k):
            ans[x][y] = k
            nx, ny = x+dx[d], y+dy[d]
            if 0 <= nx < n and  0 <= ny < n and ans[nx][ny] == 0:
                dfs(nx, ny, d, k+1)
            else:
                d = (d+1)%4
                nx, ny = x+dx[d], y+dy[d]
                if 0 <= nx < n and  0 <= ny < n and ans[nx][ny] == 0:
                    dfs(nx, ny, d, k+1)
            
        dfs(0, 0, 0, 1)
        return ans
```

**Solution 3: (Brute Force)**
```
Runtime: 4 ms
Memory Usage: 6.5 MB
```
```c++
class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> ans(n, vector<int>(n));
        int diff[4][2] = {
            {0, 1},
            {1, 0},
            {0, -1},
            {-1, 0}
        };
        int dir = 0, i = 0, j = 0;
        for (int cur = 1; cur <= n*n; cur ++) {
            ans[i][j] = cur;
            int ni, nj;
            ni = i + diff[dir][0];
            nj = j + diff[dir][1];
            if (ni >= n || ni < 0 || nj >= n || nj < 0 || ans[ni][nj]) {
                dir = (dir+1)%4;
                ni = i + diff[dir][0];
                nj = j + diff[dir][1];
            }
            i = ni;
            j = nj;
        }
        return ans;
    }
};
```
