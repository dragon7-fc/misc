778. Swim in Rising Water

On an N x N `grid`, each square `grid[i][j]` represents the elevation at that point `(i,j)`.

Now rain starts to fall. At time `t`, the depth of the water everywhere is `t`. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most `t`. You can swim infinite distance in zero time. Of course, you must stay within the boundaries of the grid during your swim.

You start at the top left square `(0, 0)`. What is the least time until you can reach the bottom right square `(N-1, N-1)`?

**Example 1:**
```
Input: [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.

You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.
```

**Example 2:**
```
Input: [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation:
 0  1  2  3  4
24 23 22 21  5
12 13 14 15 16
11 17 18 19 20
10  9  8  7  6

The final route is marked in bold.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
```

**Note:**

* `2 <= N <= 50`.
* `grid[i][j] is a permutation of [0, ..., N*N - 1]`.

# Submissions
---
**Solution 1: (Dijkstra's Algorithm)**
```
Runtime: 132 ms
Memory Usage: 13.1 MB
```
```python
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # not sure whether anyone else find this one easier than the cheapest flight
        n = len(grid)
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]

        q = [(grid[0][0], 0, 0)]
        best = {}
        while q:
            elev, x0, y0 = heapq.heappop(q)
            best[(x0, y0)] = elev
            if (x0, y0) == (n-1, n-1): return elev
            for dx, dy in dirs:
                nx, ny = x0 + dx, y0 + dy
                if n > nx >= 0 and n > ny >= 0 and max(elev, grid[nx][ny]) < best.get((nx, ny), float('inf')):
                    heapq.heappush(q,(max(elev, grid[nx][ny]), nx, ny))
                    best[(nx, ny)] = max(elev, grid[nx][ny])
```

**Solution 2: (Binary Search, DFS)**
```
Runtime: 18 ms
Memory Usage: 6.4 MB
```
```c
bool findPath(int ** grid, int row, int col, int time, int gridSize, int *** visited){
    if (row < 0 || col < 0 || row >= gridSize || col >= gridSize)
        return false;
    if ((*visited)[row][col] == 1)
        return false;
    //printf("row = %d, col = %d\n", row, col);
    (*visited)[row][col] = 1;
    if (grid[row][col] > time)
        return false;
    if (row == gridSize - 1 && col == gridSize - 1)
        return true;
    bool result = false;
    result = findPath(grid, row - 1, col, time, gridSize, visited);
    if (result)
        return true;
    result = findPath(grid, row + 1, col, time, gridSize, visited);
    if (result)
        return true;
    result = findPath(grid, row, col - 1, time, gridSize, visited);
    if (result)
        return true;
    result = findPath(grid, row, col + 1, time, gridSize, visited);
    if (result)
        return true;
    return false;
}

int swimInWater(int** grid, int gridSize, int* gridColSize){
    int max = 0x80000000;
    for (int i = 0; i < gridSize; i++){
        for (int j = 0; j < gridColSize[i]; j++){
            if (grid[i][j] > max)
                max = grid[i][j];
        }
    }
    int min = (grid[0][0] > grid[gridSize - 1][gridSize - 1])?grid[0][0]:grid[gridSize - 1][gridSize - 1];
    int ** visited = malloc(sizeof(int *) * gridSize);
    for (int i = 0; i < gridSize; i++){
        visited[i] = malloc(sizeof(int) * gridSize);
        for (int j = 0; j < gridSize; j++){
            visited[i][j] = 0;
        }
    }
    int r = 0, c = 0;
    int index = 0;
    while (min < max){
        bool result = false;
        int middle  = (min + max) / 2;
        for (int i = 0; i < gridSize; i++){
            for (int j = 0; j < gridSize; j++){
                visited[i][j] = 0;
            }
        }
        result = findPath(grid, 0, 0, middle, gridSize, &visited);
        if (result){
            max = middle;
        }
        else{
            min = middle + 1;
        }
    }
    return min;
}
```

**Solution 3: (BFS, Heap)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 13.89 MB, Beats 57.21%
```
```c++
class Solution {
    int dd[5] = {0, 1, 0, -1, 0};
public:
    int swimInWater(vector<vector<int>>& grid) {
        int n = grid.size(), d, nr, nc, ans = 1;
        if (n == 1) {
            return grid[0][0];
        }
        priority_queue<array<int, 3>, vector<array<int, 3>>, greater<>> pq;
        vector<vector<bool>> visited(n, vector<bool>(n));
        pq.push({grid[0][0], 0, 0});
        visited[0][0] = true;
        while (pq.size()) {
            auto [h, r, c] = pq.top();
            pq.pop();
            ans = max(ans, h);
            if (r == n - 1 && c == n - 1) {
                break;
            }
            for (d = 0; d < 4; d ++) {
                nr = r + dd[d];
                nc = c + dd[d + 1];
                if (0 <= nr && nr < n && 0 <= nc && nc < n && !visited[nr][nc]) {
                    visited[nr][nc] = true;
                    pq.push({grid[nr][nc], nr, nc});
                }
            }
        }
        return ans;
    }
};
```

**Solution 4: (Union Find)**
```
Runtime: 3 ms, Beats 87.63%
Memory: 12.94 MB, Beats 71.26%
```
```c++
class Solution {
    vector<int> p, r;
    int find(int x) {
        if (x != p[x]) {
            p[x] = find(p[x]);
        }
        return p[x];
    }
    void uni(int x, int y) {
        int xr = find(x), yr = find(y);
        if (xr == yr) {
            return;
        }
        if (r[xr] >= r[yr]) {
            p[yr] = xr;
            r[xr] += 1;
        } else {
            p[xr] = yr;
            r[yr] += 1;
        }
        return;
    }
    int dd[5] = {0, 1, 0, -1, 0};
public:
    int swimInWater(vector<vector<int>>& grid) {
        int n = grid.size(), i, j, d, ni, nj, ans = 1;
        if (n == 1) {
            return 0;
        }
        vector<array<int,2>> g(n*n + 1); // height
        for (i = 0; i < n; i ++) {
            for (j = 0; j < n; j ++) {
                g[grid[i][j]] = {i, j};
            }
        }
        p.resize(n*n);
        r.resize(n*n, 1);
        for (i = 0; i < n*n; i ++) {
            p[i] = i;
        }
        while (1) {
            i = g[ans][0];
            j = g[ans][1];
            for (d = 0; d < 4; d ++) {
                ni = i + dd[d];
                nj = j + dd[d+1];
                if (0 <= ni && ni < n && 0 <= nj && nj < n && grid[ni][nj] < grid[i][j]) {
                    uni(i*n + j, ni*n + nj);
                }
            }
            find(0);
            find(n*n-1);
            if (p[0] == p.back()) {
                break;
            }
            ans += 1;
        }
        return ans;
    }
};
```
