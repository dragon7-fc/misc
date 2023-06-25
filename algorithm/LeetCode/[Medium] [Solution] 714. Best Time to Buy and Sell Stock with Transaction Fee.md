714. Best Time to Buy and Sell Stock with Transaction Fee

Your are given an array of integers `prices`, for which the `i`-th element is the price of a given stock on day `i`; and a non-negative integer `fee` representing a transaction fee.

You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction. You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

Return the maximum profit you can make.

**Example 1:**
```
Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
* Buying at prices[0] = 1
* Selling at prices[3] = 8
* Buying at prices[4] = 4
* Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
```

**Note:**

* `0 < prices.length <= 50000`.
* `0 < prices[i] < 50000`.
* `0 <= fee < 50000`.

# Solution
---
## Approach #1: Dynamic Programming [Accepted]
**Intuition and Algorithm**

At the end of the `i`-th day, we maintain `cash`, the maximum profit we could have if we did not have a share of stock, and `hold`, the maximum profit we could have if we owned a share of stock.

To transition from the `i`-th day to the `i+1`-th day, we either sell our stock `cash = max(cash, hold + prices[i] - fee)` or buy a stock `hold = max(hold, cash - prices[i])`. At the end, we want to return `cash`. We can transform cash first without using temporary variables because selling and buying on the same day can't be better than just continuing to hold the stock.

```Python
class Solution(object):
    def maxProfit(self, prices, fee):
        cash, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])
        return cash
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the number of prices.

* Space Complexity: $O(1)$, the space used by cash and hold.

# Submissions
---
**Solution: (Dynamic Programming)**
```
Runtime: 820 ms
Memory Usage: 20.7 MB
```
```python
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)  # sell stock
            hold = max(hold, cash - prices[i])  # buy stock
            
        return cash
```

**Solution 1: (DP, Array)**
```
Runtime: 928 ms
Memory Usage: 19.4 MB
```
```python
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        N = len(prices)
        cash, hold = [0]*N, [float('-inf')]*N
        hold[0] = -prices[0]
        for day in range(1, len(prices)):
            cash[day] = max(cash[day-1], hold[day-1] + prices[day] - fee)  # sell stock
            hold[day] = max(hold[day-1], cash[day-1] - prices[day])  # buy stock

        return cash[-1]
```

**Solution 2: (DP)**
```
Runtime: 804 ms
Memory Usage: 19.7 MB
```
```python
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        sell, buy = 0, float('-inf')  # sell = cash, buy = hold
        for i in range(len(prices)):
            buy = max(buy, sell - prices[i])
            sell = max(sell, buy + prices[i] - fee)
        return sell
```

**Solution 3: (DP, Array)**
```
Runtime: 904 ms
Memory Usage: 19.3 MB
```
```python
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        N = len(prices)
        sell, buy = [0]*N, [float('-inf')]*N
        for day in range(len(prices)):
            buy[day] = max(buy[day-1], sell[day-1] - prices[day])
            sell[day] = max(sell[day-1], buy[day-1] + prices[day] - fee)
            
        return sell[-1]
```

**Solution 4: (DP Top-Down)**
```
Runtime: 1368 ms
Memory Usage: 259.1 MB
```
```python
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        N = len(prices)
        
        @functools.lru_cache(None)
        def dfs(i, bought):
            if i >= N:
                return 0
            #if bought previously, we have 2 option:-
            # sell the prvious stock today or skip this day
            if bought:
                return max(dfs(i+1, False) + prices[i] - fee, dfs(i+1, bought))

            #else if we can buy a new stock, then we again have 2 option:-
            #buy the current stock or skip over it
            else:
                return max(dfs(i+1, True) - prices[i], dfs(i+1, bought))

        return dfs(0, False)
```

**Solution 5: (Greedy)**
```
Runtime: 660 ms
Memory Usage: 19.2 MB
```
```python
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        Min, Max = prices[0], 0
    
        for price in prices:
            profit = price - Min - fee  # max profit = max price - min price
            if profit > 0:  # find max profit
                Max += profit
                Min = price - fee
            elif price < Min:  # find min price
                Min = price

        return Max
```

**Solution 6: (DP Bottom-Up)**
```
Runtime: 116 ms
Memory: 59.7 MB
```
```c++
class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        int n = prices.size();
        vector<int> buy(n), sell(n);
        buy[0] = -prices[0];
        for (int i = 1; i < n; i ++) {
            buy[i] = max(sell[i-1] - prices[i], buy[i-1]);
            sell[i] = max(buy[i-1] + prices[i] - fee, sell[i-1]);
        }
        return sell.back();
    }
};
```
