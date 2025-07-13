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

**Solution 4: (DFS, O((m n)! x (m n)))**
```
Runtime: 131 ms
Memory: 12.65 MB
```
```c++
class Solution {
    // Direction map for zero's possible moves in a flattened 1D array (2x3
    // board)
    vector<vector<int>> directions = {{1, 3}, {0, 2, 4}, {1, 5},
                                      {0, 4}, {3, 5, 1}, {4, 2}};
    void dfs(string state, unordered_map<string, int>& visited, int zeroPos,
             int moves) {
        // Skip if this state has been visited with fewer or equal moves
        if (visited.count(state) && visited[state] <= moves) {
            return;
        }
        visited[state] = moves;

        // Try moving zero to each possible adjacent position
        for (int nextPos : directions[zeroPos]) {
            swap(state[zeroPos], state[nextPos]);  // Swap to generate new state
            dfs(state, visited, nextPos,
                moves + 1);  // Recursive DFS with updated state and move count
            swap(state[zeroPos],
                 state[nextPos]);  // Swap back to restore original state
        }
    }
public:
    int slidingPuzzle(vector<vector<int>>& board) {
        // Convert the 2D board into a string representation to use as state
        string startState;
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 3; j++) {
                startState += to_string(board[i][j]);
            }
        }

        // Map to store the minimum moves for each visited state
        unordered_map<string, int> visited;

        // Start DFS traversal from initial board state
        dfs(startState, visited, startState.find('0'), 0);

        // Return the minimum moves required to reach the target state, or -1 if
        // unreachable
        return visited.count("123450") ? visited["123450"] : -1;
    }
};
```

**Solution 5: (BFS, O((m n)! x (m n)))**
```
Runtime: 6 ms
Memory: 11.04 MB
````
```c++
class Solution {
public:
    int slidingPuzzle(vector<vector<int>>& board) {
        // Direction map for zero's possible moves in a 1D representation of the
        // 2x3 board
        vector<vector<int>> directions = {{1, 3}, {0, 2, 4}, {1, 5},
                                          {0, 4}, {1, 3, 5}, {2, 4}};

        string target = "123450";
        string startState;

        // Convert the 2D board into a string representation
        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[0].size(); j++) {
                startState += to_string(board[i][j]);
            }
        }

        unordered_set<string> visited;  // To store visited states
        queue<string> queue;
        queue.push(startState);
        visited.insert(startState);

        int moves = 0;

        // BFS to find the minimum number of moves
        while (!queue.empty()) {
            int size = queue.size();
            while (size-- > 0) {
                string currentState = queue.front();
                queue.pop();

                // Check if we reached the target solved state
                if (currentState == target) {
                    return moves;
                }

                int zeroPos = currentState.find('0');
                for (int newPos : directions[zeroPos]) {
                    string nextState = currentState;
                    swap(nextState[zeroPos], nextState[newPos]);

                    // Skip if this state has been visited
                    if (visited.count(nextState)) continue;

                    // Mark the new state as visited and add it to the queue
                    visited.insert(nextState);
                    queue.push(nextState);
                }
            }
            moves++;
        }
        return -1;
    }
};
```

**Solution 6: (BFS, O((m n)! x (m n)), level order, try every combination)**
```
Runtime: 7 ms
Memory: 11.97 MB
```
```c++
class Solution {
public:
    int slidingPuzzle(vector<vector<int>>& board) {
        int sz, i, j, ans = 0;
        string cur = "#####", ncur;
        for (auto r: board) {
            cur += '#';
            for (auto c: r) {
                cur += c+'0';
            }
            cur += '#';
        }
        cur += "#####";
        queue<string> q;
        unordered_set<string> visited;
        q.push(cur);
        visited.insert(cur);
        while (q.size()) {
            sz = q.size();
            for (i = 0; i < sz; i ++) {
                cur = q.front();
                q.pop();
                if (cur == "######123##450######") {
                    return ans;
                }
                j = cur.find('0');
                for (auto nj: {j-1, j+1, j-5, j+5}) {
                    if (cur[nj] != '#') {
                        ncur = cur;
                        swap(ncur[nj], ncur[j]);
                        if (!visited.count(ncur)) {
                            q.push(ncur);
                            visited.insert(ncur);
                        }
                    }
                }
            }
            ans += 1;
        }
        return -1;
    }
};

```

**Solution 7: (BFS, try all soltion)**
```
Runtime: 7 ms, Beats 59.04%
Memory: 11.75 MB, Beats 57.51%
```
```c++
class Solution {
public:
    int slidingPuzzle(vector<vector<int>>& board) {
        int m = board.size(), n = board[0].size(), i, j, i2, d;
        string s, t = "123450";
        queue<tuple<string,int,int>> q;
        unordered_set<string> visited;
        vector<vector<int>> g = {
            {1,3},
            {0,2,4},
            {1,5},
            {0,4},
            {1,3,5},
            {2,4}
        };
        for (i = 0; i < m; i ++) {
            for (j = 0; j < n; j ++) {
                if (board[i][j] == 0) {
                    i2 = i*n + j;
                }
                s += board[i][j] + '0';
            }
        }
        q.push({s, i2, 0});
        visited.insert(s);
        while (q.size()) {
            auto [cs, ci, k] = q.front();
            q.pop();
            if (cs == t) {
                return k;
            }
            for (d = 0; d < 4; d ++) {
                for (auto ni: g[ci]) {
                    swap(cs[ci], cs[ni]);
                    if (!visited.count(cs)) {
                        q.push({cs, ni, k+1});
                        visited.insert(cs);
                    }
                    swap(cs[ci], cs[ni]);
                }
            }
        }
        return -1;
    }
};
```
