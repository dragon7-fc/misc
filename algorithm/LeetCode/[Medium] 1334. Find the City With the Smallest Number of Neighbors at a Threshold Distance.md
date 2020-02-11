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

**Solution 3: (BFS, Dijkstra, Graph, Graph)**
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