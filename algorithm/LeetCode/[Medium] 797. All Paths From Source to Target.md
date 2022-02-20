797. All Paths From Source to Target

Given a directed, acyclic graph of `N` nodes.  Find all possible paths from node `0` to node `N-1`, and return them in any order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  `graph[i]` is a list of all nodes `j` for which the edge `(i, j)` exists.

**Example:**
```
Input: [[1,2], [3], [3], []] 
Output: [[0,1,3],[0,2,3]] 
Explanation: The graph looks like this:
0--->1
|    |
v    v
2--->3
There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
```

**Note:**

* The number of nodes in the `graph` will be in the range `[2, 15]`.
* You can print different paths in any order, but you should keep the order of nodes inside one path.

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 144 ms
Memory Usage: 15.5 MB
```
```python
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        N = len(graph)
        ans = []

        def dfs(node, path):
            if node == N-1:
                ans.append(path)
            else:
                for nei in graph[node]:
                    dfs(nei, path+[nei])
        
        dfs(0, [0])
        return ans
```

**Solution 2: (BFS)**
```
Runtime: 124 ms
Memory Usage: 15.3 MB
```
```python
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ret = []
        q = collections.deque()
        q.append((0, [0]))
        while q:
            node, path = q.popleft()
            if node == len(graph) - 1:
                ret.append(path)
            for i in range(len(graph[node])):
                q.append((graph[node][i], path + [graph[node][i]]))
        return ret
```

**Solution 3: (DFS)**
```
Runtime: 48 ms
Memory Usage: 15.2 MB
```
```c++
class Solution {
public:
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        vector<vector<int>> res;
        vector<int> path;
        dfs(graph, 0, res, path);
        return res;
    }
    void dfs(vector<vector<int>>&graph, int node, vector<vector<int>>& res, vector<int> path)
    {
        path.push_back(node);
        if(node == graph.size()-1)
            res.push_back(path);
        for(int i=0; i<graph[node].size(); i++)
            dfs(graph, graph[node][i], res, path);
    }  
};
```

**Solution 4: (BFS)**
```
Runtime: 61 ms
Memory Usage: 16.7 MB
```
```c++
class Solution {
public:
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        vector<vector<int>> allPaths;
        
        queue<vector<int>> q;
        q.push({0});
        while(!q.empty()){
            vector<int> currPath = q.front();
            q.pop();
            int lastNode = currPath.back();
            if(lastNode==graph.size()-1) allPaths.push_back(currPath);
            for(auto u:graph[lastNode]){
                currPath.push_back(u);
                q.push(currPath);
                currPath.pop_back();
            }
        }
        return allPaths;
    }
};
```
