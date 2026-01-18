2204. Distance to a Cycle in Undirected Graph

You are given a positive integer `n` representing the number of nodes in a **connected undirected graph** containing exactly one cycle. The nodes are numbered from `0` to `n - 1` (**inclusive**).

You are also given a 2D integer array `edges`, where `edges[i] = [node1i, node2i]` denotes that there is a **bidirectional** edge connecting `node1i` and `node2i` in the graph.

The distance between two nodes `a` and `b` is defined to be the **minimum** number of edges that are needed to go from `a` to `b`.

Return an integer array `answer` of size `n`, where `answer[i]` is the minimum distance between the `i`th node and any node in the cycle.

 

**Example 1:**

![2204_image-20220315154238-1.png](img/2204_image-20220315154238-1.png)
```
Input: n = 7, edges = [[1,2],[2,4],[4,3],[3,1],[0,1],[5,2],[6,5]]
Output: [1,0,0,0,0,1,2]
Explanation:
The nodes 1, 2, 3, and 4 form the cycle.
The distance from 0 to 1 is 1.
The distance from 1 to 1 is 0.
The distance from 2 to 2 is 0.
The distance from 3 to 3 is 0.
The distance from 4 to 4 is 0.
The distance from 5 to 2 is 1.
The distance from 6 to 2 is 2.
```

**Example 2:**

![2204_image-20220315154634-1.png](img/2204_image-20220315154634-1.png)
```
Input: n = 9, edges = [[0,1],[1,2],[0,2],[2,6],[6,7],[6,8],[0,3],[3,4],[3,5]]
Output: [0,0,0,1,2,2,1,2,2]
Explanation:
The nodes 0, 1, and 2 form the cycle.
The distance from 0 to 0 is 0.
The distance from 1 to 1 is 0.
The distance from 2 to 2 is 0.
The distance from 3 to 1 is 1.
The distance from 4 to 1 is 2.
The distance from 5 to 1 is 2.
The distance from 6 to 2 is 1.
The distance from 7 to 2 is 2.
The distance from 8 to 2 is 2.
```

**Constraints:**

* `3 <= n <= 10^5`
* `edges.length == n`
* `edges[i].length == 2`
* `0 <= node1i, node2i <= n - 1`
* `node1i != node2i`
* The graph is connected.
* The graph has exactly one cycle.
* There is at most one edge between any pair of vertices.

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 116 ms, Beats 54.05%
Memory: 125.00 MB, Beats 48.65%
```
```c++
class Solution {
    // DFS to detect cycle nodes and mark them in `isInCycle`
    bool detectCycleNodes(int currentNode, vector<vector<int>> &adjacencyList,
                          vector<bool> &isInCycle, vector<bool> &visited,
                          vector<int> &parent) {
        visited[currentNode] = true;  // Mark current node as visited
        for (auto neighbor : adjacencyList[currentNode]) {
            if (!visited[neighbor]) {
                parent[neighbor] = currentNode;  // Set parent for backtracking
                if (detectCycleNodes(neighbor, adjacencyList, isInCycle,
                                     visited, parent))
                    return true;  // Return true if cycle detected
            } else if (parent[currentNode] != neighbor) {  // Cycle detected
                isInCycle[neighbor] = true;  // Mark the start of the cycle
                int tempNode = currentNode;
                // Backtrack to mark all nodes in the cycle
                while (tempNode != neighbor) {
                    isInCycle[tempNode] = true;
                    tempNode = parent[tempNode];
                }
                return true;
            }
        }
        return false;  // No cycle found in this path
    }

