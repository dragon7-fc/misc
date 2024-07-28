1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance

There are `n` cities numbered from `0` to `n-1`. Given the array `edges` where `edges[i] = [fromi, toi, weighti]` represents a bidirectional and weighted edge between cities `fromi` and `toi`, and given the integer `distanceThreshold`.

Return the city with the smallest number of cities that are reachable through some path and whose distance is **at most** `distanceThreshold`, If there are multiple such cities, return the city with the greatest number.

Notice that the distance of a path connecting cities `i` and `j` is equal to the sum of the edges' weights along that path.

**Example 1:**

![1334_find_the_city_01.png](img/1334_find_the_city_01.png)
```
Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
Output: 3
Explanation: The figure above describes the graph. 
The neighboring cities at a distanceThreshold = 4 for each city are:
City 0 -> [City 1, City 2] 
City 1 -> [City 0, City 2, City 3] 
City 2 -> [City 0, City 1, City 3] 
City 3 -> [City 1, City 2] 
Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we have to return city 3 since it has the greatest number.
```

**Example 2:**

![1334_find_the_city_02.png](img/1334_find_the_city_02.png)
```
Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
Output: 0
Explanation: The figure above describes the graph. 
The neighboring cities at a distanceThreshold = 2 for each city are:
City 0 -> [City 1] 
City 1 -> [City 0, City 4] 
City 2 -> [City 3, City 4] 
City 3 -> [City 2, City 4]
City 4 -> [City 1, City 2, City 3] 
The city 0 has 1 neighboring city at a distanceThreshold = 2.
``` 

**Constraints:**

* `2 <= n <= 100`
* `1 <= edges.length <= n * (n - 1) / 2`
* `edges[i].length == 3`
* `0 <= fromi < toi < n`
* `1 <= weighti, distanceThreshold <= 10^4`
* All pairs `(fromi, toi)` are distinct.

