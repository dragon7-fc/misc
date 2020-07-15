773. Sliding Puzzle

On a 2x3 `board`, there are 5 tiles represented by the integers 1 through 5, and an empty square represented by 0.

A move consists of choosing `0` and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the `board` is `[[1,2,3],[4,5,0]]`.

Given a puzzle board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

**Examples:**
```
Input: board = [[1,2,3],[4,0,5]]
Output: 1
Explanation: Swap the 0 and the 5 in one move.
```
```
Input: board = [[1,2,3],[5,4,0]]
Output: -1
Explanation: No number of moves will make the board solved.
```
```
Input: board = [[4,1,2],[5,0,3]]
Output: 5
Explanation: 5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]
```
```
Input: board = [[3,2,4],[1,5,0]]
Output: 14
```

**Note:**

* `board` will be a 2 x 3 array as described above.
* `board[i][j]` will be a permutation of `[0, 1, 2, 3, 4, 5]`.

# Submissions
---
**Solution 1: (BFS)**
```
Runtime: 16 ms
Memory Usage: 8.5 MB
```
```c++
class Solution {
public:
    int slidingPuzzle(vector<vector<int>>& board) {
        int m = board.size(), n = board[0].size();
        
        string state, goal = "123450";
        for(int i = 0; i < m ; i++)
            for(int j = 0 ; j < n ; j++)
                state += (board[i][j] + '0');
        
        if(goal == state )
            return 0;
        
        queue<string> q{{state}};
        unordered_set<string> visited{state};
        
        int step = 0;
        vector<pair<int,int>> moves = { {-1,0}, {1,0}, {0,-1}, {0,1}};
        
        while(!q.empty()){
            
            int size = q.size();
            step++;
            for(int a = 0 ; a < size ; a++)
            {
                auto curr = q.front(); 
                q.pop();
                
                int i = curr.find('0');
                int r = i/n , c = i % n;
                
                for(auto mo : moves)
                {
                    int nr = r + mo.first, nc = c + mo.second;
                    if(nr < 0 || (nr >= m) || nc < 0 || nc >=n )
                        continue;
                    
                    string nextStr(curr);
                    int ni = nr*n + nc;
                    swap(nextStr[i], nextStr[ni]);
                    
                    if(visited.count(nextStr))
                        continue;
                    
                    if(goal == nextStr)
                        return step;
                    
                    q.emplace(nextStr);
                    visited.emplace(nextStr);
                }
            }
        }
    
        return -1;
    }
};
```

**Solution 2: (BFS)**
```
Runtime: 76 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        R, C = len(board), len(board[0])
        goal = '123450'
        state = ''.join([''.join(map(str, _)) for _ in board])
        if goal == state: 
            return 0
        q = collections.deque([state])
        visited = set([state])
        step = 0
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            sz = len(q)
            step += 1
            for a in range(sz):
                curr = q.popleft()
                i = curr.index('0')
                r, c = i//C, i%C
                for dr, dc in direction:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < R and 0 <= nc < C:
                        nextStr = list(curr)
                        ni = nr*C + nc
                        nextStr[i], nextStr[ni] = nextStr[ni], nextStr[i]
                        nextStr = ''.join(nextStr)
                        if nextStr in visited:
                            continue
                        if goal == nextStr:
                            return step
                        q += [nextStr]
                        visited.add(nextStr)
    
        return -1
```