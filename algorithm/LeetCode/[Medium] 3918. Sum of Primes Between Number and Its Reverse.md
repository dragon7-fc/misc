3918. Sum of Primes Between Number and Its Reverse

You are given an integer `n`.

Let `r` be the integer formed by reversing the digits of `n`.

Return the **sum** of all **prime numbers** between `min(n, r)` and `max(n, r)`, inclusive.

A **prime number** is a natural number greater than 1 with only two factors, 1 and itself.

 

**Example 1:**
```
Input: n = 13

Output: 132

Explanation:

The reverse of 13 is 31. Thus, the range is [13, 31].
The prime numbers in this range are 13, 17, 19, 23, 29, and 31.
The sum of these prime numbers is 13 + 17 + 19 + 23 + 29 + 31 = 132.
```

**Example 2:**
```
Input: n = 10

Output: 17

Explanation:

The reverse of 10 is 1. Thus, the range is [1, 10].
The prime numbers in this range are 2, 3, 5, and 7.
The sum of these prime numbers is 2 + 3 + 5 + 7 = 17.
```

**Example 3:**
```
Input: n = 8

Output: 0

Explanation:

The reverse of 8 is 8. Thus, the range is [8, 8].
There are no prime numbers in this range, so the sum is 0.
```

**Constraints:**

* `1 <= n <= 1000`

# Submissions
---
**Solution 1: (Math, Brute Force)**
```
Runtime: 1 ms, Beats 75.65%
Memory: 8.52 MB, Beats 70.75%
```
```c++
class Solution {
public:
    int sumOfPrimesInRange(int n) {
        int r = 0, cn = n, left, right, a, b, ans = 0;
        bool flag;
        while (cn) {
            r = r * 10 + (cn % 10);
            cn /= 10;
        }
        left = min(n, r);
        right = max(n, r);
        for (a = max(2, left); a <= right; a ++) {
            flag = true;
            for (b = 2; b * b <= a; b ++) {
                if (a % b == 0) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                ans += a;
            }
        }
        return ans;
    }
};
```
