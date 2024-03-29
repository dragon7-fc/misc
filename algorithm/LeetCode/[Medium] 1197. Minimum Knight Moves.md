1197. Minimum Knight Moves

In an infinite chess board with coordinates from `-infinity` to `+infinity`, you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

![1197_knight](img/1197_knight.png)

Return the minimum number of steps needed to move the knight to the square [x, y].  It is guaranteed the answer exists.

 
**Example 1:**
```
Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]
```
**Example 2:**
```
Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
``` 

**Constraints:**

* |x| + |y| <= 300

# Submissions
---
**Solution 1: (BFS, Time: O((max(|x|, |y|))^2), Space: O((max(|x|, |y|))^2))**
```python
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x = abs(x)
        y = abs(y)
        MAXN = 310
        steps = 0
        dx = [-2,-1,1,2,2,1,-1,-2]
        dy = [1,2,2,1,-1,-2,-2,-1]
        q = []
        visited = [[False for _ in range(MAXN)] for _ in range(MAXN)]
        q.insert(0, [0, 0])        
        visited[0][0] = True
        
        while len(q) > 0:
            sz = len(q)
            for i in range(sz):
                curr = q.pop();
                if curr[0] == x and curr[1] == y:
                    return steps
                
                for j in range(8):
                    x1 = curr[0] + dx[j];
                    y1 = curr[1] + dy[j];
                    if x1 < 0 or y1 < 0 or x1 >= MAXN or y1 >= MAXN:
                        continue
                    
                    if not visited[x1][y1]:
                        visited[x1][y1] = True
                        q.insert(0, [x1, y1])
            steps += 1
        
        return -1
```

**Solution 2: (Bidirectional BFS, Time: O((max(|x|, |y|))^2), Space: O((max(|x|, |y|))^2))**
```
Runtime: 6518 ms
Memory: 37 MB
```
```python
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # the offsets in the eight directions
        offsets = [(1, 2), (2, 1), (2, -1), (1, -2),
                   (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

        # data structures needed to move from the origin point
        origin_queue = deque([(0, 0, 0)])
        origin_distance = {(0, 0): 0}

        # data structures needed to move from the target point
        target_queue = deque([(x, y, 0)])
        target_distance = {(x, y): 0}

        while True:
            # check if we reach the circle of target
            origin_x, origin_y, origin_steps = origin_queue.popleft()
            if (origin_x, origin_y) in target_distance:
                return origin_steps + target_distance[(origin_x, origin_y)]

            # check if we reach the circle of origin
            target_x, target_y, target_steps = target_queue.popleft()
            if (target_x, target_y) in origin_distance:
                return target_steps + origin_distance[(target_x, target_y)]

            for offset_x, offset_y in offsets:
                # expand the circle of origin
                next_origin_x, next_origin_y = origin_x + offset_x, origin_y + offset_y
                if (next_origin_x, next_origin_y) not in origin_distance:
                    origin_queue.append((next_origin_x, next_origin_y, origin_steps + 1))
                    origin_distance[(next_origin_x, next_origin_y)] = origin_steps + 1

                # expand the circle of target
                next_target_x, next_target_y = target_x + offset_x, target_y + offset_y
                if (next_target_x, next_target_y) not in target_distance:
                    target_queue.append((next_target_x, next_target_y, target_steps + 1))
                    target_distance[(next_target_x, next_target_y)] = target_steps + 1
```

**Solution 3: (DFS (Depth-First Search) with Memoization, Time: O(|xy|), Space: O(|xy|))**
```
Runtime: 115 ms
Memory: 15.5 MB
```
```python
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        @lru_cache(maxsize=None)
        def dfs(x, y):
            if x + y == 0:
                # base case: (0, 0)
                return 0
            elif x + y == 2:
                # base case: (1, 1), (0, 2), (2, 0)
                return 2
            else:
                return min(dfs(abs(x - 1), abs(y - 2)), dfs(abs(x - 2), abs(y - 1))) + 1

        return dfs(abs(x), abs(y))
```

**Solution 4: (BFS, shift location)**
```
Runtime: 442 ms
Memory: 54.6 MB
```
```c++
int dx[8] = {1, 1, 2, 2, -1, -1, -2, -2};
int dy[8] = {2, -2, 1, -1, 2, -2, 1, -1};
class Solution {
public:
    int minKnightMoves(int x, int y) {
        queue<pair<int, int>> q;
        q.push({500, 500});
        vector<vector<bool>> visited(1000, vector<bool>(1000));
        visited[500][500] = true;
        int ans = 0, sz, nx, ny;
        while (q.size()) {
            sz = q.size();
            for (int i = 0; i < sz; i ++) {
                auto [cx, cy] = q.front();
                q.pop();
                if (cx == x+500 && cy == y+500) {
                    return ans;
                }
                for (int d = 0; d < 8; d ++) {
                    nx = cx + dx[d];
                    ny = cy + dy[d];
                    if (1 <= nx && nx < 1000 && 1 <= ny && ny < 1000 && !visited[nx][ny]) {
                        visited[nx][ny] = true;
                        q.push({nx, ny});
                    }
                }
            }
            ans += 1;
        }
        return -1;
    }
};
```

**Solution 5: (BFS, bidirectional bfs)**
```
Runtime: 992 ms
Memory: 156.9 MB
```
```c++
int dx[8] = {1, 1, 2, 2, -1, -1, -2, -2};
int dy[8] = {2, -2, 1, -1, 2, -2, 1, -1};
class Solution {
public:
    int minKnightMoves(int x, int y) {
        queue<tuple<int,int,int>> sq, tq;
        sq.push({0, 0, 0});
        tq.push({x, y, 0});
        unordered_map<int, unordered_map<int,int>> sdist, tdist;
        sdist[0][0] = 0;
        tdist[x][y] = 0;
        int ans = 0, sz, nsx, nsy, ntx, nty;
        while (1) {
            auto [sx, sy, sstep] = sq.front();
            sq.pop();
            if (tdist.count(sx) && tdist[sx].count(sy)) {
                return sstep + tdist[sx][sy];
            }
            auto [tx, ty, tstep] = tq.front();
            tq.pop();
            if (sdist.count(tx) && sdist[tx].count(ty)) {
                return tstep + sdist[tx][ty];
            }
            for (int i = 0; i < 8; i ++) {
                nsx = sx + dx[i];
                nsy = sy + dy[i];
                if (!sdist.count(nsx) || !sdist[nsx].count(nsy)) {
                    sq.push({nsx, nsy, sstep+1});
                    sdist[nsx][nsy] = sstep+1;
                }
                ntx = tx + dx[i];
                nty = ty + dy[i];
                if (!tdist.count(ntx) || !tdist[ntx].count(nty)) {
                    tq.push({ntx, nty, tstep+1});
                    tdist[ntx][nty] = tstep+1;
                }
            }
        }
        return -1;
    }
};
Console

```
