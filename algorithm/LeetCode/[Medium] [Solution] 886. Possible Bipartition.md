886. Possible Bipartition

Given a set of `N` people (numbered `1, 2, ..., N`), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group. 

Formally, if `dislikes[i] = [a, b]`, it means it is not allowed to put the people numbered `a` and `b` into the same group.

Return `true` if and only if it is possible to split everyone into two groups in this way.

 

**Example 1:**
```
Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]
```

**Example 2:**
```
Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
```

**Example 3:**
```
Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false
```

**Note:**

* `1 <= N <= 2000`
* `0 <= dislikes.length <= 10000`
* `1 <= dislikes[i][j] <= N`
* `dislikes[i][0] < dislikes[i][1]`
* There does not exist `i != j` for which `dislikes[i] == dislikes[j]`.

# Solution
---
## Approach 1: Depth-First Search
**Intuition**

It's natural to try to assign everyone to a group. Let's say people in the first group are red, and people in the second group are blue.

If the first person is red, anyone disliked by this person must be blue. Then, anyone disliked by a blue person is red, then anyone disliked by a red person is blue, and so on.

If at any point there is a conflict, the task is impossible, as every step logically follows from the first step. If there isn't a conflict, then the coloring was valid, so the answer would be `true`.

**Algorithm**

Consider the graph on `N` people formed by the given "dislike" edges. We want to check that each connected component of this graph is bipartite.

For each connected component, we can check whether it is bipartite by just trying to coloring it with two colors. How to do this is as follows: color any node red, then all of it's neighbors blue, then all of those neighbors red, and so on. If we ever color a red node blue (or a blue node red), then we've reached a conflict.

```python
class Solution(object):
    def possibleBipartition(self, N, dislikes):
        graph = collections.defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        color = {}
        def dfs(node, c = 0):
            if node in color:
                return color[node] == c
            color[node] = c
            return all(dfs(nei, c ^ 1) for nei in graph[node])

        return all(dfs(node)
                   for node in range(1, N+1)
                   if node not in color)
```

**Complexity Analysis**

* Time Complexity: $O(N + E)$, where $E$ is the length of dislikes.

* Space Complexity: $O(N + E)$.

# Submissions
---
**Solution: (Breadth First Search)**
```
Runtime: 2458 ms
Memory: 19.9 MB
```
```python
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def bfs(source):
            q = deque([source])
            color[source] = 0 # Start with marking source as 'RED'
            while q:
                node = q.popleft()
                for neighbor in adj[node]:
                    # If there is a conflict, return false.
                    if color[neighbor] == color[node]: return False
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[node]
                        q.append(neighbor)
            
            return True
        
        adj = [[] for _ in range(n + 1)]
        for dislike in dislikes:
            adj[dislike[0]].append(dislike[1])
            adj[dislike[1]].append(dislike[0])
        
        color = [-1] * (n + 1) # 0 stands for red and 1 stands for blue.
        for i in range(1, n + 1):
            if color[i] == -1:
                # For each pending component, run BFS.
                if not bfs(i):
                    # Return false, if there is conflict in the component.
                    return False
        
        return True
```

**Solution: (Depth First Search)**
```
Runtime: 733 ms
Memory: 22 MB
```
```python
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def dfs(node, node_color):
            color[node] = node_color
            for neighbor in adj[node]:
                if color[neighbor] == color[node]: return False
                if color[neighbor] == -1:
                    if not dfs(neighbor, 1 - node_color):
                        return False

            return True
        
        adj = [[] for _ in range(n + 1)]
        for dislike in dislikes:
            adj[dislike[0]].append(dislike[1])
            adj[dislike[1]].append(dislike[0])
        
        color = [-1] * (n + 1) # 0 stands for red and 1 stands for blue.
        for i in range(1, n + 1):
            if color[i] == -1:
                # For each pending component, run DFS.
                if not dfs(i, 0):
                    # Return false, if there is conflict in the component.
                    return False
        
        return True
```

