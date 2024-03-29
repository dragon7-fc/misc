322. Coin Change

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.

**Example 1:**
```
Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
```

**Example 2:**
```
Input: coins = [2], amount = 3
Output: -1
```

**Note:**

* You may assume that you have an infinite number of each kind of coin.

# Summary
---
This article is for intermediate users. It introduces the following ideas: Backtracking, Dynamic programming.

# Solution
---
## Approach #1 (Brute force) [Time Limit Exceeded]
**Intuition**

The problem could be modeled as the following optimization problem : $\min_{x} \sum_{i=0}^{n - 1} x_i \\ \text{subject to} \sum_{i=0}^{n - 1} x_i*c_i = S$, where $S$ is the amount, $c_i$ is the coin denominations, $x_i$ is the number of coins with denominations $c_i$ used in change of amount $S$. We could easily see that $x_i = [{0, \frac{S}{c_i}}]$.

A trivial solution is to enumerate all subsets of coin frequencies $[x_0\dots x_{n - 1}]$ that satisfy the constraints above, compute their sums and return the minimum among them.

**Algorithm**

To apply this idea, the algorithm uses backtracking technique to generate all combinations of coin frequencies $[x_0\dots x_{n-1}]$ in the range $([{0, rac{S}{c_i}}])$ which satisfy the constraints above. It makes a sum of the combinations and returns their minimum or $-1$ in case there is no acceptable combination.

```java
public class Solution {    

    public int coinChange(int[] coins, int amount) {
        return coinChange(0, coins, amount);
    }

    private int coinChange(int idxCoin, int[] coins, int amount) {
        if (amount == 0)
            return 0;
        if (idxCoin < coins.length && amount > 0) {
            int maxVal = amount/coins[idxCoin];
            int minCost = Integer.MAX_VALUE;
            for (int x = 0; x <= maxVal; x++) {
                if (amount >= x * coins[idxCoin]) {
                    int res = coinChange(idxCoin + 1, coins, amount - x * coins[idxCoin]);
                    if (res != -1)
                        minCost = Math.min(minCost, res + x);
                }                    
            }	 		
            return (minCost == Integer.MAX_VALUE)? -1: minCost;
        }		 
        return -1;
    }  
}

// Time Limit Exceeded
```
**Complexity Analysis**

* Time complexity : $O(S^n)$. In the worst case, complexity is exponential in the number of the coins $n$. The reason is that every coin denomination $c_i$ could have at most $\frac{S}{c_i}$ values. Therefore the number of possible combinations is :
$\frac{S}{c_1}*\frac{S}{c_2}*\frac{S}{c_3}\ldots\frac{S}{c_n} = \frac{S^{n}}{{c_1}*{c_2}*{c_3}\ldots{c_n}}$

* Space complexity : $O(n)$. In the worst case the maximum depth of recursion is $n$. Therefore we need $O( n)$ space used by the system recursive stack.

## Approach #2 (Dynamic programming - Top down) [Accepted]
**Intuition**

Could we improve the exponential solution above? Definitely! The problem could be solved with polynomial time using Dynamic programming technique. First, let's define:

$F(S)$ - minimum number of coins needed to make change for amount $S$ using coin denominations $[{c_0\ldots c_{n-1}}]$

We note that this problem has an optimal substructure property, which is the key piece in solving any Dynamic Programming problems. In other words, the optimal solution can be constructed from optimal solutions of its subproblems. How to split the problem into subproblems? Let's assume that we know $F(S)$ where some change $val_1, val_2, \ldots$… for $S$ which is optimal and the last coin's denomination is CC. Then the following equation should be true because of optimal substructure of the problem:

$F(S) = F(S - C) + 1$

But we don't know which is the denomination of the last coin $C$. We compute $F(S - c_i)$ for each possible denomination $c_0, c_1, c_2 \ldots c_{n -1}$ and choose the minimum among them. The following recurrence relation holds:

$F(S) = \min_{i=0 ... n-1} { F(S - c_i) } + 1 \\ \text{subject to} \ S-c_i \geq 0$

$F(S) = 0 , \text{when} S = 0 \\ F(S) = -1 , \text{when} n = 0$

![322_coin_change_tree](img/322_coin_change_tree.png)

**Algorithm**

The idea of the algorithm is to build the solution of the problem from top to bottom. It applies the idea described above. It use backtracking and cut the partial solutions in the recursive tree, which doesn't lead to a viable solution. Тhis happens when we try to make a change of a coin with a value greater than the amount SS. To improve time complexity we should store the solutions of the already calculated subproblems in a table.

```java
public class Solution {

    public int coinChange(int[] coins, int amount) {        
        if (amount < 1) return 0;
        return coinChange(coins, amount, new int[amount]);
    }

    private int coinChange(int[] coins, int rem, int[] count) {
        if (rem < 0) return -1;
        if (rem == 0) return 0;
        if (count[rem - 1] != 0) return count[rem - 1];
        int min = Integer.MAX_VALUE;
        for (int coin : coins) {
            int res = coinChange(coins, rem - coin, count);
            if (res >= 0 && res < min)
                min = 1 + res;
        }
        count[rem - 1] = (min == Integer.MAX_VALUE) ? -1 : min;
        return count[rem - 1];
    }
}
```

