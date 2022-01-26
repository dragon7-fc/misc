2061. Number of Spaces Cleaning Robot Cleaned

A room is represented by a **0-indexed** 2D binary matrix `room` where a `0` represents an **empty** space and a `1` represents a space with an **object**. The top left corner of the room will be empty in all test cases.

A cleaning robot starts at the top left corner of the room and is facing right. The robot will continue heading straight until it reaches the edge of the room or it hits an object, after which it will turn 90 degrees **clockwise** and repeat this process. The starting space and all spaces that the robot visits are **cleaned** by it.

Return the number of **clean** spaces in the room if the robot runs indefinetely.

 

**Example 1:**

![2061_image-20211101204703-1.png](img/2061_image-20211101204703-1.png)
```
Input: room = [[0,0,0],[1,1,0],[0,0,0]]
Output: 7
Explanation:
The robot cleans the spaces at (0, 0), (0, 1), and (0, 2).
The robot is at the edge of the room, so it turns 90 degrees clockwise and now faces down.
The robot cleans the spaces at (1, 2), and (2, 2).
The robot is at the edge of the room, so it turns 90 degrees clockwise and now faces left.
The robot cleans the spaces at (2, 1), and (2, 0).
The robot has cleaned all 7 empty spaces, so return 7.
```

**Example 2:**

![2061_image-20211101204736-2.png](img/2061_image-20211101204736-2.png)
```
Input: room = [[0,1,0],[1,0,0],[0,0,0]]
Output: 1
Explanation:
The robot cleans the space at (0, 0).
The robot hits an object, so it turns 90 degrees clockwise and now faces down.
The robot hits an object, so it turns 90 degrees clockwise and now faces left.
The robot is at the edge of the room, so it turns 90 degrees clockwise and now faces up.
The robot is at the edge of the room, so it turns 90 degrees clockwise and now faces right.
The robot is back at its starting position.
The robot has cleaned 1 space, so return 1.
```

**Constraints:**

* `m == room.length`
* `n == room[r].length`
* `1 <= m, n <= 300`
* `room[r][c]` is either `0` or `1`.
* `room[0][0] == 0`

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 724 ms
Memory Usage: 17.1 MB
```
```python
class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        m, n = len(room), len(room[0])

        if not ((m > 1 and room[1][0] == 0) or (n > 1 and room[0][1] == 0)):
            return 1

        directions = (0, 1), (1, 0), (0, -1), (-1, 0)  # order matters
        cleaned = dict()  # {(row, col): direction}
        r = c = d = 0  # row, col, direction

        while True:
            if (r, c) in cleaned and cleaned[(r, c)] == d:
                break
            if (r, c) not in cleaned:
                cleaned[(r, c)] = d
            nr, nc = r + directions[d][0], c + directions[d][1]
            while nr < 0 or nr >= m or nc < 0 or nc >= n or room[nr][nc]:
                d = (d + 1) % 4
                nr, nc = r + directions[d][0], c + directions[d][1]
            r, c = nr, nc

        return len(cleaned)
```
