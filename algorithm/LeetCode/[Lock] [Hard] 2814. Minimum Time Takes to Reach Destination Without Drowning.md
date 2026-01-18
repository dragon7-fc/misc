2814. Minimum Time Takes to Reach Destination Without Drowning

You are given an `n * m` **0-indexed** grid of string `land`. Right now, you are standing at the cell that contains `"S"`, and you want to get to the cell containing `"D"`. There are three other types of cells in this land:

* `"."`: These cells are empty.
* `"X"`: These cells are stone.
* `"*"`: These cells are flooded.

At each second, you can move to a cell that shares a side with your current cell (if it exists). Also, at each second, every empty cell that shares a side with a flooded cell becomes flooded as well.
There are two problems ahead of your journey:

* You can't step on stone cells.
* You can't step on flooded cells since you will drown (also, you can't step on a cell that will be flooded at the same time as you step on it).

Return the minimum time it takes you to reach the destination in seconds, or `-1` if it is impossible.

**Note** that the destination will never be flooded.

 

**Example 1:**

![2814_ex1.png](img/2814_ex1.png)
```
Input: land = [["D",".","*"],[".",".","."],[".","S","."]]
Output: 3
Explanation: The picture below shows the simulation of the land second by second. The blue cells are flooded, and the gray cells are stone.
Picture (0) shows the initial state and picture (3) shows the final state when we reach destination. As you see, it takes us 3 second to reach destination and the answer would be 3.
It can be shown that 3 is the minimum time needed to reach from S to D.
```

**Example 2:**

![2814_ex2-2.png](img/2814_ex2-2.png)
```
Input: land = [["D","X","*"],[".",".","."],[".",".","S"]]
Output: -1
Explanation: The picture below shows the simulation of the land second by second. The blue cells are flooded, and the gray cells are stone.
Picture (0) shows the initial state. As you see, no matter which paths we choose, we will drown at the 3rd second. Also the minimum path takes us 4 seconds to reach from S to D.
So the answer would be -1.
```

**Example 3:**
```
Input: land = [["D",".",".",".","*","."],[".","X",".","X",".","."],[".",".",".",".","S","."]]
Output: 6
Explanation: It can be shown that we can reach destination in 6 seconds. Also it can be shown that 6 is the minimum seconds one need to reach from S to D.
```

**Constraints:**

* `2 <= n, m <= 100`
* `land` consists only of `"S"`, `"D"`, `"."`, `"*"` and `"X"`.
* Exactly one of the cells is equal to `"S"`.
* Exactly one of the cells is equal to `"D"`.

# Submissions
---
**Solution 1: (BFS)**

    land = [["D",".","*"],
qf                xf  xf
q
visited       2   -1  -1
            [".",".","."],
qf
q                 xf  xf
visited           -1  -1
            [".","S","."]]
qf
q             x   x   xf
visited       1   1   -1

```
Runtime: 29 ms, Beats 100.00%
Memory: 171.12 MB, Beats 57.14%
```
```c++
class Solution {
    int dd[5] = {0, 1, 0, -1, 0};
public:
    int minimumSeconds(vector<vector<string>>& land) {
        int m = land.size(), n = land[0].size(), i, j, d, nr, nc, sz;
        vector<vector<int>> visited(m, vector<int>(n));
        queue<array<int, 3>> q;
        queue<array<int, 2>> qf;
        for (i = 0; i < m; i ++) {
            for (j = 0; j < n; j ++) {
                if (land[i][j] == "S") {
                    q.push({i, j, 0});
                    visited[i][j] = 1;
                } else if (land[i][j] == "D") {
                    visited[i][j] = 2;
                } else if (land[i][j] == "*") {
                    qf.push({i, j});
                    visited[i][j] = -1;
                } else if (land[i][j] == "X") {
                    visited[i][j] = -1;
                }
            }
        }
        while (q.size()) {
            sz = qf.size();
            for (i = 0; i < sz; i ++) {
                auto [r, c] = qf.front();
                qf.pop();
                for (d = 0; d < 4; d ++) {
                    nr = r + dd[d];
                    nc = c + dd[d + 1];
                    if (0 <= nr && nr < m && 0 <= nc && nc < n && (visited[nr][nc] == 0 || visited[nr][nc] == 1)) {
                        qf.push({nr, nc});
                        visited[nr][nc] = -1;
                    }
                }
            }
            sz = q.size();
            for (i = 0; i < sz; i ++) {
                auto [r, c, s] = q.front();
                q.pop();
                if (visited[r][c] == 2) {
                    return s;
                }
                for (d = 0; d < 4; d ++) {
                    nr = r + dd[d];
                    nc = c + dd[d + 1];
                    if (0 <= nr && nr < m && 0 <= nc && nc < n && (visited[nr][nc] == 0 || visited[nr][nc] == 2)) {
                        q.push({nr, nc, s + 1});
                        if (visited[nr][nc] == 0) {
                            visited[nr][nc] = 1;
                        }
                    }
                }
            }
        }
        return -1;
    }
};
```
