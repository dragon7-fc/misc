2192. All Ancestors of a Node in a Directed Acyclic Graph

You are given a positive integer `n` representing the number of nodes of a **Directed Acyclic Graph** (DAG). The nodes are numbered from `0` to `n - 1` (inclusive).

You are also given a 2D integer array `edges`, where `edges[i] = [fromi, toi]` denotes that there is a **unidirectional** edge from `fromi` to `toi` in the graph.

Return a list `answer`, where `answer[i]` is the **list of ancestors** of the `i`th node, sorted in **ascending order**.

A node `u` is an **ancestor** of another node `v` if `u` can reach `v` via a set of edges.

 

**Example 1:**

![2192_e1.png](img/2192_e1.png)
```
Input: n = 8, edgeList = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
Output: [[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]]
Explanation:
The above diagram represents the input graph.
- Nodes 0, 1, and 2 do not have any ancestors.
- Node 3 has two ancestors 0 and 1.
- Node 4 has two ancestors 0 and 2.
- Node 5 has three ancestors 0, 1, and 3.
- Node 6 has five ancestors 0, 1, 2, 3, and 4.
- Node 7 has four ancestors 0, 1, 2, and 3.
```

**Example 2:**

![2192_e2.png](img/2192_e2.png)
```
Input: n = 5, edgeList = [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Output: [[],[0],[0,1],[0,1,2],[0,1,2,3]]
Explanation:
The above diagram represents the input graph.
- Node 0 does not have any ancestor.
- Node 1 has one ancestor 0.
- Node 2 has two ancestors 0 and 1.
- Node 3 has three ancestors 0, 1, and 2.
- Node 4 has four ancestors 0, 1, 2, and 3.
```

**Constraints:**

* `1 <= n <= 1000`
* `0 <= edges.length <= min(2000, n * (n - 1) / 2)`
* `edges[i].length == 2`
* `0 <= fromi, toi <= n - 1`
* `fromi != toi`
* There are no duplicate edges.
* The graph is **directed** and **acyclic**.

# Submissions
---
**Solution 1: (BFS)**
```
Runtime: 843 ms
Memory Usage: 41.8 MB
```
```python
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans = [set() for _ in range(n)]
        g = collections.defaultdict(list)
        indeg = [0]*n
        for fromi, toi in edges:
            g[fromi] += [toi]
            indeg[toi] += 1
        q = collections.deque([i for i, v in enumerate(indeg) if v == 0])
        while q:
            v = q.popleft();
            for nv in g[v]:
                ans[nv].add(v)
                ans[nv] |= ans[v]
                indeg[nv] -= 1
                if indeg[nv] == 0:
                    q += [nv]
        for i in range(len(ans)):
            ans[i] = sorted(ans[i])
        return ans
```

**Solution 2: (DFS)**
```
Runtime: 113 ms
Memory: 63.12 MB
```
```c++
class Solution {
    void dfs(vector<vector<int>> &g, int pv, int v, vector<vector<int>> &ans, vector<bool> &visited){
        visited[v] = true;
        for (auto &nv: g[v]){
            if (!visited[nv]){
                ans[nv].push_back(pv);
                dfs(g, pv, nv, ans, visited);
            }
            
        }
    }

public:
    vector<vector<int>> getAncestors(int n, vector<vector<int>>& edges) {
        vector<vector<int>> ans(n), g(n);
        for (auto &e: edges){
            g[e[0]].push_back(e[1]);
        }
        vector<bool> visited(n);
        for (int i = 0; i < n; i ++){
            fill(visited.begin(), visited.end(), false);
            dfs(g, i, i, ans, visited);
        }
        return ans;

    }
};
```

**Solution 3: (Depth First Search (Reversed Graph))**
```
Runtime: 434 ms
Memory: 158.41 MB
```
```c++
class Solution {
     // Helper method to perform DFS and find all children of a given node
    void findChildren(int currentNode, vector<vector<int>>& adjacencyList,
                      unordered_set<int>& visitedNodes) {
        // Mark current node as visited
        visitedNodes.insert(currentNode);

        // Recursively traverse all neighbors
        for (int neighbour : adjacencyList[currentNode]) {
            if (visitedNodes.find(neighbour) == visitedNodes.end()) {
                findChildren(neighbour, adjacencyList, visitedNodes);
            }
        }
    }

public:
    vector<vector<int>> getAncestors(int n, vector<vector<int>>& edges) {
        // Initialize adjacency list for the graph
        vector<vector<int>> adjacencyList(n);

        // Populate the adjacency list with reversed edges
        for (auto& edge : edges) {
            int from = edge[0];
            int to = edge[1];
            adjacencyList[to].push_back(from);
        }

        vector<vector<int>> ancestorsList;

        // For each node, find all its ancestors (children in reversed graph)
        for (int i = 0; i < n; i++) {
            vector<int> ancestors;
            unordered_set<int> visited;
            findChildren(i, adjacencyList, visited);
            // Add visited nodes to the current nodes' ancestor list
            for (int node = 0; node < n; node++) {
                if (node == i) continue;
                if (visited.find(node) != visited.end())
                    ancestors.push_back(node);
            }
            ancestorsList.push_back(ancestors);
        }

        return ancestorsList;
    }
};
```

