874. Walking Robot Simulation

A robot on an infinite grid starts at point (0, 0) and faces north.  The robot can receive one of three possible types of commands:

* `-2`: turn left 90 degrees
* `-1`: turn right 90 degrees
* `1 <= x <= 9`: move forward `x` units

Some of the grid squares are obstacles. 

The `i`-th obstacle is at grid point (`obstacles[i][0], obstacles[i][1]`)

If the robot would try to move onto them, the robot stays on the previous grid square instead (but still continues following the rest of the route.)

Return the **square** of the maximum Euclidean distance that the robot will be from the origin.

**Example 1:**
```
Input: commands = [4,-1,3], obstacles = []
Output: 25
Explanation: robot will go to (3, 4)
```
**Example 2:**
```
Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
Output: 65
Explanation: robot will be stuck at (1, 4) before turning left and going to (1, 8)
```
**Note:**
1. 0 <= commands.length <= 10000
1. 0 <= obstacles.length <= 10000
1. -30000 <= obstacle[i][0] <= 30000
1. -30000 <= obstacle[i][1] <= 30000
1. The answer is guaranteed to be less than 2 ^ 31.

# Solution
---
## Approach 1: Simulation
**Intuition**

We simulate the path of the robot step by step. Since there are at most 90000 steps, this is efficient enough to pass the given input limits.

**Algorithm**

We store the robot's position and direction. If we get a turning command, we update the direction; otherwise we walk the specified number of steps in the given direction.

Care must be made to use a `Set` data structure for the obstacles, so that we can check efficiently if our next step is obstructed. If we don't, our check is point in obstacles could be ~10,000 times slower.

In some languages, we need to encode the coordinates of each obstacle as a long integer so that it is a hashable key that we can put into a Set data structure. Alternatively, we could also encode the coordinates as a string.

```python
class Solution(object):
    def robotSim(self, commands, obstacles):
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x = y = di = 0
        obstacleSet = set(map(tuple, obstacles))
        ans = 0

        for cmd in commands:
            if cmd == -2:  #left
                di = (di - 1) % 4
            elif cmd == -1:  #right
                di = (di + 1) % 4
            else:
                for k in xrange(cmd):
                    if (x+dx[di], y+dy[di]) not in obstacleSet:
                        x += dx[di]
                        y += dy[di]
                        ans = max(ans, x*x + y*y)

        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N + K)$, where $N, K$ are the lengths of commands and obstacles respectively.

* Space Complexity: $O(K)$, the space used in storing the obstacleSet.

# Submissions
---
**Solution 1:**
```
Runtime: 188 ms
Memory Usage: N/A
```
```python
class Solution:
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1 ,0]
        x = y = di = 0
        obstacleSet = set(map(tuple, obstacles))
        ans = 0
        
        for cmd in commands:
            if cmd == -2:
                di = (di-1) % 4
            elif cmd == -1:
                di = (di+1) % 4
            else:
                for k in range(cmd):
                    if (x+dx[di], y+dy[di]) not in obstacleSet:
                        x += dx[di]
                        y += dy[di]
                        ans = max(ans, x*x + y*y)
        return ans
```

**Solution 2:**
```
Runtime: 136 ms
Memory Usage: N/A
```
```python
class Solution:
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        # directions = ['N', 'E', 'S', 'W']
        # 0 - N, 1 - E, 2 - S, 3 - W
        position_offset, obstacles = [(0, 1), (1, 0), (0, -1), (-1, 0)], set(map(tuple, obstacles))
        x, y, direction, max_distance = 0, 0, 0, 0
        for command in commands:
            if command == -2: direction = (direction - 1) % 4
            elif command == -1: direction = (direction + 1) % 4
            else:
                x_off, y_off = position_offset[direction][0], position_offset[direction][1]
                while command > 0:
                    if (x+x_off, y+y_off) not in obstacles:
                        x, y = x+x_off, y+y_off
                    command -= 1
                max_distance = max(max_distance, x**2 + y**2)
        return max_distance
```
