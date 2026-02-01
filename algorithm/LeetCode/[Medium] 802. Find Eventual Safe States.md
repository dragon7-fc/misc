802. Find Eventual Safe States

In a directed graph, we start at some node and every turn, walk along a directed edge of the graph.  If we reach a node that is terminal (that is, it has no outgoing directed edges), we stop.

Now, say our starting node is eventually safe if and only if we must eventually walk to a terminal node.  More specifically, there exists a natural number `K` so that for any choice of where to walk, we must have stopped at a terminal node in less than `K` steps.

Which nodes are eventually safe?  Return them as an array in sorted order.

The directed graph has `N` nodes with labels `0, 1, ..., N-1`, where `N` is the length of graph.  The graph is given in the following form: `graph[i]` is a list of labels `j` such that `(i, j)` is a directed edge of the graph.

**Example:**
```
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Here is a diagram of the above graph.

Illustration of graph
```
![802_picture1.png](img/802_picture1.png)

**Note:**

* graph will have length at most `10000`.
* The number of edges in the `graph` will not exceed `32000`.
* Each `graph[i]` will be a sorted list of different integers, chosen within the range `[0, graph.length - 1]`.

# Submissions
---
**Solution: (Reverse Edges)**
```
Runtime: 1252 ms
Memory Usage: 25.1 MB
```
```python
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        N = len(graph)
        safe = [False] * N

        graph = list(map(set, graph))
        rgraph = [set() for _ in range(N)]
        q = collections.deque()

        for i, js in enumerate(graph):
            if not js:
                q.append(i)
            for j in js:
                rgraph[j].add(i)

        while q:
            j = q.popleft()
            safe[j] = True
            for i in rgraph[j]:
                graph[i].remove(j)
                if len(graph[i]) == 0:
                    q.append(i)

        return [i for i, v in enumerate(safe) if v]
```

**Solution 1: (DFS, Graph)**
```
Runtime: 704 ms
Memory Usage: 19.6 MB
```
```python
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        N = len(graph)
        seen = [0]*N
        ans = []

        def dfs(v):
            if seen[v] == -1:
                return False
            if seen[v] == 1:
                return True
            
            seen[v] = -1  # start visit
            
            for nei in graph[v]:
                if not dfs(nei):
                    return False
                
            seen[v] = 1  # end visit
            
            return True
        
        for i, _ in enumerate(graph):
            if dfs(i):
                ans.append(i)
            
        return ans
```

**Solution 2: (BFS, topological sort)**
```
Runtime: 259 ms
Memory: 68.1 MB
```
```c++
class Solution {
public:
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        unordered_map<int, vector<int>> m;
        int n = graph.size();
        vector<int> out(n);
        queue<int> q;
        for (int i = 0; i < graph.size(); i ++) {
            for (int j = 0; j < graph[i].size(); j ++) {
                out[i] += 1;
                m[graph[i][j]].push_back(i);
            }
            if (out[i] == 0) {
                q.push(i);
            }
        }
        vector<bool> safe(n);
        int cur, ncur;
        while (!q.empty()) {
            cur = q.front();
            q.pop();
            safe[cur] = true;
            for (auto ncur: m[cur]) {
                out[ncur] -= 1;
                if (out[ncur] == 0) {
                    q.push(ncur);
                }
            }
        }
        vector<int> ans;
        for (int i = 0; i < safe.size(); i ++) {
            if (safe[i]) {
                ans.push_back(i);
            }
        }
        return ans;
    }
};
```

**Solution 3: (DFS, check cycle)**
```
Runtime: 163 ms
Memory: 47.1 MB
```
```c++
class Solution {
    bool dfs(int node, std::vector<bool>& visited, std::vector<std::vector<int>>& graph, std::vector<int>& unsafe) {
        bool isSafe = true;
        for (int neighbor : graph[node]) {
            if (visited[neighbor] || unsafe[neighbor] == 2) {
                isSafe = false;
                break;
            }
            if (unsafe[neighbor] == 1) {
                continue;
            }
            visited[neighbor] = true;
            if (!dfs(neighbor, visited, graph, unsafe)) {
                isSafe = false;
            }
            visited[neighbor] = false;
        }
        unsafe[node] = isSafe ? 1 : 2;
        return isSafe;
    }
public:
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        int n = graph.size();
        std::vector<bool> visited(n, false);
        std::vector<int> unsafe(n, 0);

        for (int i = 0; i < n; i++) {
            if (unsafe[i] == 0) {
                visited[i] = true;
                dfs(i, visited, graph, unsafe);
                visited[i] = false;
            }
        }

        std::vector<int> result;
        for (int i = 0; i < unsafe.size(); i++) {
            if (unsafe[i] == 1) {
                result.push_back(i);
            }
        }
        return result;
    }
};
```

