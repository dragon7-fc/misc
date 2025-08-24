882. Reachable Nodes In Subdivided Graph

Starting with an **undirected** graph (the "original graph") with nodes from `0` to `N-1`, subdivisions are made to some of the edges.

The graph is given as follows: `edges[k]` is a list of integer `pairs (i, j, n)` such that `(i, j)` is an edge of the original graph,

and `n` is the total number of **new** nodes on that edge. 

Then, the edge `(i, j)` is deleted from the original graph, `n` new nodes `(x_1, x_2, ..., x_n)` are added to the original graph,

and `n+1` new edges `(i, x_1), (x_1, x_2), (x_2, x_3), ..., (x_{n-1}, x_n), (x_n, j)` are added to the original graph.

Now, you start at node `0` from the original graph, and in each move, you travel along one edge. 

Return how many nodes you can reach in at most `M` moves.

 

**Example 1:**

![882_origfinal.png](img/882_origfinal.png)
```
Input: edges = [[0,1,10],[0,2,1],[1,2,2]], M = 6, N = 3
Output: 13
Explanation: 
The nodes that are reachable in the final graph after M = 6 moves are indicated below.
```

**Example 2:**
```
Input: edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]], M = 10, N = 4
Output: 23
```

**Note:**

* `0 <= edges.length <= 10000`
* `0 <= edges[i][0] < edges[i][1] < N`
* There does not exist any `i != j` for which `edges[i][0] == edges[j][0]` and `edges[i][1] == edges[j][1]`.
* The original graph has no parallel edges.
* `0 <= edges[i][2] <= 10000`
* `0 <= M <= 10^9`
* `1 <= N <= 3000`
* `A` reachable node is a node that can be travelled to using at most M moves starting from node 0.

# Solution
---
## Approach 1: Dijkstra's
**Intuition**

Treating the original graph as a weighted, undirected graph, we can use Dijkstra's algorithm to find all reachable nodes in the original graph. However, this won't be enough to solve examples where subdivided edges are only used partially.

When we travel along an edge (in either direction), we can keep track of how much we use it. At the end, we want to know every node we reached in the original graph, plus the sum of the utilization of each edge.

**Algorithm**

We use Dijkstra's algorithm to find the shortest distance from our source to all targets. This is a textbook algorithm, refer to this link for more details.

Additionally, for each (directed) edge `(node, nei)`, we'll keep track of how many "new" nodes (new from subdivision of the original edge) were `used`. At the end, we'll sum up the utilization of each edge.

Please see the inline comments for more details.

```python
class Solution(object):
    def reachableNodes(self, edges, M, N):
        graph = collections.defaultdict(dict)
        for u, v, w in edges:
            graph[u][v] = graph[v][u] = w

        pq = [(0, 0)]
        dist = {0: 0}
        used = {}
        ans = 0

        while pq:
            d, node = heapq.heappop(pq)
            if d > dist[node]: continue
            # Each node is only visited once.  We've reached
            # a node in our original graph.
            ans += 1

            for nei, weight in graph[node].iteritems():
                # M - d is how much further we can walk from this node;
                # weight is how many new nodes there are on this edge.
                # v is the maximum utilization of this edge.
                v = min(weight, M - d)
                used[node, nei] = v

                # d2 is the total distance to reach 'nei' (neighbor) node
                # in the original graph.
                d2 = d + weight + 1
                if d2 < dist.get(nei, M+1):
                    heapq.heappush(pq, (d2, nei))
                    dist[nei] = d2

        # At the end, each edge (u, v, w) can be used with a maximum
        # of w new nodes: a max of used[u, v] nodes from one side,
        # and used[v, u] nodes from the other.
        for u, v, w in edges:
            ans += min(w, used.get((u, v), 0) + used.get((v, u), 0))

        return ans
```

**Complexity Analysis**

* Time Complexity: $O(E \log N)$, where $E$ is the length of edges.

* Space Complexity: $O(N)$.

