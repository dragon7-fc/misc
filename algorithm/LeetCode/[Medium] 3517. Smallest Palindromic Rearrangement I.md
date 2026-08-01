3517. Smallest Palindromic Rearrangement I

You are given a **palindromic** string `s`.

Return the **lexicographically smallest** palindromic **permutation** of `s`.

 

**Example 1:**
```
Input: s = "z"

Output: "z"

Explanation:

A string of only one character is already the lexicographically smallest palindrome.
```

**Example 2:**
```
Input: s = "babab"

Output: "abbba"

Explanation:

Rearranging "babab" → "abbba" gives the smallest lexicographic palindrome.
```

**Example 3:**
```
Input: s = "daccad"

Output: "acddca"

Explanation:

Rearranging "daccad" → "acddca" gives the smallest lexicographic palindrome.
```
 

**Constraints:**

`1 <= s.length <= 10^5`
`s` consists of lowercase English letters.
`s` is guaranteed to be palindromic.

# Submissions
---
**Solution 1: (Counter)**
```
Runtime: 32 ms, Beats 68.42%
Memory: 60.83 MB, Beats 68.42%
```
```c++
class Solution {
public:
    string smallestPalindrome(string s) {
        int n = s.size(), i, j = 0, cnt[26] = {0};
        for (auto c: s) {
            cnt[c-'a'] += 1;
        }
        string ans = string(n, ' ');
        for (i = 0; i < 26; i ++) {
            while (cnt[i] >= 2) {
                ans[j] = i + 'a';
                ans[n-1-j] = i + 'a';
                j += 1;
                cnt[i] -= 2;
            }
        }
        for (i = 0; i < 26; i ++) {
            if (cnt[i]) {
                ans[n/2] = i + 'a';
                break;
            }
        }
        return ans;
    }
};
```

**Solution 2: (Counter, preserve original string and count half string then try to assign smallest character to first and second half)**
```
Runtime: 20 ms, Beats 88.79%
Memory: 54.22 MB, Beats 88.13%
```
```c++
class Solution {
public:
    string smallestPalindrome(string s) {
        int n = s.length();
        vector<int> cnt(26);
        for (int i = 0; i < n / 2; i ++) {
            cnt[s[i] - 'a'] += 1;
        }
        int i = 0;
        int j = n - 1;
        for (char c = 'a'; c <= 'z'; c ++) {
            while (cnt[c - 'a']) {
                cnt[c - 'a'] -= 1;
                s[i] = c;
                s[j] = c;
                i += 1;
                j -= 1;
            }
        }
        return s;
    }
};
```
