323. Number of Connected Components in an Undirected Graph

You have a graph of `n` nodes. You are given an integer `n` and an array edges where `edges[i] = [ai, bi]` indicates that there is an edge between `ai` and `bi` in the graph.

Return the number of connected components in the graph.

 

**Example 1:**

```
Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
```

**Example 2:**

```
Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1
```

**Constraints:**

* `1 <= n <= 2000`
* `1 <= edges.length <= 5000`
* `edges[i].length == 2`
* `0 <= ai <= bi < n`
* `ai != bi`
* There are no repeated edges.

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 104 ms
Memory Usage: 17.3 MB
```
```python
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ans = 0
        seen = [0]*n
        g = collections.defaultdict(list)
        for u, v in edges:
            g[u] += [v]
            g[v] += [u]
        
        def dfs(u):
            nonlocal seen
            seen[u] = 1
            for v in g[u]:
                if not seen[v]:
                    dfs(v)
        
        for i in range(n):
            if not seen[i]:
                ans += 1
                dfs(i)
        return ans
```

**Solution 2: (DFS)**
```
Runtime: 20 ms
Memory Usage: 14 MB
```
```c++
class Solution {
public:
    // Build adjacency list for each vertex 
    void buildGraph(int n, vector<vector<int>> &edges, vector<vector<int>> &graph)
    {
        for (const auto &edge:edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]); // we will have an edge from dest to source as graph is undirected graph
        }
    }
    
    void DFS(vector<vector<int>> &graph, int sourceVertex, std::vector<int> &visited) {
        if (visited[sourceVertex] == 1)
            return;
        visited[sourceVertex] = 1;
        for (auto neighbor:graph[sourceVertex])
            DFS(graph, neighbor, visited);
    }

    int countComponents(int n, vector<vector<int>>& edges) {
        // 1: Build the graph from input edges
        std::vector<std::vector<int>> graph(n);
        buildGraph(n, edges, graph);
        
        // Create Initialize visisted vertices vector with -1 to denote not visited
        std::vector<int>visited(n, -1);
        
        // 2: Call BFS on each unvisited vertex and number of times we call BFS
        //    will be equal to number of connected components in graph
        int connectedComponent {0};
        for (int sourceVertex = 0; sourceVertex < n; sourceVertex++) {
            if (visited[sourceVertex] == -1) {
                ++connectedComponent;
                DFS(graph, sourceVertex, visited);
            }
        }
        return connectedComponent;
    }
};
```

**Solution 2: (BFS)**
```
Runtime: 24 ms
Memory Usage: 14.2 MB
```
```c++
class Solution {
public:
    // Build adjacency list for each vertex 
    void buildGraph(int n, vector<vector<int>> &edges, vector<vector<int>> &graph)
    {
        for (const auto &edge:edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]); // we will have an edge from dest to source as graph is undirected graph
        }
    }
    
    void BFS(vector<vector<int>> &graph, int sourceVertex, std::vector<int> &visited) {
        visited[sourceVertex] = 1;
        std::deque<int>queue(1, sourceVertex);
        while (!queue.empty()) {
            auto vertex = queue.front();
            queue.pop_front();
            auto adjacencyList = graph[vertex];
            for (auto neighbor:adjacencyList) {
                if (visited[neighbor] == -1) {
                    visited[neighbor] = 1;
                    queue.push_back(neighbor);
                }
            }
        }
    }

    int countComponents(int n, vector<vector<int>>& edges) {
        // 1: Build the graph from input edges
        std::vector<std::vector<int>> graph(n);
        buildGraph(n, edges, graph);
        
        // Create Initialize visisted vertices vector with -1 to denote not visited
        std::vector<int>visited(n, -1);
        
        // 2: Call BFS on each unvisited vertex and number of times we call BFS
        //    will be equal to number of connected components in graph
        int connectedComponent {0};
        for (int sourceVertex = 0; sourceVertex < n; sourceVertex++) {
            if (visited[sourceVertex] == -1) {
                ++connectedComponent;
                BFS(graph, sourceVertex, visited);
            }
        }
        return connectedComponent;
    }
};
```

**Solution 3: (Union-Find)**

    0  1  2  3  4 
p   0  1  2  3  4
edge: 0,1
    1
edge: 1,2
          1
edge: 3,4
             4  
    1  1  1  4  4
```
Runtime: 0 ms, Beats 100.00%
Memory: 16.35 MB, Beats 80.29%
```
```c++
class Solution {
    vector<int> p;
    vector<int> r;
    int find(int x) {
        if (x != p[x]) {
            p[x] = find(p[x]);
        }
        return p[x];
    }
    void uni(int x, int y) {
        int xr = find(x), yr = find(y);
        if (xr == yr) {
            return;
        }
        if (r[xr] < r[yr]) {
            p[xr] = yr;
        } else if (r[xr] > r[yr]) {
            p[yr] = xr;
        } else {
            p[xr] = yr;
            r[yr] += 1;
        }
    }
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        int i, ans = 0;
        p.resize(n);
        r.resize(n);
        for (i = 0; i < n; i ++) {
            p[i] = i;
        }
        for (auto &e: edges) {
            uni(e[0], e[1]);
        }
        for (i = 0; i < n; i ++) {
            if (i == find(i)) {
                ans += 1;
            }
        }
        return ans;
    }
};
```
