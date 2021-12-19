785. Is Graph Bipartite?

Given an undirected `graph`, return `true` if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: `graph[i]` is a list of indexes `j` for which the edge between nodes `i` and `j` exists.  Each node is an integer between `0` and `graph.length - 1`.  There are no self edges or parallel edges: `graph[i]` does not contain `i`, and it doesn't contain any element twice.

**Example 1:**
```
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Explanation: 
The graph looks like this:
0----1
|    |
|    |
3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.
```

**Example 2:**
```
Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
Output: false
Explanation: 
The graph looks like this:
0----1
| \  |
|  \ |
3----2
We cannot find a way to divide the set of nodes into two independent subsets.
```

**Note:**

* graph will have length in range `[1, 100]`.
* `graph[i]` will contain integers in range `[0, graph.length - 1]`.
* `graph[i]` will not contain i or duplicate values.
* The graph is undirected: if any element `j` is in `graph[i]`, then `i` will be in `graph[j]`.

# Submissions
---
**Solution 1: (DFS, Graph)**
```
Runtime: 184 ms
Memory Usage: 13 MB
```
```python
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colored = collections.defaultdict(int)

        #
        # Color a node with white (1) and its adjacent nodes with black (-1)
        # If any node and its adjacent nodes have the same color, return False
        #

        for v, _ in enumerate(graph):
            stack = []
            if v not in colored:
                stack.append(v)

            while stack:
                node = stack.pop()

                if node not in colored:
                    colored[node] = 1  # White

                for nei in graph[node]:
                    if nei in colored:
                        if colored[nei] == colored[node]:
                            return False
                    else:  # Adj nodes to be color inverted.
                        colored[nei] = -colored[node]  
                        stack.append(nei)

        return True
```

**Solution 2: (DFS, Graph)**
```
Runtime: 180 ms
Memory Usage: 13.1 MB
```
```python
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
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
            
        for v, _ in enumerate(graph):
            if v not in colored:
                if not dfs(v, 1):
                    return False
        return True
```

**Solution 3: (BFS, Graph)**
```
Runtime: 180 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = {}

        for from_node in range(len(graph)):
            if from_node in colors:
                continue
            queue = collections.deque([from_node])
            colors[from_node] = 1 # 1 is just starting color, could be -1 also

            while queue:
                from_node = queue.popleft()
                for to_node in graph[from_node]:
                    if to_node in colors:
                        if colors[to_node] == colors[from_node]:
                            return False
                    else:
                        queue.append(to_node)
                        colors[to_node] = colors[from_node] * -1

        return True
```

**Solution 4: (DFS)**
```
Runtime: 24 ms
Memory Usage: 7.1 MB
```
```c
bool dfs(int u, int c, int *cs, int**g, int gSize, int *gColSize) {
    int v;
    cs[u] = c;
    for (int i = 0; i < gColSize[u]; i ++) {
        v = g[u][i];
        if (cs[v] == c)
            return false;
        else if (cs[v] == 0) {
            if (!dfs(v, -c, cs, g, gSize, gColSize))
                return false;
        }
    }
    return true;
}

bool isBipartite(int** graph, int graphSize, int* graphColSize){
    int *colors = calloc(1, graphSize*sizeof(int));
    for (int i = 0; i < graphSize; i ++) {
        if (colors[i] == 0) {
            if (!dfs(i, 1, colors, graph, graphSize, graphColSize))
                return false;
        }
    }
    return true;
}
```
