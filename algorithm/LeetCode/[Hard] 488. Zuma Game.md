488. Zuma Game

Think about Zuma Game. You have a row of balls on the table, colored red(R), yellow(Y), blue(B), green(G), and white(W). You also have several balls in your hand.

Each time, you may choose a ball in your hand, and insert it into the row (including the leftmost place and rightmost place). Then, if there is a group of 3 or more balls in the same color touching, remove these balls. Keep doing this until no more balls can be removed.

Find the minimal balls you have to insert to remove all the balls on the table. If you cannot remove all the balls, output -1.

 

**Example 1:**
```
Input: board = "WRRBBW", hand = "RB"
Output: -1
Explanation: WRRBBW -> WRR[R]BBW -> WBBW -> WBB[B]W -> WW
```

**Example 2:**
```
Input: board = "WWRRBBWW", hand = "WRBRW"
Output: 2
Explanation: WWRRBBWW -> WWRR[R]BBWW -> WWBBWW -> WWBB[B]WW -> WWWW -> empty
```

**Example 3:**
```
Input: board = "G", hand = "GGGGG"
Output: 2
Explanation: G -> G[G] -> GG[G] -> empty 
```

**Example 4:**
```
Input: board = "RBYYBBRRB", hand = "YRBGB"
Output: 3
Explanation: RBYYBBRRB -> RBYY[Y]BBRRB -> RBBBRRB -> RRRB -> B -> B[B] -> BB[B] -> empty 
```

**Constraints:**

* You may assume that the initial row of balls on the table won’t have any 3 or more consecutive balls with the same color.
* `1 <= board.length <= 16`
* `1 <= hand.length <= 5`
* Both input strings will be non-empty and only contain characters 'R','Y','B','G','W'.

# Submissions
---
**Solution 1: (DFS)**

The idea is straghtforward, just traverse the whole board string and find the possible place to insert. For example, if we have string WWRRBB and in the hand we have WRB, then we can try to insert into 3 places which are after [W, R, B].

```
Runtime: 48 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        
        def remove(hand: str, color: str, times: int):  ## remove ball in hand
            if times == 0:
                return hand
            result = []
            for i in range(0, len(hand)):
                if hand[i] == color:
                    if (times := times-1) == 0:
                        result.extend(hand[i+1:])
                        break
                else:
                    result.append(hand[i])
            return "".join(result) if times == 0 else None

        @functools.lru_cache(None)
        def dfs(board: str, hand: str) -> int:  # remove ball in board
            if len(board) == 0:
                return 0
            i, j, count = 0, 1, float("inf")
            while True:
                while j < len(board) and board[j] == board[i]:
                    j += 1
                times = max(0, 3-j+i)
                if (result := remove(hand, board[i], times)) != None:
                    if (r := dfs(board[:i] + board[j:], result)) != -1:
                        count = min(count, r + times)
                if j == len(board):
                    break
                i, j = j, j+1
            return count if count != float("inf") else -1

        return dfs(board, hand)
```

**Solution 2: (DFS)**
```
Runtime: 0 ms
Memory Usage: 5.9 MB
```
```c++
class Solution {
public:
    int findMinStep(string board, string hand) {
        int ans = -1;
        map<char,int>mp;
        for(char ch: hand) {
            mp[ch] += 1;
        }
        ans = dfs(board + "#", mp);
        if(ans == 1e9) {
            return -1;
        }
        return ans;
    }
    int dfs(string s, map<char,int>&mp) {
        if(s == "#") return 0;
        int res = 1e9;
        for(int i = 0, j = 0; j < s.size(); j++) {
            if(s[i] == s[j]) continue;
            int need = 3 - min(3, j - i);
            if(mp[s[i]] >= need) {
                mp[s[i]] -= need;
                res = min(res, need + dfs(s.substr(0, i) + s.substr(j), mp));
                mp[s[i]] += need;
            }
            i = j;
        }
        return res;
    }
};
```