3335. Total Characters in String After Transformations I

You are given a string `s` and an integer `t`, representing the number of transformations to perform. In one transformation, every character in `s` is replaced according to the following rules:

* If the character is `'z'`, replace it with the string `"ab`".
* Otherwise, replace it with the next character in the alphabet. For example, `'a'` is replaced with `'b'`, `'b'` is replaced with `'c'`, and so on.

Return the **length** of the resulting string after exactly `t` transformations.

Since the answer may be very large, return it modulo `10^9 + 7`.

 

**Example 1:**
```
Input: s = "abcyy", t = 2

Output: 7

Explanation:

First Transformation (t = 1):
'a' becomes 'b'
'b' becomes 'c'
'c' becomes 'd'
'y' becomes 'z'
'y' becomes 'z'
String after the first transformation: "bcdzz"
Second Transformation (t = 2):
'b' becomes 'c'
'c' becomes 'd'
'd' becomes 'e'
'z' becomes "ab"
'z' becomes "ab"
String after the second transformation: "cdeabab"
Final Length of the string: The string is "cdeabab", which has 7 characters.
```

**Example 2:**
```
Input: s = "azbk", t = 1

Output: 5

Explanation:

First Transformation (t = 1):
'a' becomes 'b'
'z' becomes "ab"
'b' becomes 'c'
'k' becomes 'l'
String after the first transformation: "babcl"
Final Length of the string: The string is "babcl", which has 5 characters.
```

**Constraints:**

* `1 <= s.length <= 10^5`
* `s` consists only of lowercase English letters.
* `1 <= t <= 10^5`

# Submissions
---
**Solution 1: (Counter, DP)**
```
Runtime: 966 ms
Memory: 465.74 MB
```
```c++
class Solution {
public:
    int lengthAfterTransformations(string s, int t) {
        const int MOD = 1e9 + 7;
        vector<long long> cnt(26, 0);

        for (char c : s) {
            cnt[c - 'a']++;
        }

        for (int j = 0; j < t; j++) {
            vector<long long> dp(26, 0);
            for (int i = 0; i < 26; i++) {
                if (i == 25) {
                    dp[0] = (dp[0] + cnt[i]) % MOD;
                    dp[1] = (dp[1] + cnt[i]) % MOD;
                } else {
                    dp[i + 1] = (dp[i + 1] + cnt[i]) % MOD;
                }
            }
            cnt = dp;
        }

        long long len = 0;
        for (long long c : cnt) {
            len = (len + c) % MOD;
        }

        return len;
    }
};
```
