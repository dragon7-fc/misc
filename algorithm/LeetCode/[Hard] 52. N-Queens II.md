52. N-Queens II

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

![52_8-queens.png](img/52_8-queens.png)

Given an integer `n`, return the number of distinct solutions to the n-queens puzzle.

**Example:**
```
Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
```

# Submissions
---
**Solution 1: (Backtracking)**
```
Runtime: 104 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def totalNQueens(self, n: int) -> int:
        queens = []
        solution = []
        ans = 0

        def isValid(location):
            row, col = location
            for queen in queens:
                x, y = queen
                if abs(row - x) == abs(col - y):
                    return False
                if row == x or col == y:
                    return False
            return True

        def solve(col):
            nonlocal ans
            if col >= n:
                return 1
            rst = 0
            for r in range(n):
                if isValid((r, col)):
                    queens.append((r, col))
                    rst += solve(col + 1)
                    queens.remove((r, col))
            return rst

        return solve(0)
```

**Solution 2: (Backtracking)**
```
Runtime: 4 ms
Memory Usage: 6.1 MB
```
```c++
class Solution {
    bool is_not_under_attack(vector<string>& board,int row,int col){
        for(int i=0;i!=row;i++)
            if(board[i][col] == 'Q') return false;
        for(int i=row-1, j=col-1; i>=0 && j>=0; i--,j--)
            if(board[i][j] == 'Q') return false;
        for(int i=row-1,j=col+1;i>=0 and j < board.size();--i,++j)
            if(board[i][j] == 'Q') return false;
        
        return true;
    }
    int backtrack(vector<string>& board, int row){
        if(row == board.size()) return 1;
        int getSolution(0);
        for(int col=0; col!=board.size();++col){
            if(is_not_under_attack(board, row, col)){
                board[row][col] = 'Q'; // place Q
                getSolution += backtrack(board, row+1);
                board[row][col] = '.'; // remove Q
            }
        }
        return getSolution;
    }
public:
    int totalNQueens(int n) {
        vector<string> board(n, string(n,'.'));
        return backtrack(board, 0);
    }
};
```
