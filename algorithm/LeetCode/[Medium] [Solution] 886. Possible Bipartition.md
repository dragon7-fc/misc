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
