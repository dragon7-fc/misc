3983. Subsequence After One Replacement

You are given two strings `s` and `t` consisting of lowercase English letters.

You may choose at most one index in `s` and replace the character at that index with any lowercase English letter.

Return `true` if it is possible to make `s` a **subsequence** of `t`; otherwise, return `false`.

 

**Example 1:**
```
Input: s = "cat", t = "chat"

Output: true

Explanation:

Replace s[1] from 'a' to 'h'. The resulting string is "cht".
"cht" is a subsequence of "chat" because we can match 'c', 'h', and 't' in order.
```

**Example 2:**
```
Input: s = "plane", t = "apple"

Output: false

Explanation:

The characters 'p', 'l', and 'e' can be matched in t, but the remaining characters cannot be matched while preserving the required order.
Even after replacing any one character in s, it is impossible to make s a subsequence of t.
```

**Constraints:**

* `1 <= s.length, t.length <= 10^5`
* `s` and `t` consist only of lowercase English letters.

# Submissions
---
**Solution 1: (Prefix Sum, precompute left and right earliest match index and check 0 replace then try each character on source to find right - left index > 1 for 1 replace)**
```
Runtime: 11 ms, Beats 88.99%
Memory: 38.65 MB, Beats 71.00%
```
```c++
class Solution {
public:
    bool canMakeSubsequence(string s, string t) {
        int n = s.length();
        int m = t.length();
        
        // If s is longer than t, it can never be a subsequence
        if (n > m) {
            return false;
        }
        
        // left_match[i] stores the earliest index in t that matches s[0...i]
        std::vector<int> left_match(n, m);
        int tp = 0;
        for (int sp = 0; sp < n; ++sp) {
            while (tp < m && t[tp] != s[sp]) {
                tp++;
            }
            if (tp < m) {
                left_match[sp] = tp;
                tp++;
            } else {
                break;
            }
        }
        
        // If s is already a subsequence of t without any changes
        if (left_match[n - 1] < m) {
            return true;
        }
        
        // right_match[i] stores the latest index in t that matches s[i...n-1]
        std::vector<int> right_match(n, -1);
        tp = m - 1;
        for (int sp = n - 1; sp >= 0; --sp) {
            while (tp >= 0 && t[tp] != s[sp]) {
                tp--;
            }
            if (tp >= 0) {
                right_match[sp] = tp;
                tp--;
            } else {
                break;
            }
        }
        
        if (right_match[0] >= 0) {
            return true;
        }

        // Try replacing exactly one character at index i
        for (int i = 0; i < n; ++i) {
            // Get the boundaries in t for the surrounding prefix and suffix
            int l_bound = (i > 0) ? left_match[i - 1] : -1;
            int r_bound = (i < n - 1) ? right_match[i + 1] : m;
            
            // Check if both prefix and suffix are validly matched,
            // and if there is at least one unused index left between them in t
            if (l_bound < m && r_bound > -1 && (r_bound - l_bound) > 1) {
                return true;
            }
        }
        
        return false;
    }
};
```


**Solution 2: (Prefix Sum, try max 1 replacement based on current match)**

                          
    s = "c a t", t = "c h a t"
         ji           ^
           ji           ^
           i j            ^
             ij             ^
                ji
               
-----------------------------------
    s = "p l a n e", t = "a p p l e"
         ji               ^
         i j                ^
           ji                 ^
           i j                  ^
             ji                   ^
             i j


```
Runtime: 12 ms, Beats 84.46%
Memory: 26.04 MB, Beats 84.95%
```
```c++
class Solution {
public:
    bool canMakeSubsequence(string s, string t) {
        int i = 0;  // match length with 0 replacement.
        int j = 0;  // match length with 1 replacement.
        int n = s.length();
        for (char c : t) {
            j = max(j + (j < n && c == s[j] ? 1 : 0), i + 1);
            i += (i < n && c == s[i] ? 1 : 0);
        }
        return j >= n;
    }
};
```
