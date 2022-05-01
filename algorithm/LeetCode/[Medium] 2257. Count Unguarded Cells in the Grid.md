2257. Count Unguarded Cells in the Grid

You are given two integers `m` and `n` representing a **0-indexed** `m x n` grid. You are also given two 2D integer arrays `guards` and `walls` where `guards[i] = [rowi, coli]` and `walls[j] = [rowj, colj]` represent the positions of the `i`th guard and `j`th wall respectively.

A guard can see **every** cell in the four cardinal directions (north, east, south, or west) starting from their position unless **obstructed** by a wall or another guard. A cell is **guarded** if there is **at least** one guard that can see it.

Return the number of unoccupied cells that are **not guarded**.

 

**Example 1:**

![2257_example1drawio2.png](img/2257_example1drawio2.png)
```
Input: m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
Output: 7
Explanation: The guarded and unguarded cells are shown in red and green respectively in the above diagram.
There are a total of 7 unguarded cells, so we return 7.
```

**Example 2:**

![2257_example2drawio.png](img/2257_example2drawio.png)
```
Input: m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]
Output: 4
Explanation: The unguarded cells are shown in green in the above diagram.
There are a total of 4 unguarded cells, so we return 4.
```

**Constraints:**

* `1 <= m, n <= 10^5`
* `2 <= m * n <= 10^5`
* `1 <= guards.length, walls.length <= 5 * 10^4`
* `2 <= guards.length + walls.length <= m * n`
* `guards[i].length == walls[j].length == 2`
* `0 <= rowi, rowj < m`
* `0 <= coli, colj < n`
* All the positions in `guards` and `walls` are **unique**.

# Submissions
---
**Solution 1: (Graph)**
```
Runtime: 2940 ms
Memory Usage: 42.6 MB
```
```python
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        dp = [[0] * n for _ in range(m)]
        for x, y in guards+walls:
            dp[x][y] = 1
               
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        for x, y in guards:
            for dx, dy in directions:
                curr_x = x
                curr_y = y
                
                while 0 <= curr_x+dx < m and 0 <= curr_y+dy < n and dp[curr_x+dx][curr_y+dy] != 1:
                    curr_x += dx
                    curr_y += dy
                    dp[curr_x][curr_y] = 2
                    
        return sum(1 for i in range(m) for j in range(n) if dp[i][j] == 0)  
```

**Solution 2: (Graph)**
```
Runtime: 539 ms
Memory Usage: 154 MB
```
```c++
class Solution {
public:
    int countUnguarded(int m, int n, vector<vector<int>>& guards, vector<vector<int>>& walls) {
        // m is no. of rows, n is no. of columns, g is guards vector and w is walls vector
        vector<vector<int>> v(m, vector<int> (n,0));
        int k = walls.size();
        for(int i=0;i<k;i++){
            int x = walls[i][0], y = walls[i][1];
            v[x][y] = -2;
        }
        k = guards.size();
        for(int i=0;i<k;i++){
            int x = guards[i][0], y = guards[i][1];
            v[x][y] = 2;
        }
        for(int j=0;j<k;j++){
            int x = guards[j][0], y = guards[j][1];
            for(int i=x-1;i>=0;i--){ // up
                if(v[i][y]==-2 || v[i][y]==2) break;
                v[i][y] = 1;
            }
            for(int i=x+1;i<m;i++){ // down
                if(v[i][y]==-2 || v[i][y]==2) break;
                v[i][y] = 1;
            }
            for(int i=y-1;i>=0;i--){ // left
                if(v[x][i]==-2 || v[x][i]==2) break;
                v[x][i] = 1;
            }
            for(int i=y+1;i<n;i++){ // right
                if(v[x][i]==-2 || v[x][i]==2) break;
                v[x][i] = 1;
            }
        }
        int ans = 0;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(!v[i][j]) ans++;
            }
        }
        return ans;
    }
};
```
