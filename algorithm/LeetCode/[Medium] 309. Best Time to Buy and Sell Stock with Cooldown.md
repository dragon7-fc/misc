309. Best Time to Buy and Sell Stock with Cooldown

Say you have an array for which the $i{th}$ element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

1. You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
1. After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

**Example:**
```
Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]
```

# Submissions
---
**Solution 1: (DP Bottom-Up)**
```
Runtime: 44 ms
Memory Usage: N/A
```
```python
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if not prices:
            return 0

        buy = [0]*n
        sell = [0]*n
        cool = [0]*n
        buy[0] = -prices[0]

        for i in range(1, n):
            buy[i] = max(buy[i-1], cool[i-1] - prices[i])
            sell[i] = max(sell[i-1], buy[i-1] + prices[i])
            cool[i] = max(cool[i-1], sell[i-1])

        return sell[-1]
```

**Solution 2: (DP Bottom-Up)**

This is very similar to problem 714. Best Time to Buy and Sell Stock with Transaction Fee  
The strategy is to keep 2 variables:  
cash[i]: the max profit we have on day i if we don't have stock  
hold[i]: the max profit we have on day i if we have a stock

The transition function from day i to day i+1:
* for cash[i+1], we either don't do anything, so remain cash[i]; or we sell to stock hold in hand
* for hold[i+1], we either don't do anything, so remain hold[i]; or we buy a stock, but use the cash from two days ago, i.e. cash[i-1], becasue of the cooldown requirement

```
Runtime: 40 ms
Memory Usage: 13.1 MB
```
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        if N <=1 :
            return 0
        cash = [0]*N
        cash[1] = max(0, prices[1]-prices[0])
        hold = [float('-inf')] * N
        hold[0] = [-prices[0]]
        hold[1] = max(-prices[0], -prices[1])
        for day in range(2,len(prices)):
            cash[day] = max(cash[day-1], hold[day-1]+prices[day])
            hold[day] = max(hold[day-1], cash[day-2]-prices[day])
            
        return cash[-1]
```

**Solution 3: (DP Top-Down)**
```
Runtime: 44 ms
Memory Usage: 18 MB
```
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @lru_cache(None)
        def dp(i, bs):
            if i>=n:
                return 0
            if bs==1: #should buy
                op1 = -prices[i] + dp(i+1, bs^1) # buy now and possibly the next day
                op2 = dp(i+1, bs)                # don't buy now
            else: # should sell
                op1 = prices[i] + dp(i+2, bs^1)  # sell now and possibly buy only two days later
                op2 = dp(i+1, bs)                # don't sell now
            return max(op1, op2)
        
        return dp(0, 1)
```

**Solution 4: (DP Bottom-Up)**
```
Runtime: 22 ms
Memory: 14.2 MB
```
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        if N == 1:
            return 0
        buy = [0]*N
        sell = [0]*N
        buy[0] = -prices[0]
        buy[1] = max(-prices[0], -prices[1])
        sell[1] = max(0, prices[1] - prices[0])
        for i in range(2, N):
            sell[i] = max(sell[i-1], buy[i-1] + prices[i])
            buy[i] = max(buy[i-1], sell[i-2] - prices[i])
        return sell[-1]
```

**Solution 5: (DP Bottom-Up)**

               v
prices   1, 2, 3, 0, 2
b       -1 -1 -1  1  
s           1  2  2  3
                     ^ans

```
Runtime: 3 ms, Beats 35.45%
Memory: 16.00 MB, Beats 71.19%
```
```c++
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size(), i;
        vector<vector<int>> dp(n, vector<int>(2));
        dp[0][0] = -prices[0];
        for (i = 1; i < n; i ++) {
            if (i > 1) {
                dp[i][0] = max(dp[i-1][0], dp[i-2][1] - prices[i]);
            } else {
                dp[i][0] = max(dp[i-1][0], -prices[i]);
            }
            dp[i][1] = max(dp[i-1][1], prices[i] + dp[i-1][0]);
        }
        return dp[n-1][1];
    }
};

```
