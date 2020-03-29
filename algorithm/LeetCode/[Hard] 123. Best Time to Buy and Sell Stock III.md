123. Best Time to Buy and Sell Stock III

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

**Example 1:**
```
Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
```

**Example 2:**
```
Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
```

**Example 3:**
```
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
```

# Submissions
---
**Solution 1: (DP)**
```
Runtime: 80 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        sell, sell2, buy, buy2 = 0, 0, -float('inf'), -float('inf')
        for i in range(len(prices)):
            buy = max(buy, -prices[i])
            sell = max(sell, buy + prices[i])
            buy2 = max(buy2, sell - prices[i])
            sell2 = max(sell2, buy2 + prices[i])
        return sell2
```

**Solution 2: (DP Array)**
```
Runtime: 84 ms
Memory Usage: 14.7 MB
```
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        if N == 0:
            return 0
        sell, buy = [0]*N, [float('-inf')]*N
        sell2, buy2 = [0]*N, [float('-inf')]*N
        buy[0], buy2[0] = -prices[0], -prices[0]
        for day in range(1, len(prices)):
            buy[day] = max(buy[day-1], -prices[day])
            sell[day] = max(sell[day-1], buy[day-1] + prices[day])
            buy2[day] = max(buy2[day-1], sell[day-1] - prices[day])
            sell2[day] = max(sell2[day-1], buy2[day-1] + prices[day])
            
        return sell2[-1]
```