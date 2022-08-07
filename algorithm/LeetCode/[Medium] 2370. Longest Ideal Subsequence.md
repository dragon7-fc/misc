2370. Longest Ideal Subsequence

You are given a string `s` consisting of lowercase letters and an integer `k`. We call a string `t` **ideal** if the following conditions are satisfied:

* `t` is a subsequence of the string `s`.
* The absolute difference in the alphabet order of every two **adjacent** letters in `t` is less than or equal to `k`.

Return the length of the **longest** ideal string.

A **subsequence** is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

**Note** that the alphabet order is not cyclic. For example, the absolute difference in the alphabet order of `'a'` and `'z'` is `25`, not `1`.

 

**Example 1:**
```
Input: s = "acfgbd", k = 2
Output: 4
Explanation: The longest ideal string is "acbd". The length of this string is 4, so 4 is returned.
Note that "acfgbd" is not ideal because 'c' and 'f' have a difference of 3 in alphabet order.
```

**Example 2:**
```
Input: s = "abcd", k = 3
Output: 4

Explanation: The longest ideal string is "abcd". The length of this string is 4, so 4 is returned.
```

**Constraints:**

* `1 <= s.length <= 10^5`
* `0 <= k <= 25`
* `s` consists of lowercase English letters.

# Submissions
---
**Solution 1: (DP Bottom-Up)**
```
Runtime: 790 ms
Memory Usage: 14.7 MB
```
```python
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 128
        for c in s:
            i = ord(c)
            dp[i] = max(dp[i - k : i + k + 1]) + 1
        return max(dp)
```

**Solution 2: (DP Bottom-Up)**
```
Runtime: 103 ms
Memory Usage: 10 MB
```
```c++
class Solution {
public:
    int longestIdealString(string s, int k) {
        int dp[150] = {}, res = 0;
        for (auto& i : s) {
            for (int j = i - k; j <= i + k; ++j)
                dp[i] = max(dp[i], dp[j]);
            res = max(res, ++dp[i]);
        }
        return res;
    }
};
```
