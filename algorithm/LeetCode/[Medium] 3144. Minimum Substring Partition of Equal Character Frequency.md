3144. Minimum Substring Partition of Equal Character Frequency

Given a string `s`, you need to partition it into one or more **balanced substrings**. For example, if `s == "ababcc"` then `("abab", "c", "c")`, `("ab", "abc", "c")`, and `("ababcc")` are all valid partitions, but `("a", "bab", "cc")`, `("aba", "bc", "c")`, and `("ab", "abcc")` are not. The unbalanced substrings are bolded.

Return the **minimum** number of substrings that you can partition `s` into.

**Note:** A **balanced** string is a string where each character in the string occurs the same number of times.

 

**Example 1:**
```
Input: s = "fabccddg"

Output: 3

Explanation:

We can partition the string s into 3 substrings in one of the following ways: ("fab, "ccdd", "g"), or ("fabc", "cd", "dg").
```

**Example 2:**
```
Input: s = "abababaccddb"

Output: 2

Explanation:

We can partition the string s into 2 substrings like so: ("abab", "abaccddb").
```
 

**Constraints:**

* `1 <= s.length <= 1000`
* `s` consists only of English lowercase letters.

# Submissions
---
**Solution 1: (DP Bottom-Up)**
```
Runtime: 89 ms
Memory: 8.97 MB
```
```c++
class Solution {
public:
    int minimumSubstringsInPartition(string s) {
        int n = s.size(), c;
        vector<int> dp(n+1, INT_MAX);
        bool flag;
        dp[0] = 0;
        int cnt[26];
        for (int i = 0; i < n; i ++) {
            memset(cnt, 0, sizeof(cnt));
            for (int j = i; j < n; j ++) {
                cnt[s[j]-'a'] += 1;
                flag = true;
                c = 0;
                for (int k = 0; k < 26; k ++) {
                    if (c == 0) {
                        c = cnt[k];
                    } else if (cnt[k] && c != cnt[k]) {
                        flag = false;
                        break;
                    }
                }
                if (flag) {
                    dp[j+1] = min(dp[j+1], dp[i] + 1);
                }
            }
        }
        return dp.back();
    }
};
```
