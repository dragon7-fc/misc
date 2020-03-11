782. Transform to Chessboard

An N x N `board` contains only `0`s and `1`s. In each move, you can swap any 2 rows with each other, or any 2 columns with each other.

What is the minimum number of moves to transform the board into a "chessboard" - a board where no 0s and no 1s are 4-directionally adjacent? If the task is impossible, return `-1`.

**Examples:**
```
Input: board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
Output: 2
Explanation:
One potential sequence of moves is shown below, from left to right:

0110     1010     1010
0110 --> 1010 --> 0101
1001     0101     1010
1001     0101     0101

The first move swaps the first and second column.
The second move swaps the second and third row.
```

```
Input: board = [[0, 1], [1, 0]]
Output: 0
Explanation:
Also note that the board with 0 in the top left corner,
01
10

is also a valid chessboard.
```

```
Input: board = [[1, 0], [1, 0]]
Output: -1
Explanation:
No matter what sequence of moves you make, you cannot end with a valid chessboard.
```

**Note:**

* `board` will have the same number of rows and columns, a number in the range `[2, 30]`.
* `board[i][j]` will be only `0`s or `1`s.

# Submissions
---
**Solution 1: (Array)**

How to check impossible board?

1. Each row in the board must either equal to the first row or equal to the reverse of the first row. The same apply to column, but you don't need to check column, because if all rows complies with this rule, all columns automatically comply with this rule by themselves. Only need to check rows.
1. Count of "1" in each row must equal to the count of "0", or at most differ by 1. Since rule #1 is already passed, you don't need to check every row this time. Checking only the 1st row is enough. But you need to check both 1st row and 1st column in this case. Can't skip column this time When both #1 and #2 passed, it means the board can be tranformed to chessboard.

How to count number of swaps to transform?  
Only need to count 1st row and 1st column. When the 1st row and 1st column becomes valid, the rest must be valid by themselves according to rule #1.

Taking 1st row for example.

1. We don't know whether the first cell should be "0" or "1". Assume it to be "0" first, then we know the expected values of all cells in 1st row.
1. Count the difference against actual values. The number of swap should be diffCnt/2. If the diffCnt is an odd number, that means the first cell cannot be "0", we should choose "1" as the first cell.
1. If both choosing "0" and choosing "1" makes even diffCount, then we choose the one with smallest number of swaps.

Same applies to column.

```
Runtime: 84 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        if n <= 1:
            return 0
        rows = [''.join(str(c) for c in r) for r in board]
        counter = collections.Counter(rows)
        keys = list(counter)
        if len(keys) != 2 \
            or abs(counter[keys[0]] - counter[keys[1]]) > 1 \
            or abs(keys[0].count('1') - keys[0].count('0')) > 1 \
            or any(a == b for a, b in zip(*keys)):
            return -1
        rowdiff = sum(board[0][i] != (i%2) for i in range(n))
        coldiff = sum(board[i][0] != (i%2) for i in range(n))
        rowdiff = n - rowdiff if rowdiff%2 != 0 or (n%2 == 0 and (n - rowdiff) < rowdiff) else rowdiff
        coldiff=n - coldiff if coldiff%2 != 0 or (n%2 == 0 and (n - coldiff) < coldiff) else coldiff
        return (rowdiff+coldiff) // 2
```