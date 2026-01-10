1102. Path With Maximum Minimum Value

Given a matrix of integers `A` with R rows and C columns, find the **maximum** score of a path starting at `[0,0]` and ending at [R-1,C-1].

The score of a path is the **minimum** value in that path.  For example, the value of the path `8 →  4 →  5 →  9` is `4`.

A path moves some number of times from one visited cell to any neighbouring unvisited cell in one of the 4 cardinal directions (north, east, west, south).

 

**Example 1:**

![1102_1313_ex1.jpeg](img/1102_1313_ex1.jpeg)
```
Input: [[5,4,5],[1,2,6],[7,4,6]]
Output: 4
Explanation: 
The path with the maximum score is highlighted in yellow. 
```

**Example 2:**

![1102_1313_ex2.jpeg](img/1102_1313_ex2.jpeg)
```
Input: [[2,2,1,2,2,2],[1,2,2,2,1,2]]
Output: 2
```

**Example 3:**

![1102_1313_ex3.jpeg](img/1102_1313_ex3.jpeg)
```
Input: [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]
Output: 3
```

**Note:**

* `1 <= R, C <= 100`
* `0 <= A[i][j] <= 10^9`

# Submissions
---
**Solution 1: (Dijkstra)**
```
Runtime: 1532 ms
Memory Usage: 17.1 MB
```
```python
class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        R, C = len(A), len(A[0])
        d = [[0] * C for _ in range(R)]
        d[0][0] = A[0][0]
        queue = [(-A[0][0], 0, 0)]
        seen = set()
        while queue:
            _, r, c = heapq.heappop(queue)
            seen.add((r, c))
            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in seen:
                    cur = min(d[r][c], A[nr][nc])
                    if d[nr][nc] < cur:
                        d[nr][nc] = cur
                        heapq.heappush(queue, (-cur, nr, nc))
        return d[-1][-1]
```

**Solution 2: (Dijkstra)**

    grid = [[ 5, 4, 5],
pq           (5) (4) (4)
              x   x   x
            [ 1, 2, 6],
             (1) (2) (4)
              1   2   4
                      x
            [ 7, 4, 6]]
                    (4)x

```
Runtime: 118 ms, Beats 73.26%
Memory: 40.23 MB, Beats 74.42%
```
```c++
class Solution {
    int dd[5] = {0, 1, 0, -1, 0};
public:
    int maximumMinimumPath(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size(), d, nr, nc, nw;
        priority_queue<array<int, 3>> pq;
        vector<vector<int>> dist(m, vector<int>(n, INT_MIN));
        pq.push({grid[0][0], 0, 0});
        dist[0][0] = grid[0][0];
        while (pq.size()) {
            auto [w, r, c] = pq.top();
            pq.pop();
            if (r == m - 1 && c == n - 1) {
                return w;
            }
            for (d = 0; d < 4; d ++) {
                nr = r + dd[d];
                nc = c + dd[d + 1];
                if (0 <= nr && nr < m && 0 <= nc && nc < n && w > dist[nr][nc]) {
                    nw = min(w, grid[nr][nc]);
                    pq.push({nw, nr, nc});
                    dist[nr][nc] = nw;
                }
            }
        }
        return -1;
    }
};
```
