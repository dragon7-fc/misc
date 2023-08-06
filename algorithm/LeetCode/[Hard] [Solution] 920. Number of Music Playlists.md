920. Number of Music Playlists

Your music player contains `N` different songs and she wants to listen to `L` (not necessarily different) songs during your trip.  You create a playlist so that:

* Every song is played **at least once**
* A song can only be played again only if `K` other songs have been played

Return the number of possible playlists.  **As the answer can be very large, return it modulo** `10^9 + 7`.

 

**Example 1:**
```
Input: N = 3, L = 3, K = 1
Output: 6
Explanation: There are 6 possible playlists. [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1].
```

**Example 2:**
```
Input: N = 2, L = 3, K = 0
Output: 6
Explanation: There are 6 possible playlists. [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2, 1], [2, 1, 2], [1, 2, 2]
```

**Example 3:**
```
Input: N = 2, L = 3, K = 1
Output: 2
Explanation: There are 2 possible playlists. [1, 2, 1], [2, 1, 2]
```

**Note:**

* `0 <= K < N <= L <= 100`

# Submissions
---
## Approach 1: Dynamic Programming
**Intuition**

Let `dp[i][j]` be the number of playlists of length `i` that have exactly `j` unique songs. We want `dp[L][N]`, and it seems likely we can develop a recurrence for `dp`.

**Algorithm**

Consider `dp[i][j]`. Last song, we either played a song for the first time or we didn't. If we did, then we had `dp[i-1][j-1] * (N-j)` ways to choose it. If we didn't, then we repeated a previous song in `dp[i-1][j] * max(j-K, 0)` ways (`j` of them, except the last `K` ones played are banned.)

```python
from functools import lru_cache

class Solution:
    def numMusicPlaylists(self, N, L, K):
        @lru_cache(None)
        def dp(i, j):
            if i == 0:
                return +(j == 0)
            ans = dp(i-1, j-1) * (N-j+1)
            ans += dp(i-1, j) * max(j-K, 0)
            return ans % (10**9+7)

        return dp(L, N)
```

**Complexity Analysis**

* Time Complexity: $O(NL)$.

* Space Complexity: $O(NL)$. (However, we can adapt this algorithm to only store the last row of `dp` to easily get $O(L)$ space complexity.)


## Approach 2: Partitions + Dynamic Programming
(Note: This solution is extremely challenging, but is a natural consequence of trying to enumerate the playlists in this manner.)

**Intuition**

Since we are interested in playing every song at least once, let's keep track of what times $x = (x_1, x_2, \cdots)$ a song was played that wasn't yet played before. For example, if we have 5 songs `abcde`, and we play `abacabdcbaeacbd`, then $x = (1, 2, 4, 7, 11)$ as these are the first occurrences of a unique song. For convenience, we'll also put $x_{N+1} = L+1$. Our strategy is to count the number of playlists $\#_x$ that satisfy this $x$, so that our final answer will be $\sum \#_x$.

Doing a direct count,

$\#_x = N * (N-1) * \cdots * (N-K+1) 1^{x_{K+1} - x_K - 1} * (N-K+2) 2^{x_{K+2} - x_{K+1}} * \cdots$

$\Rightarrow \#_x = N! \prod_{j=1}^{N-K+1} j^{x_{K+j} - x_{K+j-1} - 1}$
 
Now, let $\delta_i = x_{K+i} - x_{K+i-1} - 1$, so that $\sum \delta_i = L-N$. To recap, the final answer will be (for $S = L-N, P = N-K+1$):

N! $\Big(\sum\limits_{\delta : \sum\limits_{0 \leq i \leq P} \delta_i = S} \prod\limits_{j=1}^P j^{\delta_j} \Big)$

For convenience, let's denote the stuff in the large brackets as $\langle S, P\rangle$.

**Algorithm**

We can develop a recurrence for $\langle S, P\rangle$ mathematically, by factoring out the $P^{\delta_P}$ term.

$\langle S, P\rangle = \sum_{\delta_P = 0}^S P^{\delta_P} \sum_{\sum\limits_{0\leq i < P} \delta_i = S - \delta_P} \prod\limits_{j=1}^{P-1} j^{\delta_j}$
 

$\Rightarrow \langle S, P\rangle = \sum_{\delta_P = 0}^S P^{\delta_P} \langle S - \delta_P, P-1\rangle$

so that it can be shown through algebraic manipulation that: $\langle S, P \rangle = P \langle S-1, P-1 \rangle + \langle S, P-1 \rangle$

With this recurrence, we can perform dynamic programming similar to Approach 1. The final answer is $N! \langle L-N, N-K+1 \rangle$.

```python
class Solution(object):
    def numMusicPlaylists(self, N, L, K):
        # dp[S] at time P = <S, P> as discussed in article
        dp = [1] * (L-N+1)
        for p in xrange(2, N-K+1):
            for i in xrange(1, L-N+1):
                dp[i] += dp[i-1] * p

        # Multiply by N!
        ans = dp[-1]
        for k in xrange(2, N+1):
            ans *= k
        return ans % (10**9 + 7)
```

**Complexity Analysis**

* Time Complexity: $O(NL)$.

* Space Complexity: $O(L)$.

## Approach 3: Generating Functions
(Note: This solution is extremely challenging and not recommended for interviews, but is included here for completeness.)

