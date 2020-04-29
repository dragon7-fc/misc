1227. Airplane Seat Assignment Probability

`n` passengers board an airplane with exactly `n` seats. The first passenger has lost the ticket and picks a seat randomly. But after that, the rest of passengers will:

* Take their own seat if it is still available, 
* Pick other seats randomly when they find their seat occupied 

What is the probability that the n-th person can get his own seat?

 

**Example 1:**

```
Input: n = 1
Output: 1.00000
Explanation: The first person can only get the first seat.
```

**Example 2:**

```
Input: n = 2
Output: 0.50000
Explanation: The second person has a probability of 0.5 to get the second seat (when first person gets the first seat).
```

**Constraints:**

* `1 <= n <= 10^5`

# Submissions
---
**Solution 1: (DP, Bottom-Up)**

Each round we have 3 choices:

1. the 1st person gets his/her own seat. (with probability 1/n). Then the n-th person is sure (with probability 1) to get the n-th seat.
1. the 1st person gets the n-th person's seat. (with probability 1/n). Then the n-th person cannot (with probability 0) get the n-th seat.
1. the 1st person gets a seat between 2 and n-1 (with probability (n-2)/n). Assume the 1st person gets a-th seat. Then in the next round, we have 3 choices again:
    1. if the a-th person gets 1st seat (with probability 1/(n-1)), then this is just like 1st and a-th person swap their seats, it never affect our result for the n-th person.
    1. if the a-th person gets n-th seat (with probability 1/(n-1)), game over.
    1. if the a-th person gets a seat which is not 1st or n-th, (with probability (n-1-2)/(n-1)), we jump into a loop.
Therefore the dp pattern is dp[i] = 1.0 / (i+1) + 0.0 / (i+1) + dp[i-1] * (i-1) / (i+1), with dp[0]=1 for the case there's only one person. If you manually calculate it you'll find dp[i] is always 1/2 except the base condition.

```
Runtime: 804 ms
Memory Usage: 16.6 MB
```
```python
class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        # return 0.5 if n > 1 else 1.0
        
        dp = [0] * n
        dp[0] = 1.0
        for i in range(1, n):
            dp[i] = 1.0 / (i+1) +  dp[i-1] * (i-1) / (i+1) 
        return dp[-1]
```

**Solution 2: (DP Top-Down, RecursionError: maximum recursion depth exceeded)**
```python
class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        
        @functools.lru_cache(None)
        def dp(i):
            if i == 0:
                return 1
            return 1/(i+1) + (i-1)/(i+1) * dp(i-1)
        
        return dp(n-1)
```

**Solution 3: (DFS)**
```
Runtime: 1260 ms
Memory Usage: 101.5 MB
```
```python
class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n == 1: return 1.0
        #case 1: first person take his own seat
        #case 2: first person take second persons seat, will lead the second person into the same situation as person one
        return 1/n + (n-2) / n * self.nthPersonGetsNthSeat(n-1)
```

**Solution 4: (Brainteaser, Math)**

It is clear that answer is `1` when `n = 1`. When `n > 1`, it is clear that if first seat is taken before `n`th seat, `n`th person will take nth seat; otherwise, `n`th person won't take nth seat. As the seat is taken randomly, it is symmetric to take first seat or `n`th seat. As a result, the probably should be 0.5.
```
Runtime: 28 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
        
    def nthPersonGetsNthSeat(self, n: int) -> float:
        return 1 if n == 1 else 0.5
```