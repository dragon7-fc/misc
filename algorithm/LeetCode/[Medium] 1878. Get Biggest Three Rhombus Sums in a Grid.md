1878. Get Biggest Three Rhombus Sums in a Grid

You are given an `m x n` integer matrix `grid`.

A **rhombus sum** is the sum of the elements that form **the border** of a regular rhombus shape in `grid`. The rhombus must have the shape of a square rotated 45 degrees with each of the corners centered in a grid cell. Below is an image of four valid rhombus shapes with the corresponding colored cells that should be included in each **rhombus sum**:

![1878_pc73-q4-desc-2.png](img/1878_pc73-q4-desc-2.png)
Note that the rhombus can have an area of 0, which is depicted by the purple rhombus in the bottom right corner.

Return the biggest three distinct **rhombus sums** in the grid in **descending order**. If there are less than three distinct values, return all of them.

 

**Example 1:**

![1878_pc73-q4-ex1.png](img/1878_pc73-q4-ex1.png)
```
Input: grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
Output: [228,216,211]
Explanation: The rhombus shapes for the three biggest distinct rhombus sums are depicted above.
- Blue: 20 + 3 + 200 + 5 = 228
- Red: 200 + 2 + 10 + 4 = 216
- Green: 5 + 200 + 4 + 2 = 211
```

**Example 2:**

![1878_pc73-q4-ex2.png](img/1878_pc73-q4-ex2.png)
```
Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
Output: [20,9,8]
Explanation: The rhombus shapes for the three biggest distinct rhombus sums are depicted above.
- Blue: 4 + 2 + 6 + 8 = 20
- Red: 9 (area 0 rhombus in the bottom right corner)
- Green: 8 (area 0 rhombus in the bottom middle)
```

**Example 3:**
```
Input: grid = [[7,7,7]]
Output: [7]
Explanation: All three possible rhombus sums are the same, so return [7].
```

**Constraints:**

* `m == grid.length`
* `n == grid[i].length`
* `1 <= m, n <= 50`
* `1 <= grid[i][j] <= 10^5`

# Submissions
---
**Solution 1: (Brute Force, Heap)**
```
Runtime: 1940 ms
Memory Usage: 17.7 MB
```
```python
class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        S = {cell for row in grid for cell in row}
        heap = list(S)
        heapq.heapify(heap)
        while len(heap) > 3:
            heapq.heappop(heap)
        for i in range(m):
            for j in range(n):
                for k in range(1, min(m, n)):
                    if i - k < 0 or i + k >= m or j - k < 0 or j + k >= n:
                        break
                    curr = 0
                    for l in range(k + 1):
                        curr += grid[i+l][j+k-l] + grid[i-l][j+k-l] + grid[i+l][j-k+l] + grid[i-l][j-k+l]
                    curr -= grid[i+k][j] + grid[i-k][j] + grid[i][j+k] + grid[i][j-k]
                    if curr not in S:
                        S.add(curr)
                        heapq.heappush(heap, curr)
                        if len(heap) > 3: heapq.heappop(heap)
        return sorted(heap, reverse=True)
```

**Solution 2: (Enumerate All Rhombuses, Prefix Sum)**
```
Runtime: 19 ms, Beats 92.41%
Memory: 18.74 MB, Beats 84.83%
```
```c++
struct Answer {
    array<int, 3> ans{};

    void put(int x) {
        if (x > ans[0]) {
            tie(ans[0], ans[1], ans[2]) = tuple{x, ans[0], ans[1]};
        } else if (x != ans[0] && x > ans[1]) {
            tie(ans[1], ans[2]) = tuple{x, ans[1]};
        } else if (x != ans[0] && x != ans[1] && x > ans[2]) {
            ans[2] = x;
        }
    }

    vector<int> get() const {
        vector<int> ret;
        for (int num : ans) {
            if (num) {
                ret.push_back(num);
            }
        }
        return ret;
    }
};

class Solution {
public:
    vector<int> getBiggestThree(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector<vector<int>> sum1(m + 1, vector<int>(n + 2));
        vector<vector<int>> sum2(m + 1, vector<int>(n + 2));
        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                sum1[i][j] = sum1[i - 1][j - 1] + grid[i - 1][j - 1];
                sum2[i][j] = sum2[i - 1][j + 1] + grid[i - 1][j - 1];
            }
        }
        Answer ans;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                // a single cell is also a rhombus
                ans.put(grid[i][j]);
                for (int k = i + 2; k < m; k += 2) {
                    int ux = i, uy = j;
                    int dx = k, dy = j;
                    int lx = (i + k) / 2, ly = j - (k - i) / 2;
                    int rx = (i + k) / 2, ry = j + (k - i) / 2;
                    if (ly < 0 || ry >= n) {
                        break;
                    }
                    ans.put((sum2[lx + 1][ly + 1] - sum2[ux][uy + 2]) +
                            (sum1[rx + 1][ry + 1] - sum1[ux][uy]) +
                            (sum1[dx + 1][dy + 1] - sum1[lx][ly]) +
                            (sum2[dx + 1][dy + 1] - sum2[rx][ry + 2]) -
                            (grid[ux][uy] + grid[dx][dy] + grid[lx][ly] +
                             grid[rx][ry]));
                }
            }
        }
        return ans.get();
    }
};
```

**Solution 3: (Brute Force, expand around center)**
```
Runtime: 27 ms, Beats 86.90%
Memory: 16.11 MB, Beats 100.00%
```
```c++
class Solution {
    void add(vector<int> &dp, int a) {
        if (a > dp[0]) {
            dp = {a, dp[0], dp[1]};
        } else if (a != dp[0] && a > dp[1]) {
            dp = {dp[0], a, dp[1]};
        } else if (a != dp[0] && a != dp[1] && a > dp[2]) {
            dp[2] = a;
        }
    }
public:
    vector<int> getBiggestThree(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size(), i, j, k, sum, r, c, t;
        vector<int> dp(3);
        for (int i = 0; i < m; i++) {
            for (j = 0; j < n; j++) {
                add(dp, grid[i][j]);
                for (k = 1; ; k++) {
                    if (i - k < 0 || i + k >= m || j - k < 0 || j + k >= n) {
                        break;
                    }
                    sum = 0;
                    r = i - k;
                    c = j;
                    for (t = 0; t < k; t++) {
                        sum += grid[r + t][c + t];
                    }
                    r = i;
                    c = j + k;
                    for (t = 0; t < k; t++) {
                        sum += grid[r + t][c - t];
                    }
                    r = i + k;
                    c = j;
                    for (t = 0; t < k; t++) {
                        sum += grid[r - t][c - t];
                    }
                    r = i;
                    c = j - k;
                    for (t = 0; t < k; t++) {
                        sum += grid[r - t][c + t];
                    }
                    add(dp, sum);
                }
            }
        }
        vector<int> ans;
        for (auto &a: dp) {
            if (a) {
                ans.push_back(a);
            }
        }
        return ans;
    }
};
```
