3573. Best Time to Buy and Sell Stock V

You are given an integer array `prices` where `prices[i]` is the price of a stock in dollars on the ith day, and an integer `k`.

You are allowed to make at most `k` transactions, where each transaction can be either of the following:

* **Normal transaction**: Buy on day `i`, then sell on a later day `j` where `i < j`. You profit `prices[j] - prices[i]`.

* **Short selling transaction**: Sell on day `i`, then buy back on a later day `j` where `i < j`. You profit `prices[i] - prices[j]`.

Note that you must complete each transaction before starting another. Additionally, you can't buy or sell on the same day you are selling or buying back as part of a previous transaction.

Return the **maximum** total profit you can earn by making at most `k` transactions.

 

**Example 1:**
```
Input: prices = [1,7,9,8,2], k = 2

Output: 14

Explanation:

We can make $14 of profit through 2 transactions:
A normal transaction: buy the stock on day 0 for $1 then sell it on day 2 for $9.
A short selling transaction: sell the stock on day 3 for $8 then buy back on day 4 for $2.
```

**Example 2:**
```
Input: prices = [12,16,19,19,8,1,19,13,9], k = 3

Output: 36

Explanation:

We can make $36 of profit through 3 transactions:
A normal transaction: buy the stock on day 0 for $12 then sell it on day 2 for $19.
A short selling transaction: sell the stock on day 3 for $19 then buy back on day 4 for $8.
A normal transaction: buy the stock on day 5 for $1 then sell it on day 6 for $19.
```

**Constraints:**

* `2 <= prices.length <= 10^3`
* `1 <= prices[i] <= 10^9`
* `1 <= k <= prices.length / 2`

# Submissions
---
**Solution 1: (DP Bottom-Up)**

188. Best Time to Buy and Sell Stock IV
v
| * dp[i][j][0] (complete)
| maximum profit after day i if exactly j transactions have been completed and we end the day holding no stock
| * dp[i][j][1] (buy)
| maximum profit after day i with exactly j completed transactions while holding one stock
* dp[i][j][2] (sell)
maximum profit after day i with exactly j completed transactions while holding a short position

dp[i][j][0] = max(dp[i−1][j][0], dp[i−1][j][1]) + prices[i], dp[i−1][j][2] − prices[i])
dp[i][j][1] = max(dp[i−1][j][1], dp[i−1][j−1][0] − prices[i])
dp[i][j][2] = max(dp[i−1][j][2], dp[i−1][j−1][0] + prices[i])


dp[i][j][0]:
    dp[i-1][j]   dp[i][j]
0       x        dp[i][j][0]    (same transaction)
1       x
2       x
----------------------------------

dp[i][j][1]:
    dp[i-1][j-1]
0       x
1      
2        

    dp[i-1][j]   dp[i][j]
0
1       x        dp[i][j][1]     (new transaction)
2
--------------------------------

dp[i][j][2]:
    dp[i-1][j-1]
0       x
1      
2        

    dp[i-1][j]   dp[i][j]
0
1       
2       x        dp[i][j][2]     (new transaction)


    prices = [1,       7,      9,        8,       2], k = 2 | k
            ------------------------------------------------|-----
dp
0
1                                                              0
2
       --------------------------------------------------------------
0              0        6       8         8        8               
1             -1       -1      -1        -1       -1           1   
2              1        7       9         9        9               
       ----------------------------------------------
0              0       6       8         8       14
1             -1      -1      -1         0        6           2
2              1       6      15        16       10

```
Runtime: 739 ms, Beats 35.09%
Memory: 344.59 MB, Beats 29.65%
```
```c++
class Solution {
public:
    long long maximumProfit(vector<int>& prices, int k) {
        int n = prices.size();
        vector<vector<vector<long long>>> dp(
            n, vector<vector<long long>>(k + 1, vector<long long>(3, 0)));
        // initialize the state on day 0
        for (int j = 1; j <= k; j++) {
            dp[0][j][1] = -prices[0];
            dp[0][j][2] = prices[0];
        }

        for (int i = 1; i < n; i++) {
            for (int j = 1; j <= k; j++) {
                dp[i][j][0] =
                    max(dp[i - 1][j][0], max(dp[i - 1][j][1] + prices[i],
                                             dp[i - 1][j][2] - prices[i]));
                dp[i][j][1] =
                    max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i]);
                dp[i][j][2] =
                    max(dp[i - 1][j][2], dp[i - 1][j - 1][0] + prices[i]);
            }
        }

        return dp[n - 1][k][0];
    }
};
```

**Solution 2: (DP Bottom-Up)**

    prices = [1,       7,      9,        8,       2], k = 2
            ------------------------------------------
        res   0        6       8         8        8
      bought -1       -1      -1        -1       -1     k = 1
        sold  1        7       9         9        9
       ----------------------------------------------
        res    0       6       8         8       14
      bought  -1      -1      -1         0        6     k = 2
        sold   1       6      15        16       10

```
Runtime: 51 ms, Beats 100.00%
Memory: 29.88 MB, Beats 100.00%
```
```c++
class Solution {
public:
    long long maximumProfit(vector<int>& prices, int k) {
        vector<long long> res(k + 1), bought(k, -1e9), sold(k);
        for (int a : prices) {
            for (int j = k; j >= 1; --j) {
                res[j] = max({res[j], bought[j - 1] + a, sold[j - 1] - a}); // transaction complete state
                bought[j - 1] = max(bought[j - 1], res[j - 1] - a);
                sold[j - 1] = max(sold[j - 1], res[j - 1] + a);
            }
        }
        return *max_element(res.begin(), res.end());
    }
};
```
