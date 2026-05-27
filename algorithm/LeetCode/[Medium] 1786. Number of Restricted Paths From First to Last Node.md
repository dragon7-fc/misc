1786. Number of Restricted Paths From First to Last Node

There is an undirected weighted connected graph. You are given a positive integer `n` which denotes that the graph has `n` nodes labeled from `1` to `n`, and an array `edges` where each `edges[i] = [ui, vi, weighti]` denotes that there is an edge between nodes `ui` and `vi` with weight equal to `weighti`.

A path from node `start` to node `end` is a sequence of nodes `[z0, z1, z2, ..., zk]` such that `z0 = start` and `zk = end` and there is an edge between `zi` and `zi+1` where `0 <= i <= k-1`.

The distance of a path is the sum of the weights on the edges of the path. Let `distanceToLastNode(x)` denote the shortest distance of a path between node `n` and node `x`. A **restricted path** is a path that also satisfies that `distanceToLastNode(zi) > distanceToLastNode(zi+1)` where `0 <= i <= k-1`.

Return the number of restricted paths from node `1` to node `n`. Since that number may be too large, return it modulo `10^9 + 7`.

 

**Example 1:**

```
Input: n = 5, edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]
Output: 3
Explanation: Each circle contains the node number in black and its distanceToLastNode value in blue. The three restricted paths are:
1) 1 --> 2 --> 5
2) 1 --> 2 --> 3 --> 5
3) 1 --> 3 --> 5
```

**Example 2:**

```
Input: n = 7, edges = [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]]
Output: 1
Explanation: Each circle contains the node number in black and its distanceToLastNode value in blue. The only restricted path is 1 --> 3 --> 7.
```

**Constraints:**

* `1 <= n <= 2 * 10^4`
* `n - 1 <= edges.length <= 4 * 10^4`
* `edges[i].length == 3`
* `1 <= ui, vi <= n`
* `ui != vi`
* `1 <= weighti <= 10^5`
* There is at most one edge between any two nodes.
* There is at least one path between any two nodes.

# Submissions
---
**Solution 1: (Dijkstra's algorithm + DP Top-Down)**
```
Runtime: 2383 ms
Memory: 86.5 MB
```
```
Runtime: 4179 ms
Memory: 85.2 MB
```
```python
class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        g = collections.defaultdict(dict)
        for u, v, w in edges:
            g[u][v] = w
            g[v][u] = w
        hq = [(0, n)]
        dist = {}
        while hq:
            w, v = heapq.heappop(hq)
            if v in dist:
                continue
            dist[v] = w
            for nv in g[v]:
                if dist.get(nv, float('inf')) > g[v][nv] + dist[v]:
                    heapq.heappush(hq, (g[v][nv] + dist[v], nv))
                    
        @functools.lru_cache(None)
        def dp(u):
            if u == 1:
                return 1
            return sum([dp(v) for v in g[u] if dist[v] > dist[u]]) % (10**9 + 7)
            
        return dp(n)
```

**Solution 2: (Dijkstra, DP Top-Down, dijkstra from target to get shortest path from each node to target then dp top-dwon to count path from target to source)**
```
Runtime: 96 ms, Beats 89.37%
Memory: 151.38 MB, Beats 83.48%
```
```c++
class Solution {
    int dfs(int u, vector<vector<pair<int, int>>> &g, vector<int> &dist, vector<int> &dp) {
        if (u == 1) {
            return 1;
        }
        if (dp[u] != -1) {
            return dp[u];
        }
        long long rst = 0;
        const int MOD = 1e9 + 7;
        for (auto [v, _]: g[u]) {
            if (dist[v] > dist[u]) {
                rst += dfs(v, g, dist, dp);
                rst %= MOD;
            }
        }
        dp[u] = rst;
        return rst;
    }
public:
    int countRestrictedPaths(int n, vector<vector<int>>& edges) {
        vector<vector<pair<int, int>>> g(n + 1);
        for (auto &e: edges) {
            auto u = e[0];
            auto v = e[1];
            auto w = e[2];
            g[u].push_back({v, w});
            g[v].push_back({u, w});
        }
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
        vector<int> dist(n + 1, INT_MAX);
        dist[n] = 0;
        pq.push({0, n});
        while (!pq.empty()) {
            auto [w, u] = pq.top();
            pq.pop();
            if (u == 1) {
                break;
            }
            if (dist[u] < w) {
                continue;
            }
            for (auto [v, dw]: g[u]) {
                int nw = w + dw;
                if (dist[v] > nw) {
                    dist[v] = nw;
                    pq.push({nw, v});
                }
            }
        }
        vector<int> dp(n + 1, -1);
        return dfs(n, g, dist, dp);
    }
};
```