**Solution: (Union-Find)**
```
Runtime: 2777 ms
Memory: 19.7 MB
```
```python
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]
    
    def union_set(self, x, y):
        xset = self.find(x)
        yset = self.find(y)
        if xset == yset:
            return
        
        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
        else:
            self.parent[yset] = xset
            self.rank[xset] += 1

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = [[] for _ in range(n + 1)]
        for dislike in dislikes:
            adj[dislike[0]].append(dislike[1])
            adj[dislike[1]].append(dislike[0])
        
        dsu = UnionFind(n + 1)
        for node in range(1, n + 1):
            for neighbor in adj[node]:
                # Check if the node and its neighbor is in the same set.
                if dsu.find(node) == dsu.find(neighbor): return False
                # Move all the neighbours into same set as the first neighbour.
                dsu.union_set(adj[node][0], neighbor)
        
        return True
```

**Solution 1: (Depth-First Search)**
```
Runtime: 736 ms
Memory Usage: 21.1 MB
```
```python
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
            
        colored = collections.defaultdict(int)

        def dfs(node, color):
            colored[node] = color
            for nei in graph[node]:
                if nei in colored:
                    if colored[nei] == colored[node]:
                        return False
                else:  # Adj nodes to be color inverted.
                    if not dfs(nei, -color):
                        return False
            return True

        for v in graph:
            if v not in colored:
                if not dfs(v, 1):
                    return False
        return True
```

**Solution 2: (DFS)**
```
Runtime: 248 ms
Memory Usage: 71.7 MB
```
```c++
class Solution {
    bool isBipartite(int node,vector<vector<int>>&adj,vector<int>&color){
        queue<int>q;
        q.push(node);
        color[node]=1;
        
        while(!q.empty()){
            int x=q.front();
            q.pop();
            
            for(auto it:adj[x]){
                if(color[it]==-1){
                    
                    color[it]=1-color[x];
                    q.push(it);
                    
                }
                else if(color[it]==color[x]) return false;
            }
        }
        
        return true;
    }
public:
    bool possibleBipartition(int n, vector<vector<int>>& dislikes) {
        vector<vector<int>> adj(n+1);
        vector<int>color(n+1,-1);
        
        for(auto it:dislikes){
            int u=it[0];
            int v=it[1];
            
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
            
        for(int i=1;i<=n;i++){
            if(color[i]==-1){
                if(!isBipartite(i,adj,color)) return false;
            }
        }
        
        return true;
    }
};
```

**Solution 3: (BFS)**
```
Runtime: 288 ms
Memory Usage: 64.6 MB
```
```c++
class Solution {
    bool bfs(int node, vector<int> &color, vector<vector<int>>& adj){
        queue<int> q;
        q.push(node);
        color[node]=1;
        while(!q.empty()){
            int n=q.front();
            q.pop();
            for(auto& x:adj[n]){
                if(color[x]==-1){
                    color[x]=1-color[n];
                    q.push(x);
                }
                else if(color[x]==color[n])
                    return false;
            }
        }
        return true;
    }
public:
    bool possibleBipartition(int n, vector<vector<int>>& dislikes) {
        vector<vector<int>> adj(n+1);
        for(int i=0;i<dislikes.size();i++){
            adj[dislikes[i][0]].push_back(dislikes[i][1]);
            adj[dislikes[i][1]].push_back(dislikes[i][0]);
        }
        vector<int> color(n+1,-1);
        for(int i=1;i<=n;i++){
            if(color[i]==-1){
                if(!bfs(i, color, adj))
                    return false;
            }
        }
        return true;
    }
};
```

**Solution 4: (DFS)**
```
Runtime: 43 ms, Beats 51.52%
Memory: 69.05 MB, Beats 80.13%
```
```c++
class Solution {
    bool dfs(int u, int c, vector<vector<int>> &g, vector<int> &visited) {
        visited[u] = c;
        for (auto v: g[u]) {
            if (visited[v] == c || visited[v] == -1 && !dfs(v, 1^c, g, visited)) {
                return false;
            }
        }
        return true;
    }
public:
    bool possibleBipartition(int n, vector<vector<int>>& dislikes) {
        int i;
        vector<vector<int>> g(n+1);
        vector<int> visited(n+1, -1);
        for (auto &d: dislikes) {
            g[d[0]].push_back(d[1]);
            g[d[1]].push_back(d[0]);
        }
        for (i = 1; i <= n; i ++) {
            if (visited[i] == -1) {
                if (!dfs(i, 0, g, visited)) {
                    return false;
                }
            }
        }
        return true;
    }
};
```
