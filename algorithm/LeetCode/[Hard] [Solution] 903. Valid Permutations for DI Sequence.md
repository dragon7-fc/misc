903. Valid Permutations for DI Sequence

We are given `S`, a length `n` string of characters from the set `{'D', 'I'}`. (These letters stand for "decreasing" and "increasing".)

A valid permutation is a permutation `P[0], P[1], ..., P[n]` of integers {`0, 1, ..., n`}, such that for all `i`:

1. If `S[i] == 'D'`, then `P[i] > P[i+1]`, and;
1. If `S[i] == 'I'`, then `P[i] < P[i+1]`.

How many valid permutations are there?  Since the answer may be large, **return your answer modulo** 10^9 + 7.

 

**Example 1:**
```
Input: "DID"
Output: 5
Explanation: 
The 5 valid permutations of (0, 1, 2, 3) are:
(1, 0, 3, 2)
(2, 0, 3, 1)
(2, 1, 3, 0)
(3, 0, 2, 1)
(3, 1, 2, 0)
```

**Note:**

* `1 <= S.length <= 200`
* `S` consists only of characters from the set `{'D', 'I'}`.

# Solution
---
## Approach 1: Dynamic Programming
**Intuition**

When writing the permutation `P = P_0, P_1, ..., P_N` from left to right, we only care about the relative rank of the last element placed. For example, if `N = 5` (so that we have elements `{0, 1, 2, 3, 4, 5}`), and our permutation starts `2, 3, 4`, then it is similar to a situation where we have placed `?, ?, 2` and the remaining elements are `{0, 1, 3}`, in terms of how many possibilities there are to place the remaining elements in a valid way.

To this end, let `dp(i, j)` be the number of ways to place every number up to and inlcuding `P_i`, such that `P_i` when placed had relative rank `j`. (Namely, there are `j` remaining numbers less than `P_i`.)

**Algorithm**

When placing `P_i` following a decreasing instruction `S[i-1] == 'D'`, we want `P_{i-1}` to have a higher value. When placing `P_i` following an increasing instruction, we want `P_{i-1}` to have a lower value. It is relatively easy to deduce the recursion from this fact.

```python
from functools import lru_cache

class Solution:
    def numPermsDISequence(self, S):
        MOD = 10**9 + 7
        N = len(S)

        @lru_cache(None)
        def dp(i, j):
            # How many ways to place P_i with relative rank j?
            if i == 0:
                return 1
            elif S[i-1] == 'D':
                return sum(dp(i-1, k) for k in range(j, i)) % MOD
            else:
                return sum(dp(i-1, k) for k in range(j)) % MOD

        return sum(dp(N, j) for j in range(N+1)) % MOD
```

**Optimization**

Actually, we can do better than this. For any given `i`, let's look at how the sum of `D_k = dp(i-1, k)` is queried. Assuming `S[i-1] == 'I'`, we query `D_0, D_0 + D_1, D_0 + D_1 + D_2, ...` etc. The case for `S[i-1] == 'D'` is similar.

Thus, we don't need to query the sum every time. Instead, we could use (for `S[i-1] == 'I'`) the fact that `dp(i, j) = dp(i, j-1) + dp(i-1, j-1)`. For `S[i-1] == 'D'`, we have the similar fact that `dp(i, j) = dp(i, j+1) + dp(i-1, j)`.

These two facts make the work done for each state of `dp` have $O(1)$ (amortized) complexity, leading to a total time complexity of $O(N^2)$ for this solution.

```python
from functools import lru_cache

class Solution:
    def numPermsDISequence(self, S):
        MOD = 10**9 + 7
        N = len(S)

        @lru_cache(None)
        def dp(i, j):
            # How many ways to place P_i with relative rank j?
            if not(0 <= j <= i):
                return 0
            if i == 0:
                return 1
            elif S[i-1] == 'D':
                return (dp(i, j+1) + dp(i-1, j)) % MOD
            else:
                return (dp(i, j-1) + dp(i-1, j-1)) % MOD

        return sum(dp(N, j) for j in range(N+1)) % MOD
```

**Complexity Analysis**

* Time Complexity: $O(N^3)$, where $N$ is the length of `S`, or $O(N^2)$ with the optimized version.

* Space Complexity: $O(N^2)$.

## Approach 2: Divide and Conquer
**Intuition**

Let's place the zero of the permutation first. It either goes between a `'DI'` part of the sequence, or it could go on the ends (the left end if it starts with `'I'`, and the right end if it ends in `'D'`.) Afterwards, this splits the problem into two disjoint subproblems that we can solve with similar logic.

**Algorithm**

Let `dp(i, j)` be the number of valid permutations (of `n = j-i+2` total integers from `0` to `n-1`) corresponding to the `DI` sequence `S[i], S[i+1], ..., S[j]`. If we can successfully place a zero between `S[k-1]` and `S[k]`, then there are two disjoint problems `S[i], ..., S[k-2]` and `S[k+1], ..., S[j]`.

To count the number of valid permutations in this case, we should choose `k-i` elements from `n-1` (`n` total integers, minus the zero) to put in the left group; then the answer is this, times the number of ways to arrange the left group [`dp(i, k-2)`], times the number of ways to arrange the right group [`dp(k+1, j)`].

