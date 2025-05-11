3342. Find Minimum Time to Reach Last Room II

There is a dungeon with `n x m` rooms arranged as a grid.

You are given a 2D array moveTime of size `n x m`, where `moveTime[i][j]` represents the minimum time in seconds when you can start moving to that room. You start from the room `(0, 0)` at time `t = 0` and can move to an **adjacent** room. Moving between **adjacent** rooms takes one second for one move and two seconds for the next, **alternating** between the two.

Return the **minimum** time to reach the room `(n - 1, m - 1)`.

Two rooms are **adjacent** if they share a common wall, either horizontally or vertically.

 

**Example 1:**
```
Input: moveTime = [[0,4],[4,4]]

Output: 7

Explanation:

The minimum time required is 7 seconds.

At time t == 4, move from room (0, 0) to room (1, 0) in one second.
At time t == 5, move from room (1, 0) to room (1, 1) in two seconds.
```

**Example 2:**
```
Input: moveTime = [[0,0,0,0],[0,0,0,0]]

Output: 6

Explanation:

The minimum time required is 6 seconds.

At time t == 0, move from room (0, 0) to room (1, 0) in one second.
At time t == 1, move from room (1, 0) to room (1, 1) in two seconds.
At time t == 3, move from room (1, 1) to room (1, 2) in one second.
At time t == 4, move from room (1, 2) to room (1, 3) in two seconds.
```

**Example 3:**
```
Input: moveTime = [[0,1],[1,2]]

Output: 4
```
 

**Constraints:**

* `2 <= n == moveTime.length <= 750`
* `2 <= m == moveTime[i].length <= 750`
* `0 <= moveTime[i][j] <= 10^9`

# Submissions
---
**Solution 1: (Dijkstra)**
```
Runtime: 204 ms, Beats 89.66%
Memory: 97.05 MB, Beats 82.49%
```
```c++
class Solution {
    int dd[5] = {0, 1, 0, -1, 0};
public:
    int minTimeToReach(vector<vector<int>>& moveTime) {
        int m = moveTime.size(), n = moveTime[0].size(), d, nr, nc, nw, ns;
        priority_queue<tuple<int,int,int,int>, vector<tuple<int,int,int,int>>, greater<>> pq;
        vector<vector<int>> dist(m, vector<int>(n, INT_MAX));
        pq.push({0, 0, 0, 1});
        while (pq.size()) {
            auto [w, r, c, s] = pq.top();
            pq.pop();
            if (w > dist[r][c]) {
                continue;
            }
            if (r == m-1 && c == n-1) {
                return w;
            }
            ns = s == 1 ? 2 : 1;
            for (d = 0; d < 4; d ++) {
                nr = r + dd[d];
                nc = c + dd[d+1];
                if (0 <= nr && nr < m && 0 <= nc && nc < n) {
                    nw = max(w, moveTime[nr][nc]) + s;
                    if (dist[nr][nc] > nw) {
                        dist[nr][nc] = nw;
                        pq.push({nw, nr, nc, ns});
                    }
                }
            }
        }
        return -1;
    }
};
```
