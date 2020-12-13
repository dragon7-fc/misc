1690. Stone Game VII

Alice and Bob take turns playing a game, with **Alice starting first**.

There are `n` stones arranged in a row. On each player's turn, they can **remove** either the leftmost stone or the rightmost stone from the row and receive points equal to the **sum** of the remaining stones' values in the row. The winner is the one with the higher score when there are no stones left to remove.

Bob found that he will always lose this game (poor Bob, he always loses), so he decided to **minimize the score's difference**. Alice's goal is to **maximize the difference** in the score.

Given an array of integers `stones` where `stones[i]` represents the value of the `i`th stone from the left, return the **difference** in Alice and Bob's score if they both play **optimally**.

 

**Example 1:**
```
Input: stones = [5,3,1,4,2]
Output: 6
Explanation: 
- Alice removes 2 and gets 5 + 3 + 1 + 4 = 13 points. Alice = 13, Bob = 0, stones = [5,3,1,4].
- Bob removes 5 and gets 3 + 1 + 4 = 8 points. Alice = 13, Bob = 8, stones = [3,1,4].
- Alice removes 3 and gets 1 + 4 = 5 points. Alice = 18, Bob = 8, stones = [1,4].
- Bob removes 1 and gets 4 points. Alice = 18, Bob = 12, stones = [4].
- Alice removes 4 and gets 0 points. Alice = 18, Bob = 12, stones = [].
The score difference is 18 - 12 = 6.
```

**Example 2:**
```
Input: stones = [7,90,5,1,100,10,10,2]
Output: 122
```

**Constraints:**

* `n == stones.length`
* `2 <= n <= 1000`
* `1 <= stones[i] <= 1000`

# Submissions
---
**Solution 1: (DP Bottom-Up)**
```
Runtime: 5136 ms
Memory Usage: 38.8 MB
```
```python
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        presum = [0] + stones[:]
        for i in range(1, len(presum)):
            presum[i] += presum[i-1]

        def score(i, j):
            j += 1
            return presum[j] - presum[i]

        n = len(stones)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                dp[i][j] = max(score(i+1, j) - dp[i+1][j], score(i, j-1) - dp[i][j-1])

        return dp[0][n-1]
```

**Solution 2: (DP Top-Down)**
```
Runtime: 6832 ms
Memory Usage: 123.3 MB
```
```python
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        accum_sum = [0]
        for i in stones:
            accum_sum.append(i+accum_sum[-1])
        
        n = len(stones)
        dp = [[-1 for _ in range(n)] for _ in range(n)]
                
        def help(i, j):
            if i>j:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            
            a = accum_sum[j+1]-accum_sum[i+1] -  help(i+1, j)  
            b = accum_sum[j]-accum_sum[i] -  help(i, j-1)
            
            dp[i][j] = max(a, b)
            return max(a, b)
        
        return help(0, len(stones)-1)
```