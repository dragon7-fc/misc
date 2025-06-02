3568. Minimum Moves to Clean the Classroom

You are given an `m x n` grid `classroom` where a student volunteer is tasked with cleaning up litter scattered around the room. Each cell in the grid is one of the following:

* `'S'`: Starting position of the student
* `'L'`: Litter that must be collected (once collected, the cell becomes empty)
* `'R'`: Reset area that restores the student's energy to full capacity, regardless of their current energy level (can be used multiple times)
* `'X'`: Obstacle the student cannot pass through
* `'.'`: Empty space

You are also given an integer `energy`, representing the student's maximum energy capacity. The student starts with this energy from the starting position `'S'`.

Each move to an adjacent cell (up, down, left, or right) costs 1 unit of energy. If the energy reaches 0, the student can only continue if they are on a reset area `'R'`, which resets the energy to its maximum capacity `energy`.

Return the **minimum** number of moves required to collect all litter items, or `-1` if it's impossible.

 

**Example 1:**
```
Input: classroom = ["S.", "XL"], energy = 2

Output: 2

Explanation:

The student starts at cell (0, 0) with 2 units of energy.
Since cell (1, 0) contains an obstacle 'X', the student cannot move directly downward.
A valid sequence of moves to collect all litter is as follows:
Move 1: From (0, 0) → (0, 1) with 1 unit of energy and 1 unit remaining.
Move 2: From (0, 1) → (1, 1) to collect the litter 'L'.
The student collects all the litter using 2 moves. Thus, the output is 2.
```

**Example 2:**
```
Input: classroom = ["LS", "RL"], energy = 4

Output: 3

Explanation:

The student starts at cell (0, 1) with 4 units of energy.
A valid sequence of moves to collect all litter is as follows:
Move 1: From (0, 1) → (0, 0) to collect the first litter 'L' with 1 unit of energy used and 3 units remaining.
Move 2: From (0, 0) → (1, 0) to 'R' to reset and restore energy back to 4.
Move 3: From (1, 0) → (1, 1) to collect the second litter 'L'.
The student collects all the litter using 3 moves. Thus, the output is 3.
```

**Example 3:**
```
Input: classroom = ["L.S", "RXL"], energy = 3

Output: -1

Explanation:

No valid path collects all 'L'.
```
 

**Constraints:**

* `1 <= m == classroom.length <= 20`
* `1 <= n == classroom[i].length <= 20`
* `classroom[i][j]` is one of `'S'`, `'L'`, `'R'`, `'X'`, or `'.'`
* `1 <= energy <= 50`
* There is exactly one `'S'` in the `grid`.
* There are at most 10 `'L'` cells in the grid.

# Submissions
---
**Solution 1: (BFS, distance constraint, dijkstra like)**
```
Runtime: 1637 ms, Beats 23.08%
Memory: 680.78 MB, Beats 15.38%
```
```c++
int dd[5] = {0, 1, 0, -1, 0};
class Solution {
public:
    int minMoves(vector<string>& classroom, int energy) {
        int m = classroom.size(), n = classroom[0].size(), i, j, i0, j0, k = 0, d, nr, nc;
        vector<vector<int>> dp(m, vector<int>(n, -1));
        for (i = 0; i < m; i ++) {
            for (j = 0; j < n; j ++) {
                if (classroom[i][j] == 'S') {
                    i0 = i;
                    j0 = j;
                } else if (classroom[i][j] == 'L') {
                    dp[i][j] = k;
                    k += 1;
                }
            }
        }
        queue<tuple<int,int,int,int,int>> q;
        vector<vector<vector<vector<int>>>> dist(m, vector<vector<vector<int>>>(n, vector<vector<int>>(energy + 1, vector<int>(1<<k, INT_MAX))));
        q.push({i0, j0, energy, 0, 0});
        while (q.size()) {
            auto [r, c, e, visited, s] = q.front();
            q.pop();
            if (visited == ((1<<k)-1)) {
                return s;
            }
            if (e == 0) {
                continue;
            }
            for (d = 0; d < 4; d ++) {
                nr = r + dd[d];
                nc = c + dd[d+1];
                if (0 <= nr && nr < m && 0 <= nc && nc < n) {
                    if (classroom[nr][nc] == 'X') {
                        continue;
                    } else if (classroom[nr][nc] == 'R') {
                        if (dist[nr][nc][energy][visited] > s+1) {
                            dist[nr][nc][energy][visited] = s+1;
                            q.push({nr , nc, energy, visited, s+1});
                        }
                    } else if (classroom[nr][nc] == '.' || classroom[nr][nc] == 'S') {
                        if (dist[nr][nc][e-1][visited] > s+1) {
                            dist[nr][nc][e-1][visited] = s+1;
                            q.push({nr, nc, e-1, visited, s+1});   
                        }
                    } else if (classroom[nr][nc] == 'L') {
                        if (((1<<dp[nr][nc]) & visited) == 0) {
                            if (dist[nr][nc][e-1][visited | (1<<dp[nr][nc])] > s+1) {
                                dist[nr][nc][e-1][visited | (1<<dp[nr][nc])] = s+1;
                                q.push({nr, nc, e-1, visited | (1<<dp[nr][nc]), s+1});
                            }
                        } else {
                            if (dist[nr][nc][e-1][visited] > s+1) {
                                dist[nr][nc][e-1][visited] = s+1;
                                q.push({nr, nc, e-1, visited, s+1});
                            }
                        }
                    }
                }
            }
        }
        return -1;
    }
};
```
