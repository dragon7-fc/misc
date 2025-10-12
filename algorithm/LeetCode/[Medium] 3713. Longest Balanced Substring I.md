3713. Longest Balanced Substring I

You are given a string `s` consisting of lowercase English letters.

A **substring** of `s` is called **balanced** if all distinct characters in the **substring** appear the **same** number of times.

Return the length of the **longest** balanced substring of `s`.

 

**Example 1:**
```
Input: s = "abbac"

Output: 4

Explanation:

The longest balanced substring is "abba" because both distinct characters 'a' and 'b' each appear exactly 2 times.
```

**Example 2:**
```
Input: s = "zzabccy"

Output: 4

Explanation:

The longest balanced substring is "zabc" because the distinct characters 'z', 'a', 'b', and 'c' each appear exactly 1 time.​​​​​​​
```

**Example 3:**
```
Input: s = "aba"

Output: 2

Explanation:

One of the longest balanced substrings is "ab" because both distinct characters 'a' and 'b' each appear exactly 1 time. Another longest balanced substring is "ba".
```
 

**Constraints:**

* `1 <= s.length <= 1000`
* `s` consists of lowercase English letters.

# Submissions
---
**Solution 1: (Counter)**
```
Runtime: 392 ms, Beats 12.50%
Memory: 11.59 MB, Beats 75.00%
```
```c++
class Solution {
public:
    int longestBalanced(string s) {
        int n = s.size(), i, j, ans = 0;
        vector<int> cnt(26);
        for (i = 0; i < n; i ++) {
            fill(cnt.begin(), cnt.end(), 0);
            for (j = i; j < n; j ++) {
                cnt[s[j] - 'a'] += 1;
                if (all_of(cnt.begin(), cnt.end(), [&](auto c){return c == 0 || c == cnt[s[j] - 'a'];})) {
                    ans = max(ans, j - i + 1);
                }
            }
        }
        return ans;
    }
};
```
