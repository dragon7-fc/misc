188. Best Time to Buy and Sell Stock IV

Say you have an array for which the i-th element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most **k** transactions.

**Note:**

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

**Example 1:**
```
Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
```

**Example 2:**
```
Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
```

# Submissions
---
**Solution 1: (DP Bottom-Up)**
```
Runtime: 112 ms
Memory Usage: 13.6 MB
```
```python
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k == 0:
            return 0
        n = len(prices)

        #PRECHECK if 2*k >= n  that means we just need to count everyday's profit no need to DP 
        if 2*k >= n:
            res = 0
            for i in range(1, n):
                res += max(prices[i] - prices[i-1], 0)
            return res

        #dp status of buy and sell, only need One-Dimention
        bsk = [0 for i in range(2*k)]   #buy_1 sell_1 buy_2 sell_2 ==> buy_k sell_k (k times)
        for b in range(2*k):
            if b%2 == 0:
                bsk[b] = -prices[0]

        for i in range(1, n):
            bsk[0] = max(bsk[0], -prices[i])
            #for buys
            for j in range(2, 2*k, 2):
                bsk[j] = max(bsk[j-1]-prices[i], bsk[j])
            #for sells
            for o in range(1, 2*k, 2):
                bsk[o] = max(bsk[o-1]+prices[i], bsk[o])
        return bsk[2*k-1]
```