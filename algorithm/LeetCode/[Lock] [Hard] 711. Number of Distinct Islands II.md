711. Number of Distinct Islands II

You are given an `m x n` binary matrix `grid`. An island is a group of `1`'s (representing land) connected **4-directionally** (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

An island is considered to be the same as another if they have the same shape, or have the same shape after rotation (90, 180, or 270 degrees only) or reflection (left/right direction or up/down direction).

Return the number of **distinct** islands.

 

**Example 1:**

![711_distinctisland2-1-grid.jpg](img/711_distinctisland2-1-grid.jpg)
```
Input: grid = [[1,1,0,0,0],[1,0,0,0,0],[0,0,0,0,1],[0,0,0,1,1]]
Output: 1
Explanation: The two islands are considered the same because if we make a 180 degrees clockwise rotation on the first island, then two islands will have the same shapes.
```

**Example 2:**

![711_distinctisland1-1-grid.jpg](img/711_distinctisland1-1-grid.jpg)
```
Input: grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
Output: 1
```

**Constraints:**

* `m == grid.length`
* `n == grid[i].length`
* `1 <= m, n <= 50`
* `grid[i][j]` is either `0` or `1`.

# Submissions
---
**Solution 1: (DFS, sort)**
```
Runtime: 75 ms, Beats 46.67%
Memory: 52.63 MB, Beats 56.67%
```
```C++
class Solution {
    map<int, vector<pair<int,int>>> mp;
    
    void dfs(int r, int c, vector<vector<int>> &g, int cnt) {
        if ( r < 0 || c < 0 || r >= g.size() || c >= g[0].size()) {
            return;
        }
        if (g[r][c] != 1) {
            return;
        }
        g[r][c] = cnt;
        mp[cnt].push_back({r, c});
        dfs(r + 1, c, g, cnt);
        dfs(r - 1, c, g, cnt);
        dfs(r, c + 1, g, cnt);
        dfs(r, c - 1, g, cnt);
    }
    
    vector<pair<int,int>> norm(vector<pair<int,int>> v) {
        vector<vector<pair<int,int>>> s(8);
        // compute rotations/reflections.
        for (auto p:v) {
            int x = p.first, y = p.second;
            s[0].push_back({x, y});
            s[1].push_back({x, -y});
            s[2].push_back({-x, y});
            s[3].push_back({-x, -y});
            s[4].push_back({y, -x});
            s[5].push_back({-y, x});
            s[6].push_back({-y, -x});
            s[7].push_back({y, x});
        }
        for (auto &l:s) {
            sort(l.begin(),l.end());
        }
        for (auto &l:s) {
            for (int i = 1; i < v.size(); ++i) {
                l[i] = {l[i].first-l[0].first, l[i].second - l[0].second};
            }
            l[0] = {0,0};
        }
        sort(s.begin(),s.end());
        return s[0];
    }
public:
    int numDistinctIslands2(vector<vector<int>>& grid) {
        int cnt = 1;
        set<vector<pair<int,int>>> s;
        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < grid[i].size(); ++j) {
                if (grid[i][j] == 1) {
                    dfs(i, j, grid, ++cnt);
                    s.insert(norm(mp[cnt]));
                }
            }
        }
        
        return s.size();
    }
};

```