**Complexity Analysis**

* Time complexity : $O(S*n)$. where S is the amount, n is denomination count. In the worst case the recursive tree of the algorithm has height of $S$ and the algorithm solves only $S$ subproblems because it caches precalculated solutions in a table. Each subproblem is computed with $n$ iterations, one by coin denomination. Therefore there is $O(S*n)$ time complexity.

* Space complexity : $O(S)$, where $S$ is the amount to change We use extra space for the memoization table.

## Approach #3 (Dynamic programming - Bottom up) [Accepted]
**Algorithm**

For the iterative solution, we think in bottom-up manner. Before calculating $F(i)$, we have to compute all minimum counts for amounts up to $i$. On each iteration $i$ of the algorithm $F(i)$ is computed as $\min_{j=0 \ldots n-1}{F(i -c_j)} + 1$

![322_coin_change_table](img/322_coin_change_table.png)

In the example above you can see that:

```
F(3) =min{F(3−c1),F(3−c2),F(3−c)}+1
=min{F(3−1),F(3−2),F(3−3)}+1
=min{F(2),F(1),F(0)}+1
=min{1,1,0}+1
=1
```

```java
public class Solution {
    public int coinChange(int[] coins, int amount) {
        int max = amount + 1;             
        int[] dp = new int[amount + 1];  
        Arrays.fill(dp, max);  
        dp[0] = 0;   
        for (int i = 1; i <= amount; i++) {
            for (int j = 0; j < coins.length; j++) {
                if (coins[j] <= i) {
                    dp[i] = Math.min(dp[i], dp[i - coins[j]] + 1);
                }
            }
        }
        return dp[amount] > amount ? -1 : dp[amount];
    }
}
```

**Complexity Analysis**

* Time complexity : $O(S*n)$. On each step the algorithm finds the next $F(i)$ in $n$ iterations, where $1\leq i \leq S$. Therefore in total the iterations are $S*n$.
* Space complexity : $O(S)$. We use extra space for the memoization table.

# Submissions
---
**Solution 1: (Dynamic programming - Top down)**
```
Runtime: 1820 ms
Memory Usage: 17.5 MB
```
```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def coinChange(coins, rem, count):
            if rem < 0:
                return -1
            if rem == 0:
                return 0
            if count[rem - 1] != 0:
                return count[rem - 1];
            min_ = float('inf')
            for coin in coins:
                res = coinChange(coins, rem - coin, count);
                if res >= 0 and res < min_:
                    min_ = 1 + res;
            count[rem - 1] = -1 if (min_ == float('inf')) else min_
            return count[rem - 1]
        
        if amount < 1:
            return 0
        return coinChange(coins, amount, [0 for _ in range(amount)])
```

**Solution 2: (DP Top-Down)**
```
Runtime: 1128 ms
Memory Usage: 43.1 MB
```
```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @functools.lru_cache(None)
        def coinChange(rem):
            if rem < 0:
                return -1
            if rem == 0:
                return 0
            min_ = float('inf')
            for coin in coins:
                res = coinChange(rem - coin)
                if res >= 0 and res < min_:
                    min_ = 1 + res
            return -1 if (min_ == float('inf')) else min_

        if amount < 1:
            return 0
        return coinChange(amount)
        
```

**Solution 3: (Dynamic programming - Bottom up)**
```
Runtime: 1348 ms
Memory Usage: 13 MB
```
```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(amount+1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[-1] if dp[-1] != float('inf') else -1    
```

**Solution 4: (DP Bottom-Up)**
```
Runtime: 1280 ms
Memory Usage: 13.2 MB
```
```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1 
```

**Solution 5: (Dynamic programming - Bottom up)**
```
Runtime: 148 ms
Memory Usage: 14.3 MB
```
```c++
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        // we initialise with amount+1 beecause max we will need is "amount" steps(if max coin value=1)
        std::vector<int> dp(amount+1, amount+1);

        dp[0]=0;
        // we will do a bottom up dp to calulate for each target the min. no. of steps 
        // and build it up till the target amount
        for( int i=1; i<=amount; i++){

            //loop thorugh the coins collection, and if teh current target(i) >= current_coin, then
            // store the minimum of dp[i](min. steps to get i till now) and (dp[i-val] +1) { +1, is for the inclusion of 
            // current coin 'val' }
            for( auto val: coins){
                if( val <= i)
                    dp[i]= min( dp[i], dp[i-val]+1);
            }
        }

        // if dp[amount] hasnt been changed that means we cant get the current target with our coins collection
        return (dp[amount] == (amount+1)) ? -1: dp[amount];
    }
};
```

**Solution 5: (Heap)**
```
Runtime: 972 ms
Memory Usage: 14.9 MB
```
```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return -1
        seen = set()
        heap = [(0,amount)]
        while heap:
            depth, curr = heapq.heappop(heap)
            if curr == 0:
                return depth
            for coin in coins:
                currentAmount = curr - coin
                if currentAmount >= 0 and currentAmount not in seen:
                    seen.add(currentAmount)
                    heapq.heappush(heap, (depth+1, currentAmount))
        return -1
```