**Analysis**

Following the terminology of Approach 2, we would like to compute \langle S, P \rangle⟨S,P⟩ quickly. We can use generating functions.

For a fixed $P$, consider the function:

$f(x) = (1^0x^0 + 1^1x^1 + 1^2x^2 + 1^3x^3 + \cdots) * (2^0x^0 + 2^1x^1 + 2^2x^2 + 2^3x^3 + \cdots)$ $\cdots * (P^0x^0 + P^1x^1 + P^2x^2 + P^3x^3 + \cdots)$

$\Leftrightarrow f(x) = \prod_{k=1}^{P} (\sum_{j \geq 0} k^j x^j) = \prod_{k=1}^P \frac{1}{1-kx}$
 

The coefficient of $x^S$ in $f (denoted [x^S]$ is the desired $\langle S, P \rangle$.

By the Chinese Remainder theorem on polynomials, this product can be written as a partial fraction decomposition:

$\prod_{k=1}^P \frac{1}{1-kx} = \sum_{k=1}^P \frac{A_k}{1-kx}$
 

for some rational coefficients $A_k$. We can solve for these coefficients by clearing denominators and setting $x = 1/m$ for $1 \leq m \leq P$. Then for a given $m$, all the terms except the $m$-th vanish, and:

$A_m = \frac{1}{\prod\limits_{\substack{1 \leq j \leq P\\j \neq m}} 1 - j/m} = \prod_{j \neq m} \frac{m}{m-j}$

Since a geometric series has sum $\sum_{j \geq 0} (kx)^j = \frac{1}{1-kx}$, altogether it implies:

$[x^S]f = \sum_{k=1}^P A_k * k^S$
 

so that the final answer is

$\text{answer} = N! \sum_{k=1}^{N-K} k^{L-N} \prod_{\substack{1 \leq j \leq N-K\\j \neq k}} \frac{k}{k-j}$

$\Rightarrow \text{answer} = N! \sum_k k^{L-K-1} \prod_{j \neq k} \frac{1}{k-j}$
 

We only need a quick way to compute $C_k = \prod\limits_{j \neq k} \frac{1}{k-j}$. Indeed,

$C_{k+1} = C_k * \frac{k - (N-K)}{k}$

so that we now have everything we need to compute the answer quickly.

```python
class Solution(object):
    def numMusicPlaylists(self, N, L, K):
        MOD = 10**9 + 7
        def inv(x):
            return pow(x, MOD-2, MOD)

        C = 1
        for x in xrange(1, N-K):
            C *= -x
            C %= MOD
        C = inv(C)

        ans = 0
        for k in xrange(1, N-K+1):
            ans += pow(k, L-K-1, MOD) * C
            C = C * (k - (N-K)) % MOD * inv(k) % MOD

        for k in xrange(1, N+1):
            ans = ans * k % MOD
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N \log L)$.

* Space Complexity: $O(1)$.

# Submissions
---
**Solution 1: (Dynamic Programming)**
```
Runtime: 128 ms
Memory Usage: 17.1 MB
```
```python
from functools import lru_cache

class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        @lru_cache(None)
        def dp(i, j):
            if i == 0:
                return +(j == 0)
            ans = dp(i-1, j-1) * (N-j+1)
            ans += dp(i-1, j) * max(j-K, 0)
            return ans % (10**9+7)

        return dp(L, N)
```

**Solution 2: (Partitions + Dynamic Programming)**
```
Runtime: 28 ms
Memory Usage: 13.7 MB
```
```python
class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        # dp[S] at time P = <S, P> as discussed in article
        dp = [1] * (L-N+1)
        for p in range(2, N-K+1):
            for i in range(1, L-N+1):
                dp[i] += dp[i-1] * p

        # Multiply by N!
        ans = dp[-1]
        for k in range(2, N+1):
            ans *= k
        return ans % (10**9 + 7)
```

**Solution 3: (Generating Functions)**
```
Runtime: 32 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        MOD = 10**9 + 7
        def inv(x):
            return pow(x, MOD-2, MOD)

        C = 1
        for x in range(1, N-K):
            C *= -x
            C %= MOD
        C = inv(C)

        ans = 0
        for k in range(1, N-K+1):
            ans += pow(k, L-K-1, MOD) * C
            C = C * (k - (N-K)) % MOD * inv(k) % MOD

        for k in range(1, N+1):
            ans = ans * k % MOD
        return ans
```

**Solution 4: (DP Top-Town)**
```
Runtime: 5 ms
Memory: 8 MB
```
```c++
class Solution {
    #define ll long long
    const int MOD = 1e9 + 7;
    ll solve(int n, int goal, int k, vector<vector<int>>& dp) {
        if (n == 0 && goal == 0) return 1;
        if (n == 0 || goal == 0) return 0;
        if (dp[n][goal] != -1) return dp[n][goal];
        ll pick = solve(n - 1, goal - 1, k, dp) * n;
        ll notpick = solve(n, goal - 1, k, dp) * max(n - k, 0);
        return dp[n][goal] = (pick + notpick) % MOD;
    }
public:
    int numMusicPlaylists(int n, int goal, int k) {
        vector<vector<int>> dp(n + 1, vector<int>(goal + 1, -1));
        return solve(n, goal, k, dp);
    }
};
```
