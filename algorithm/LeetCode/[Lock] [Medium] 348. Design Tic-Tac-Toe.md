348. Design Tic-Tac-Toe

Design a Tic-tac-toe game that is played between two players on a n x n grid.

You may assume the following rules:

1. A move is guaranteed to be valid and is placed on an empty block.
1. Once a winning condition is reached, no more moves is allowed.
1. A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.

**Example:**
```
Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.

TicTacToe toe = new TicTacToe(3);

toe.move(0, 0, 1); -> Returns 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

toe.move(0, 2, 2); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

toe.move(2, 2, 1); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

toe.move(1, 1, 2); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

toe.move(2, 0, 1); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

toe.move(1, 0, 2); -> Returns 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|
```

**Follow up:**

* Could you do better than O(n2) per `move()` operation?

# Submissions
---
**Solution 1: (Hash Table)**
```
Runtime: 92 ms
Memory Usage: 16.2 MB
```
```python
class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.d = [collections.defaultdict(int) for _ in range(2)]

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        self.d[player-1][row] += 1
        if self.d[player-1][row] == self.n:
            return player
        
        self.d[player-1][col+self.n] += 1
        if self.d[player-1][col+self.n] == self.n:
            return player
        
        if row == col:
            self.d[player-1][self.n*2] += 1
            if self.d[player-1][self.n*2] == self.n:
                return player
        if row+col == self.n-1:
            self.d[player-1][self.n*2 + 1] += 1
            if self.d[player-1][self.n*2 + 1] == self.n:
                return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
```

**Solution 2: (Hash Table)**
```
Runtime: 64 ms
Memory Usage: 18.2 MB
```
```c++
class TicTacToe {
public:
    vector<vector<char>> grid;
    int size ;
    unordered_map<int, unordered_map<int, int>> rows, cols, diag, adiag;
    /** Initialize your data structure here. */
    TicTacToe(int n) {
        size = n;
    }
    
    /** Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins. */
    int move(int row, int col, int player) {
        rows[row][player]++;
        cols[col][player]++;
        diag[row-col][player]++;
        adiag[row+col][player]++;
        if(rows[row][player] == size or cols[col][player] == size or 
           diag[row-col][player]  == size or adiag[row+col][player]  == size)
            return player;
        return 0;
    }
};

/**
 * Your TicTacToe object will be instantiated and called as such:
 * TicTacToe* obj = new TicTacToe(n);
 * int param_1 = obj->move(row,col,player);
 */
```

**Solution 3: (Hash Table)**
```
Runtime: 21 ms
Memory: 19.5 MB
```
```c++
class TicTacToe {
    int t;
    vector<vector<int>> dp;
public:
    TicTacToe(int n) {
        t = n;
        dp = vector<vector<int>>(2, vector<int>(2*n+2));
    }
    
    int move(int row, int col, int player) {
        dp[player-1][row] += 1;
        dp[player-1][t + col] += 1;
        if (row == col) {
            dp[player-1][2*t] += 1;
        }
        if (row + col == t-1) {
            dp[player-1][2*t+1] += 1;
        }
        if (any_of(dp[player-1].begin(), dp[player-1].end(), [&](int &v){return v == t;})) {
            return player;
        }
        return 0;
    }
};

/**
 * Your TicTacToe object will be instantiated and called as such:
 * TicTacToe* obj = new TicTacToe(n);
 * int param_1 = obj->move(row,col,player);
 */
```