**Solution 4: (BFS)**
```
Runtime: 48 ms
Memory: 65.76 MB
```
```c++
class Solution {
public:
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        int n = graph.size(), i;
        vector<vector<int>> par(n);
        for (i = 0; i < n; i ++) {
            for (auto j: graph[i]) {
                par[j].push_back(i);
            }
        }
        vector<bool> visited(n), is_safe(n);
        queue<int> q;
        vector<int> ans;
        for (i = 0; i < n; i ++) {
            if (!graph[i].size()) {
                visited[i] = true;
                is_safe[i] = true;
                q.push(i);
            }
        }
        while (q.size()) {
            auto u = q.front();
            q.pop();
            for (auto v: par[u]) {
                if (!visited[v] && all_of(graph[v].begin(), graph[v].end(), [&](int nv){return is_safe[nv];})) {
                    visited[v] = true;
                    is_safe[v] = true;
                    q.push(v);
                }
            }
        }
        for (i = 0; i < n; i ++) {
            if (is_safe[i]) {
                ans.push_back(i);
            }
        }
        return ans;
    }
};
```

**Solution 5: (DFS, check cycle)**
```
Runtime: 4 ms
Memory: 51.40 MB
```
```c++
class Solution {
    bool dfs(int node, vector<vector<int>>& adj, vector<bool>& visit,
             vector<bool>& inStack) {
        // If the node is already in the stack, we have a cycle.
        if (inStack[node]) {
            return true;
        }
        if (visit[node]) {
            return false;
        }
        // Mark the current node as visited and part of current recursion stack.
        visit[node] = true;
        inStack[node] = true;
        for (auto neighbor : adj[node]) {
            if (dfs(neighbor, adj, visit, inStack)) {
                return true;
            }
        }
        // Remove the node from the stack.
        inStack[node] = false;
        return false;
    }
public:
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        int n = graph.size();
        vector<bool> visit(n), inStack(n);

        for (int i = 0; i < n; i++) {
            dfs(i, graph, visit, inStack);
        }

        vector<int> safeNodes;
        for (int i = 0; i < n; i++) {
            if (!inStack[i]) {
                safeNodes.push_back(i);
            }
        }

        return safeNodes;
    }
};
```

**Solution 6: (Topological Sort)**

    graph = [[1,2],[2,3],[5],[0],[5],[],[]]

        ---------
    ----|----   |         
    |   |   v   v        
    0 > 1 > 2 > 3   4 > 5   6
    ^       x   |   x   x   x
    --------|----       ^
            -------------
                         
q:
    5 6
    2 4

```
Runtime: 51 ms, Beats 43.30%
Memory: 66.98 MB, Beats 9.04%
```
```c++
class Solution {
public:
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        int n = graph.size(), i;
        vector<vector<int>> g(n);
        queue<int> q;
        vector<int> outdeg(n), visited(n);
        vector<int> ans;
        for (i = 0; i < n; i ++) {
            outdeg[i] = graph[i].size();
            for (auto j: graph[i]) {
                g[j].push_back(i);
            }
        }
        for (i = 0; i < n; i ++) {
            if (outdeg[i] == 0) {
                q.push(i);
                visited[i] = 1;
            }
        }
        while (q.size()) {
            auto u = q.front();
            q.pop();
            for (auto v: g[u]) {
                outdeg[v] -= 1;
                if (outdeg[v] == 0) {
                    q.push(v);
                    visited[v] = 1;
                }
            }
        }
        for (i = 0; i < n; i ++) {
            if (visited[i]) {
                ans.push_back(i);
            }
        }
        return ans;
    }
};

```
