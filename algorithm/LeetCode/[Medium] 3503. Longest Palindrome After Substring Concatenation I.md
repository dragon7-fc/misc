3503. Longest Palindrome After Substring Concatenation I

You are given two strings, `s` and `t`.

You can create a new string by selecting a substring from `s` (possibly empty) and a substring from `t` (possibly empty), then concatenating them in order.

Return the length of the **longest palindrome** that can be formed this way.

 

**Example 1:**
```
Input: s = "a", t = "a"

Output: 2

Explanation:

Concatenating "a" from s and "a" from t results in "aa", which is a palindrome of length 2.
```

**Example 2:**
```
Input: s = "abc", t = "def"

Output: 1

Explanation:

Since all characters are different, the longest palindrome is any single character, so the answer is 1.
```

**Example 3:**
```
Input: s = "b", t = "aaaa"

Output: 4

Explanation:

Selecting "aaaa" from t is the longest palindrome, so the answer is 4.
```

**Example 4:**
```
Input: s = "abcde", t = "ecdba"

Output: 5

Explanation:

Concatenating "abc" from s and "ba" from t results in "abcba", which is a palindrome of length 5.
```
 

**Constraints:**

* `1 <= s.length, t.length <= 30`
* `s` and `t` consist of lowercase English letters.

# Submissions
---
**Solution 1: (Brute Force)**
```
Runtime: 763 ms, Beats 66.67%
Memory: 179.18 MB, Beats 66.67%
```
```c++
class Solution {
    int check (string &s1, string &s2) {
        string s = s1 + s2;
        int i = 0, j = s.size()-1, rst = 0;
        while (i < j) {
            if (s[i] == s[j]) {
                i += 1;
                j -= 1;
                rst += 2;
            } else{
                break;
            }
        }
        if (i == j) {
            rst += 1;
            i += 1;
            j -= 1;
        }
        if (i <= j) {
            return 0;
        }
        return rst;
    }
public:
    int longestPalindrome(string s, string t) {
        int m = s.size(), n = t.size(), i, j, k, k2, ans = 0;
        vector<string> dp, dp2;
        dp.push_back("");
        dp2.push_back("");
        for (i = 0; i < m; i ++) {
            for (k = 1; i + k <= m; k ++) {
                dp.push_back(s.substr(i, k));
            }
        }
        for (j = 0; j < n; j ++) {
            for (k2 = 1; j + k2 <= n; k2 ++) {
                dp2.push_back(t.substr(j, k2));
            }
        }
        for (auto &s1: dp) {
            for (auto &s2: dp2) {
                ans = max(ans, check(s1, s2));
            }
        }
        return ans;
    }
};
```