**Solution 4: (Topological Sort (BFS))**
```
Runtime: 381 ms
Memory: 144.58 MB
```
```c++
class Solution {
public:
    vector<vector<int>> getAncestors(int n, vector<vector<int>>& edges) {
        // Create adjacency list
        vector<vector<int>> adjacencyList(n);
        for (int i = 0; i < n; i++) {
            adjacencyList[i] = {};
        }

        // Fill the adjacency list and indegree array based on the edges
        vector<int> indegree(n, 0);
        for (auto& edge : edges) {
            int from = edge[0];
            int to = edge[1];
            adjacencyList[from].push_back(to);
            indegree[to]++;
        }

        queue<int> nodesWithZeroIndegree;
        for (int i = 0; i < indegree.size(); i++) {
            if (indegree[i] == 0) {
                nodesWithZeroIndegree.push(i);
            }
        }

        // List to store the topological order of nodes
        vector<int> topologicalOrder;
        while (!nodesWithZeroIndegree.empty()) {
            int currentNode = nodesWithZeroIndegree.front();
            nodesWithZeroIndegree.pop();
            topologicalOrder.push_back(currentNode);

            // Reduce indegree of neighboring nodes and add them to the queue
            // if they have no more incoming edges
            for (int neighbor : adjacencyList[currentNode]) {
                indegree[neighbor]--;
                if (indegree[neighbor] == 0) {
                    nodesWithZeroIndegree.push(neighbor);
                }
            }
        }

        // Initialize the result list and set list for storing ancestors
        vector<vector<int>> ancestorsList(n);
        vector<set<int>> ancestorsSetList(n);

        // Fill the set list with ancestors using the topological order
        for (int node : topologicalOrder) {
            for (int neighbor : adjacencyList[node]) {
                // Add immediate parent, and other ancestors
                ancestorsSetList[neighbor].insert(node);
                ancestorsSetList[neighbor].insert(
                    ancestorsSetList[node].begin(),
                    ancestorsSetList[node].end());
            }
        }

        // Convert sets to lists and sort them
        for (int i = 0; i < ancestorsList.size(); i++) {
            ancestorsList[i].assign(ancestorsSetList[i].begin(),
                                    ancestorsSetList[i].end());
            sort(ancestorsList[i].begin(), ancestorsList[i].end());
        }

        return ancestorsList;
    }
};
```

**Solution 5: (Depth First Search (Optimized))**
```
Runtime: 92 ms
Memory: 64.30 MB
```
```c++
class Solution {
     // Helper method to perform DFS and find ancestors
    void findAncestorsDFS(int ancestor, vector<vector<int>>& adjacencyList,
                          int currentNode, vector<vector<int>>& ancestors) {
        for (int childNode : adjacencyList[currentNode]) {
            // Check if the ancestor is already added to avoid duplicates
            if (ancestors[childNode].empty() ||
                ancestors[childNode].back() != ancestor) {
                ancestors[childNode].push_back(ancestor);
                findAncestorsDFS(ancestor, adjacencyList, childNode, ancestors);
            }
        }
    }

public:
    vector<vector<int>> getAncestors(int n, vector<vector<int>>& edges) {
        // Initialize adjacency list for each node and ancestors list
        vector<vector<int>> adjacencyList(n);
        vector<vector<int>> ancestors(n);

        // Populate the adjacency list with edges
        for (vector<int> edge : edges) {
            int from = edge[0];
            int to = edge[1];
            adjacencyList[from].push_back(to);
        }

        // Perform DFS for each node to find all its ancestors
        for (int i = 0; i < n; i++) {
            findAncestorsDFS(i, adjacencyList, i, ancestors);
        }

        return ancestors;
    }
};
```
