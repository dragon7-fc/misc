3881. Direction Assignments with Exactly K Visible People

You are given three integers `n`, `pos`, and `k`.

There are `n` people standing in a line indexed from 0 to `n - 1`. Each person **independently** chooses a direction:

`'L'`: **visible** only to people on their **right**
`'R'`: **visible** only to people on their **left**

A person at index `pos` sees others as follows:
* A person `i < pos` is visible if and only if they choose `'L'`.
* A person `i > pos` is visible if and only if they choose `'R'`.

Return the number of possible direction assignments such that the person at index `pos` sees exactly `k` people.

Since the answer may be large, return it modulo `10^9 + 7`.

 

**Example 1:**
```
Input: n = 3, pos = 1, k = 0

Output: 2

Explanation:

Index 0 is to the left of pos = 1, and index 2 is to the right of pos = 1.
To see k = 0 people, index 0 must choose 'R' and index 2 must choose 'L', keeping both invisible.
The person at index 1 can choose 'L' or 'R' since it does not affect the count. Thus, the answer is 2.
```

**Example 2:**
```
Input: n = 3, pos = 2, k = 1

Output: 4

Explanation:

Index 0 and index 1 are left of pos = 2, and there is no index to the right.
To see k = 1 person, exactly one of index 0 or index 1 must choose 'L', and the other must choose 'R'.
There are 2 ways to choose which index is visible from the left.
The person at index 2 can choose 'L' or 'R' since it does not affect the count. Thus, the answer is 2 + 2 = 4.
```

**Example 3:**
```
Input: n = 1, pos = 0, k = 0

Output: 2

Explanation:

There are no indices to the left or right of pos = 0.
To see k = 0 people, no additional condition is required.
The person at index 0 can choose 'L' or 'R'. Thus, the answer is 2.
```

**Constraints:**

* `1 <= n <= 10^5`
* `0 <= pos, k <= n - 1`

# Submissions
---
**Solution 1: (Math, Modular Inverse & Binary Exp)**

ans = c(n - 1, k) (mod 10^9 + 7)

* Binary Exponentiation (power function):
Calculates (base^exp) % MOD in O(log exp) time. It squares the base at each step and only multiplies it into the result when the current bit of the exponent is 1. This is required for an efficient modular inverse.

* Modular Multiplicative Inverse (modInverse function):
In modular arithmetic, division is performed by multiplying by the modular inverse. By Fermat's Little Theorem, since 10^9 + 7 is prime, the inverse of B
B^−1 ≡ B^(MOD−2)(mod MOD)


```
Runtime: 4 ms, Beats 100.00%
Memory: 8.78 MB, Beats 90.91%
```
```c++
class Solution {
    const long long MOD = 1e9 + 7;
    long long power(long long base, long long exp) {
        long long res = 1;
        base %= MOD;
        while (exp > 0) {
            if (exp % 2 == 1) {
                res = (res * base) % MOD;
            }
            base = (base * base) % MOD;
            exp /= 2;
        }
        return res;
    }
    long long modInverse(long long n) {
        return power(n, MOD - 2);
    }
    long long nCr(int n, int k) {
        if (k < 0 || k > n) {
            return 0;
        }
        if (k == 0 || k == n) {
            return 1;
        }
        if (k > n / 2 ) {
            k = n - k;
        }
        long long num = 1, den = 1;
        for (int i = 0; i < k; i ++) {
            num = (num * (n - i)) % MOD;
            den = (den * (i + 1)) % MOD;
        }
        return (num * modInverse(den)) % MOD;
    }
public:
    int countVisiblePeople(int n, int pos, int k) {
        return (nCr(n - 1, k)*2) % MOD;
    }
};
```
