980. Unique Paths III

On a 2-dimensional `grid`, there are 4 types of squares:

* `1` represents the starting square.  There is exactly one starting square.
* `2` represents the ending square.  There is exactly one ending square.
* `0` represents empty squares we can walk over.
* `-1` represents obstacles that we cannot walk over.

Return the number of 4-directional walks from the starting square to the ending square, that **walk over every non-obstacle square exactly once**.

 

**Example 1:**
```
Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
```

**Example 2:**
```
Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
```

**Example 3:**
```
Input: [[0,1],[2,0]]
Output: 0
Explanation: 
There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.
```

**Note:**

* `1 <= grid.length * grid[0].length <= 20`

# Solution
---
## Approach 1: Backtracking DFS
**Intuition and Algorithm**

Let's try walking to each `0`, leaving an obstacle behind from where we walked. After, we can remove the obstacle.

Given the input limits, this can work because bad paths tend to get stuck quickly and run out of free squares.

```python
class Solution:
    def uniquePathsIII(self, grid):
        R, C = len(grid), len(grid[0])

        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] % 2 == 0:
                    yield nr, nc

        todo = 0
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val != -1: todo += 1
                if val == 1: sr, sc = r, c
                if val == 2: tr, tc = r, c

        self.ans = 0
        def dfs(r, c, todo):
            todo -= 1
            if todo < 0: return
            if r == tr and c == tc:
                if todo == 0:
                    self.ans += 1
                return

            grid[r][c] = -1
            for nr, nc in neighbors(r, c):
                dfs(nr, nc, todo)
            grid[r][c] = 0

        dfs(sr, sc, todo)
        return self.ans
```

**Complexity Analysis**

* Time Complexity: $O(4^{R*C})$, where $R, C$ are the number of rows and columns in the `grid`. (We can find tighter bounds, but such a bound is beyond the scope of this article.)

* Space Complexity: $O(R*C)$.

## Approach 2: Dynamic Programming
**Intuition and Algorithm**

Let `dp(r, c, todo)` be the number of paths starting from where we are `(r, c)`, and given that todo is the set of empty squares we've yet to walk on.

We can use a similar approach to Approach 1, except we will memoize these states `(r, c, todo)` so as not to repeat work.

```python
from functools import lru_cache
class Solution:
    def uniquePathsIII(self, grid):
        R, C = len(grid), len(grid[0])

        def code(r, c):
            return 1 << (r * C + c)

        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] % 2 == 0:
                    yield nr, nc

        target = 0
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val % 2 == 0:
                    target |= code(r, c)

                if val == 1:
                    sr, sc = r, c
                if val == 2:
                    tr, tc = r, c

        @lru_cache(None)
        def dp(r, c, todo):
            if r == tr and c == tc:
                return +(todo == 0)

            ans = 0
            for nr, nc in neighbors(r, c):
                if todo & code(nr, nc):
                    ans += dp(nr, nc, todo ^ code(nr, nc))
            return ans

        return dp(sr, sc, target)
```

**Complexity Analysis**

* Time Complexity: $O(R * C * 2^{R*C})$, where $R, C$ are the number of rows and columns in the `grid`.

* Space Complexity: $O(R * C)$

# Submissions
---
**Solution 1: (Backtracking DFS)**
```
Runtime: 60 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] % 2 == 0:
                    yield nr, nc

        todo = 0
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val != -1: todo += 1
                if val == 1: sr, sc = r, c
                if val == 2: tr, tc = r, c

        self.ans = 0
        def dfs(r, c, todo):
            todo -= 1
            if todo < 0: return
            if r == tr and c == tc:
                if todo == 0:
                    self.ans += 1
                return

            grid[r][c] = -1
            for nr, nc in neighbors(r, c):
                dfs(nr, nc, todo)
            grid[r][c] = 0

        dfs(sr, sc, todo)
        return self.ans
```

**Solution 2: (DP Top-Down)**
```
Runtime: 84 ms
Memory Usage: 15.3 MB
```
```python
from functools import lru_cache
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        def code(r, c):
            return 1 << (r * C + c)

        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] % 2 == 0:
                    yield nr, nc

        target = 0
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val % 2 == 0:
                    target |= code(r, c)

                if val == 1:
                    sr, sc = r, c
                if val == 2:
                    tr, tc = r, c

        @lru_cache(None)
        def dp(r, c, todo):
            if r == tr and c == tc:
                return +(todo == 0)

            ans = 0
            for nr, nc in neighbors(r, c):
                if todo & code(nr, nc):
                    ans += dp(nr, nc, todo ^ code(nr, nc))
            return ans

        return dp(sr, sc, target)
```

**Solution 3: (DFS)**
```
Runtime: 4 ms
Memory Usage: 7.2 MB
```
```c++
class Solution {
public:
    int ans=0;
    void dfs(int i,int j,int n,int m,vector<vector<int>>& grid,int zero,int c){
        if(i<0 || i>=n || j<0 || j>=m || grid[i][j]==-1) return;
        if(grid[i][j]==2){
            if(zero+1==c)ans++;
            return;
        }
        grid[i][j]=-1;
        dfs(i+1,j,n,m,grid,zero,c+1);
        dfs(i,j+1,n,m,grid,zero,c+1);
        dfs(i-1,j,n,m,grid,zero,c+1);
        dfs(i,j-1,n,m,grid,zero,c+1);
        grid[i][j]=0;
    }
    int uniquePathsIII(vector<vector<int>>& grid) {
        int n=grid.size();
        if(n==0) return 0;
        int m=grid[0].size();
        int r,c,zero=0;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(grid[i][j]==1){
                    r=i;
                    c=j;
                }if(grid[i][j]==0){
                    zero++;
                }
            }
        }
        dfs(r,c,n,m,grid,zero,0);
        return ans;
    }
};
```