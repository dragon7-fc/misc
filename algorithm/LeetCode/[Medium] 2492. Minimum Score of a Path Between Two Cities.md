2492. Minimum Score of a Path Between Two Cities

You are given a positive integer `n` representing `n` cities numbered from `1` to `n`. You are also given a 2D array `roads` where `roads[i] = [ai, bi, distancei]` indicates that there is a bidirectional road between cities ai and bi with a distance equal to `distancei`. The cities graph is not necessarily connected.

The **score** of a path between two cities is defined as the **minimum** distance of a road in this path.

Return the **minimum** possible score of a path between cities `1` and `n`.

**Note:**

* A path is a sequence of roads between two cities.
* It is allowed for a path to contain the same road **multiple** times, and you can visit cities `1` and `n` multiple times along the path.
* The test cases are generated such that there is **at least** one path between `1` and `n`.
 

**Example 1:**

![2492_graph11.png](img/2492_graph11.png)
```
Input: n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
Output: 5
Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 4. The score of this path is min(9,5) = 5.
It can be shown that no other path has less score.
```

**Example 2:**

![2492_graph22.png](img/2492_graph22.png)
```
Input: n = 4, roads = [[1,2,2],[1,3,4],[3,4,7]]
Output: 2
Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 1 -> 3 -> 4. The score of this path is min(2,2,4,7) = 2.
```

**Constraints:**

* `2 <= n <= 10^5`
* `1 <= roads.length <= 10^5`
* `roads[i].length == 3`
* `1 <= ai, bi <= n`
* `ai != bi`
* `1 <= distancei <= 10^4`
* There are no repeated edges.
* There is at least one path between `1` and `n`.

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 5028 ms
Memory: 76 MB
```
```python
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = collections.defaultdict(list)
        for a, b, d in roads:
            g[a] += [[b, d]]
            g[b] += [[a, d]]
        seen = set()
        ans = float('inf')
        def dfs(u):
            nonlocal ans
            seen.add(u)
            for v, d in g[u]:
                ans = min(ans, d)
                if not v in seen:
                    dfs(v)
            
        dfs(1)
        return ans
```

**Solution 2: (DFS)**
```
Runtime: 501 ms
Memory: 147.1 MB
```
```c++
class Solution {
    void dfs(int v, int &ans, unordered_set<int> &seen, unordered_map<int, vector<pair<int, int>>> &g) {
        seen.insert(v);
        for (auto &[nv, d]: g[v]) {
            ans = min(ans, d);
            if (!seen.count(nv)) {
                dfs(nv, ans, seen, g);
            }
        }
    }
public:
    int minScore(int n, vector<vector<int>>& roads) {
        unordered_map<int, vector<pair<int, int>>> g;
        for (int i = 0; i < roads.size(); i ++) {
            g[roads[i][0]].push_back({roads[i][1], roads[i][2]});
            g[roads[i][1]].push_back({roads[i][0], roads[i][2]});
        }
        unordered_set<int> seen;
        int ans = INT_MAX;
        dfs(1, ans, seen, g);
        return ans;
    }
};
```
