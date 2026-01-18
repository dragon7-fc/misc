3383. Minimum Runes to Add to Cast Spell

Alice has just graduated from wizard school, and wishes to cast a magic spell to celebrate. The magic spell contains certain focus points where magic needs to be concentrated, and some of these focus points contain magic crystals which serve as the spell's energy source. Focus points can be linked through directed runes, which channel magic flow from one focus point to another.

You are given a integer n denoting the number of focus points and an array of integers `crystals` where `crystals[i]` indicates a focus point which holds a magic crystal. You are also given two integer arrays `flowFrom` and `flowTo`, which represent the existing directed runes. The `i`th rune allows magic to freely flow from focus point `flowFrom[i]` to focus point `flowTo[i]`.

You need to find the number of directed runes Alice must add to her spell, such that each focus point either:

* **Contains** a magic crystal.
* **Receives** magic flow from another focus point.

Return the **minimum** number of directed runes that she should add.

 

**Example 1:**
```
Input: n = 6, crystals = [0], flowFrom = [0,1,2,3], flowTo = [1,2,3,0]

Output: 2

Explanation: 
```
![3383_runesexample0.png](img/3383_runesexample0.png)
```
Add two directed runes:

From focus point 0 to focus point 4.
From focus point 0 to focus point 5.
```

**Example 2:**
```
Input: n = 7, crystals = [3,5], flowFrom = [0,1,2,3,5], flowTo = [1,2,0,4,6]

Output: 1

Explanation: 
```
![3383_runesexample1.png](img/3383_runesexample1.png)
```
Add a directed rune from focus point 4 to focus point 2.
```
 

**Constraints:**

* `2 <= n <= 10^5`
* `1 <= crystals.length <= n`
* `0 <= crystals[i] <= n - 1`
* `1 <= flowFrom.length == flowTo.length <= min(2 * 105, (n * (n - 1)) / 2)`
* `0 <= flowFrom[i], flowTo[i] <= n - 1`
* `flowFrom[i] != flowTo[i]`
* All pre-existing directed runes are **distinct**.

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 134 ms, Beats 94.12%
Memory: 230.41 MB, Beats 100.00%
```
```c++
class Solution {
    void dfs(int u, vector<bool> &visited, vector<vector<int>> &g) {
        visited[u] = true;
        for (auto &v: g[u]) {
            if (!visited[v]) {
                dfs(v, visited, g);
            }
        }
    }
public:
    int minRunesToAdd(int n, vector<int>& crystals, vector<int>& flowFrom, vector<int>& flowTo) {
        int i, ans = 0;
        vector<vector<int>> g(n);
        vector<bool> visited(n);
        vector<int> indeg(n);
        for (i = 0; i < flowFrom.size(); i ++) {
            g[flowFrom[i]].push_back(flowTo[i]);
            indeg[flowTo[i]] += 1;
        }
        for (auto &crystal: crystals) {
            if (!visited[crystal]) {
                dfs(crystal, visited, g);
            }
        }
        for (i = 0; i < n; i ++) {
            if (indeg[i] == 0 && !visited[i]) {
                ans += 1;
                dfs(i, visited, g);
            }
        }
        ans += count(visited.begin(), visited.end(), false) != 0;
        return ans;
    }
};
```
