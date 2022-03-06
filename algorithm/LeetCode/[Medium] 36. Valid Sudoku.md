36. Valid Sudoku

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

* Each row must contain the digits `1-9` without repetition.
* Each column must contain the digits `1-9` without repetition.
* Each of the 9 `3x3` sub-boxes of the grid must contain the digits 1-9 without repetition.

![36_250px-Sudoku-by-L2G-20050714.svg.png](img/36_250px-Sudoku-by-L2G-20050714.svg.png)

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

**Example 1:**
```
Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
```

**Example 2:**
```
Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being 
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
```

**Note:**

* A Sudoku `board` (partially filled) could be valid but is not necessarily solvable.
* Only the filled cells need to be validated according to the mentioned rules.
* The given board contain only digits `1-9` and the character '.'.
* The given board size is always `9x9`.

# Submissions
---
**Solution 1: (Array, Hash Table)**
```
Runtime: 100 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # init data
        rows = [{} for _ in range(9)]
        columns = [{} for _ in range(9)]
        boxes = [{} for _ in range(9)]

        # validate a board
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    box_index = (i // 3 ) * 3 + j // 3
                    
                    # keep the current cell value
                    rows[i][num] = rows[i].get(num, 0) + 1
                    columns[j][num] = columns[j].get(num, 0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num, 0) + 1
                    
                    # check if this value has been already seen before
                    if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
                        return False         
        return True
```

**Solution 2: (Array)**
```
Runtime: 4 ms
Memory Usage: 5.8 MB
```
```c


bool isValidSudoku(char** board, int boardSize, int* boardColSize){
    int r, c, value, check[3][9][10] = {0};
    for(r=0;r<9;r++)
        for(c=0;c<9;c++){
            value = board[r][c] - '0';
            if(value != -2){
                if(check[0][r][value]++ >0) return false;
                if(check[1][c][value]++ >0) return false;
                if(check[2][(r/3)*3 + c/3][value]++ >0) return false;
        }
    }
    return true;
}
```

**Solution 3: (Array, Hash Table)**
```
Runtime: 27 ms
Memory Usage: 18 MB
```
```c++
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        // use Bitmasking.
        const int N = 9;

        int rows[N] = {0};
        int cols[N] = {0};
        int boxes[N] = {0};

        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                // Check if the position is filled with number
                if (board[r][c] == '.') {
                    continue;
                }
                int val = board[r][c] - '1';
                int pos = (1 << val);

                // Check the row
                if ((rows[r] & pos) > 0) {
                    return false;
                }
                rows[r] |= pos;

                // Check the column
                if ((cols[c] & pos) > 0) {
                    return false;
                }
                cols[c] |= pos;

                // Check the box
                int idx = (r / 3) * 3 + c / 3;
                if ((boxes[idx] & pos) > 0) {
                    return false;
                }
                boxes[idx] |= pos;
            }
        }
        return true;
    }
};
```
