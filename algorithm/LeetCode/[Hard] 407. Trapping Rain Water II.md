407. Trapping Rain Water II

Given an `m x n` matrix of positive integers representing the height of each unit cell in a 2D elevation map, compute the volume of water it is able to trap after raining.

 

**Note:**

* Both `m` and `n` are less than `110`. The height of each unit cell is greater than `0` and is less than `20,000`.

 

**Example:**
```
Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.
```

![407_rainwater_empty.png](img/407_rainwater_empty.png)

The above image represents the elevation map `[[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]` before the rain.

![407_rainwater_fill.png](img/407_rainwater_fill.png)

After the rain, water is trapped between the blocks. The total volume of water trapped is `4`.

# Submissions
---
**Solution 1: (Heap)**

* Visit boundary first
    * append( height[x][y] (x, y) ) to a list
* heapify the list and start from the point with smallest height to check its neighbor.
    * If neighbor has height higher than start point water_top, then this neighbor cannot hold water with water_top as its height
    * Otherwise the neighbor holds the same amount of water with the same water_top as start point.
        * Add the water the neighbor can hold to results.
        * Append the visited neighbor to heap.
* Return final results when heap is empty

* Time: O(nlogn), n is the total size of heightMap
* Space: O(n)

```
Runtime: 200 ms
Memory Usage: 15.5 MB
```
```python
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0] or len(heightMap)<3 or len(heightMap[0])<3:
            return 0
        
        R, C = len(heightMap), len(heightMap[0])
        height_dict = {}
        water_top_heap = []
        # Check bondary first
        for c in range(C):
            # Top boundary
            water_top_heap.append( (heightMap[0][c], (0, c)) )
            height_dict[(0, c)] = (heightMap[0][c])
            # Bottom boundary
            water_top_heap.append( (heightMap[R - 1][c], (R - 1, c)) )
            height_dict[(R - 1, c)] = (heightMap[R - 1][c])
        for r in range(R):
            if (r, 0) not in height_dict:
                # Left boundary
                water_top_heap.append( (heightMap[r][0], (r, 0)) )
                height_dict[(r, 0)] = (heightMap[r][0])
            if (r, C-1) not in height_dict:
                # Right boundary
                water_top_heap.append( (heightMap[r][C - 1], (r, C - 1)) )
                height_dict[(r, C - 1)] = (heightMap[r][C - 1])
        heapq.heapify(water_top_heap)
    
        res = 0
        dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
        while water_top_heap:
            cur_height, cur_pos = heapq.heappop(water_top_heap)
            for i in range(4):
                nr, nc = cur_pos[0] + dr[i], cur_pos[1] + dc[i]
                if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in height_dict:
                    if heightMap[nr][nc] > height_dict[cur_pos]: 
                        height_dict[(nr, nc)] = heightMap[nr][nc]
                    else:
                        height_dict[(nr, nc)] = height_dict[cur_pos]
                    res += height_dict[(nr, nc)] - heightMap[nr][nc]
                    heapq.heappush(water_top_heap, (heightMap[nr][nc], (nr, nc)) )
        return res
```