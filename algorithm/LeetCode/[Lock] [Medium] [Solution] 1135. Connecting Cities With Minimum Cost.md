1135. Connecting Cities With Minimum Cost

There are N cities numbered from 1 to N.

You are given connections, where each `connections[i] = [city1, city2, cost]` represents the cost to connect `city1` and `city2` together.  (A connection is bidirectional: connecting `city1` and `city2` is the same as connecting `city2` and `city1`.)

Return the minimum cost so that for every pair of cities, there exists a path of connections (possibly of length 1) that connects those two cities together.  The cost is the sum of the connection costs used. If the task is impossible, return -1.

 

**Example 1:**

![1135_1314_ex2.png](img/1135_1314_ex2.png)
```
Input: N = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
Output: 6
Explanation: 
Choosing any 2 edges will connect all cities so we choose the minimum 2.
```

**Example 2:**

![1135_1314_ex1.png](img/1135_1314_ex1.png)
```
Input: N = 4, connections = [[1,2,3],[3,4,4]]
Output: -1
Explanation: 
There is no way to connect all cities even if all edges are used.
```

**Note:**

* `1 <= N <= 10000`
* `1 <= connections.length <= 10000`
* `1 <= connections[i][0], connections[i][1] <= N`
* `0 <= connections[i][2] <= 10^5`
* `connections[i][0] != connections[i][1]`

# Submissions
---
**Solution 1: (Kruskals Algorithm)**
```
Runtime: 640 ms
Memory Usage: 19.9 MB
```
```python
class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        #UnionFind:
        def find(city):
            if parent[city] != city:
                parent[city] = find(parent[city])
            return parent[city]

        def union(c1, c2):
            root1, root2 = find(c1), find(c2)
            if root1 == root2:
                return False
            parent[root2] = root1  # Always join roots!
            return True
        parent = [i for i in range(N+1)]


        connections.sort(key = lambda x: x[2])
        total = 0
        for city1, city2, cost in connections:
            if union(city1, city2):
                total += cost
        root = find(N)
        return total if all(root == find(city) for city in parent[1:]) else -1 
```

**Solution 1: (Prims Algorithm)**
```
Runtime: 664 ms
Memory Usage: 20.2 MB
```
```python
class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        q = []
        graph = collections.defaultdict(list)
        for city1, city2, cost in connections:
            graph[city1].append([cost, city2])
            graph[city2].append([cost, city1])


        q.append([0, N])
        visited, total = set(), 0
        while q:
            cost, node = heapq.heappop(q)
            if node not in visited:
                visited.add(node)
                total += cost
                for edge_cost, next_city in graph[node]:
                    heapq.heappush(q, [edge_cost, next_city])
        return total if len(visited) == N else -1
```     