3341. Find Minimum Time to Reach Last Room I

There is a dungeon with `n x m` rooms arranged as a grid.

You are given a 2D array `moveTime` of size `n x m`, where `moveTime[i][j]` represents the minimum time in seconds when you can start moving to that room. You start from the room `(0, 0)` at time `t = 0` and can move to an adjacent room. Moving between adjacent rooms takes exactly one second.

Return the **minimum** time to reach the room `(n - 1, m - 1)`.

Two rooms are **adjacent** if they share a common wall, either horizontally or vertically.

 

**Example 1:**
```
Input: moveTime = [[0,4],[4,4]]

Output: 6

Explanation:

The minimum time required is 6 seconds.

At time t == 4, move from room (0, 0) to room (1, 0) in one second.
At time t == 5, move from room (1, 0) to room (1, 1) in one second.
```

**Example 2:**
```
Input: moveTime = [[0,0,0],[0,0,0]]

Output: 3

Explanation:

The minimum time required is 3 seconds.

At time t == 0, move from room (0, 0) to room (1, 0) in one second.
At time t == 1, move from room (1, 0) to room (1, 1) in one second.
At time t == 2, move from room (1, 1) to room (1, 2) in one second.
```

**Example 3:**
```
Input: moveTime = [[0,1],[1,2]]

Output: 3
```
 

**Constraints:**

* `2 <= n == moveTime.length <= 50`
* `2 <= m == moveTime[i].length <= 50`
* `0 <= moveTime[i][j] <= 10^9`

# Submissions
---
**Solution 1: (Dijkstra)**
```
Runtime: 17 ms, Beats 82.47%
Memory: 30.00 MB, Beats 49.26%
```
```c++
class Solution {
    int dd[5] = {0, 1, 0, -1, 0};
public:
    int minTimeToReach(vector<vector<int>>& moveTime) {
        int m = moveTime.size(), n = moveTime[0].size(), d, nr, nc;
        priority_queue<tuple<int,int,int>, vector<tuple<int,int,int>>, greater<>> pq;
        vector<vector<int>> dist(m, vector<int>(n, INT_MAX));
        pq.push({0, 0, 0});
        dist[0][0] = 0;
        while (pq.size()) {
            auto [w, r, c] = pq.top();
            pq.pop();
            if (w > dist[r][c]) {
                continue;
            }
            if (r == m-1 && c == n-1) {
                return w;
            }
            for (d = 0; d < 4; d ++) {
                nr = r + dd[d];
                nc = c + dd[d+1];
                if (0 <= nr && nr < m && 0 <= nc && nc < n) {
                    if (max(w, moveTime[nr][nc]) + 1 < dist[nr][nc]) {
                        dist[nr][nc] = max(w, moveTime[nr][nc]) + 1;
                        pq.push({max(w, moveTime[nr][nc])+1, nr, nc});
                    }
                }
            }
        }
        return -1;
    }
};
```
