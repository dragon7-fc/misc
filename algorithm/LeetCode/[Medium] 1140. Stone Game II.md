1140. Stone Game II

Alex and Lee continue their games with piles of stones.  There are a number of piles **arranged in a row**, and each pile has a positive integer number of stones `piles[i]`.  The objective of the game is to end with the most stones. 

Alex and Lee take turns, with Alex starting first.  Initially, `M = 1`.

On each player's turn, that player can take **all the stones** in the **first** X remaining piles, where `1 <= X <= 2M`.  Then, we set `M = max(M, X)`.

The game continues until all the stones have been taken.

Assuming Alex and Lee play optimally, return the maximum number of stones Alex can get.

 

**Example 1:**

```
Input: piles = [2,7,9,4,4]
Output: 10
Explanation:  If Alex takes one pile at the beginning, Lee takes two piles, then Alex takes 2 piles again. Alex can get 2 + 4 + 4 = 10 piles in total. If Alex takes two piles at the beginning, then Lee can take all three piles left. In this case, Alex get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 
```

**Constraints:**

* `1 <= piles.length <= 100`
* `1 <= piles[i] <= 10 ^ 4`

# Submissions
---
**Solution 1: (DP Bottom-up, Prefix Sum)**
```
Runtime: 104 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dp = [[0]*n for _ in range(n)]
        for i in range(n-2,-1,-1):
            piles[i] += piles[i+1]      
        for i in range(n-1,-1,-1):
            for m in range(n-1,0,-1):
                dp[i][m] = piles[i]
                if i + 2*m < n:
                    dp[i][m] -= min(dp[i+x][max(m,x)] for x in range(1,2*m+1))
        return dp[0][1]
```

**Solution 2: (DP Top-Down, Prefix Sum)**
```
Runtime: 60 ms
Memory Usage: 14.4 MB
```
```python
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        N = len(piles)
        sums = [0] * (N+1)
        for lo in range(N-1, -1, -1):
            sums[lo] = sums[lo+1] + piles[lo]
        @lru_cache(None)
        def dfs(index, M):
            if index + 2 * M >= N: 
                return sums[index]
            res = 0
            for i in range(1, 2*M+1):
                res = max(res, sums[index] - dfs(index+i, max(M,i)))
            return res
        
        return dfs(0, 1)
```

**Solution 3: (DP Bottom-Up, Prefix Sum)**
```
Runtime: 62 ms
Memory: 12.38 MB
```
```c++
class Solution {
public:
    int stoneGameII(vector<int>& piles) {
        int length = piles.size();
        vector<vector<int>> dp(length + 1, vector<int>(length + 1, 0));

        // Store suffix sum for all possible suffix
        vector<int> suffixSum(length + 1, 0);
        for (int i = length - 1; i >= 0; i--) {
            suffixSum[i] = suffixSum[i + 1] + piles[i];
        }

        // Initialize the dp array.
        for (int i = 0; i <= length; i++) {
            dp[i][length] = suffixSum[i];
        }

        // Start from the last index to store the future state first.
        for (int index = length - 1; index >= 0; index--) {
            for (int maxTillNow = length - 1; maxTillNow >= 1; maxTillNow--) {
                for (int X = 1; X <= 2 * maxTillNow && index + X <= length;
                     X++) {
                    dp[index][maxTillNow] = max(
                        dp[index][maxTillNow],
                        suffixSum[index] - dp[index + X][max(maxTillNow, X)]);
                }
            }
        }
        return dp[0][1];
    }
};
```

**Solution 4: (DP Bottom-up, Prefix Sum)**
```
Runtime: 57 ms
Memory: 10.1 MB
```
```c++
class Solution {
public:
    int stoneGameII(vector<int>& piles) {
        int n = piles.size();
        vector<int> suffixSums(n + 1);
        suffixSums[n - 1] = piles[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            suffixSums[i] = suffixSums[i + 1] + piles[i];
        }
        vector<vector<int>> dp(n, vector<int>(n + 1));
        for (int i = n - 1; i >= 0; i--) {
            for (int m = 1; m <= n; m++) {
                if (i + 2 * m >= n) {
                    dp[i][m] = suffixSums[i];
                } else {
                    for (int x = 1; x <= 2 * m; x++) {
                        int opponentScore = dp[i + x][max(x, m)];
                        int score = suffixSums[i] - opponentScore;
                        dp[i][m] = max(dp[i][m], score);
                    }
                }
            }
        }

        return dp[0][1];
    }
};
```

