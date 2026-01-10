261. Graph Valid Tree

You have a graph of `n` nodes labeled from `0` to `n - 1`. You are given an integer `n` and a list of `edges` where `edges[i] = [ai, bi]` indicates that there is an undirected edge between nodes `ai` and `bi` in the graph.

Return `true` if the edges of the given graph make up a valid tree, and `false` otherwise.

 

**Example 1:**

![261_tree1-graph.jpg](img/261_tree1-graph.jpg)
```
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
```

**Example 2:**

![261_tree2-graph.jpg](img/261_tree2-graph.jpg)
```
Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
```

**Constraints:**

* `1 <= 2000 <= n`
* `0 <= edges.length <= 5000`
* `edges[i].length == 2`
* `0 <= ai, bi < n`
* `ai != bi`
* There are no self-loops or repeated edges.

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 88 ms
Memory Usage: 16.3 MB
```
```python
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        # if number of edges is not equal number of nodes - 1, indicates there is a cyle           as cycle always has extra edges
        if len(edges) > n-1:
            return False
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        visited.add(0)
        dfs(0)
        return len(visited) == n
```

**Solution 2: (DFS)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 16.83 MB, Beats 57.43%
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
    bool validTree(int n, vector<vector<int>>& edges) {
        if (edges.size() > n - 1){
            return false;
        }
        vector<vector<int>> g(n);
        for (auto &e: edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        vector<bool> visited(n);
        dfs(0, visited, g);
        return count(begin(visited), end(visited), true) == n;
    }
};
```
