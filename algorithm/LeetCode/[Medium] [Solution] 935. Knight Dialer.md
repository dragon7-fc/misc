935. Knight Dialer

A chess knight can move as indicated in the chess diagram below:

![935_knight](img/935_knight.png) ![935_keypad](img/935_keypad.png)

This time, we place our chess knight on any numbered key of a phone pad (indicated above), and the knight makes `N-1` hops.  Each hop must be from one key to another numbered key.

Each time it lands on a key (including the initial placement of the knight), it presses the number of that key, pressing `N` digits total.

How many distinct numbers can you dial in this manner?

Since the answer may be large, output the answer modulo `10^9 + 7`.

 

**Example 1:**

```
Input: 1
Output: 10
```

**Example 2:**

```
Input: 2
Output: 20
```

**Example 3:**

```
Input: 3
Output: 46
``` 

**Note:**

* `1 <= N <= 5000`

# Solution
---
## Approach 1: Dynamic Programming
**Intuition**

Let `f(start, n)` be the number of ways to dial an `n` digit number, where the knight starts at square `start`. We can create a recursion, writing this in terms of `f(x, n-1)`'s.

**Algorithm**

By hand or otherwise, have a way to query what moves are available at each square. This implies the exact recursion for `f`. For example, from `1` we can move to `6, 8`, so `f(1, n) = f(6, n-1) + f(8, n-1)`.

After, let's keep track of `dp[start] = f(start, n)`, and update it for each n from `1, 2, ..., N`.

At the end, the answer is `f(0, N) + f(1, N) + ... + f(9, N) = sum(dp)`.

```python
class Solution(object):
    def knightDialer(self, N):
        MOD = 10**9 + 7
        moves = [[4,6],[6,8],[7,9],[4,8],[3,9,0],[],
                     [1,7,0],[2,6],[1,3],[2,4]]

        dp = [1] * 10
        for hops in xrange(N-1):
            dp2 = [0] * 10
            for node, count in enumerate(dp):
                for nei in moves[node]:
                    dp2[nei] += count
                    dp2[nei] %= MOD
            dp = dp2
        return sum(dp) % MOD
```

**Complexity Analysis**

* Time Complexity: $O(N)$.

* Space Complexity: $O(1)$.

# Submissions
---
**Solution 1: (Dynamic Programming Bottom-Up)**
```
Runtime: 1080 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def knightDialer(self, N: int) -> int:
        MOD = 10**9 + 7
        moves = [[4,6],[6,8],[7,9],[4,8],[3,9,0],[],
                     [1,7,0],[2,6],[1,3],[2,4]]

        dp = [1] * 10
        for hops in range(N-1):
            dp2 = [0] * 10
            for node, count in enumerate(dp):
                for nei in moves[node]:
                    dp2[nei] += count
                    dp2[nei] %= MOD
            dp = dp2
        return sum(dp) % MOD
```

**Solution 2: (DP Top-Down)**
```
Runtime: 3344 ms
Memory Usage: 74.9 MB
```
```python
class Solution:
    def knightDialer(self, N: int) -> int:
        moves = [[4,6],[6,8],[7,9],[4,8],[3,9,0],[],
                     [1,7,0],[2,6],[1,3],[2,4]]
        
        @functools.lru_cache(None)
        def dfs(number, rounds):
            if rounds == 1:
                return 1
            return sum([dfs(next_number, rounds-1) for next_number in moves[number]])

        return sum([dfs(number, N) for number in range(0,10)]) % (10**9+7)
```