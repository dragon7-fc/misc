1197. Minimum Knight Moves

In an infinite chess board with coordinates from `-infinity` to `+infinity`, you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

![1197_knight](img/1197_knight.png)

Return the minimum number of steps needed to move the knight to the square [x, y].  It is guaranteed the answer exists.

 
**Example 1:**
```
Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]
```
**Example 2:**
```
Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
``` 

**Constraints:**

* |x| + |y| <= 300

# Submissions
---
**Solution 1: (BFS)**
```python
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x = abs(x)
        y = abs(y)
        MAXN = 310
        steps = 0
        dx = [-2,-1,1,2,2,1,-1,-2]
        dy = [1,2,2,1,-1,-2,-2,-1]
        q = []
        visited = [[False for _ in range(MAXN)] for _ in range(MAXN)]
        q.insert(0, [0, 0])        
        visited[0][0] = True
        
        while len(q) > 0:
            sz = len(q)
            for i in range(sz):
                curr = q.pop();
                if curr[0] == x and curr[1] == y:
                    return steps
                
                for j in range(8):
                    x1 = curr[0] + dx[j];
                    y1 = curr[1] + dy[j];
                    if x1 < 0 or y1 < 0 or x1 >= MAXN or y1 >= MAXN:
                        continue
                    
                    if not visited[x1][y1]:
                        visited[x1][y1] = True
                        q.insert(0, [x1, y1])
            steps += 1
        
        return -1
```