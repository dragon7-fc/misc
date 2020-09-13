1584. Min Cost to Connect All Points

You are given an array `points` representing integer coordinates of some points on a 2D-plane, where `points[i] = [xi, yi]`.

The cost of connecting two points `[xi, yi]` and `[xj, yj]` is the manhattan distance between them: `|xi - xj| + |yi - yj|`, where `|val|` denotes the absolute value of `val`.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

 

**Example 1:**

![1584_d.png](img/1584_d.png)
```
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation:
```
![1584_c.png](img/1584_c.png)
```
We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
```

**Example 2:**
```
Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
```

**Example 3:**
```
Input: points = [[0,0],[1,1],[1,0],[-1,1]]
Output: 4
```

**Example 4:**
```
Input: points = [[-1000000,-1000000],[1000000,1000000]]
Output: 4000000
```

**Example 5:**
```
Input: points = [[0,0]]
Output: 0
```

**Constraints:**

* `1 <= points.length <= 1000`
* `-106 <= xi, yi <= 106`
* All pairs `(xi, yi)` are distinct.

# Submissions
---
**Solution 1: (Graph, Minimum Spanning Tree)**
```
Runtime: 2388 ms
Memory Usage: 126.9 MB
```
```python
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        manhattan = lambda p1, p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        N = len(points)
        g = collections.defaultdict(list)
        for i in range(N):
            for j in range(i+1, N):
                d = manhattan(points[i], points[j])
                g[i].append((d, j))
                g[j].append((d, i))
        cnt, ans, visited, heap = 1, 0, [0] * N, g[0]
        visited[0] = 1
        heapq.heapify(heap)
        while heap:
            d, j = heapq.heappop(heap)
            if not visited[j]:
                visited[j], cnt, ans = 1, cnt+1, ans+d
                for record in g[j]: heapq.heappush(heap, record)
            if cnt >= N: break        
        return ans
```