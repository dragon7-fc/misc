827. Making A Large Island

In a 2D grid of `0`s and `1`s, we change at most one `0` to a `1`.

After, what is the size of the largest island? (An island is a 4-directionally connected group of `1`s).

**Example 1:**
```
Input: [[1, 0], [0, 1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
```

**Example 2:**
```
Input: [[1, 1], [1, 0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
```

**Example 3:**
```
Input: [[1, 1], [1, 1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.
```

**Notes:**

* `1 <= grid.length = grid[0].length <= 50`.
* `0 <= grid[i][j] <= 1`.
 
# Solution
---
## Approach #1: (Naive) Depth First Search [Time Limit Exceeded]
**Intuition**

For each `0` in the grid, let's temporarily change it to a `1`, then count the size of the group from that square.

**Algorithm**

For each `0`, change it to a `1`, then do a depth first search to find the size of that component. The answer is the maximum size component found.

Of course, if there is no `0` in the grid, then the answer is the size of the whole grid.

```python
class Solution(object):
    def largestIsland(self, grid):
        N = len(grid)

        def check(r, c):
            seen = {(r, c)}
            stack = [(r, c)]
            while stack:
                r, c = stack.pop()
                for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
                    if (nr, nc) not in seen and 0 <= nr < N and 0 <= nc < N and grid[nr][nc]:
                        stack.append((nr, nc))
                        seen.add((nr, nc))
            return len(seen)

        ans = 0
        has_zero = False
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 0:
                    has_zero = True
                    grid[r][c] = 1
                    ans = max(ans, check(r, c))
                    grid[r][c] = 0

        return ans if has_zero else N*N
```

**Complexity Analysis**

* Time Complexity: $O(N^4)$, where $N$ is the length and width of the grid.

* Space Complexity: $O(N^2)$, the additional space used in the depth first search by `stack` and `seen`.

## Approach #2: Component Sizes [Accepted]
**Intuition**

As in the previous solution, we check every `0`. However, we also store the size of each group, so that we do not have to use depth-first search to repeatedly calculate the same size.

However, this idea fails when the `0` touches the same group. For example, consider `grid = [[0,1],[1,1]]`. The answer is `4`, not `1 + 3 + 3`, since the right neighbor and the bottom neighbor of the `0` belong to the same group.

We can remedy this problem by keeping track of a group id (or index), that is unique for each group. Then, we'll only add areas of neighboring groups with different ids.

**Algorithm**

For each group, fill it with value index and remember it's size as `area[index] = dfs(...)`.

Then for each `0`, look at the neighboring group ids seen and add the area of those groups, plus 1 for the `0` we are toggling. This gives us a candidate answer, and we take the maximum.

To solve the issue of having potentially no `0`, we take the maximum of the previously calculated areas.

```python
class Solution(object):
    def largestIsland(self, grid):
        N = len(grid)

        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= nr < N and 0 <= nc < N:
                    yield nr, nc

        def dfs(r, c, index):
            ans = 1
            grid[r][c] = index
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 1:
                    ans += dfs(nr, nc, index)
            return ans

        area = {}
        index = 2
        for r in xrange(N):
            for c in xrange(N):
                if grid[r][c] == 1:
                    area[index] = dfs(r, c, index)
                    index += 1

        ans = max(area.values() or [0])
        for r in xrange(N):
            for c in xrange(N):
                if grid[r][c] == 0:
                    seen = {grid[nr][nc] for nr, nc in neighbors(r, c) if grid[nr][nc] > 1}
                    ans = max(ans, 1 + sum(area[i] for i in seen))
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N^2)$, where $N$ is the length and width of the `grid`.

* Space Complexity: $O(N^2)$, the additional space used in the depth first search by area.

# Submissions
---
**Solution 1: (Component Sizes)**
```
Runtime: 184 ms
Memory Usage: 16.4 MB
```
```python
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)

        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= nr < N and 0 <= nc < N:
                    yield nr, nc

        def dfs(r, c, index):
            ans = 1
            grid[r][c] = index
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 1:
                    ans += dfs(nr, nc, index)
            return ans

        area = {}
        index = 2
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    area[index] = dfs(r, c, index)
                    index += 1

        ans = max(area.values() or [0])
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 0:
                    seen = {grid[nr][nc] for nr, nc in neighbors(r, c) if grid[nr][nc] > 1}
                    ans = max(ans, 1 + sum(area[i] for i in seen))
        return ans
```

**Solution 2: (Union Find)**
```
Runtime: 295 ms, Beats 36.39%
Memory: 159.23 MB, Beats 41.73%
```
```c++
class Solution {
    int dd[5] = {0, 1, 0, -1, 0};
    int find(int x, vector<int> &p) {
        if (p[x] != x) {
            p[x] = find(p[x], p);
        }
        return p[x];
    }
    void uni(int x, int y, vector<int> &p, vector<int> &sz) {
        int xr = find(x, p), yr = find(y, p);
        if (xr == yr) {
            return;
        }
        if (sz[xr] < sz[yr]) {
            p[xr] = yr;
            sz[yr] += sz[xr];
        } else if (sz[yr] < sz[xr]) {
            p[yr] = xr;
            sz[xr] += sz[yr];
        } else {
            p[xr] = yr;
            sz[yr] += sz[xr];
        }
    }
public:
    int largestIsland(vector<vector<int>>& grid) {
        int n = grid.size(), i, j, ni, nj, d, y, cur, ans = 0;
        vector<int> p(n*n), sz(n*n);
        for (i = 0; i < n; i ++) {
            for (j = 0; j < n; j ++) {
                p[i*n + j] = i*n + j;
                if (grid[i][j]) {
                    sz[i*n + j] = 1;
                }
            }
        }
        for (i = 0; i < n; i ++) {
            for (j = 0; j < n; j ++) {
                if (grid[i][j]) {
                    for (d = 0; d < 4; d ++) {
                        ni = i + dd[d];
                        nj = j + dd[d+1];
                        if (0 <= ni && ni < n && 0 <= nj && nj < n && grid[ni][nj]) {
                            uni(i*n + j, ni*n + nj, p, sz);
                        }
                    }
                }
            }
        }
        for (i = 0; i < n; i ++) {
            for (j = 0; j < n; j ++) {
                if (grid[i][j] == 0) {
                    cur = 1;
                    unordered_set<int> st;
                    for (d = 0; d < 4; d ++) {
                        ni = i + dd[d];
                        nj = j + dd[d+1];
                        if (0 <= ni && ni < n && 0 <= nj && nj < n && grid[ni][nj]) {
                            y = find(ni*n + nj, p);
                            if (!st.count(y)) {
                                st.insert(y);
                                cur += sz[y];
                            }
                        }
                    }
                    ans = max(ans, cur);
                } else {
                    ans = max(ans, sz[i*n + j]);
                }
            }
        }
        return ans;
    }
};
```
