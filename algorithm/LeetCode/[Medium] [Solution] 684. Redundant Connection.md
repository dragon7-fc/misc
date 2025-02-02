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
private:
    unordered_map<int, int> p;
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

**Solution 4: (DFS, brute force)**
```
Runtime: 4 ms, Beats 27.53%
Memory: 15.19 MB, Beats 12.03%
```
```c++
class Solution {
    bool dfs2(int i, int p, vector<bool> &visited, vector<unordered_set<int>> &g) {
        if (visited[i]) {
            return true;
        }
        visited[i] = true;
        for (auto j: g[i]) {
            if (j == p) {
                continue;
            }
            if (dfs2(j, i, visited, g)) {
                return true;
            }
        }
        return false;
    }
    bool dfs(int n, vector<unordered_set<int>> &g) {
        vector<bool> visited(n+1);
        int i;
        for (i = 1; i <= n; i ++) {
            if (!visited[i] && dfs2(i, -1, visited, g)) {
                return true;
            }
        }
        return false;
    }
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int n = edges.size(), i;
        vector<unordered_set<int>> g(n+1);
        for (auto e: edges) {
            g[e[0]].insert(e[1]);
            g[e[1]].insert(e[0]);
        }
        for (i = n-1; i >= 0; i --) {
            g[edges[i][0]].erase(edges[i][1]);
            g[edges[i][1]].erase(edges[i][0]);
            if (!dfs(n, g)) {
                return edges[i];
            }
            g[edges[i][0]].insert(edges[i][1]);
            g[edges[i][1]].insert(edges[i][0]);
        }
        return {};
    }
};
```


**Solution 5: (Depth-First Search - Single Traversal)**

single cycle

    2 - 1 - 5
    |   |
    3 - 4


start 1
          0 1 2 3 4 5
          ---------------
p           4 1 2 3
is_cycle    1 1 1 1
```
Runtime: 4 ms, Beats 27.53%
Memory: 14.24MB, Beats 20.29%
```
```c++
class Solution {
    void dfs(int i, int &start, int n, vector<int> &p, vector<bool> &visited, vector<vector<int>> &g) {
        visited[i] = true;
        for (auto j: g[i]) {
            if (!visited[j]) {
                p[j] = i;
                dfs(j, start, n, p, visited, g);
            } else {
                if (start == 0 && j != p[i]) {
                    start = j;
                    p[j] = i;
                }
            }
        }
    }
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int n = edges.size(), i, start = 0;
        vector<vector<int>> g(n+1);
        vector<bool> visited(n+1), is_cycle(n+1);
        vector<int> p(n+1);
        for (auto e: edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        dfs(1, start, n, p, visited, g);
        i = start;
        do {
            is_cycle[i] = true;
            i = p[i];
        } while (i != start);
        for (i = n-1; i >= 0; i --) {
            if (is_cycle[edges[i][0]] && is_cycle[edges[i][1]]) {
                return edges[i];
            }
        }
        return {};
    }
};
````

**Solution 6: (Disjoint Set Union (DSU))**
````
Runtime: 0 ms, Beats 100.00%
Memory: 12.87 MB, Beats 83.18%
```
```c++
class Solution {
    class DSU {
    private:
        int N;
        vector<int> size;
        vector<int> representative;

    public:
        // Initialize DSU class, size of each component will be one and each
        // node will be representative of it's own.
        DSU(int N) {
            this->N = N;

            for (int node = 0; node < N; node++) {
                size.push_back(1);
                representative.push_back(node);
            }
        }

        // Returns the ultimate representative of the node.
        int find(int node) {
            if (representative[node] == node) {
                return node;
            }

            return representative[node] = find(representative[node]);
        }

        // Returns true if nodeOne and nodeTwo belong to different component and
        // update the representatives accordingly, otherwise returns false.
        bool doUnion(int nodeOne, int nodeTwo) {
            nodeOne = find(nodeOne);
            nodeTwo = find(nodeTwo);

            if (nodeOne == nodeTwo) {
                return 0;
            } else {
                if (size[nodeOne] > size[nodeTwo]) {
                    representative[nodeTwo] = nodeOne;
                    size[nodeOne] += size[nodeTwo];
                } else {
                    representative[nodeOne] = nodeTwo;
                    size[nodeTwo] += size[nodeOne];
                }
                return 1;
            }
        }
    };
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int N = edges.size();

        DSU dsu(N);
        for (auto edge : edges) {
            // If union returns false, we know the nodes are already connected
            // and hence we can return this edge.
            if (!dsu.doUnion(edge[0] - 1, edge[1] - 1)) {
                return edge;
            }
        }

        return {};
    }
};
```

**Solution 7: (Union Find)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 13.06 MB, Beats 56.09%
```
```c++
class Solution {
    class DSU {
        vector<int> p;
        vector<int> r;
    public:
        DSU(int n) {
            p.resize(n);
            r.resize(n);
            for (int i = 1; i < n; i ++) {
                p[i] = i;
                r[i] = 1;
            }
        }
        int find (int x) {
            if (p[x] == x) {
                return p[x];
            }
            p[x] = find(p[x]);
            return p[x];
        }
        bool uni(int x, int y) {
            int xr = find(x), yr = find(y);
            if (xr == yr) {
                return false;
            }
            if (r[xr] < r[yr]) {
                p[xr] = p[yr];
            } else if (r[yr] < r[xr]) {
                p[yr] = p[xr];
            } else {
                p[yr] = xr;
                r[xr] += 1;
            }
            return true;
        }
    };
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int n = edges.size();
        DSU dsu(n+1);
        for (auto e: edges) {
            if (!dsu.uni(e[0], e[1])) {
                return e;
            }
        }
        return {};
    }
};
```
