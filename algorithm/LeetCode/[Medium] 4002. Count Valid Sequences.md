4002. Count Valid Sequences

You are given two positive integers `n` and `k`.

A **valid sequence** is a sequence of `k` positive integers such that:

* The sum of all integers in the sequence is equal to `n`.
* The product of all integers in the sequence is even.

Return the number of valid sequences. Since the answer may be very large, return it modulo` 10^9 + 7`.

Two sequences are considered **different** if they differ at any index. For example, `[1, 1, 2]` and `[1, 2, 1]` are considered different sequences.

 

**Example 1:**
```
Input: n = 5, k = 3

Output: 3

Explanation:

The sequences of length k = 3 whose sum is 5 are:

Sequence	Product	Parity
[1, 1, 3]	1 * 1 * 3 = 3	Odd
[1, 2, 2]	1 * 2 * 2 = 4	Even
[2, 1, 2]	2 * 1 * 2 = 4	Even
[2, 2, 1]	2 * 2 * 1 = 4	Even
[1, 3, 1]	1 * 3 * 1 = 3	Odd
[3, 1, 1]	3 * 1 * 1 = 3	Odd
There are 3 sequences with an even product, thus the answer is 3.
```

**Example 2:**
```
Input: n = 3, k = 2

Output: 2

Explanation:

The sequences of length k = 2 whose sum is 3 are:

Sequence	Product	Parity
[1, 2]	1 * 2 = 2	Even
[2, 1]	2 * 1 = 2	Even
There are 2 sequences with an even product, thus the answer is 2.
```

**Example 3:**
```
Input: n = 5, k = 5

Output: 0

Explanation:

The only possible sequence of length k = 5 whose sum is 5 is [1, 1, 1, 1, 1], which has an odd product. Thus, the answer is 0.
```
 

**Constraints:**

* `1 <= n <= 5 * 10^5`
* `1 <= k <= n`

# Submissions

__Intuition__
Total sequences of length k summing to n
can be found using the Stars and Bars formula.
This yields comb(n - 1, k - 1) total ways.

__Explanation__
We substitute xi = 2∗yi +1 for each element.
The new target sum becomes (n - k) / 2 The invalid count is comb((n + k) / 2 - 1, k - 1)$.

We subtract this invalid count from the total
and return the result modulo 10^9 + 7.

__Complexity__
Time O(klogk)
Space O(1)

-------------------------------------------------------
                                                            combination
all:
    x1     +   x2   + ... +   xk    = n                     c(n-1, k-1)
odd product: (only when all number are odd)
  2xi - 1    2y2 - 1       2yk - 1
  2(y1 + y2 + ... + yk)             = n + k
  y1 + y2 + ... + yk                = (n + k) / 2           c((n+k)/2 - 1, k - 1)
                                      ^^^^^^^^^^^
                                      (n + k) is even

---
**Solution 1: (Math, Combination, total combination - odd product)**
```
Runtime: 7 ms, Beats 92.44%
Memory: 8.42 MB, Beats 90.41%
```
```c++
class Solution {
    int MOD = 1e9 + 7;
    long long power(long long b, long long e) {
        long long r = 1;
        for (; e; e >>= 1, b = b * b % MOD)
            if (e & 1) r = r * b % MOD;
        return r;
    }

    // n*(n-1)*...*(n-k+1) / 1*2*...*k
    long long comb(int n, int k) {
        if (k < 0 || k > n) return 0;
        k = min(k, n - k);
        long long res = 1, den = 1;
        for (int i = 1; i <= k; ++i) {
            res = res * (n - i + 1) % MOD;
            den = den * i % MOD;
        }
        return res * power(den, MOD - 2) % MOD;
                     // e^(-1) (mod p) = e^(p - 2)
    }
public:
    int countValidSequences(int n, int k) {
        long long res = comb(n - 1, k - 1);

        // (n + k) is even
        // odd product
        if ((n & 1) == (k & 1))
            res = (res - comb((n + k) / 2 - 1, k - 1) + MOD) % MOD;
        return res;
    }
};
```
