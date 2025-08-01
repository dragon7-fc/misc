934. Shortest Bridge

n a given 2D binary array `A`, there are two islands.  (An island is a 4-directionally connected group of 1s not connected to any other 1s.)

Now, we may change `0`s to `1`s so as to connect the two islands together to form 1 island.

Return the smallest number of `0`s that must be flipped.  (It is guaranteed that the answer is at least `1`.)

 

**Example 1:**
```
Input: [[0,1],[1,0]]
Output: 1
```

**Example 2:**
```
Input: [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
```

**Example 3:**
```
Input: [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
```

**Note:**

* `1 <= A.length = A[0].length <= 100`
* `A[i][j] == 0` or `A[i][j] == 1`

# Solution
---
## Approach 1: Find and Grow
**Intuition**

Conceptually, our method is very straightforward: find both islands, then for one of the islands, keep "growing" it by 1 until we touch the second island.

We can use a depth-first search to find the islands, and a breadth-first search to "grow" one of them. This leads to a verbose but correct solution.

**Algorithm**

To find both islands, look for a square with a `1` we haven't visited, and dfs to get the component of that region. Do this twice. After, we have two components `source` and `target`.

To find the shortest bridge, do a BFS from the nodes `source`. When we reach any node in `target`, we will have found the shortest distance.

Please see the code for more implementation details.

```python
class Solution(object):
    def shortestBridge(self, A):
        R, C = len(A), len(A[0])

        def neighbors(r, c):
            for nr, nc in ((r-1,c),(r,c-1),(r+1,c),(r,c+1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        def get_components():
            done = set()
            components = []
            for r, row in enumerate(A):
                for c, val in enumerate(row):
                    if val and (r, c) not in done:
                        # Start dfs
                        stack = [(r, c)]
                        seen = {(r, c)}
                        while stack:
                            node = stack.pop()
                            for nei in neighbors(*node):
                                if A[nei[0]][nei[1]] and nei not in seen:
                                    stack.append(nei)
                                    seen.add(nei)
                        done |= seen
                        components.append(seen)
            return components

        source, target = get_components()
        print source, target
        queue = collections.deque([(node, 0) for node in source])
        done = set(source)
        while queue:
            node, d = queue.popleft()
            if node in target: return d-1
            for nei in neighbors(*node):
                if nei not in done:
                    queue.append((nei, d+1))
                    done.add(nei)
```

**Complexity Analysis**

* Time Complexity: $O(\mathcal{A})$, where $\mathcal{A}$ is the content of `A`.

* Space Complexity: $O(\mathcal{A})$.

# Submissions
---
**Solution: (DFS, BFS)**
```
Runtime: 524 ms
Memory Usage: 13.7 MB
```
```python
class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        R, C = len(A), len(A[0])

        def neighbors(r, c):
            for nr, nc in ((r-1,c),(r,c-1),(r+1,c),(r,c+1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        def get_components():
            done = set()
            components = []
            for r, row in enumerate(A):
                for c, val in enumerate(row):
                    if val and (r, c) not in done:
                        # Start dfs
                        stack = [(r, c)]
                        seen = {(r, c)}
                        while stack:
                            node = stack.pop()
                            for nei in neighbors(*node):
                                if A[nei[0]][nei[1]] and nei not in seen:
                                    stack.append(nei)
                                    seen.add(nei)
                        done |= seen
                        components.append(seen)
            return components

        source, target = get_components()
        queue = collections.deque([(node, 0) for node in source])
        done = set(source)
        while queue:
            node, d = queue.popleft()
            if node in target: return d-1
            for nei in neighbors(*node):
                if nei not in done:
                    queue.append((nei, d+1))
                    done.add(nei)
```

**Solution 2: (BFS)**
```
Runtime: 69 ms
Memory Usage: 10.5 MB
```
```c
#define MAX_LEN 10000
#define LAND1 2
#define LAND2 1
#define TURNED 3
#define EMPTY 0

typedef struct {
    int x; 
    int y;
    int step;
} Point;

Point* bfs(int **A, int ASize, int AColSize, Point p, int *size) 
{
    Point *res = (Point*) malloc(MAX_LEN * sizeof(Point));
    *size = 1;
    res[0] = p;
    int head = 0;
    A[p.x][p.y] = LAND1;
    
    int directs[][2] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
    
    while (head < *size) {
        Point cur = res[head++];
        for (int i = 0; i < 4; i++) {
            int dx = directs[i][0];
            int dy = directs[i][1];
            Point new = {cur.x + dx, cur.y + dy, 0};
            if (0 <= new.x && new.x < ASize && 0 <= new.y && new.y < AColSize && A[new.x][new.y] == 1) {
                A[new.x][new.y] = LAND1;
                res[*size] = new;
                (*size)++;
            }
        }
    }
    return res;
}

int shortestBridge(int** grid, int gridSize, int* gridColSize){
    if (grid == NULL || gridSize <= 0 || *gridColSize <= 0) return 0;
    Point *lands;
    int *size = (int*) malloc(sizeof(int));
    *size = -1;
    int flag = 0;
    for (int i = 0; i < gridSize; i++) {
        for (int j = 0; j < *gridColSize; j++) {
            if (grid[i][j] == EMPTY) continue;
            Point tmp = {i, j, 0};
            lands = bfs(grid, gridSize, *gridColSize, tmp, size);
            flag = 1;
            break;
        }
        if (flag) break;
    }

    int head = 0;
    int directs[][2] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
    while (head < *size) {
        Point cur = lands[head++];
        for (int i = 0; i < 4; i++) {
            int dx = directs[i][0];
            int dy = directs[i][1];
            Point new = {cur.x + dx, cur.y + dy, cur.step + 1};
            if (0 <= new.x && new.x < gridSize && 0 <= new.y && new.y < *gridColSize && grid[new.x][new.y] != TURNED) {
                if (grid[new.x][new.y] == LAND2) {
                    free(size);
                    free(lands);
                    lands = NULL;
                    return cur.step;
                }
                if (grid[new.x][new.y] == EMPTY) {
                    lands[*size] = new;
                    (*size)++;
                    grid[new.x][new.y] = TURNED;
                }
            }
        }
    }
    
    free(size);
    free(lands);
    lands = NULL;
    return -1;
}
```

