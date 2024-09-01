947. Most Stones Removed with Same Row or Column

On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point may have at most one stone.

Now, a move consists of removing a stone that shares a column or row with another stone on the grid.

What is the largest possible number of moves we can make?

 

**Example 1:**
```
Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
```

**Example 2:**
```
Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
```

**Example 3:**
```
Input: stones = [[0,0]]
Output: 0
```

**Note:**

* `1 <= stones.length <= 1000`
* `0 <= stones[i][j] < 10000`

# Solution
---
## Approach 1: Depth-First Search
**Intuition**

Let's say two stones are connected by an edge if they share a row or column, and define a connected component in the usual way for graphs: a subset of stones so that there doesn't exist an edge from a stone in the subset to a stone not in the subset. For convenience, we refer to a component as meaning a connected component.

The main insight is that we can always make moves that reduce the number of stones in each component to 1.

Firstly, every stone belongs to exactly one component, and moves in one component do not affect another component.

Now, consider a spanning tree of our component. We can make moves repeatedly from the leaves of this tree until there is one stone left.

**Algorithm**

To count connected components of the above graph, we will use depth-first search.

For every stone not yet visited, we will visit it and any stone in the same connected component. Our depth-first search traverses each node in the component.

For each component, the answer changes by ``-1 + component.size`.

```python
class Solution(object):
    def removeStones(self, stones):
        graph = collections.defaultdict(list)
        for i, x in enumerate(stones):
            for j in xrange(i):
                y = stones[j]
                if x[0]==y[0] or x[1]==y[1]:
                    graph[i].append(j)
                    graph[j].append(i)

        N = len(stones)
        ans = 0

        seen = [False] * N
        for i in xrange(N):
            if not seen[i]:
                stack = [i]
                seen[i] = True
                while stack:
                    ans += 1
                    node = stack.pop()
                    for nei in graph[node]:
                        if not seen[nei]:
                            stack.append(nei)
                            seen[nei] = True
                ans -= 1
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N^2)$, where $N$ is the length of `stones`.

* Space Complexity: $O(N^2)$.

## Approach 2: Union-Find
**Intuition**

As in Approach 1, we will need to consider components of an underlying graph. A "Disjoint Set Union" (DSU) data structure is ideal for this.

We will skip the explanation of how a DSU structure is implemented. Please refer to https://leetcode.com/problems/redundant-connection/solution/ for a tutorial on DSU.

**Algorithm**

Let's connect row `i` to column `j`, which will be represented by `j+10000`. The answer is the number of components after making all the connections.

Note that for brevity, our `DSU` implementation does not use union-by-rank. This makes the asymptotic time complexity larger.

```python
class DSU:
    def __init__(self, N):
        self.p = range(N)

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr

class Solution(object):
    def removeStones(self, stones):
        N = len(stones)
        dsu = DSU(20000)
        for x, y in stones:
            dsu.union(x, y + 10000)

        return N - len({dsu.find(x) for x, y in stones})
```

**Complexity Analysis**

* Time Complexity: $O(N \log N)$, where $N$ is the length of `stones`. (If we used union-by-rank, this can be $O(N * \alpha(N))$), where $\alpha$ is the Inverse-Ackermann function.)

* Space Complexity: $O(N)$.

# Submissions
---
**Solution: (DFS, Stack)**
```
Runtime: 1616 ms
Memory Usage: 13.2 MB
```
```python
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for i, x in enumerate(stones):
            for j in range(i):
                y = stones[j]
                if x[0]==y[0] or x[1]==y[1]:
                    graph[i].append(j)
                    graph[j].append(i)

        N = len(stones)
        ans = 0

        seen = [False] * N
        for i in range(N):
            if not seen[i]:
                stack = [i]
                seen[i] = True
                while stack:
                    ans += 1
                    node = stack.pop()
                    for nei in graph[node]:
                        if not seen[nei]:
                            stack.append(nei)
                            seen[nei] = True
                ans -= 1
        return ans
```
**Solution: (DFS)**
```
Runtime: 1636 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for i, x in enumerate(stones):
            for j in range(i):
                y = stones[j]
                if x[0]==y[0] or x[1]==y[1]:
                    graph[i].append(j)
                    graph[j].append(i)

        N = len(stones)
        ans = 0

        seen = [False] * N
        def dfs(node):
            nonlocal ans
            if not seen[node]:
                seen[node] = True
                ans += 1
                for nei in graph[node]:
                    dfs(nei)

        for i in range(N):
            if not seen[i]:
                dfs(i)
                ans -= 1
        return ans
```

**Solution: (Union Find)**
```
Runtime: 192 ms
Memory Usage: 13.6 MB
```
```python
class DSU:
    def __init__(self, N):
        self.p = [_ for _ in range(N)]

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr
        
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        N = len(stones)
        dsu = DSU(20000)
        for x, y in stones:
            dsu.union(x, y + 10000)

        return N - len({dsu.find(x) for x, y in stones})
```

