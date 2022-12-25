2291. Maximum Profit From Trading Stocks

You are given two **0-indexed** integer arrays of the same length `present` and `future` where `present[i]` is the current price of the `i`th stock and `future[i]` is the price of the `i`th stock a year in the future. You may buy each stock at most once. You are also given an integer `budget` representing the amount of money you currently have.

Return the maximum amount of profit you can make.

 

**Example 1:**
```
Input: present = [5,4,6,2,3], future = [8,5,4,3,5], budget = 10
Output: 6
Explanation: One possible way to maximize your profit is to:
Buy the 0th, 3rd, and 4th stocks for a total of 5 + 2 + 3 = 10.
Next year, sell all three stocks for a total of 8 + 3 + 5 = 16.
The profit you made is 16 - 10 = 6.
It can be shown that the maximum profit you can make is 6.
```

**Example 2:**
```
Input: present = [2,2,5], future = [3,4,10], budget = 6
Output: 5
Explanation: The only possible way to maximize your profit is to:
Buy the 2nd stock, and make a profit of 10 - 5 = 5.
It can be shown that the maximum profit you can make is 5.
```

**Example 3:**
```
Input: present = [3,3,12], future = [0,3,15], budget = 10
Output: 0
Explanation: One possible way to maximize your profit is to:
Buy the 1st stock, and make a profit of 3 - 3 = 0.
It can be shown that the maximum profit you can make is 0.
```

**Constraints:**

* `n == present.length == future.length`
* `1 <= n <= 1000`
* `0 <= present[i], future[i] <= 100`
* `0 <= budget <= 1000`

# Submissions
---
**Solution 1: (DP Top-Down)**
```
Runtime: 2746 ms
Memory: 512.4 MB
```
```python
class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        canEarn = []
        for i in range(len(present)):
            if present[i] <= budget and future[i] - present[i] > 0:
                canEarn.append((present[i], future[i] - present[i]))

        @cache
        def dfs(i, budget):
            if budget < 0 or i < 0:
                return 0
            if budget < canEarn[i][0]:
                return dfs(i - 1, budget)
            else:
                return max(dfs(i - 1, budget), dfs(i - 1, budget - canEarn[i][0]) + canEarn[i][1])
        
        return dfs(len(canEarn) - 1, budget)
```
