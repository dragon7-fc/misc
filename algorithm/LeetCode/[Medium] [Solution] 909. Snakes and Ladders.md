909. Snakes and Ladders

On an N x N `board`, the numbers from `1` to N*N are written boustrophedonically **starting from the bottom left of the board**, and alternating direction each row.  For example, for a 6 x 6 board, the numbers are written as follows:

![909_snakes.png](img/909_snakes.png)

You start on square `1` of the board (which is always in the last row and first column).  Each move, starting from square `x`, consists of the following:

* You choose a destination square `S` with number `x+1`, `x+2`, `x+3`, `x+4`, `x+5`, or `x+6`, provided this number is `<= N*N`.
    * (This choice simulates the result of a standard 6-sided die roll: ie., there are always **at most 6 destinations, regardless of the size of the board.**)
* If `S` has a snake or ladder, you move to the destination of that snake or ladder.  Otherwise, you move to `S`.

A board square on row `r` and column `c` has a "snake or ladder" if `board[r][c] != -1`.  The destination of that snake or ladder is `board[r][c]`.

Note that you only take a snake or ladder at most once per move: if the destination to a snake or ladder is the start of another snake or ladder, you do **not** continue moving.  (For example, if the board is `[[4,-1],[-1,3]]`, and on the first move your destination square is `2`, then you finish your first move at `3`, because you do **not** continue moving to `4`.)

Return the least number of moves required to reach square N*N.  If it is not possible, return `-1`.

**Example 1:**
```
Input: [
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,35,-1,-1,13,-1],
[-1,-1,-1,-1,-1,-1],
[-1,15,-1,-1,-1,-1]]
Output: 4
Explanation: 
At the beginning, you start at square 1 [at row 5, column 0].
You decide to move to square 2, and must take the ladder to square 15.
You then decide to move to square 17 (row 3, column 5), and must take the snake to square 13.
You then decide to move to square 14, and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
It can be shown that you need at least 4 moves to reach the N*N-th square, so the answer is 4.
```

**Note:**

* `2 <= board.length = board[0].length <= 20`
* `board[i][j]` is between `1` and `N*N` or is equal to `-1`.
* The board square with number `1` has no snake or ladder.
* The board square with number `N*N` has no snake or ladder.

# Solution
---
## Approach 1: Breadth-First Search
**Intuition**

As we are looking for a shortest path, a breadth-first search is ideal. The main difficulty is to handle enumerating all possible moves from each square.

**Algorithm**

Suppose we are on a square with number `s`. We would like to know all final destinations with number `s2` after making one move.

This requires knowing the coordinates `get(s2)` of square `s2`. This is a small puzzle in itself: we know that the row changes every `N` squares, and so is only based on `quot = (s2-1) / N`; also the column is only based on `rem = (s2-1) % N` and what row we are on (forwards or backwards.)

From there, we perform a breadth first search, where the nodes are the square numbers s.

```python
class Solution(object):
    def snakesAndLadders(self, board):
        N = len(board)

        def get(s):
            # Given a square num s, return board coordinates (r, c)
            quot, rem = divmod(s-1, N)
            row = N - 1 - quot
            col = rem if row%2 != N%2 else N - 1 - rem
            return row, col

        dist = {1: 0}
        queue = collections.deque([1])
        while queue:
            s = queue.popleft()
            if s == N*N: return dist[s]
            for s2 in xrange(s+1, min(s+6, N*N) + 1):
                r, c = get(s2)
                if board[r][c] != -1:
                    s2 = board[r][c]
                if s2 not in dist:
                    dist[s2] = dist[s] + 1
                    queue.append(s2)
        return -1
```

**Complexity Analysis**

* Time Complexity: $O(N^2)$, where $N$ is the length of the `board`.

* Space Complexity: $O(N^2)$.

# Submissions
---
**Solution 1: (BFS)**
```
Runtime: 144 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        N = len(board)

        def get(s):
            # Given a square num s, return board coordinates (r, c)
            quot, rem = divmod(s-1, N)
            row = N - 1 - quot
            col = rem if row%2 != N%2 else N - 1 - rem
            return row, col

        dist = {1: 0}
        queue = collections.deque([1])
        while queue:
            s = queue.popleft()
            if s == N*N: return dist[s]
            for s2 in range(s+1, min(s+6, N*N) + 1):
                r, c = get(s2)
                if board[r][c] != -1:
                    s2 = board[r][c]
                if s2 not in dist:
                    dist[s2] = dist[s] + 1
                    queue.append(s2)
        return -1
```