**Solution 1: (DFS)**
```
Runtime: 384 ms
Memory: 17.4 MB
```
```python
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        N = len(stones)
        seen = set()
        xs = collections.defaultdict(list)
        ys = collections.defaultdict(list)
        for x, y in stones:
            xs[x] += [(x, y)]
            ys[y] += [(x, y)]

        def dfs(x, y):
            seen.add((x, y))
            for nx, ny in xs[x] + ys[y]:
                if (nx, ny) not in seen:
                    dfs(nx, ny)
        
        comp = 0
        for x, y in stones:
            if (x, y) not in seen:
                comp += 1
                dfs(x, y)

        return N - comp
```

**Solution 2: (DFS)**
```
Runtime: 194 ms
Memory: 16.3 MB
```
```c++
class Solution {
    // Return true if stone a and b shares row or column
    int shareSameRowOrColumn(vector<int>& a, vector<int>& b) {
        return a[0] == b[0] || a[1] == b[1];
    }
    
    void dfs(vector<vector<int>>& stones, vector<int> adj[], vector<int>& visited, int src) {
        // Mark the stone as visited
        visited[src] = 1;
        
        // Iterate over the adjacent, and iterate over it if not visited yet
        for (int adjacent : adj[src]) {
            if (visited[adjacent] == 0) {
                dfs(stones, adj, visited, adjacent);
            }
        }
    }
public:
    int removeStones(vector<vector<int>>& stones) {
        // Adjacency list to store edges
        vector<int> adj[stones.size()];
        for (int i = 0; i < stones.size(); i++) {
            for (int j = i + 1; j < stones.size(); j++) {
                if (shareSameRowOrColumn(stones[i], stones[j])) {
                    adj[i].push_back(j);
                    adj[j].push_back(i);
                }
            }
        }
        
        // Array to mark visited stones
        vector<int> visited(stones.size(), 0);
        // Counter for connected components
        int componentCount = 0;
        for (int i = 0; i < stones.size(); i++) {
            if (visited[i] == 0) {
                // If the stone is not visited yet,
                // Start the DFS and increment the counter
                componentCount++;
                dfs(stones, adj, visited, i);
            }
        }
        
        // Return the maximum stone that can be removed
        return stones.size() - componentCount;
    }
};
```

**Solution 3: (Depth First Search)**
```
Runtime: 94 ms
Memory: 20.53 MB
```
```c++
class Solution {
    // DFS to visit all stones in a connected component
    void depthFirstSearch(vector<vector<int>>& adjacencyList,
                          vector<bool>& visited, int stone) {
        visited[stone] = true;

        for (int neighbor : adjacencyList[stone]) {
            if (!visited[neighbor]) {
                depthFirstSearch(adjacencyList, visited, neighbor);
            }
        }
    }
public:
    int removeStones(vector<vector<int>>& stones) {
        int n = stones.size();

        // Adjacency list to store graph connections
        vector<vector<int>> adjacencyList(n);

        // Build the graph: Connect stones that share the same row or column
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (stones[i][0] == stones[j][0] ||
                    stones[i][1] == stones[j][1]) {
                    adjacencyList[i].push_back(j);
                    adjacencyList[j].push_back(i);
                }
            }
        }

        int numOfConnectedComponents = 0;
        vector<bool> visited(n, false);

        // Traverse all stones using DFS to count connected components
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                depthFirstSearch(adjacencyList, visited, i);
                numOfConnectedComponents++;
            }
        }

        // Maximum stones that can be removed is total stones minus number of
        // connected components
        return n - numOfConnectedComponents;
    }
};
```

**Solution 4: (Disjoint Set Union)**
```
Runtime: 68 ms
Memory: 18.12 MB
```
```c++
class Solution {
    // Union-Find data structure for tracking connected components
    class UnionFind {
    public:
        vector<int> parent;  // Array to track the parent of each node
        int count;           // Number of connected components

        UnionFind(int n) {
            parent.resize(n, -1);  // Initialize all nodes as their own parent
            count = n;  // Initially, each stone is its own connected component
        }

        // Find the root of a node with path compression
        int find(int node) {
            if (parent[node] == -1) {
                return node;
            }
            return parent[node] = find(parent[node]);
        }

        // Union two nodes, reducing the number of connected components
        void unionNodes(int n1, int n2) {
            int root1 = find(n1);
            int root2 = find(n2);

            if (root1 == root2) {
                return;  // If they are already in the same component, do
                         // nothing
            }

            // Merge the components and reduce the count of connected components
            count--;
            parent[root1] = root2;
        }
    };
public:
    int removeStones(vector<vector<int>>& stones) {
        int n = stones.size();
        UnionFind uf(n);

        // Populate uf by connecting stones that share the same row or column
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (stones[i][0] == stones[j][0] ||
                    stones[i][1] == stones[j][1]) {
                    uf.unionNodes(i, j);
                }
            }
        }

        return n - uf.count;
    }
};
```
