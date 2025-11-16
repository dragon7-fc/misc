3747. Count Distinct Integers After Removing Zeros

You are given a positive integer `n`.

For every integer `x` from `1` to `n`, we write down the integer obtained by removing all zeros from the decimal representation of `x`.

Return an integer denoting the number of **distinct** integers written down.

 

**Example 1:**
```
Input: n = 10

Output: 9

Explanation:

The integers we wrote down are 1, 2, 3, 4, 5, 6, 7, 8, 9, 1. There are 9 distinct integers (1, 2, 3, 4, 5, 6, 7, 8, 9).
```

**Example 2:**
```
Input: n = 3

Output: 3

Explanation:

The integers we wrote down are 1, 2, 3. There are 3 distinct integers (1, 2, 3).
```
 

**Constraints:**

* `1 <= n <= 10^15`

# Submissions
---
**Solution 1: (Math)**
```
Runtime: 1 ms, Beats 36.36%
Memory: 9.41 MB, Beats 54.55%
```
```c++
class Solution {
public:
    long long countDistinct(long long n) {
        vector<long long> pow(16, 1);
        string s = to_string(n);
        long long ans = 0, i, j, m = s.length();
        for (i = 1; i <= 15; i++) {
            pow[i] = pow[i-1] * 9;
        }
        for (i = 1; i < m; i++) {
            ans += pow[i];
        }
        for (i = 0; i < m; i++) {
            if (s[i] == '0') {
                break;
            }
            for (j = 1; j < s[i] - '0'; j++) {
                ans += pow[m - i - 1];
            }
        }
        
        return ans + (i >= s.size());
    }
};
```
