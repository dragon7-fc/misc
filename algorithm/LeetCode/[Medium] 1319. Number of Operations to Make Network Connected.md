1319. Number of Operations to Make Network Connected

There are `n` computers numbered from `0` to `n-1` connected by ethernet cables connections forming a network where `connections[i] = [a, b]` represents a connection between computers `a` and `b`. Any computer can reach any other computer directly or indirectly through the network.

Given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected. Return the minimum number of times you need to do this in order to make all the computers connected. If it's not possible, return `-1`. 

 

**Example 1:**

![1319_sample_1_1677.png](img/1319_sample_1_1677.png)
```
Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
```

**Example 2:**

![1319_sample_2_1677.png](img/1319_sample_2_1677.png)
```
Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2
```

**Example 3:**
```
Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
Explanation: There are not enough cables.
```

**Example 4:**
```
Input: n = 5, connections = [[0,1],[0,2],[3,4],[2,3]]
Output: 0
```

**Constraints:**

* `1 <= n <= 10^5`
* `1 <= connections.length <= min(n*(n-1)/2, 10^5)`
* `connections[i].length == 2`
* `0 <= connections[i][0], connections[i][1] < n`
* `connections[i][0] != connections[i][1]`
* There are no repeated connections.
* No two computers are connected by more than one cable.

# Submissions
---
**Solution 1: (DFS)**

**Explanation**

We need at least `n - 1` cables to connect all nodes (like a tree).
If `connections.size() < n - 1`, we can directly return `-1`.

One trick is that, if we have enough cables,
we don't need to worry about where we can get the cable from.

We only need to count the number of connected networks.
To connect two unconneccted networks, we need to set one cable.

The number of operations we need = the number of **connected networks - 1**

**Complexity**

* Time O(connections)
* Space O(n)
```
Runtime: 524 ms
Memory Usage: 37.4 MB
```
```python
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1: return -1
        g = [set() for i in range(n)]
        for i, j in connections:
            g[i].add(j)
            g[j].add(i)
        seen = [False] * n
        num_connected_components = 0

        def dfs(i):
            seen[i] = True
            for j in g[i]:
                if not seen[j]:
                    dfs(j)
        
        for i in range(n):
            if not seen[i]:
                num_connected_components += 1
                dfs(i)
        
        return num_connected_components - 1
```

**Solution 2: (BFS)**
```
Runtime: 536 ms
Memory Usage: 34.3 MB
```
```python
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1: return -1
        g = [set() for i in range(n)]
        for i, j in connections:
            g[i].add(j)
            g[j].add(i)
        seen = [False] * n
        num_connected_components = 0

        for i in range(n):
            if not seen[i]:
                num_connected_components += 1
                q = collections.deque([i])
                seen[i] = True
                while q:
                    el = q.popleft()
                    for nei in g[el]:
                        if not seen[nei]:
                            q.append(nei)
                            seen[nei] = True
        
        return num_connected_components - 1
```

**Solution 3: (Union Find)**
```
Runtime: 492 ms
Memory Usage: 32.9 MB
```
```python
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        def find(x):
            while x != nodes[x]:
                nodes[x] = nodes[nodes[x]]
                x = nodes[x]
            return x
        
        nodes = [i for i in range(n)]
        used = 0
        free = 0
        
        for x, y in connections:
            x = find(x)
            y = find(y)
            
            if x != y:
                used += 1
                nodes[x] = y
            else:
                free += 1
        
        disconected = n - 1 - used
        
        if disconected > free:
            return -1
        
        return disconected
```

**Solution 4: (DFS)**
```
Runtime: 133 ms
Memory: 51.6 MB
```
```c++
class Solution {
    void dfs(int v, vector<bool> &seen, vector<vector<int>> &g) {
        seen[v] = true;
        for (int &nv: g[v]) {
            if (!seen[nv]) {
                dfs(nv, seen, g);
            }
        }
    }
public:
    int makeConnected(int n, vector<vector<int>>& connections) {
        if (connections.size() < n-1) {
            return -1;
        }
        vector<vector<int>> g(n);
        for (int i = 0; i < connections.size(); i ++) {
            g[connections[i][0]].push_back(connections[i][1]);
            g[connections[i][1]].push_back(connections[i][0]);
        }
        vector<bool> seen(n);
        int ans = 0;
        for (int i = 0; i < n; i ++) {
            if (!seen[i]) {
                dfs(i, seen, g);
                ans += 1;
            }
        }
        return ans - 1;
    }
};
```
