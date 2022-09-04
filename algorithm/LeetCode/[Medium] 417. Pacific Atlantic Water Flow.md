417. Pacific Atlantic Water Flow

Given an `m x n` matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

**Note:**

* The order of returned grid coordinates does not matter.
* Both `m` and `n` are less than 150.
 

**Example:**
```
Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
```

# Submissions
---
**Solution 1: (DFS, question transform, from side to center)**
```
Runtime: 280 ms
Memory Usage: 16.2 MB
```
```python
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        # Check for an empty graph.
        if not matrix:
            return []

        p_visited = set()
        a_visited = set()
        rows, cols = len(matrix), len(matrix[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def traverse(i, j, visited):
            if (i, j) in visited:
                return
            visited.add((i, j))
            # Traverse neighbors.
            for direction in directions:
                next_i, next_j = i + direction[0], j + direction[1]
                if 0 <= next_i < rows and 0 <= next_j < cols:
                    # Add in your question-specific checks.
                    if matrix[next_i][next_j] >= matrix[i][j]:
                        traverse(next_i, next_j, visited)

        for row in range(rows):
            traverse(row, 0, p_visited)
            traverse(row, cols - 1, a_visited)

        for col in range(cols):
            traverse(0, col, p_visited)
            traverse(rows - 1, col, a_visited)

        return list(p_visited & a_visited)
```

**Solution 2: (BFS, question transform, from side to center)**
```
Runtime: 316 ms
Memory Usage: 14.1 MB
```
```python
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return 
        row = len(matrix)
        col = len(matrix[0])
        pacific = [[False for _ in range(col)] for _ in range(row)]
        atlantic = [[False for _ in range(col)] for _ in range(row)]
        queue_p = []
        queue_a = []
        re = []
        for i in [0,row-1]:
            for j in range(col):
                if i == 0:
                    pacific[i][j]= True
                    queue_p.append((i,j))
                if i == row-1:
                    atlantic[i][j] = True
                    queue_a.append((i,j))
        for i in range(row):
            for j in [0,col-1]:
                if j == 0:
                    pacific[i][j] = True
                    queue_p.append((i,j))
                if j == col-1:
                    atlantic[i][j] = True
                    queue_a.append((i,j))
        while queue_p:
            a, b = queue_p.pop(0)
            for m, n in ((a-1,b),(a+1,b),(a,b-1),(a,b+1)):
                if 0 <= m < row and 0 <= n < col and not pacific[m][n] and matrix[m][n] >= matrix[a][b]:
                    pacific[m][n] = True
                    queue_p.append((m,n))
   
                
        while queue_a:
            a, b = queue_a.pop(0)
            for m, n in ((a-1,b),(a+1,b),(a,b-1),(a,b+1)):
                if 0 <= m < row and 0 <= n < col and not atlantic[m][n] and matrix[m][n] >= matrix[a][b]:
                    atlantic[m][n]= True
                    queue_a.append((m,n))
   

        for i in range(row):
            for j in range(col):
                if pacific[i][j] and atlantic[i][j]:
                    re.append([i,j])
        return re
```

**Solution 3: (DFS)**
```
Runtime: 59 ms
Memory Usage: 11.9 MB
```
```c
void dfs(int** matrix, int matrixRowSize, int *matrixColSizes,int** map,int row,int col,int value,int** ret,int* returnSize){
    if(map[row][col]==value){
        return;
    }
    int direction[4][2]={{1,0},{-1,0},{0,1},{0,-1}};
    if(map[row][col]==0){
        map[row][col]=value;
    }else{
        map[row][col]=value;
        ret[(*returnSize)++]=(int*)calloc(2,sizeof(int));
        ret[(*returnSize)-1][0]=row;
        ret[(*returnSize)-1][1]=col;
    }
    for(int i=0;i<4;i++){
        int tmp_row=row+direction[i][0];
        int tmp_col=col+direction[i][1];
        if(tmp_row>-1&&tmp_row<matrixRowSize&&tmp_col>-1
           &&tmp_col<matrixColSizes[tmp_row]&&matrix[row][col]<=matrix[tmp_row][tmp_col]){
            dfs(matrix,matrixRowSize,matrixColSizes,map,tmp_row,tmp_col,value,ret,returnSize);
        }
    }
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** pacificAtlantic(int** heights, int heightsSize, int* heightsColSize, int* returnSize, int** returnColumnSizes){
    int** map=(int**)malloc(heightsSize*sizeof(int*));
    *returnSize=0;
    if(heightsSize==0){
        return NULL;
    }
    returnColumnSizes[0]=(int*)malloc(heightsSize*heightsColSize[0]*sizeof(int));
    int** ret=(int**)malloc(heightsSize*heightsColSize[0]*sizeof(int*));
    for(int i=0;i<heightsSize;i++){
        map[i]=(int*)calloc(heightsColSize[i],sizeof(int));
    }
    for(int i=0;i<heightsColSize[0];i++){
        dfs(heights,heightsSize,heightsColSize,map,0,i,1,ret,returnSize);
    }
    for(int i=0;i<heightsSize;i++){
        dfs(heights,heightsSize,heightsColSize,map,i,0,1,ret,returnSize);
    }
    for(int i=0;i<heightsColSize[0];i++){
        dfs(heights,heightsSize,heightsColSize,map,heightsSize-1,i,-1,ret,returnSize);
    }
    for(int i=0;i<heightsSize;i++){
        dfs(heights,heightsSize,heightsColSize,map,i,heightsColSize[0]-1,-1,ret,returnSize);
    }
    for(int i=0;i<*returnSize;i++){
        returnColumnSizes[0][i]=2;
    }
    return ret;
}
```

