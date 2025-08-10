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

**Constraints:**

* `0 <= k <= 109`
* `0 <= prices.length <= 104`
* `0 <= prices[i] <= 1000`

# Submissions
---
**Solution 1: (Dynamic Programming)**
```
Runtime: 176 ms
Memory Usage: 25.7 MB
```
```python
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        # solve special cases
        if not prices or k==0:
            return 0

        if 2*k > n:
            res = 0
            for i, j in zip(prices[1:], prices[:-1]):
                res += max(0, i - j)
            return res

        # dp[i][used_k][ishold] = balance
        # ishold: 0 nothold, 1 hold
        dp = [[[-math.inf]*2 for _ in range(k+1)] for _ in range(n)]

        # set starting value
        dp[0][0][0] = 0
        dp[0][1][1] = -prices[0]

        # fill the array
        for i in range(1, n):
            for j in range(k+1):
                # transition equation
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]+prices[i])
                # you can't hold stock without any transaction
                if j > 0:
                    dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0]-prices[i])

        res = max(dp[n-1][j][0] for j in range(k+1))
        return res
```

**Solution 2: (Merging)**
```
Runtime: 80 ms
Memory Usage: 14.8 MB
```
```python
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        # solve special cases
        if not prices or k == 0:
            return 0

        # find all consecutively increasing subsequence
        transactions = []
        start = 0
        end = 0
        for i in range(1, n):
            if prices[i] >= prices[i-1]:
                end = i
            else:
                if end > start:
                    transactions.append([start, end])
                start = i
        if end > start:
            transactions.append([start, end])

        while len(transactions) > k:
            # check delete loss
            delete_index = 0
            min_delete_loss = math.inf
            for i in range(len(transactions)):
                t = transactions[i]
                profit_loss = prices[t[1]] - prices[t[0]]
                if profit_loss < min_delete_loss:
                    min_delete_loss = profit_loss
                    delete_index = i

            # check merge loss
            merge_index = 0
            min_merge_loss = math.inf
            for i in range(1, len(transactions)):
                t1 = transactions[i-1]
                t2 = transactions[i]
                profit_loss = prices[t1[1]] - prices[t2[0]]
                if profit_loss < min_merge_loss:
                    min_merge_loss = profit_loss
                    merge_index = i

            # delete or merge
            if min_delete_loss <= min_merge_loss:
                transactions.pop(delete_index)
            else:
                transactions[merge_index - 1][1] = transactions[merge_index][1]
                transactions.pop(merge_index)

        return sum(prices[j]-prices[i] for i, j in transactions)
```

**Solution 3: (DP Bottom-Up)**
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

**Solution 4: (DP, Top-Down DP)**
```
Runtime: 568 ms
Memory Usage: 106.4 MB
```
```python
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        N = len(prices)
        if not N: return 0
        if N < 2 * k:
            return sum([max(0, prices[i+1] - prices[i]) for i in range(N - 1)])

        max_price = 1001
        @functools.lru_cache(None)
        def max_profit_from(idx=0, tr_left=k, buy_price=max_price):
            if not tr_left: return 0
            if idx == N - 1: return max(0, prices[idx] - buy_price)

            profit = prices[idx] - buy_price
            profit_when_buying = max_profit_from(idx + 1, tr_left, prices[idx])
            if profit <= 0: return profit_when_buying
            profit_when_sold = profit + max_profit_from(idx + 1, tr_left - 1, max_price)
            profit_when_pass = max_profit_from(idx + 1, tr_left, buy_price)

            return max(profit_when_sold, profit_when_buying, profit_when_pass)

        return max_profit_from()
```

**Solution 5: (DP Bottom-Up)**
```
Runtime: 11 ms
Memory Usage: 10.8 MB
```
```c++
class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        int N = prices.size();
		vector<vector<int>> ahead(2,vector<int>(k+1,0)),curr(2,vector<int>(k+1,0));
		for(int ind=N-1;ind>=0;ind--){
			for(int buy=0;buy<=1;buy++){
				for(int trans=0;trans<k;trans++){
					long profit = 0;
					if(buy==0) profit = max(-prices[ind] + ahead[1][trans] ,ahead[0][trans]);
					else profit = max(prices[ind] + ahead[0][trans+1] ,ahead[1][trans]);
					curr[buy][trans] = profit;
				}
			}
			ahead = curr;
		}
		return ahead[0][0];
    }
};
```

**Solution 6: (DP Top-Down)**
```
Runtime: 27 ms
Memory Usage: 13.2 MB
```
```c++
class Solution {
    int func(int i,int buy,int cap,vector<int>& prices,vector<vector<vector<int>>>& dp){
        int n=prices.size();
        if(cap==0) return 0; // if we dont have any Tx left just return 0;
        if(i==n) return 0;  // index reached end of the array.
        if(dp[i][buy][cap]!=-1) return dp[i][buy][cap]; 
        
        int profit=0;     //      pick                                 notpick
        if(buy){      //( we are buying the stock)   or     (we are not buying the stock)
            profit=max(-prices[i]+func(i+1,0,cap,prices,dp),0+func(i+1,1,cap,prices,dp)); 
        }else {      //we are selling(hence we can buy again) ,or   will not sell this turn.                              
            profit=max(prices[i]+func(i+1,1,cap-1,prices,dp),0+func(i+1,0,cap,prices,dp));
        }
        return dp[i][buy][cap]=profit;
    }
public:
    int maxProfit(int k, vector<int>& prices) {
        int n=prices.size();
        vector<vector<vector<int>>> dp(n,vector<vector<int>>(2,vector<int>(k+1,-1)));
        return func(0,1,k,prices,dp); //(index==0, buy==1(initially we can buy) , k (number of Tx), prices, Memorized space));
    }
};
```

**Solution 7: (DP Bottom-Up 1-D)**

        -----       -----
    3,  2,  6,  5,  0,  3
   -3  -2  -2  -2   0   0
       -1   4   4   4   4
           -7  -1   4   4
               -2  -1   7

```
Runtime: 2 ms, Beats 88.77%
Memory: 17.09 MB, Beats 65.50%
```
```c++
class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        int n = prices.size(), i, j;
        vector<int> pre(k*2, -1e5), cur(k*2, -1e5);
        pre[0] = -prices[0];
        for (i = 1; i < n; i ++) {
            cur[0] = max(pre[0], -prices[i]);
            for (j = 1; j < 2*k; j ++) {
                if (j%2) {
                    cur[j] = max(pre[j], pre[j-1] + prices[i]);
                } else {
                    cur[j] = max(pre[j], pre[j-1] - prices[i]);
                }
            }
            pre = move(cur);
            cur.resize(2*k, -1e5);
        }
        return max(0, *max_element(pre.begin(), pre.end()));
    }
};
```