**Solution 3: (DFS, BFS)**
```
Runtime: 43 ms
Memory: 20.2 MB
```
```c++
class Solution {
    void dfs(int r, int c, queue<tuple<int,int>> &q, vector<vector<int>> &grid) {
        q.push({r, c});
        grid[r][c] = -1;
        if (r+1 < grid.size() && grid[r+1][c] == 1) {
            dfs(r+1, c, q, grid);
        }
        if (r-1 >= 0 && grid[r-1][c] == 1) {
            dfs(r-1, c, q, grid);
        }
        if (c+1 < grid.size() && grid[r][c+1] == 1) {
            dfs(r, c+1, q, grid);
        }
        if (c-1 >= 0 && grid[r][c-1] == 1) {
            dfs(r, c-1, q, grid);
        }
    }
public:
    int shortestBridge(vector<vector<int>>& grid) {
        queue<tuple<int,int>> q;
        int sz, cr, cc, ans = 0;
        bool flag = false;
        for (int r = 0; r < grid.size(); r ++) {
            for (int c = 0; c < grid.size(); c++) {
                if (grid[r][c] == 1) {
                    dfs(r, c, q, grid);
                    flag = true;
                    break;
                }
            }
            if (flag) {
                break;
            }
        }
        while (!q.empty()) {
            sz = q.size();
            while (sz) {
                auto [cr, cc] = q.front();
                q.pop();
                if (cr+1 < grid.size()) {
                    if (grid[cr+1][cc] == 1) {
                        return ans;
                    } else if (grid[cr+1][cc] == 0) {
                        q.push({cr+1, cc});
                        grid[cr+1][cc] = -1;
                    }
                    
                }
                if (cr-1 >= 0) {
                    if (grid[cr-1][cc] == 1) {
                        return ans;
                    } else if (grid[cr-1][cc] == 0) {
                        q.push({cr-1, cc});
                        grid[cr-1][cc] = -1;
                    }
                }
                if (cc+1 < grid.size()) {
                    if (grid[cr][cc+1] == 1) {
                        return ans;
                    } else if (grid[cr][cc+1] == 0) {
                        q.push({cr, cc+1});
                        grid[cr][cc+1] = -1;
                    }
                }
                if (cc-1 >= 0) {
                    if (grid[cr][cc-1] == 1) {
                        return ans;
                    } else if (grid[cr][cc-1] == 0) {
                        q.push({cr, cc-1});
                        grid[cr][cc-1] = -1;
                    }
                }
                sz -= 1;
            }
            ans += 1;
        }
        return -1;
    }
};
```

**Solution 3: (DFS, BFS, locate one then try to find the other)**
```
Runtime: 5 ms, Beats 74.30%
Memory: 24.75 MB, Beats 49.10%
```
```c++
class Solution {
    int dd[5] = {0, 1, 0, -1, 0};
public:
    int shortestBridge(vector<vector<int>>& grid) {
        int n = grid.size(), i, j, d, nr, nc;
        bool flag = false;
        vector<vector<int>> visited(n, vector<int>(n));
        queue<array<int,2>> gq;
        queue<array<int,3>> q;
        for (i = 0; i < n; i ++) {
            for (j = 0; j < n; j ++) {
                if (grid[i][j] == 1 && visited[i][j] == 0) {
                    gq.push({i, j});
                    visited[i][j] = 1;
                    while (gq.size()) {
                        auto [r, c] = gq.front();
                        gq.pop();
                        q.push({r, c, 0});
                        for (d = 0; d < 4; d ++) {
                            nr = r + dd[d];
                            nc = c + dd[d+1];
                            if (0 <= nr && nr < n && 0 <= nc && nc < n && grid[nr][nc] == 1 && visited[nr][nc] == 0) {
                                visited[nr][nc] = 1;
                                gq.push({nr, nc});
                            }
                        }
                    }
                    flag = true;
                    break;
                }
            }
            if (flag) {
                break;
            }
        }
        while (q.size()) {
            auto [r, c, cd] = q.front();
            q.pop();
            for (d = 0; d < 4; d ++) {
                nr = r + dd[d];
                nc = c + dd[d+1];
                if (0 <= nr && nr < n && 0 <= nc && nc < n) {
                    if (visited[nr][nc] == 0) {
                        if (grid[nr][nc] == 1) {
                            return cd;
                        } else {
                            visited[nr][nc] = 1;
                            q.push({nr, nc, cd+1});
                        }
                    }
                }
            }
        }
        return -1;
    }
};
```