**Solution 4: (DFS)**
```
Runtime: 69 ms
Memory Usage: 17.4 MB
```
```c++
class Solution {
    void dfs(vector<vector<int>>& h, vector<vector<bool>>& vis, int i, int j) {
        
        int m = h.size();
        int n = h[0].size();

        vis[i][j] = true;
        //up
        if (i-1 >= 0 && vis[i-1][j] != true && h[i-1][j] >= h[i][j])
            dfs(h, vis, i-1, j);
        //down
        if (i+1 < m && vis[i+1][j] != true && h[i+1][j] >= h[i][j])
            dfs(h, vis, i+1, j);
        //left
        if (j-1 >= 0 && vis[i][j-1] != true && h[i][j-1] >= h[i][j])
            dfs(h, vis, i, j-1);
        //right
        if (j+1 < n && vis[i][j+1] != true && h[i][j+1] >= h[i][j])
            dfs(h, vis, i, j+1);
    }
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        vector<vector<int>>ans;
        int m = heights.size();
        int n = heights[0].size();
        
        vector<vector<bool>> pacific(m, vector<bool>(n));
        vector<vector<bool>> atlantic(m, vector<bool>(n));
        
        for (int i = 0; i < m; i++) {
            
            dfs(heights, pacific, i, 0);
            dfs(heights, atlantic, i, n-1);

        }
        
        for (int j = 0; j < n; j++) {
            
            dfs(heights, pacific, 0, j);
            dfs(heights, atlantic, m-1, j);
        }

        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                
                if (pacific[i][j] && atlantic[i][j]) // agar uss particular point se dono oceans mai jaa paa rahe hai
                    ans.push_back({i,j});           // toh answer push kardo
            }
        }
        return ans;
    }
};
```

**Solution 5: (BFS)**
```
Runtime: 44 ms
Memory Usage: 20 MB
```
```c++
class Solution {
    int m,n;
    vector<int>dir={0,1,0,-1,0};
    queue<pair<int,int>> pac;
    queue<pair<int,int>> atl;
    
    bool isValid(int x, int y){
        return x>=0 && x<m && y>=0 && y<n;
    }
    
    // andar se bahar ki taraf jaa rahe hai
    void bfs(queue<pair<int,int>> &q, vector<vector<int>> &vis, vector<vector<int>>& matrix)
    {
        while(!q.empty())
        {
            int x=q.front().first;
            int y=q.front().second;
            vis[x][y]=1;
            q.pop();
            for(int k=0;k<4;k++)
            {
                int xx = x+dir[k];
                int yy = y+dir[k+1];
                if(isValid(xx,yy) && matrix[x][y] <= matrix[xx][yy] && vis[xx][yy]==0) // greater equal 
                {
                    q.push({xx,yy});
                }
            }
        }
    }
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        vector<vector<int>> ans;
        m=heights.size();
        n=heights[0].size();
 
        vector<vector<int>> visp(m, vector<int>(n,0));
        vector<vector<int>> visq(m, vector<int>(n,0));
        // push boundaries of pacific ocean
        for(int i=m-1;i>=0;i--)
            pac.push({i,0});
        for(int i=n-1;i>=0;i--)
            pac.push({0,i});
        
        // push boundaries of atlantic ocean
        for(int i=m-1;i>=0;i--)
            atl.push({i,n-1});
        for(int i=n-1;i>=0;i--)
            atl.push({m-1,i});
        
        bfs(pac, visp, heights);
        bfs(atl, visq, heights);
        
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                
                if(visp[i][j]==1 && visq[i][j]==1)
                    ans.push_back({i,j});
            }
        }
        return ans;
    }
};
```
