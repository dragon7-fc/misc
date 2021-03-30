286. Walls and Gates

You are given an `m x n` grid rooms initialized with these three possible values.

* `-1` A wall or an obstacle.
* `0` A gate.
* `INF` Infinity means an empty room. We use the value `2^31 - 1 = 2147483647` to represent `INF` as you may assume that the distance to a gate is less than `2147483647`.

Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with `INF`.

 

**Example 1:**

```
Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
```

**Example 2:**
```
Input: rooms = [[-1]]
Output: [[-1]]
```

**Example 3:**
```
Input: rooms = [[2147483647]]
Output: [[2147483647]]
```

**Example 4:**
```
Input: rooms = [[0]]
Output: [[0]]
```

**Constraints:**

* `m == rooms.length`
* `n == rooms[i].length`
* `1 <= m, n <= 250`
* `rooms[i][j]` is `-1`, `0`, or `2^31 - 1`.

# Submissions
---
**Solution 1: (BFS, think backward - fromt target to source)**
```
Runtime: 292 ms
Memory Usage: 20.5 MB
```
```python
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        def bfs():
            direction = [[-1,0],[1,0],[0,1],[0,-1]]
            depth = 0
            while queue:
                cur_length = len(queue)
                depth += 1
                while cur_length > 0:
                    node = queue.popleft()
                    for dir in direction:
                        new_row = node[0] + dir[0]
                        new_col = node[1] + dir[1]
                        if new_row >= 0 and new_col >= 0 and new_row < m and new_col < n:
                            if tuple([new_row, new_col]) not in seen and (rooms[new_row][new_col] == 2147483647):
                                queue.append([new_row,new_col])
                                seen.add(tuple([new_row,new_col]))
                                rooms[new_row][new_col] = depth 
                    cur_length -= 1
        
        m, n = len(rooms), len(rooms[0])
        queue = deque()
        seen = set()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append([i,j])
                    seen.add(tuple([i,j]))
        
        bfs()
        
        return rooms
```

**Solution 2: (BFS, think backward - fromt target to source)**
```
Runtime: 28 ms
Memory Usage: 14.4 MB
```
```c++
class Solution {
public:
    vector<int> roff = {-1, 0, 1, 0};
    vector<int> coff = {0, 1, 0, -1};
    void wallsAndGates(vector<vector<int>>& rooms) {
        int m = rooms.size();
        int n = rooms[0].size();
        int maxrooms = m * n;
        
        queue<pair<int, int>> q;
        for (int i=0; i<m; i++){
            for (int j=0; j<n; j++){
                if (rooms[i][j] == 0) {
                    q.push( {i, j} ); 
                }
            }
        }
        
        while (!q.empty()) {
            auto node = q.front(); q.pop();
            
            for (int i=0; i<4; i++) {
                int nrow = node.first + roff[i];
                int ncol = node.second + coff[i];
                if (0 <= nrow && nrow < rooms.size() && 0<=ncol && ncol < rooms[0].size() && rooms[nrow][ncol] == 2147483647) {
                    rooms[nrow][ncol] = rooms[node.first][node.second] + 1;
                    q.push( {nrow, ncol});
                }
            }
        }
    }
};
```