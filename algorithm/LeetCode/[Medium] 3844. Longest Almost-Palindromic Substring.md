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
**Solution 1: (Center Expansion)**
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