```python
from functools import lru_cache

class Solution:
    def numPermsDISequence(self, S):
        MOD = 10**9 + 7

        fac = [1, 1]
        for x in range(2, 201):
            fac.append(fac[-1] * x % MOD)
        facinv = [pow(f, MOD-2, MOD) for f in fac]

        def binom(n, k):
            return fac[n] * facinv[n-k] % MOD * facinv[k] % MOD

        @lru_cache(None)
        def dp(i, j):
            if i >= j: return 1
            ans = 0
            n = j - i + 2
            if S[i] == 'I': ans += dp(i+1, j)
            if S[j] == 'D': ans += dp(i, j-1)

            for k in range(i+1, j+1):
                if S[k-1:k+1] == 'DI':
                    ans += binom(n-1, k-i) * dp(i, k-2) % MOD * dp(k+1, j) % MOD
                    ans %= MOD
            return ans

        return dp(0, len(S) - 1)
```

**Complexity Analysis**

* Time Complexity: $O(N^2)$, where $N$ is the length of `S`.

* Space Complexity: $O(N^2)$.

# Submissions
---
**Solution: (Dynamic Programming Top-Down)**
```
Runtime: 1172 ms
Memory Usage: 21.8 MB
```
```python
from functools import lru_cache

class Solution:
    def numPermsDISequence(self, S: str) -> int:
        MOD = 10**9 + 7
        N = len(S)

        @lru_cache(None)
        def dp(i, j):
            # How many ways to place P_i with relative rank j?
            if i == 0:
                return 1
            elif S[i-1] == 'D':
                return sum(dp(i-1, k) for k in range(j, i)) % MOD
            else:
                return sum(dp(i-1, k) for k in range(j)) % MOD

        return sum(dp(N, j) for j in range(N+1)) % MOD
```

**Solution: (Dynamic Programming Top-Down)**
```
Runtime: 92 ms
Memory Usage: 33.8 MB
```
```python
from functools import lru_cache

class Solution:
    def numPermsDISequence(self, S: str) -> int:
        MOD = 10**9 + 7
        N = len(S)

        @lru_cache(None)
        def dp(i, j):
            # How many ways to place P_i with relative rank j?
            if not(0 <= j <= i):
                return 0
            if i == 0:
                return 1
            elif S[i-1] == 'D':
                return (dp(i, j+1) + dp(i-1, j)) % MOD
            else:
                return (dp(i, j-1) + dp(i-1, j-1)) % MOD

        return sum(dp(N, j) for j in range(N+1)) % MOD
```

**Solution: (Divide and Conquer)**
```
Runtime: 744 ms
Memory Usage: 14.9 MB
```
```python
from functools import lru_cache

class Solution:
    def numPermsDISequence(self, S: str) -> int:
        MOD = 10**9 + 7

        fac = [1, 1]
        for x in range(2, 201):
            fac.append(fac[-1] * x % MOD)
        facinv = [pow(f, MOD-2, MOD) for f in fac]

        def binom(n, k):
            return fac[n] * facinv[n-k] % MOD * facinv[k] % MOD

        @lru_cache(None)
        def dp(i, j):
            if i >= j: return 1
            ans = 0
            n = j - i + 2
            if S[i] == 'I': ans += dp(i+1, j)
            if S[j] == 'D': ans += dp(i, j-1)

            for k in range(i+1, j+1):
                if S[k-1:k+1] == 'DI':
                    ans += binom(n-1, k-i) * dp(i, k-2) % MOD * dp(k+1, j) % MOD
                    ans %= MOD
            return ans

        return dp(0, len(S) - 1)
```

**Solution 4: (DP Bottom-Up)**


        vi
    D I D
    0 1 3 3
3   1
2   1 1
1   1 2 5
0   1 3 3 5

__Intuition__
dp[i][j] means the number of possible permutations of first i + 1 digits,
where the i + 1th digit is j + 1th smallest in the rest of unused digits.

Ok, may not make sense ... Let's see the following diagram.
image

I take the example of S = "DID".
In the parenthesis, I list all possible permutations.

The permutation can start from 1, 2, 3, 4.
So dp[0][0] = dp[0][1] = dp[0][2] = dp[0][3] = 1.

We decrese from the first digit to the second,
the down arrow show the all possibile decresing pathes.

The same, because we increase from the second digit to the third,
the up arrow show the all possibile increasing pathes.

dp[2][1] = 5, mean the number of permutations
where the third digitis the second smallest of the rest.
We have 413,314,214,423,324.
Fow example 413, where 2,3 are left and 3 the second smallest of them.


__Explanation__
As shown in the diagram,
for "I", we calculate prefix sum of the array,
for "D", we calculate sufixsum of the array.


_Complexity_
Time O(N^2)
Space O(N^2)

```
Runtime: 0 ms, Beats 100.00%
Memory: 9.76 MB, Beats 58.89%
```
```c++
class Solution {
public:
    int numPermsDISequence(string s) {
        int n = s.length(), mod = 1e9 + 7;
        vector<vector<int>> dp(n + 1, vector<int>(n + 1));
        for (int j = 0; j <= n; j++) dp[0][j] = 1;
        for (int i = 0; i < n; i++)
            if (s[i] == 'I')
                for (int j = 0, cur = 0; j < n - i; j++)
                    dp[i + 1][j] = cur = (cur + dp[i][j]) % mod;
            else
                for (int j = n - i - 1, cur = 0; j >= 0; j--)
                    dp[i + 1][j] = cur = (cur + dp[i][j + 1]) % mod;
        return dp[n][0];
    }
};
```
