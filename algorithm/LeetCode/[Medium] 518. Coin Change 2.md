518. Coin Change 2

You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

 

**Example 1:**
```
Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
```

**Example 2:**
```
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
```

**Example 3:**
```
Input: amount = 10, coins = [10] 
Output: 1
```

**Note:**

You can assume that

* `0 <= amount <= 5000`
* `1 <= coin <= 5000`
* the number of `coins` is less than `500`
* the answer is guaranteed to fit into signed 32-bit integer

# Submissions
---
**Solution 1: (DP Bottom-Up)**
```
Runtime: 132 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * amount
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]
                
        return dp[-1]
```

**Solution 2: (DP Top-Down)**
```
Runtime: 976 ms
Memory Usage: 321.4 MB
```
```python
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N = len(coins)
        
        @functools.lru_cache(None)
        def dp(i, t):
            if (t == amount):
                return 1
            if t > amount or i == N:
                return 0

            return dp(i, t + coins[i]) + dp(i + 1, t)
        
        return dp(0, 0)
```

**Solution 3: (DP Top-Down)**
```
Runtime: 644 ms
Memory Usage: 46 MB
```
```python
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0: return 1
        N = len(coins)
        coins.sort(reverse=True)
        
        @functools.lru_cache(None)
        def dp(i, t):
            if t == amount:
                return 1
            if i >= N or t > amount:
                return 0
            return sum(dp(ni, t + coins[ni]) for ni in range(i, N))
        
        return dp(0, 0)
```

**Solution4 4: (DP Bottom-Up)**
```
Runtime: 43 ms
Memory: 18.6 MB
```
```c++
class Solution {
public:
    int change(int amount, vector<int>& coins) {
        vector<vector<int>> dp(coins.size() + 1, vector<int>(amount + 1, 0));
        dp[0][0] = 1;//1 comb: no coins for no amount 

        for (int j = 1; j <= coins.size(); j++) {
            for (int i = 0; i <= amount; i++) {
                dp[j][i] = dp[j-1][i]; // Exclude the current coin
            
                if (i >= coins[j-1]) {
                    dp[j][i] += dp[j][i-coins[j-1]];//Include the current coin
                }
            }
        }
        return dp[coins.size()][amount];
    }
};
```

**Solution 5: (DP Bottom-Up 1D)**
```
Runtime: 7 ms
Memory: 7.2 MB
```
```c++
class Solution {
public:
    int numRollsToTarget(int n, int k, int target) {
        int MOD = 1e9 + 7;
        int dp[n+1][target+1];
        memset(dp, 0, sizeof(dp));
        dp[0][0] = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= min(i*k, target); j++) {
                for (int f = 1; f <= min(k, j); f++) {
                    dp[i][j] = (dp[i][j] + dp[i-1][j-f]) % MOD;
                }
            }
        }
        return dp[n][target];
    }
};
```
