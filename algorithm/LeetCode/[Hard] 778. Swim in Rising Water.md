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
Runtime: 3 ms, Beats 87.68%
Memory: 13.90 MB, Beats 53.44%
```
```c++
class Solution {
    int dd[5] = {0, 1, 0, -1, 0};
public:
    int swimInWater(vector<vector<int>>& grid) {
        int n = grid.size(), d, ni, nj;
        priority_queue<array<int,3>, vector<array<int,3>>, greater<>> pq;
        vector<vector<int>> visited(n, vector<int>(n));
        pq.push({grid[0][0], 0, 0});
        visited[0][0] = 1;
        while (pq.size()) {
            auto [a, i, j]= pq.top();
            pq.pop();
            if (i == n-1 && j == n-1) {
                return a;
            }
            for (d = 0; d < 4; d ++) {
                ni = i + dd[d];
                nj = j + dd[d+1];
                if (0 <= ni && ni < n && 0 <= nj && nj < n && !visited[ni][nj]) {
                    pq.push({max(a, grid[ni][nj]), ni, nj});
                    visited[ni][nj] = 1;
                }
            }
        }
        return -1;
    }
};
```
