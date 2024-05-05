3138. Minimum Length of Anagram Concatenation

You are given a string `s`, which is known to be a concatenation of anagrams of some string `t`.

Return the **minimum** possible length of the string `t`.

An anagram is formed by rearranging the letters of a string. For example, `"aab"`, `"aba"`, and, `"baa"` are anagrams of `"aab"`.

 

**Example 1:**
```
Input: s = "abba"

Output: 2

Explanation:

One possible string t could be "ba".
```

**Example 2:**
```
Input: s = "cdef"

Output: 4

Explanation:

One possible string t could be "cdef", notice that t can be equal to s.
```
 

**Constraints:**

* `1 <= s.length <= 10^5`
* `s` consist only of lowercase English letters.

# Submissions
---
**Solution 1: (Brute Force)**
```
Runtime: 53 ms
Memory: 12.66 MB
```
```c++
class Solution {
    bool check(int c, string &s) {
        int pre[26] = {0}, cur[26];
        for (int i = 0; i < c; i ++) {
            pre[s[i]-'a'] += 1;
        }
        for (int i = c; i < s.size(); i += c) {
            memset(cur, 0, sizeof(cur));
            for (int j = i; j < i+c; j ++) {
                cur[s[j]-'a'] += 1;
            }
            if (memcmp(pre, cur, sizeof(pre)) != 0) {
                return false;
            }
        }
        return true;
    }
public:
    int minAnagramLength(string s) {
        int n = s.size();
        for (int d = 1; d <= n/2; d ++) {
            if (n%d == 0 && check(d, s)) {
                return d;
            }
        }
        return n;
    }
};
```
