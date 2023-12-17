1631. Path With Minimum Effort

You are a hiker preparing for an upcoming hike. You are given `heights`, a 2D array of size `rows x columns`, where `heights[row][col]` represents the height of cell `(row, col)`. You are situated in the top-left cell, `(0, 0)`, and you hope to travel to the bottom-right cell, `(rows-1, columns-1)` (i.e., **0-indexed**). You can move **up**, **down**, **left**, or **right**, and you wish to find a route that requires the minimum **effort**.

A route's **effort** is the **maximum absolute difference** in heights between two consecutive cells of the route.

Return the minimum **effort** required to travel from the top-left cell to the bottom-right cell.

 

**Example 1:**

![1631_ex1.png](img/1631_ex1.png)
```
Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
```

**Example 2:**

![1631_ex2.png](img/1631_ex2.png)
```
Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].
```

**Example 3:**

![1631_ex3.png](img/1631_ex3.png)
```
Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.
```

**Constraints:**

* `rows == heights.length`
* `columns == heights[i].length`
* `1 <= rows, columns <= 100`
* `1 <= heights[i][j] <= 106`

# Submissions
---
**Solution 1: (BFS, Dijkstra)**
```
Runtime: 708 ms
Memory Usage: 15.2 MB
```
```python
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        dist = [[float('inf')] * n for _ in range(m)]
        minHeap = []
        minHeap.append((0, 0, 0))  # distance, row, col
        DIR = [0, 1, 0, -1, 0]
        while minHeap:
            d, r, c = heappop(minHeap)
            if r == m - 1 and c == n - 1:
                return d  # Reach to bottom right
            for i in range(4):
                nr, nc = r + DIR[i], c + DIR[i + 1]
                if 0 <= nr < m and 0 <= nc < n:
                    newDist = max(d, abs(heights[nr][nc] - heights[r][c]))
                    if dist[nr][nc] > newDist:
                        dist[nr][nc] = newDist
                        heappush(minHeap, (dist[nr][nc], nr, nc))
```

**Solution 2: (BFS, Dijkstra)**
```
Runtime: 75 ms
Memory: 19.4 MB
```
```c++
class Solution {
    int dd[5] = {0, 1, 0, -1, 0};
public:
    int minimumEffortPath(vector<vector<int>>& heights) {
        int R = heights.size(), C = heights[0].size();
        priority_queue<pair<int, pair<int, int>>> pq;
        pq.push({0, {0, 0}});
        vector<vector<int>> dist(R, vector<int>(C, INT_MAX));
        int r, c, nr, nc, neffort;
        while (!pq.empty()) {
            auto [effort, p] = pq.top();
            pq.pop();
            r = p.first, c = p.second;
            dist[r][c] = -effort;
            if (r == R-1 && c == C-1) {
                return -effort;
            }
            for (int d = 0; d < 4; d ++) {
                nr = r + dd[d];
                nc = c + dd[d+1];
                if (0 <= nr && nr < R && 0 <= nc && nc < C) {
                    neffort = max(-effort, abs(heights[nr][nc] - heights[r][c]));
                    if (neffort < dist[nr][nc]) {
                        dist[nr][nc] = neffort;
                        pq.push({-neffort, {nr, nc}});
                    }
                }
            }
        }
        return -1;
    }
};
```
