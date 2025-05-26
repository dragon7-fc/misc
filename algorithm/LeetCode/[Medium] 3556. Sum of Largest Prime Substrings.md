3556. Sum of Largest Prime Substrings

Given a string `s`, find the sum of the **3 largest unique** prime numbers that can be formed using any of its substrings.

Return the sum of the three largest unique prime numbers that can be formed. If fewer than three exist, return the sum of all available primes. If no prime numbers can be formed, return `0`.

**Note**: Each prime number should be counted only once, even if it appears in multiple substrings. Additionally, when converting a substring to an integer, any leading zeros are ignored.

 

**Example 1:**
```
Input: s = "12234"

Output: 1469

Explanation:

The unique prime numbers formed from the substrings of "12234" are 2, 3, 23, 223, and 1223.
The 3 largest primes are 1223, 223, and 23. Their sum is 1469.
```

**Example 2:**
```
Input: s = "111"

Output: 11

Explanation:

The unique prime number formed from the substrings of "111" is 11.
Since there is only one prime number, the sum is 11.
```

**Constraints:**

* `1 <= s.length <= 10`
* `s` consists of only digits.

# Submissions
---
**Solution 1: (Brute Force, Math)**
```
Runtime: 12 ms, Beats 100.00%
Memory: 9.76 MB, Beats 100.00%
```
```c++
class Solution {
    bool is_prime(long long a) {
        if (a < 2) {
            return false;
        }
        for (long long b = 2; b*b <= a; b ++) {
            if (a%b == 0) {
                return false;
            }
        }
        return true;
    }
public:
    long long sumOfLargestPrimes(string s) {
        size_t n = s.length(), i, j, k;
        long long ans = 0, cur;
        set<long long> st;
        for (i = 0; i < n; i ++) {
            cur = 0;
            for (j = i; j < n; j ++) {
                cur = cur*10 + s[j] - '0';
                if (is_prime(cur)) {
                   st.insert(cur); 
                }
            }
        }
        k = 0;
        for (auto it = st.rbegin(); it != st.rend() && k < 3; it++) {
            ans += *it;
            k += 1;
        }
        return ans;
    }
};
```
