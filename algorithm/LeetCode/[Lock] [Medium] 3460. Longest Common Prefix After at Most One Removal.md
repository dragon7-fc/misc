3460. Longest Common Prefix After at Most One Removal

You are given two strings `s` and `t`.

Return the length of the **longest common prefix** between `s` and `t` after removing at most one character from `s`.

**Note**: `s` can be left without any removal.

 

**Example 1:**
```
Input: s = "madxa", t = "madam"

Output: 4

Explanation:

Removing s[3] from s results in "mada", which has a longest common prefix of length 4 with t.
```

**Example 2:**
```
Input: s = "leetcode", t = "eetcode"

Output: 7

Explanation:

Removing s[0] from s results in "eetcode", which matches t.
```

**Example 3:**
```
Input: s = "one", t = "one"

Output: 3

Explanation:

No removal is needed.
```

**Example 4:**
```
Input: s = "a", t = "b"

Output: 0

Explanation:

s and t cannot have a common prefix.
```
 

**Constraints:**

* `1 <= s.length <= 10^5`
* `1 <= t.length <= 10^5`
* `s` and `t` contain only lowercase English letters.

# Submissions
---
**Solution 1: (Greedy)**

    s = "m a d x a", t = "m a d a m"
         ^^^^^   ^        ^^^^^^^

```
Runtime: 0 ms, Beats 100.00%
Memory: 31.92 MB, Beats 9.68%
```
```c++
class Solution {
public:
    int longestCommonPrefix(string s, string t) {
        int m = s.size(), n = t.size(), i = 0, j;
        for (j = 0; i < m && j < n && i - j < 2; j ++) {
            if (s[i] == t[j]) {
                i += 1;
            } else {
                i += 1;
                j -= 1;
            }
        }
        return j;
    }
};
```
