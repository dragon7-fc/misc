695. Max Area of Island

Given a non-empty 2D array `grid` of 0's and 1's, an island is a group of `1`'s (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

**Example 1:**
```
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
```

**Example 2:**
```
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
```

**Note:** The length of each dimension in the given grid does not exceed 50.

# Solution
## Approach #1: Depth-First Search (Recursive) [Accepted]
**Intuition and Algorithm**

We want to know the area of each connected shape in the grid, then take the maximum of these.

If we are on a land square and explore every square connected to it 4-directionally (and recursively squares connected to those squares, and so on), then the total number of squares explored will be the area of that connected shape.

To ensure we don't count squares in a shape more than once, let's use `seen` to keep track of squares we haven't visited before. It will also prevent us from counting the same shape more than once.

```python
class Solution(object):
    def maxAreaOfIsland(self, grid):
        seen = set()
        def area(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                    and (r, c) not in seen and grid[r][c]):
                return 0
            seen.add((r, c))
            return (1 + area(r+1, c) + area(r-1, c) +
                    area(r, c-1) + area(r, c+1))

        return max(area(r, c)
                   for r in range(len(grid))
                   for c in range(len(grid[0])))
```

**Complexity Analysis**

* Time Complexity: $O(R*C)$, where $R$ is the number of rows in the given grid, and $C$ is the number of columns. We visit every square once.

* Space complexity: $O(R*C)$, the space used by seen to keep track of visited squares, and the space used by the call stack during our recursion.

## Approach #2: Depth-First Search (Iterative) [Accepted]
**Intuition and Algorithm**

We can try the same approach using a stack based, (or "iterative") depth-first search.

Here, `seen` will represent squares that have either been visited or are added to our list of squares to visit (`stack`). For every starting land square that hasn't been visited, we will explore 4-directionally around it, adding land squares that haven't been added to `seen` to our `stack`.

On the side, we'll keep a count `shape` of the total number of squares seen during the exploration of this shape. We'll want the running max of these counts.

```python
class Solution(object):
    def maxAreaOfIsland(self, grid):
        seen = set()
        ans = 0
        for r0, row in enumerate(grid):
            for c0, val in enumerate(row):
                if val and (r0, c0) not in seen:
                    shape = 0
                    stack = [(r0, c0)]
                    seen.add((r0, c0))
                    while stack:
                        r, c = stack.pop()
                        shape += 1
                        for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                            if (0 <= nr < len(grid) and 0 <= nc < len(grid[0])
                                    and grid[nr][nc] and (nr, nc) not in seen):
                                stack.append((nr, nc))
                                seen.add((nr, nc))
                    ans = max(ans, shape)
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(R*C)$, where $R$ is the number of rows in the given grid, and $C$ is the number of columns. We visit every square once.

* Space complexity: $O(R*C)$, the space used by seen to keep track of visited squares, and the space used by stack.

# Submissions
---
**Solution 1: (DFS, recursive)**
```
Runtime: 128 ms
Memory Usage: N/A
```
```python
class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        seen = set()
        def area(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                   and (r, c) not in seen and grid[r][c]):
                return 0
            seen.add((r, c))
            return (1 
                    + area(r-1, c) 
                    + area(r+1, c) 
                    + area(r, c-1) 
                    + area(r, c+1))
            
        return max(area(r, c)
                  for r in range(len(grid))
                  for c in range(len(grid[0])))
```

**Solution 2: (DFS, recursive)**
```
Runtime: 108 ms
Memory Usage: N/A
```
```python
class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def area(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                   and grid[r][c]):
                return 0
            grid[r][c] = 0
            return (1 
                    + area(r-1, c) 
                    + area(r+1, c) 
                    + area(r, c-1) 
                    + area(r, c+1))
            
        return max(area(r, c)
                  for r in range(len(grid))
                  for c in range(len(grid[0])))
```

**Solution 3: (DFS, iterative)**
```
Runtime: 136 ms
Memory Usage: N/A
```
```python
class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        seen = set()
        ans = 0
        for r0, row in enumerate(grid):
            for c0, val in enumerate(row):
                if val and (r0, c0) not in seen:
                    shape = 0
                    stack = [(r0, c0)]
                    seen.add((r0, c0))
                    while stack:
                        r, c = stack.pop()
                        shape += 1
                        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                            if (0 <= nr < len(grid) and 0 <= nc < len(grid[0]) 
                                and grid[nr][nc] and (nr, nc) not in seen):
                                stack.append((nr, nc))
                                seen.add((nr, nc))
                    ans = max(ans, shape)
        return ans
```

**Solution 4: (DFS)**
```
Runtime: 38 ms
Memory Usage: 23.3 MB
```
```c++
class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int ans = 0;
        for (int r = 0; r < grid.size(); r++) {
            for (int c = 0; c < grid[0].size(); c++) {
                if (grid[r][c] == 1) {
                    ans = max(ans, dfs(r, c, grid));
                }
            }
        }
        return ans;
    }
    int dfs(int r, int c, vector<vector<int>> &grid) {
        if (r < 0 || r >= grid.size() || c < 0 || c >= grid[0].size() || grid[r][c] == 0)
            return 0;
        grid[r][c] = 0;
        int rst = 1;
        rst += dfs(r+1, c, grid);
        rst += dfs(r-1, c, grid);
        rst += dfs(r, c+1, grid);
        rst += dfs(r, c-1, grid);
        return rst;
    }
};
```

**Solution 5: (BFS)**
```
Runtime: 33 ms
Memory Usage: 26.8 MB
```
```c++
class Solution {
public:
    int dir[5]= {0, 1, 0, -1, 0};
    bool valid(int x,int y,vector<vector<int>>& grid){
        int n = grid.size();
        int m = grid[0].size();
        if(x>=0 && y>=0 && x<n && y<m && grid[x][y]==1)return true;
        return false;
    }
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int n = grid.size();
       int m = grid[0].size();
        int maxm = INT_MIN;
        for(int i = 0;i<n;i++){
            for(int j = 0;j<m;j++){
                int c=0;
                if(grid[i][j]){
                    queue<pair<int,int>>q;
                    grid[i][j]=0;
                    q.push({i,j});
                    while(!q.empty()){
                        auto src = q.front();
                        
                        q.pop();
                        c++;
                        for(int i = 0;i<4;i++){
                        int dx = dir[i]+src.first;
                        int dy = dir[i+1]+src.second;
                            if(valid(dx,dy,grid)){
                                
                                q.push({dx,dy});
                                grid[dx][dy]=0;
                            }
                        }
                    }
                  
                }
                  maxm = max(maxm,c);
            }
        }
        return maxm;
    }
};
```
