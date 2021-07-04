1922. Count Good Numbers

A digit string is **good** if the digits (**0-indexed**) at **even** indices are **even** and the digits at **odd** indices are **prime** (`2`, `3`, `5`, or `7`).

* For example, `"2582"` is good because the digits (`2` and `8`) at even positions are even and the digits (`5` and `2`) at odd positions are prime. However, `"3245"` is **not** good because `3` is at an even index but is not even.

Given an integer `n`, return the **total** number of good digit strings of length `n`. Since the answer may be large, **return it modulo** `10^9 + 7`.

A **digit string** is a string consisting of digits `0` through `9` that may contain leading zeros.

 

**Example 1:**
```
Input: n = 1
Output: 5
Explanation: The good numbers of length 1 are "0", "2", "4", "6", "8".
```

**Example 2:**
```
Input: n = 4
Output: 400
```

**Example 3:**
```
Input: n = 50
Output: 564908303
```

**Constraints:**

* `1 <= n <= 10^15`

# Submissions
---
**Solution 1: (Math)**
```
Runtime: 32 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        return pow(5, (n + 1) // 2, MOD) * pow(4, n // 2, MOD) % MOD
```

**Solution 2: (Math)**

1. For each even index, there are 5 options: 0, 2, 4, 6, 8;
1. For each odd index, there are 4 options: 2, 3, 5, 7;
1. If n is even, the solution is (4 * 5) ^ (n / 2); if odd, (4 * 5) ^ (n / 2) * 5.

```
Runtime: 24 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        good, x, i = 5 ** (n % 2), 4 * 5, n // 2
        while i > 0:
            if i % 2 == 1:
                good = good * x % (10 ** 9 + 7)
            x = x * x % (10 ** 9 + 7)
            i //= 2
        return good
```
