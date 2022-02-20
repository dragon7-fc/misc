529. Minesweeper

Let's play the minesweeper game (Wikipedia, online game)!

You are given a 2D char matrix representing the game board. '**M**' represents an **unrevealed** mine, '**E**' represents an **unrevealed** empty square, '**B**' represents a **revealed** blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines, **digit** ('1' to '8') represents how many mines are adjacent to this **revealed** square, and finally '**X**' represents a revealed mine.

Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'), return the board after revealing this position according to the following rules:

* If a mine ('M') is revealed, then the game is over - change it to '**X**'.
* If an empty square ('E') with **no adjacent mines** is revealed, then change it to revealed blank ('B') and all of its adjacent **unrevealed** squares should be revealed recursively.
* If an empty square ('E') with **at least one adjacent mine** is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed.
 

**Example 1:**
```
Input: 

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

Output: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Explanation:
```
![529_minesweeper_example_1.png](img/529_minesweeper_example_1.png)

**Example 2:**
```
Input: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Click : [1,2]

Output: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'X', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Explanation:
```
![529_minesweeper_example_2.png](img/529_minesweeper_example_2.png) 

**Note:**

* The range of the input matrix's height and width is [1,50].
* The click position will only be an unrevealed square ('M' or 'E'), which also means the input board contains at least one clickable square.
* The input board won't be a stage when game is over (some mines have been revealed).
* For simplicity, not mentioned rules should be ignored in this problem. For example, you **don't** need to reveal all the unrevealed mines when the game is over, consider any cases that you will win the game or flag any squares.

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 196 ms
Memory Usage: 18.4 MB
```
```python
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        R, C = len(board), len(board[0])
        visited = set()

        def neighbours(r, c):
            directions = ((r-1, c),(r+1, c),(r, c+1),(r, c-1),
                          (r+1, c+1),(r-1, c-1),(r-1, c+1),(r+1, c-1)
                         )
            for nr, nc in directions:
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        def traverse(r, c):
            if (r, c) in visited:
                return 
            if board[r][c] == 'M':
                board[r][c] = 'X'
            else:
                count = 0
                for nr, nc in neighbours(r, c):
                    if board[nr][nc] in 'MX':
                        count += 1
                board[r][c] = 'B' if count == 0 else str(count)
            visited.add((r, c))
            if board[r][c] == 'B':
                for nr,nc in neighbours(r, c):
                    traverse(nr, nc)

        traverse(*click)
        return board
```

**Solution 2:(BFS)**
```
Runtime: 192 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        R, C = len(board), len(board[0])
        visited = set()

        def neighbours(r, c):
            directions = ((r-1, c),(r+1, c),(r, c+1),(r, c-1),
                          (r+1, c+1),(r-1, c-1),(r-1, c+1),(r+1, c-1)
                         )
            for nr, nc in directions:
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        queue = collections.deque([click])
        while queue:
            (r, c) = queue.popleft()
            if (r, c) in visited:
                continue
            if board[r][c] == 'M':
                board[r][c] = 'X'
            else:
                count = 0
                for nr, nc in neighbours(r, c):
                    if board[nr][nc] in 'MX':
                        count += 1
                board[r][c] = 'B' if count == 0 else str(count)
            visited.add((r, c))
            if board[r][c] == 'B':
                for nr, nc in neighbours(r, c):
                    queue.append([nr, nc])

        return board
```

**Solution 3: (DFS)**
```
Runtime: 19 ms
Memory Usage: 11.9 MB
```
```c++
class Solution {
public:
    bool inboard(const vector<vector<char>>& board, int x, int y){
        return ( x>=0 && x<board.size() && y>=0 && y<board[0].size() );
    }
    
