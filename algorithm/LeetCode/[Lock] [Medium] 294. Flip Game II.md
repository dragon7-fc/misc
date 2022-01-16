294. Flip Game II

You are playing a Flip Game with your friend.

You are given a string `currentState` that contains only `'+'` and `'-'`. You and your friend take turns to flip **two consecutive** `"++"` into `"--"`. The game ends when a person can no longer make a move, and therefore the other person will be the winner.

Return `true` if the starting player can guarantee a win, and `false` otherwise.

 

**Example 1:**
```
Input: currentState = "++++"
Output: true
Explanation: The starting player can guarantee a win by flipping the middle "++" to become "+--+".
```

**Example 2:**
```
Input: currentState = "+"
Output: false
```

**Constraints:**

* `1 <= currentState.length <= 60`
* `currentState[i]` is either `'+'` or `'-'`.

# Submissions
---
**Solution 1: (Backtracking, Bit Manipulation, DP Top-Down)**
```
Runtime: 55 ms
Memory Usage: 15 MB
```
```python
class Solution:
    def canWin(self, currentState: str) -> bool:
        # check if the current player taking the move can win the game
        # @cache for memoization
        @cache
        def check(mask):
            nonlocal currentState
            for i in range(len(currentState)-1):
                # check if there are two consecutive flipable bits
                if not mask & 1 << i and not mask & 1 << (i+1):
                    # flip the two bits to 1, meaning it's flipped
                    new_mask = mask | (1 << i | 1 << (i+1))
                    # if after taking this move the opponent cannot win the game, then the current play wins
                    if not check(new_mask):
                        return True
			# no way to win the game no matter which move to take
            return False
        
        # bit mask tracking available bits for flip
        # ++++ -> 0000 , ++-- -> 1100 (the mask is a reversed matching of flippable bits, not as intuitive as 0011, 
        # but it actually doesn't matter as long as one bit map to one coin)
        mask = 0
        for i in range(len(currentState)):
            if currentState[i] == '-':
                mask |= 1 << i
        return check(mask)
```

**Solution 2: (Backtracking, DP Top-Down)**
```
Runtime: 32 ms
Memory Usage: 10.9 MB
```
```c++
class Solution {
public:
    bool canWin(string currentState) {
        unordered_map<string, bool> dp;
        return helper(currentState, dp);
    }
    
    bool helper(const string& state, 
               unordered_map<string, bool>& dp) {
        if (dp.find(state) != dp.end()) {
            return dp[state];
        }
        
        for (int i=0; i+1<state.length(); ++i) {
            if (state[i] == state[i+1] && state[i] == '+') {
                string s = state;
                s[i] = '-';
                s[i+1] = '-';
                if (!helper(s, dp)) {
                    dp[state] = true;
                    return true;
                }
            }
        }
        dp[state] = false;
        return false;
    }
};
```
