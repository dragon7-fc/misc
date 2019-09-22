121. Best Time to Buy and Sell Stock

Say you have an array for which the $i^{th}$ element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

**Example 1:**
```
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
```

**Example 2:**
```
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
```

# Solution
---
We need to find out the maximum difference (which will be the maximum profit) between two numbers in the given array. Also, the second number (selling price) must be larger than the first one (buying price).

In formal terms, we need to find $\max(prices[j] - prices[i])$, for every $i$ and $j$ such that $j > i$.

## Approach 1: Brute Force

```java
public class Solution {
    public int maxProfit(int prices[]) {
        int maxprofit = 0;
        for (int i = 0; i < prices.length - 1; i++) {
            for (int j = i + 1; j < prices.length; j++) {
                int profit = prices[j] - prices[i];
                if (profit > maxprofit)
                    maxprofit = profit;
            }
        }
        return maxprofit;
    }
}
```

**Complexity Analysis**

* Time complexity : $O(n^2)$. Loop runs $\dfrac{n (n-1)}{2}$ times.

* Space complexity : $O(1)$. Only two variables - $\text{maxprofit}$ and $\text{profit}$ are used.

## Approach 2: One Pass
**Algorithm**

Say the given array is:

[7, 1, 5, 3, 6, 4]

If we plot the numbers of the given array on a graph, we get:

![profit_graph](img/121_profit_graph.png)

```java
public class Solution {
    public int maxProfit(int prices[]) {
        int minprice = Integer.MAX_VALUE;
        int maxprofit = 0;
        for (int i = 0; i < prices.length; i++) {
            if (prices[i] < minprice)
                minprice = prices[i];
            else if (prices[i] - minprice > maxprofit)
                maxprofit = prices[i] - minprice;
        }
        return maxprofit;
    }
}
```

**Complexity Analysis**

* Time complexity : $O(n)$. Only a single pass is needed.

* Space complexity : $O(1)$. Only two variables are used.

# Submissions
---
**Solution:**
```
Runtime: 68 ms
Memory Usage: 14.7 MB
```
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = sys.maxsize
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i]-min_price > max_profit:
                max_profit = prices[i]-min_price
        return max_profit
```