    void dfs(vector<vector<char>>& board, int x, int y)
    {
        // boundary condition..
        if(!inboard(board,x,y)) return;
        if(board[x][y] == 'B') return;
        
        // if it is 'E' then go forward recursively 
        // check 8 adjacent squares & count all mines adjacent to board[x][y], and place count to the current 
        // position of board[x][y]
        int count = 0;
        if(inboard(board,x-1,y-1) && board[x-1][y-1] == 'M') count++;
        if(inboard(board,x-1,y  ) && board[x-1][y  ] == 'M') count++;
        if(inboard(board,x-1,y+1) && board[x-1][y+1] == 'M') count++;
        if(inboard(board,x  ,y-1) && board[x  ][y-1] == 'M') count++;
        if(inboard(board,x  ,y+1) && board[x  ][y+1] == 'M') count++;
        if(inboard(board,x+1,y-1) && board[x+1][y-1] == 'M') count++;
        if(inboard(board,x+1,y  ) && board[x+1][y  ] == 'M') count++;
        if(inboard(board,x+1,y+1) && board[x+1][y+1] == 'M') count++;
        
        // set board with different values either 'count' or 'B' 
        if(count>0)
            board[x][y] = '0'+count;
        else
        {
            board[x][y] = 'B';
            // search recursively in 8 directions
            dfs(board,x-1,y-1);
            dfs(board,x-1,y  );
            dfs(board,x-1,y+1);
            dfs(board,x  ,y-1);
            dfs(board,x  ,y+1);
            dfs(board,x+1,y-1);
            dfs(board,x+1,y  );
            dfs(board,x+1,y+1);
        }
    }
    vector<vector<char>> updateBoard(vector<vector<char>>& board, vector<int>& click) {
        // m X n character matrix
        // first click start from ----> (r, c)
        int r = click[0];
        int c = click[1];
        if(board[r][c] == 'M'){
            board[r][c]= 'X';
            return board;
        }
        
        dfs(board, r, c);
        return board;
    }
};
```

**Solution 4: (BFS)**
```
Runtime: 28 ms
Memory Usage: 13.6 MB
```
```c++
class Solution {
public:
    bool inboard(const vector<vector<char>>& board, int x, int y){
        return ( x>=0 && x<board.size() && y>=0 && y<board[0].size() );
    }
    
    void bfs(vector<vector<char>>& board, int sr, int sc)
    {
        // 8 directions
       //   Trick to write 8 - Directions fastly:                  ___ ___ ___
    //   -1 ----> Previous row cells => {-1,-1},{-1,0},{-1,1}     |_*_|_*_|_*_| 
    //    0 ----> Current row cells  => {0,-1},{0,1}              |_*_|_X_|_*_|
    //    1 ----> Next row cells     => {1,-1},{1,0},{1,1}        |_*_|_*_|_*_|
        vector<vector<int>>dirs = {{1,-1},{1,0},{1,1},{0,-1},{0,1},{-1,-1},{-1,0},{-1,1}};
        
        queue<pair<int, int>>q;
        q.push({sr, sc});
            
        while(!q.empty())
        {
            auto cur = q.front(); q.pop();   
            int x = cur.first;
            int y = cur.second;
            
            // Search 8 directions for mines
            // Rule 2 : if there is atleast one mine present then place their count. (i.e board[x][y] = count)
            // Rule 3 : if there is no mine in all 8 directions then mark current as Blank 'B', and then push 
            // their 8 adjacent coordinates into the queue.
            int count = 0;
            for(auto d : dirs)
            {
                int nx = x + d[0];
                int ny = y + d[1];        
                if(inboard(board, nx, ny) and board[nx][ny] == 'M')
                    count++;
            }
            
            // Rule 2 : implementation - atleast one mine present
            if(count > 0){
                board[x][y] = count + '0';
            }
            else // Rule 3 : implementation - No mine present
            { 
                board[x][y] = 'B'; // mark current as blank
                for(auto d : dirs){
                    
                    int nx = x + d[0];
                    int ny = y + d[1];
                    // push only empty squares, traversal only possible through empty squares
                    if(inboard(board, nx, ny) and board[nx][ny] == 'E') {
                        q.push({nx, ny});
                        board[nx][ny] = 'B';
                    }
                        
                }
            }
        }
    }
    
    vector<vector<char>> updateBoard(vector<vector<char>>& board, vector<int>& click) {
        // m X n character matrix
        // first click start from ----> (r, c)
        int r = click[0];
        int c = click[1];
        // Rule 1: If a mine 'M' is revealed, then the game is over. You should change it to 'X'.
        if(board[r][c] == 'M'){
            board[r][c]= 'X';
            return board;
        }
        
        bfs(board, r, c);
        return board;
    }
};
```
