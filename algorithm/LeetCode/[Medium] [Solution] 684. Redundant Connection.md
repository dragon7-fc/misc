684. Redundant Connection

In this problem, a tree is an **undirected** graph that is connected and has no cycles.

The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of `edges`. Each element of `edges` is a pair `[u, v]` with `u < v`, that represents an **undirected** edge connecting nodes `u` and `v`.

Return an edge that can be removed so that the resulting graph is a tree of `N` nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array. The answer edge `[u, v]` should be in the same format, with `u < v`.

**Example 1:**
```
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given undirected graph will be like this:
  1
 / \
2 - 3
```

**Example 2:**
```
Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
Output: [1,4]
Explanation: The given undirected graph will be like this:
5 - 1 - 2
    |   |
    4 - 3
```

**Note:**

* The size of the input 2D-array will be between `3` and `1000`.
* Every integer represented in the 2D-array will be between `1` and `N`, where `N` is the size of the input array.

**Update (2017-09-26):**

We have overhauled the problem description + test cases and specified clearly the graph is an undirected graph. For the directed graph follow up please see Redundant Connection II). We apologize for any inconvenience caused.

# Solution
---
## Approach #1: DFS [Accepted]
**Intuition and Algorithm**

For each edge `(u, v)`, traverse the graph with a depth-first search to see if we can connect `u` to `v`. If we can, then it must be the duplicate edge.

```python
class Solution(object):
    def findRedundantConnection(self, edges):
        graph = collections.defaultdict(set)

        def dfs(source, target):
            if source not in seen:
                seen.add(source)
                if source == target: return True
                return any(dfs(nei, target) for nei in graph[source])

        for u, v in edges:
            seen = set()
            if u in graph and v in graph and dfs(u, v):
                return u, v
            graph[u].add(v)
            graph[v].add(u)
```

**Complexity Analysis**

* Time Complexity: $O(N^2)$ where $N$ is the number of vertices (and also the number of edges) in the graph. In the worst case, for every edge we include, we have to search every previously-occurring edge of the graph.

* Space Complexity: $O(N)$. The current construction of the graph has at most $N$ nodes.

## Approach #2: Union-Find [Accepted]
**Intuition and Algorithm**

If we are familiar with a Disjoint Set Union (DSU) data structure, we can use this in a straightforward manner to solve the problem: we simply find the first edge occurring in the graph that is already connected. The rest of this explanation will focus on the details of implementing DSU.

A DSU data structure can be used to maintain knowledge of the connected components of a graph, and query for them quickly. In particular, we would like to support two operations:

* `dsu.find(node x)`, which outputs a unique id so that two nodes have the same id if and only if they are in the same connected component, and:

* `dsu.union(node x, node y)`, which draws an edge `(x, y)` in the graph, connecting the components with id `find(x)` and `find(y)` together.

To achieve this, we keep track of `parent`, which remembers the `id` of a smaller node in the same connected component. If the node is it's own parent, we call this the leader of that connected component.

A naive implementation of a DSU structure would look something like this:

Psuedocode

```python
# parent initialized as (x -> x)
function find(x):
    while parent[x] != x: #While x isn't the leader
        x = parent[x]
    return x

function union(x, y):
    parent[find(x)] = find(y)
```

We use two techniques to improve the run-time complexity: path compression, and union-by-rank.

* Path compression involves changing the `x = parent[x]` in the find function to `parent[x] = find(parent[x])`. Basically, as we compute the correct leader for `x`, we should remember our calculation.

* Union-by-rank involves distributing the workload of find across leaders evenly. Whenever we `dsu.union(x, y)`, we have two leaders `xr`, `yr` and we have to choose whether we want `parent[x] = yr` or `parent[y] = xr`. We choose the leader that has a higher following to pick up a new follower.

Specifically, the meaning of rank is that there are less than `2 ^ rank[x]` followers of `x`. This strategy can be shown to give us better bounds for how long the recursive loop in `dsu.find` could run for.

```python
class DSU(object):
    def __init__(self):
        self.par = range(1001)
        self.rnk = [0] * 1001

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        elif self.rnk[xr] < self.rnk[yr]:
            self.par[xr] = yr
        elif self.rnk[xr] > self.rnk[yr]:
            self.par[yr] = xr
        else:
            self.par[yr] = xr
            self.rnk[xr] += 1
        return True

class Solution(object):
    def findRedundantConnection(self, edges):
        dsu = DSU()
        for edge in edges:
            if not dsu.union(*edge):
                return edge
```

Alternate Implementation of DSU without Union-By-Rank

```python
class DSU:
    def __init__(self):
        self.par = range(1001)
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    def union(self, x, y):
        self.par[self.find(x)] = self.find(y)
```

**Complexity Analysis**

* Time Complexity: $O(N\alpha(N)) \approx O(N)$, where $N$ is the number of vertices (and also the number of edges) in the graph, and $\alphaα$ is the Inverse-Ackermann function. We make up to $N$ queries of `dsu.union`, which takes (amortized) $O(\alpha(N))$ time. Outside the scope of this article, it can be shown why `dsu.union` has $O(\alpha(N))$ complexity, what the Inverse-Ackermann function is, and why $O(\alpha(N))$ is approximately $O(1)$.

* Space Complexity: $O(N)$. The current construction of the graph (embedded in our `dsu` structure) has at most $N$ nodes.

# Submissions
---
**Solution: (DFS, Graph)**
```
Runtime: 68 ms
Memory Usage: 14.1 MB
```
```python
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)

        def dfs(source, target):
            if source not in seen:
                seen.add(source)
                if source == target: return True
                return any(dfs(nei, target) for nei in graph[source])

        for u, v in edges:
            seen = set()
            if u in graph and v in graph and dfs(u, v):
                return u, v
            graph[u].add(v)
            graph[v].add(u)
```

**Solution: (Union-Find)**
```
Runtime: 52 ms
Memory Usage: 13.2 MB
```
```python
class DSU(object):
    def __init__(self):
        self.par = list(range(1001))
        self.rnk = [0] * 1001

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        elif self.rnk[xr] < self.rnk[yr]:
            self.par[xr] = yr
        elif self.rnk[xr] > self.rnk[yr]:
            self.par[yr] = xr
        else:
            self.par[yr] = xr
            self.rnk[xr] += 1
        return True
    
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU()
        for edge in edges:
            if not dsu.union(*edge):
                return edge
```

**Solution 3: (Union-Find)**
```
Runtime: 15 ms
Memory Usage: 9.1 MB
```
```c++
class DSU {
public:
    DSU (int n) {
        for (int i = 0 ; i<n; i++) {
            p[i] = i;
        }
    }
    void Union(int x, int y) {
        p[find(x)] = find(y); 
    }
    int find(int i) {
        if (p[i] != i) p[i] = find(p[i]);
        return p[i];
    }
private:
    unordered_map<int, int> p;
};

class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int n = edges.size();
        DSU dsu(n);
        for (const auto& e:edges) {
            if (dsu.find(e[0]) == dsu.find(e[1])) return e;
            dsu.Union(e[0], e[1]);
        }
        return {};
    }
};
```