    // DFS to calculate distances from cycle nodes
    void calculateDistances(int currentNode, int currentDistance,
                            vector<vector<int>> &adjacencyList,
                            vector<int> &distances, vector<bool> &visited,
                            vector<bool> &isInCycle) {
        distances[currentNode] =
            currentDistance;          // Set distance for current node
        visited[currentNode] = true;  // Mark node as visited
        for (auto neighbor : adjacencyList[currentNode]) {
            if (visited[neighbor]) continue;  // Skip if already visited
            int newDistance = isInCycle[neighbor]
                                  ? 0
                                  : currentDistance + 1;  // Reset if on cycle
            calculateDistances(neighbor, newDistance, adjacencyList, distances,
                               visited, isInCycle);
        }
    }
public:
    vector<int> distanceToCycle(int n, vector<vector<int>>& edges) {
        vector<bool> isInCycle(n, false), visited(n, false);
        vector<int> parent(n), distances(n);
        vector<vector<int>> adjacencyList(n);

        // Build adjacency list for the graph
        for (auto edge : edges) {
            adjacencyList[edge[0]].push_back(edge[1]);
            adjacencyList[edge[1]].push_back(edge[0]);
        }

        // Detect and mark cycle nodes
        detectCycleNodes(0, adjacencyList, isInCycle, visited, parent);

        // Reset visited array before distance calculation
        fill(visited.begin(), visited.end(), false);

        // Calculate distances starting from any cycle node
        for (int i = 0; i < n; i++) {
            if (isInCycle[i]) {
                calculateDistances(i, 0, adjacencyList, distances, visited,
                                   isInCycle);
                break;  // Only need to start from one cycle node
            }
        }
        return distances;
    }
};
```

**Solution 2: (Layer By Layer + Multisource BFS)**
```
Runtime: 119 ms, Beats 54.05%
Memory: 112.96 MB, Beats 78.38%
```
```c++
class Solution {
public:
    vector<int> distanceToCycle(int n, vector<vector<int>>& edges) {
        vector<bool> isInCycle(n, true),
            visited(n, false);  // 'isInCycle' is initially true for all nodes
        vector<int> degree(n, 0), distances(n);
        vector<vector<int>> adjacencyList(n, vector<int>(0));

        // Build the adjacency list and calculate node degrees
        for (auto edge : edges) {
            adjacencyList[edge[0]].push_back(edge[1]);
            adjacencyList[edge[1]].push_back(edge[0]);
            degree[edge[0]]++;
            degree[edge[1]]++;
        }

        queue<int> nodeQueue;

        // Start by adding all leaf nodes (degree 1) to the queue
        for (int i = 0; i < n; i++) {
            if (degree[i] == 1) {
                nodeQueue.push(i);
            }
        }

        // Perform BFS to remove nodes with degree 1, progressively reducing the
        // graph
        while (!nodeQueue.empty()) {
            int currentNode = nodeQueue.front();
            nodeQueue.pop();
            isInCycle[currentNode] =
                false;  // Mark the node as not in the cycle

            // Update the degree of neighbors and add them to the queue if their
            // degree becomes 1
            for (auto neighbor : adjacencyList[currentNode]) {
                degree[neighbor]--;
                if (degree[neighbor] == 1) {
                    nodeQueue.push(neighbor);
                }
            }
        }

        // Add all cycle nodes to the queue and mark them as visited
        for (int currentNode = 0; currentNode < n; currentNode++) {
            if (isInCycle[currentNode]) {
                nodeQueue.push(currentNode);
                visited[currentNode] = true;
            }
        }

        // BFS to calculate distances from cycle nodes
        int currentDistance = 0;
        while (!nodeQueue.empty()) {
            int queueSize = nodeQueue.size();  // Track number of nodes to
                                               // process at this distance level
            for (int i = 0; i < queueSize; i++) {
                int currentNode = nodeQueue.front();
                nodeQueue.pop();

                distances[currentNode] =
                    currentDistance;  // Set the distance for the current node

                // Add unvisited neighbors to the queue
                for (auto neighbor : adjacencyList[currentNode]) {
                    if (visited[neighbor]) continue;
                    nodeQueue.push(neighbor);
                    visited[neighbor] = true;
                }
            }
            currentDistance++;  // Increment distance after processing all nodes
                                // at the current level
        }

        return distances;
    }
};
```

**Solution 3: (Topological Sort, BFS, cycle detection)**
```
Runtime: 73 ms, Beats 94.59%
Memory: 105.14 MB, Beats 83.78%
```
```c++
class Solution {
public:
    vector<int> distanceToCycle(int n, vector<vector<int>>& edges) {
        int i;
        vector<vector<int>> g(n);
        vector<int> deg(n);
        vector<bool> visited(n);
        for (auto &e: edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
            deg[e[0]] += 1;
            deg[e[1]] += 1;
        }
        queue<int> q;
        for (i = 0; i < n; i ++) {
            if (deg[i] == 1) {
                q.push(i);
                visited[i] = true;
            }
        }
        while (q.size()) {
            auto u = q.front();
            q.pop();
            for (auto v: g[u]) {
                deg[v] -= 1;
                if (deg[v] == 1) {
                    q.push(v);
                    visited[v] = true;
                }
            }
        }
        vector<int> ans(n);
        queue<array<int, 2>> q2;
        for (i = 0; i < n; i ++) {
            if (!visited[i]) {
                ans[i] = 0;
                q2.push({i, 0});
            }
        }
        while (q2.size()) {
            auto [u, k] = q2.front();
            q2.pop();
            for (auto v: g[u]) {
                if (visited[v]) {
                    ans[v] = k + 1;
                    q2.push({v, k + 1});
                    visited[v] = false;
                }
            }
        }
        return ans;
    }
};
```
