1066. Campus Bikes II

On a campus represented as a 2D grid, there are `N` workers and `M` bikes, with `N <= M`. Each worker and bike is a 2D coordinate on this grid.

We assign one unique bike to each worker so that the sum of the Manhattan distances between each worker and their assigned bike is minimized.

The Manhattan distance between two points `p1` and `p2` is `Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|`.

Return the minimum possible sum of Manhattan distances between each worker and their assigned bike.

 

**Example 1:**

![1066_1261_example_1_v2.png](img/1066_1261_example_1_v2.png)
```
Input: workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]
Output: 6
Explanation: 
We assign bike 0 to worker 0, bike 1 to worker 1. The Manhattan distance of both assignments is 3, so the output is 6.
```

**Example 2:**

![1066_1261_example_2_v2.png](img/1066_1261_example_2_v2.png)
```
Input: workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]]
Output: 4
Explanation: 
We first assign bike 0 to worker 0, then assign bike 1 to worker 1 or worker 2, bike 2 to worker 2 or worker 1. Both assignments lead to sum of the Manhattan distances as 4.
```

**Note:**

* `0 <= workers[i][0], workers[i][1], bikes[i][0], bikes[i][1] < 1000`
* All worker and bike locations are distinct.
* `1 <= workers.length <= bikes.length <= 10`

# Submissions
---
**Solution 1: (DP Top-Down)**
```
Runtime: 252 ms
Memory Usage: 15.2 MB
```
```python
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        M, N = len(bikes), len(workers)
        
        def minimum_distance(i,mask):    
            if i == N:
                return 0
            res = float('inf')
            if (i,tuple(mask)) in memo:
                return memo[(i,tuple(mask))]
            for j in range(M):  
                if not mask[j]:
                    mask[j] = 1
                    res = min(res,(abs(workers[i][0]-bikes[j][0])+abs(workers[i][1]-bikes[j][1]))+minimum_distance(i+1,mask))
                    mask[j] = 0  
            memo[(i, tuple(mask))] = res
            return memo[(i, tuple(mask))]
        
        m = [0]*len(bikes)
        memo = {}
        return minimum_distance(0, m)
```

**Solution 2: (DP Top-Down)**
```
Runtime: 76 ms
Memory Usage: 14.6 MB
```
```python
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        M, N = len(bikes), len(workers)
        manhattanDist = lambda i,j: abs(workers[i][0]-bikes[j][0])+abs(workers[i][1]-bikes[j][1])
        dist = []
        for i in range(N):
            dist.append([])
            for j in range(M):
                dist[-1].append(manhattanDist(i,j))
        
        @functools.lru_cache(None)
        def dp(remainingBikes, i):
            if i == N:
                return 0            
            rst = math.inf
            for j in range(len(remainingBikes)):
                rst = min(rst, dist[i][remainingBikes[j]] + dp(remainingBikes[:j] + remainingBikes[j+1:], i+1))
            return rst
        
        return dp(tuple(range(M)), 0)
```