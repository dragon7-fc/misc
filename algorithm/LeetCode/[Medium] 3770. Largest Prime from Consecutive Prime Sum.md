3770. Largest Prime from Consecutive Prime Sum

You are given an integer `n`.

Return the largest prime number less than or equal to `n` that can be expressed as the sum of one or more **consecutive prime numbers** starting from 2. If no such number exists, return 0.

 

**Example 1:**
```
Input: n = 20

Output: 17

Explanation:

The prime numbers less than or equal to n = 20 which are consecutive prime sums are:

2 = 2

5 = 2 + 3

17 = 2 + 3 + 5 + 7

The largest is 17, so it is the answer.
```

**Example 2:**
```
Input: n = 2

Output: 2

Explanation:

The only consecutive prime sum less than or equal to 2 is 2 itself.
```
 

**Constraints:**

* `1 <= n <= 5 * 10^5`

# SUbmissions
---
**Solution 1: (Math, Prefix Sum)**
```
Runtime: 622 ms, Beats 58.98%
Memory: 325.26 MB, Beats 11.96%
```
```c++
class Solution {
public:
    int largestPrime(int n) {
        int f, ans = 0;
        long long a;
        vector<long long> dp(n + 1);
        for (f = 2; f <= sqrt(n); f ++) {
            if (dp[f] == 0) {
                for (a = 2 * f; a <= n; a += f) {
                    dp[a] = 1;
                }
            }
        }
        a = 0;
        for (f = 2; f <= n; f ++) {
            if (dp[f] == 0) {
                a += f;
                if (a <= n) {
                    if (dp[a] == 0) {
                        ans = a;
                    }
                } else {
                    break;
                }
            }
        }
        return ans;
    }
};
```
