1057. Campus Bikes

On a campus represented as a 2D grid, there are `N` workers and `M` bikes, with `N <= M`. Each worker and bike is a 2D coordinate on this grid.

Our goal is to assign a bike to each worker. Among the available bikes and workers, we choose the (worker, bike) pair with the shortest Manhattan distance between each other, and assign the bike to that worker. (If there are multiple (worker, bike) pairs with the same shortest Manhattan distance, we choose the pair with the smallest worker index; if there are multiple ways to do that, we choose the pair with the smallest bike index). We repeat this process until there are no available workers.

The Manhattan distance between two points `p1` and `p2` is `Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y`|.

Return a vector ans of length `N`, where `ans[i]` is the index (`0`-indexed) of the bike that the `i`-th worker is assigned to.

 

**Example 1:**

![1057_1261_example_1_v2.png](img/1057_1261_example_1_v2.png)
```
Input: workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]
Output: [1,0]
Explanation: 
Worker 1 grabs Bike 0 as they are closest (without ties), and Worker 0 is assigned Bike 1. So the output is [1, 0].
```

**Example 2:**

![1057_1261_example_2_v2.png](img/1057_1261_example_2_v2.png)
```
Input: workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]]
Output: [0,2,1]
Explanation: 
Worker 0 grabs Bike 0 at first. Worker 1 and Worker 2 share the same distance to Bike 2, thus Worker 1 is assigned to Bike 2, and Worker 2 will take Bike 1. So the output is [0,2,1].
```

**Note:**

* `0 <= workers[i][j], bikes[i][j] < 1000`
* All worker and bike locations are distinct.
* `1 <= workers.length <= bikes.length <= 1000`

# Submissions
---
**Solution 1: (Sort, Greedy)**
```
Runtime: 824 ms
Memory Usage: 110.9 MB
```
```python
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        distances = {}
        used = set()
        res = [None]*len(workers)
        for w, worker in enumerate(workers): 
            for b, bike in enumerate(bikes):
                dist = abs(worker[0]-bike[0]) + abs(worker[1]-bike[1])
                if dist not in distances: 
                    distances[dist] = [(w, b)]
                else: 
                    distances[dist].append((w,b))
        keyList = list(distances.keys())
        keyList.sort()
        for k in keyList: 
            wbList = distances[k]
            for pair in wbList: 
                w = pair[0]
                b = pair[1]
                if res[w] == None and b not in used: 
                    res[w] = b 
                    used.add(b)
        return res 
```