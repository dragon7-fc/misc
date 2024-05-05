650. 2 Keys Keyboard

Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:

1. `Copy All`: You can copy all the characters present on the notepad (partial copy is not allowed).
1. `Paste`: You can paste the characters which are copied last time.
 

Given a number `n`. You have to get exactly `n` 'A' on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get `n` 'A'.

**Example 1:**
```
Input: 3
Output: 3
Explanation:
Intitally, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.
```

**Note:**

1. The `n` will be in the range [1, 1000].

# Solution
---
## Approach #1: Prime Factorization [Accepted]
**Intuition**

We can break our moves into groups of `(copy, paste, ..., paste)`. Let `C` denote copying and `P` denote pasting. Then for example, in the sequence of moves `CPPCPPPPCP`, the groups would be `[CPP][CPPPP][CP]`.

Say these groups have lengths `g_1, g_2, ....` After parsing the first group, there are `g_1` 'A's. After parsing the second group, there are `g_1 * g_2` 'A's, and so on. At the end, there are `g_1 * g_2 * ... * g_n` 'A's.

We want exactly `N = g_1 * g_2 * ... * g_n`. If any of the `g_i` are composite, say `g_i = p * q`, then we can split this group into two groups (the first of which has one copy followed by `p-1` pastes, while the second group having one copy and `q-1` pastes).

Such a split never uses more moves: we use `p+q` moves when splitting, and `pq` moves previously. As `p+q <= pq` is equivalent to `1 <= (p-1)(q-1)`, which is true as long as `p >= 2` and `q >= 2`.

**Algorithm**

By the above argument, we can suppose `g_1, g_2, ...` is the prime factorization of `N`, and the answer is therefore the sum of these prime factors.

```python
class Solution(object):
    def minSteps(self, n):
        ans = 0
        d = 2
        while n > 1:
            while n % d == 0:
                ans += d
                n /= d
            d += 1
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(\sqrt{N})$. When N is the square of a prime, our loop does $O(\sqrt{N})$ steps.

* Space Complexity: $O(1)$, the space used by ans and d.

# Submissions
---
**Solution 1: (Prime Factorization)**
```
Runtime: 40 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def minSteps(self, n: int) -> int:
        ans = 0
        d = 2
        while n > 1:
            while n % d == 0:
                ans += d
                n /= d
            d += 1
        return ans
```

**Solution 2: (DP Top-Down)**
```
Runtime: 192 ms
Memory Usage: 32.6 MB
```
```python
class Solution:
    def minSteps(self, n: int) -> int:
        
        @functools.lru_cache(None)
        def copy_or_paste(num_a, num_copied):
            if num_a == n: #found a solution
                return 0
            if num_a > n or num_a + num_copied > n: # won't lead to a solution, so we stop.
                return float('inf')
                      
            #try pasting, if we have something to paste
            paste = 1 + copy_or_paste(num_a + num_copied, num_copied) if num_copied > 0 else float('inf')

            # try copying, if what we have on the board is > what we have copied
            copy_all = 1 + copy_or_paste(num_a, num_a) if num_a > num_copied else float('inf')
                
            return min(paste, copy_all)
        
        #start with 1 A on the board and 0 copied
        return copy_or_paste(1, 0)
```

**Solution 3: (DP Bottom-Up)**
```
Runtime: 287 ms
Memory: 16.64 MB
```
```python
class Solution:
    def minSteps(self, n: int) -> int:
        dp = [i for i in range(0, n+1)]
        dp[1] = 0
        for i in range(1, n + 1):
            for j in range(i // 2, 1, -1):
                if i % j == 0: 
                    dp[i] = min(dp[i], dp[j] + i // j)
        return dp[-1]
```
