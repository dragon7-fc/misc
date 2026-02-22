3844. Longest Almost-Palindromic Substring

You are given a string `s` consisting of lowercase English letters.

A substring is **almost-palindromic** if it becomes a **palindrome** after removing exactly one character from it.

Return an integer denoting the length of the **longest almost-palindromic** substring in `s`.

 

**Example 1:**
```
Input: s = "abca"

Output: 4

Explanation:

Choose the substring "abca".

Remove "abca".
The string becomes "aba", which is a palindrome.
Therefore, "abca" is almost-palindromic.
```

**Example 2:**
```
Input: s = "abba"

Output: 4

Explanation:

Choose the substring "abba".

Remove "abba".
The string becomes "aba", which is a palindrome.
Therefore, "abba" is almost-palindromic.
```

**Example 3:**
```
Input: s = "zzabba"

Output: 5

Explanation:

Choose the substring "zzabba".

Remove "zabba".
The string becomes "abba", which is a palindrome.
Therefore, "zabba" is almost-palindromic.
```

**Constraints:**

* `2 <= s.length <= 2500`
* `s` consists of only lowercase English letters.

# Submissions
---
**Solution 1: (DP Bottom-Up, LPS)**
```
Runtime: 769 ms, Beats 59.19%
Memory: 553.62 MB, Beats 12.02%
```
```c++
class Solution {
public:
    int almostPalindromic(string s) {
        int n = s.size(), i, j, k, ans = 1;
        vector<vector<int>> dp(n, vector<int>(n));
        for (i = 0; i < n; i ++) {
            dp[i][i] = 1;
            if (i + 1 < n) {
                if (s[i] == s[i + 1]) {
                    dp[i][i + 1] = 2;
                } else {
                    dp[i][i + 1] = 1;
                }
                ans = 2;
            }
        }
        for (i = n - 3; i >= 0; i --) {
            for (j = i + 2; j < n; j ++) {
                if (s[i] == s[j] && dp[i + 1][j - 1]) {
                    dp[i][j] = 2 + dp[i + 1][j - 1];
                } else {
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);
                }
                k = j - i + 1;
                if (dp[i][j] >= k - 1) {
                    ans = max(ans, k);
                }
            }
        }
        return ans;
    }
};
```

**Solution 2: (DP Bottom-Up, LPS)**
```
Runtime: 575 ms, Beats 62.43%
Memory: 553.48 MB, Beats 15.64%
```
```c++
class Solution {
public:
    int almostPalindromic(string s) {
        int n = s.size(), i, j, k, ans = 1;
        vector<vector<int>> dp(n, vector<int>(n));
        for (i = n - 1; i >= 0; i --) {
            dp[i][i] = 1;
            for (j = i + 1; j < n; j ++) {
                if (s[i] == s[j]) {
                    dp[i][j] = 2 + dp[i + 1][j - 1];
                } else {
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);
                }
                k = j - i + 1;
                if (dp[i][j] >= k - 1) {
                    ans = max(ans, k);
                }
            }
        }
        return ans;
    }
};
```

**Solution 3: (Center Expansion)**
```
Runtime: 22 ms, Beats 88.21%
Memory: 10.25 MB, Beats 93.70%
```
```c++
class Solution {
public:
    int almostPalindromic(string s) {
        int n = s.length(), res = 0;
        for (int i = 0; i < n; i++) {
            int l = i, r = i;
            while (l >= 0 && r < n && s[l] == s[r]) {
                res = max(res, r - l + 2);
                l--; r++;
            }
            int sl = l - 1, sr = r;
            while (sl >= 0 && sr < n && s[sl] == s[sr]) {
                res = max(res, sr - sl + 1);
                sl--; sr++;
            }
            sl = l; sr = r + 1;
            while (sl >= 0 && sr < n && s[sl] == s[sr]) {
                res = max(res, sr - sl + 1);
                sl--; sr++;
            }
        }
        for (int i = 0; i < n; i++) {
            int l = i, r = i + 1;
            while (l >= 0 && r < n && s[l] == s[r]) {
                res = max(res, r - l + 2);
                l--; r++;
            }
            int sl = l - 1, sr = r;
            while (sl >= 0 && sr < n && s[sl] == s[sr]) {
                res = max(res, sr - sl + 1);
                sl--; sr++;
            }
            sl = l; sr = r + 1;
            while (sl >= 0 && sr < n && s[sl] == s[sr]) {
                res = max(res, sr - sl + 1);
                sl--; sr++;
            }
        }
        return min(res, n);
    }
};
```
