573. Squirrel Simulation

There's a tree, a squirrel, and several nuts. Positions are represented by the cells in a 2D grid. Your goal is to find the **minimal** distance for the squirrel to collect all the nuts and put them under the tree one by one. The squirrel can only take at most **one nut** at one time and can move in four directions - up, down, left and right, to the adjacent cell. The distance is represented by the number of moves.

**Example 1:**
```
Input: 
Height : 5
Width : 7
Tree position : [2,2]
Squirrel : [4,4]
Nuts : [[3,0], [2,5]]
Output: 12
Explanation:
```
![573_squirrel_simulation.png](img/573_squirrel_simulation.png)

**Note:**

* All given positions won't overlap.
* The squirrel can take at most one nut at one time.
* The given positions of nuts have no order.
* Height and width are positive integers. `3 <= height * width <= 10,000`.
* The given positions contain at least one nut, only one tree and one squirrel.

# Submissions
---
**Solution 1: (Greedy)**
```
Runtime: 140 ms
Memory Usage: 15 MB
```
```python
class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        total_d = 0
        for nut in nuts:
            total_d += 2 * (abs(nut[0] - tree[0]) + abs(nut[1] - tree[1]))
        min_dist = float("inf")
        for nut in nuts:
            min_dist = min(min_dist, total_d - (abs(nut[0] - tree[0]) + abs(nut[1] - tree[1])) + abs(nut[0] - squirrel[0]) + abs(nut[1] - squirrel[1]))
        return min_dist
```