# Submissions
---
**Solution 1: (Dijkstra's)**
```
Runtime: 532 ms
Memory Usage: 19.8 MB
```
```python
class Solution:
    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        graph = collections.defaultdict(dict)
        for u, v, w in edges:
            graph[u][v] = graph[v][u] = w

        pq = [(0, 0)]
        dist = {0: 0}
        used = {}
        ans = 0

        while pq:
            d, node = heapq.heappop(pq)
            if d > dist[node]: continue
            # Each node is only visited once.  We've reached
            # a node in our original graph.
            ans += 1

            for nei, weight in graph[node].items():
                # M - d is how much further we can walk from this node;
                # weight is how many new nodes there are on this edge.
                # v is the maximum utilization of this edge.
                v = min(weight, M - d)
                used[node, nei] = v

                # d2 is the total distance to reach 'nei' (neighbor) node
                # in the original graph.
                d2 = d + weight + 1
                if d2 < dist.get(nei, M+1):
                    heapq.heappush(pq, (d2, nei))
                    dist[nei] = d2

        # At the end, each edge (u, v, w) can be used with a maximum
        # of w new nodes: a max of used[u, v] nodes from one side,
        # and used[v, u] nodes from the other.
        for u, v, w in edges:
            ans += min(w, used.get((u, v), 0) + used.get((v, u), 0))

        return ans
```

**Solution 2: (Dijkstra's)**
```
Runtime: 155 ms, Beats 16.86%
Memory: 70.61 MB, Beats 21.75%
```
```c++
#define pii pair<int, int>
class Solution {
public:
    int reachableNodes(vector<vector<int>>& edges, int maxMoves, int n) {
        vector<vector<pii>> graph(n);
        for (vector<int> edge: edges) {
            int u = edge[0], v = edge[1], w = edge[2];
            graph[u].push_back({v, w});
            graph[v].push_back({u, w});
        }

        map<int, int> dist;
        dist[0] = 0;
        for (int i = 1; i < n; ++i)
            dist[i] = maxMoves+1;

        map<pii, int> used;
        int ans = 0;

        priority_queue<pii, vector<pii>, greater<pii>> pq;
        pq.push({0, 0});

        while (!pq.empty()) {
            pii top = pq.top();
            pq.pop();
            int d = top.first, node = top.second;
            if (d > dist[node]) continue;

            // Each node is only visited once.  We've reached
            // a node in our original graph.
            ans++;

            for (auto pair: graph[node]) {
                // M - d is how much further we can walk from this node;
                // weight is how many new nodes there are on this edge.
                // v is the maximum utilization of this edge.
                int nei = pair.first;
                int weight = pair.second;
                used[{node, nei}] = min(weight, maxMoves - d);

                // d2 is the total distance to reach 'nei' (neighbor) node
                // in the original graph.
                int d2 = d + weight + 1;
                if (d2 < min(dist[nei], maxMoves+1)) {
                    pq.push({d2, nei});
                    dist[nei] = d2;
                }
            }
        }

        // At the end, each edge (u, v, w) can be used with a maximum
        // of w new nodes: a max of used[u, v] nodes from one side,
        // and used[v, u] nodes from the other.
        for (vector<int> edge: edges) {
            int u = edge[0], v = edge[1], w = edge[2];
            ans += min(w, used[{u, v}] + used[{v, u}]);
        }
        return ans;
    }
};
```

**Solution 3: (Dijkstra's)**

   0            5   7
    .  . . . .  . . .
    0  x x x x  1 x 3
    .x         .x
     .x        .x
      .x       .x
       .x      .x
        .x     .x
         .x     x.
          .x x  2
             .  .
                9

```
Runtime: 83 ms, Beats 37.27%
Memory: 65.17 MB, Beats 26.98%
```
```c++
class Solution {
public:
    int reachableNodes(vector<vector<int>>& edges, int maxMoves, int n) {
        int m = edges.size(), i, nw, ans = 0;
        vector<vector<array<int,2>>> g(n);
        for (auto &e: edges) {
            g[e[0]].push_back({e[1], e[2]});
            g[e[1]].push_back({e[0], e[2]});
        }
        vector<int> dist(n, INT_MAX);
        priority_queue<array<int,2>, vector<array<int,2>>, greater<>> pq;
        unordered_map<int, unordered_map<int,int>> cnt;
        pq.push({0, 0});
        dist[0] = 0;
        while (pq.size()) {
            auto [w, u] = pq.top();
            pq.pop();
            if (w > dist[u]) {
                continue;
            }
            ans += 1;
            for (auto &[v, dw]: g[u]) {
                cnt[u][v] = min(dw, maxMoves - w);
                nw = w + dw + 1;
                if (nw < dist[v] && nw < maxMoves + 1) {
                    dist[v] = nw;
                    pq.push({nw, v});
                }
            }
        }
        for (auto &e: edges) {
            ans += min(e[2], cnt[e[0]][e[1]] + cnt[e[1]][e[0]]);
        }
        return ans;
    }
};
```