# Submissions
---
**Solution 1: (DP, Floyd Warshall's shortest path)**

**Explanation**

Find the minium distance between two cities.


**Complexity**

* Time O(N^3)
* Space O(N^2)

```
Runtime: 980 ms
Memory Usage: 13.6 MB
```
```python
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dis = [[float('inf')] * n for _ in range(n)]
        for i, j, w in edges:
            dis[i][j] = dis[j][i] = w
        for i in range(n):
            dis[i][i] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
        res = {sum(d <= distanceThreshold for d in dis[i]): i for i in range(n)}
        return res[min(res)]
```

**Example 2: (DFS, Graph)**
```
Runtime: 2608 ms
Memory Usage: 13.6 MB
```
```python
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        def dfs(i, d):
            visited[i] = d 
            for nei, w in graph[i]:
                if w > d:
                    continue
                # note that when node is visited, if the distance residue is greater than the previous one, 
                # we should do the dfs again with this greater distance residue 
                if nei not in visited or (d-w > visited[nei]):
                    dfs(nei, d-w)
            return 
        res = []
        for i in range(n):
            visited = {}
            dfs(i, distanceThreshold)
            res.append( len(visited))
        minRes = min(res)
        for i in reversed(range(n)):
            if res[i] == minRes:
                return i

```

**Solution 3: (Dijkstra, Graph)**
```
Runtime: 1720 ms
Memory Usage: 13.7 MB
```
```python
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        g = collections.defaultdict(dict)
        for u, v, w in edges:
            g[u][v] = g[v][u] = w
        def bfs(s, distanceThreshold):
            visited = [False] * n
            dist = [float('inf')] * n
            hq = [(0, s)]
            visited[s] = True
            dist[s] = 0
            while hq:
                d, s = heapq.heappop(hq)
                if d > distanceThreshold: break
                dist[s] = d
                visited[s] = True
                for t in g[s]:
                    if not visited[t]:
                        heapq.heappush(hq, (d + g[s][t], t))
            return len([d for d in dist if d <= distanceThreshold])
        res = 0
        count = n
        for i in range(n):
            c = bfs(i, distanceThreshold)
            if c <= count:
                res = i
                count = c
        return res
```


**Solution 4: (Dijkstra Algorithm, O(N^3 log(N)))**
```
Runtime: 40 ms
Memory: 20.17 MB
```
```c++
lass Solution {
     // Dijkstra's algorithm to find shortest paths from a source city
    void dijkstra(int n, const vector<vector<pair<int, int>>>& adjacencyList,
                  vector<int>& shortestPathDistances, int source) {
        // Priority queue to process nodes with the smallest distance first
        priority_queue<pair<int, int>, vector<pair<int, int>>,
                       greater<pair<int, int>>>
            priorityQueue;
        priorityQueue.emplace(0, source);
        fill(shortestPathDistances.begin(), shortestPathDistances.end(),
             INT_MAX);
        shortestPathDistances[source] = 0;  // Distance to source itself is zero

        // Process nodes in priority order
        while (!priorityQueue.empty()) {
            auto [currentDistance, currentCity] = priorityQueue.top();
            priorityQueue.pop();
            if (currentDistance > shortestPathDistances[currentCity]) {
                continue;
            }

            // Update distances to neighboring cities
            for (const auto& [neighborCity, edgeWeight] :
                 adjacencyList[currentCity]) {
                if (shortestPathDistances[neighborCity] >
                    currentDistance + edgeWeight) {
                    shortestPathDistances[neighborCity] =
                        currentDistance + edgeWeight;
                    priorityQueue.emplace(shortestPathDistances[neighborCity],
                                          neighborCity);
                }
            }
        }
    }

    // Determine the city with the fewest number of reachable cities within the
    // distance threshold
    int getCityWithFewestReachable(
        int n, const vector<vector<int>>& shortestPathMatrix,
        int distanceThreshold) {
        int cityWithFewestReachable = -1;
        int fewestReachableCount = n;

        // Count number of cities reachable within the distance threshold for
        // each city
        for (int i = 0; i < n; i++) {
            int reachableCount = 0;
            for (int j = 0; j < n; j++) {
                if (i == j) {
                    continue;
                }  // Skip self
                if (shortestPathMatrix[i][j] <= distanceThreshold) {
                    reachableCount++;
                }
            }
            // Update the city with the fewest reachable cities
            if (reachableCount <= fewestReachableCount) {
                fewestReachableCount = reachableCount;
                cityWithFewestReachable = i;
            }
        }
        return cityWithFewestReachable;
    }
public:
    int findTheCity(int n, vector<vector<int>>& edges, int distanceThreshold) {
        // Adjacency list to store the graph
        vector<vector<pair<int, int>>> adjacencyList(n);
        // Matrix to store shortest path distances from each city
        vector<vector<int>> shortestPathMatrix(n, vector<int>(n, INT_MAX));

        // Initialize adjacency list and shortest path matrix
        for (int i = 0; i < n; i++) {
            shortestPathMatrix[i][i] = 0;  // Distance to itself is zero
        }

        // Populate the adjacency list with edges
        for (const auto& edge : edges) {
            int start = edge[0];
            int end = edge[1];
            int weight = edge[2];
            adjacencyList[start].emplace_back(end, weight);
            adjacencyList[end].emplace_back(start,
                                            weight);  // For undirected graph
        }

        // Compute shortest paths from each city using Dijkstra's algorithm
        for (int i = 0; i < n; i++) {
            dijkstra(n, adjacencyList, shortestPathMatrix[i], i);
        }

        // Find the city with the fewest number of reachable cities within the
        // distance threshold
        return getCityWithFewestReachable(n, shortestPathMatrix,
                                          distanceThreshold);
    }
};
```

**Solution 5: (Bellman-Ford Algorithm, O(N^4))**
```
Runtime: 277 ms
Memory: 15.61 MB
```
```c++
class Solution {
    // Bellman-Ford algorithm to find shortest paths from a source city
    void bellmanFord(int n, const vector<vector<int>>& edges,
                     vector<int>& shortestPathDistances, int source) {
        // Initialize distances from the source
        fill(shortestPathDistances.begin(), shortestPathDistances.end(), INF);
        shortestPathDistances[source] = 0;  // Distance to source itself is zero

        // Relax edges up to n-1 times
        for (int i = 1; i < n; i++) {
            for (const auto& edge : edges) {
                int start = edge[0];
                int end = edge[1];
                int weight = edge[2];
                // Update shortest path distances if a shorter path is found
                if (shortestPathDistances[start] != INF &&
                    shortestPathDistances[start] + weight <
                        shortestPathDistances[end]) {
                    shortestPathDistances[end] =
                        shortestPathDistances[start] + weight;
                }
                if (shortestPathDistances[end] != INF &&
                    shortestPathDistances[end] + weight <
                        shortestPathDistances[start]) {
                    shortestPathDistances[start] =
                        shortestPathDistances[end] + weight;
                }
            }
        }
    }

    // Determine the city with the fewest number of reachable cities within the
    // distance threshold
    int getCityWithFewestReachable(
        int n, const vector<vector<int>>& shortestPathMatrix,
        int distanceThreshold) {
        int cityWithFewestReachable = -1;
        int fewestReachableCount = n;

        // Count number of cities reachable within the distance threshold for
        // each city
        for (int i = 0; i < n; i++) {
            int reachableCount = 0;
            for (int j = 0; j < n; j++) {
                if (i == j) {
                    continue;
                }  // Skip self
                if (shortestPathMatrix[i][j] <= distanceThreshold) {
                    reachableCount++;
                }
            }
            // Update the city with the fewest reachable cities
            if (reachableCount <= fewestReachableCount) {
                fewestReachableCount = reachableCount;
                cityWithFewestReachable = i;
            }
        }
        return cityWithFewestReachable;
    }
public:
    // Large value to represent infinity
    const int INF = 1e9 + 7;
    int findTheCity(int n, vector<vector<int>>& edges, int distanceThreshold) {
        // Matrix to store shortest path distances from each city
        vector<vector<int>> shortestPathMatrix(n, vector<int>(n, INF));

        // Initialize shortest path matrix
        for (int i = 0; i < n; i++) {
            shortestPathMatrix[i][i] = 0;  // Distance to itself is zero
        }

        // Populate the matrix with initial edge weights
        for (const auto& edge : edges) {
            int start = edge[0];
            int end = edge[1];
            int weight = edge[2];
            shortestPathMatrix[start][end] = weight;
            shortestPathMatrix[end][start] = weight;  // For undirected graph
        }

        // Compute shortest paths from each city using Bellman-Ford algorithm
        for (int i = 0; i < n; i++) {
            bellmanFord(n, edges, shortestPathMatrix[i], i);
        }

        // Find the city with the fewest number of reachable cities within the
        // distance threshold
        return getCityWithFewestReachable(n, shortestPathMatrix,
                                          distanceThreshold);
    }
};
```

**Solution 6: (Shortest Path First Algorithm (SPFA), O(N^4))**
```
Runtime: 42 ms
Memory: 18.78 MB
```
```
class Solution {
    // SPFA algorithm to find shortest paths from a source city
    void spfa(int n, const vector<vector<pair<int, int>>>& adjacencyList,
              vector<int>& shortestPathDistances, int source) {
        // Queue to process nodes with updated shortest path distances
        deque<int> queue;
        vector<int> updateCount(n, 0);
        queue.push_back(source);
        fill(shortestPathDistances.begin(), shortestPathDistances.end(),
             INT_MAX);
        shortestPathDistances[source] = 0;  // Distance to source itself is zero

        // Process nodes in queue
        while (!queue.empty()) {
            int currentCity = queue.front();
            queue.pop_front();
            for (const auto& [neighborCity, edgeWeight] :
                 adjacencyList[currentCity]) {
                if (shortestPathDistances[neighborCity] >
                    shortestPathDistances[currentCity] + edgeWeight) {
                    shortestPathDistances[neighborCity] =
                        shortestPathDistances[currentCity] + edgeWeight;
                    updateCount[neighborCity]++;
                    queue.push_back(neighborCity);

                    // Detect negative weight cycles (not expected in this
                    // problem)
                    if (updateCount[neighborCity] > n) {
                        cerr << "Negative weight cycle detected" << endl;
                    }
                }
            }
        }
    }

    // Determine the city with the fewest number of reachable cities within the
    // distance threshold
    int getCityWithFewestReachable(
        int n, const vector<vector<int>>& shortestPathMatrix,
        int distanceThreshold) {
        int cityWithFewestReachable = -1;
        int fewestReachableCount = n;

        // Count number of cities reachable within the distance threshold for
        // each city
        for (int i = 0; i < n; i++) {
            int reachableCount = 0;
            for (int j = 0; j < n; j++) {
                if (i == j) {
                    continue;
                }  // Skip self
                if (shortestPathMatrix[i][j] <= distanceThreshold) {
                    reachableCount++;
                }
            }
            // Update the city with the fewest reachable cities
            if (reachableCount <= fewestReachableCount) {
                fewestReachableCount = reachableCount;
                cityWithFewestReachable = i;
            }
        }
        return cityWithFewestReachable;
    }
public:
    int findTheCity(int n, vector<vector<int>>& edges, int distanceThreshold) {
        // Adjacency list to store the graph
        vector<vector<pair<int, int>>> adjacencyList(n);
        // Matrix to store shortest path distances from each city
        vector<vector<int>> shortestPathMatrix(n, vector<int>(n, INT_MAX));

        // Initialize adjacency list and shortest path matrix
        for (int i = 0; i < n; i++) {
            shortestPathMatrix[i][i] = 0;  // Distance to itself is zero
        }

        // Populate the adjacency list with edges
        for (const auto& edge : edges) {
            int start = edge[0];
            int end = edge[1];
            int weight = edge[2];
            adjacencyList[start].emplace_back(end, weight);
            adjacencyList[end].emplace_back(start,
                                            weight);  // For undirected graph
        }

        // Compute shortest paths from each city using SPFA algorithm
        for (int i = 0; i < n; i++) {
            spfa(n, adjacencyList, shortestPathMatrix[i], i);
        }

        // Find the city with the fewest number of reachable cities within the
        // distance threshold
        return getCityWithFewestReachable(n, shortestPathMatrix,
                                          distanceThreshold);
    }
};
```

**Solution 7: (Dijkstra)**
```
Runtime: 63 ms
Memory: 17.13 MB
```
```c++
class Solution {
public:
    int findTheCity(int n, vector<vector<int>>& edges, int distanceThreshold) {
        vector<vector<pair<int,int>>> g(n);
        for (auto e: edges) {
            g[e[0]].push_back({e[1], e[2]});
            g[e[1]].push_back({e[0], e[2]});
        }
        int cur, mn = INT_MAX, ans;
        vector<int> dist(n);
        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
        for (int i = 0; i < n; i ++) {
            fill(dist.begin(), dist.end(), INT_MAX);
            cur = 0;
            pq.push({0, i});
            while (pq.size()) {
                auto [w, v] = pq.top();
                pq.pop();
                if (w >= dist[v]) {
                    continue;
                }
                cur += 1;
                dist[v] = w;
                for (auto [nv, nw]: g[v]) {
                    if (w + nw < dist[nv] && w + nw <= distanceThreshold) {
                        pq.push({w+nw, nv});
                    }
                }
            }
            if (cur <= mn) {
                mn = cur;
                ans = i;
            }
        }
        return ans;
    }
};
```

**Solution 8: (Floyd-Warshall Algorithm, O(N^3))**
```
Runtime: 24 ms
Memory: 15.59 MB
```
```c++
class Solution {
    // Floyd-Warshall algorithm to compute shortest paths between all pairs of
    // cities
    void floyd(int n, vector<vector<int>>& distanceMatrix) {
        // Update distances for each intermediate city
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    // Update shortest path from i to j through k
                    distanceMatrix[i][j] =
                        min(distanceMatrix[i][j],
                            distanceMatrix[i][k] + distanceMatrix[k][j]);
                }
            }
        }
    }

    // Determine the city with the fewest number of reachable cities within the
    // distance threshold
    int getCityWithFewestReachable(int n,
                                   const vector<vector<int>>& distanceMatrix,
                                   int distanceThreshold) {
        int cityWithFewestReachable = -1;
        int fewestReachableCount = n;

        // Count number of cities reachable within the distance threshold for
        // each city
        for (int i = 0; i < n; i++) {
            int reachableCount = 0;
            for (int j = 0; j < n; j++) {
                if (i == j) {
                    continue;
                }  // Skip self
                if (distanceMatrix[i][j] <= distanceThreshold) {
                    reachableCount++;
                }
            }
            // Update the city with the fewest reachable cities
            if (reachableCount <= fewestReachableCount) {
                fewestReachableCount = reachableCount;
                cityWithFewestReachable = i;
            }
        }
        return cityWithFewestReachable;
    }
public:
    int findTheCity(int n, vector<vector<int>>& edges, int distanceThreshold) {
        // Large value to represent infinity
        const int INF = 1e9 + 7;
        // Distance matrix to store shortest paths between all pairs of cities
        vector<vector<int>> distanceMatrix(n, vector<int>(n, INF));

        // Initialize distance matrix
        for (int i = 0; i < n; i++) {
            distanceMatrix[i][i] = 0;  // Distance to itself is zero
        }

        // Populate the distance matrix with initial edge weights
        for (const auto& edge : edges) {
            int start = edge[0];
            int end = edge[1];
            int weight = edge[2];
            distanceMatrix[start][end] = weight;
            distanceMatrix[end][start] = weight;  // For undirected graph
        }

        // Compute shortest paths using Floyd-Warshall algorithm
        floyd(n, distanceMatrix);

        // Find the city with the fewest number of reachable cities within the
        // distance threshold
        return getCityWithFewestReachable(n, distanceMatrix, distanceThreshold);
    }
};
```
