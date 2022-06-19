2311. Longest Binary Subsequence Less Than or Equal to K

You are given a binary string `s` and a positive integer `k`.

Return the length of the longest subsequence of `s` that makes up a binary number less than or equal to `k`.

**Note:**

* The subsequence can contain **leading zeroes**.
* The empty string is considered to be equal to `0`.
* A **subsequence** is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
 

**Example 1:**
```
Input: s = "1001010", k = 5
Output: 5
Explanation: The longest subsequence of s that makes up a binary number less than or equal to 5 is "00010", as this number is equal to 2 in decimal.
Note that "00100" and "00101" are also possible, which are equal to 4 and 5 in decimal, respectively.
The length of this subsequence is 5, so 5 is returned.
```

**Example 2:**
```
Input: s = "00101001", k = 1
Output: 6
Explanation: "000001" is the longest subsequence of s that makes up a binary number less than or equal to 1, as this number is equal to 1 in decimal.
The length of this subsequence is 6, so 6 is returned.
```

**Constraints:**

* `1 <= s.length <= 1000`
* `s[i]` is either `'0'` or `'1'`.
* `1 <= k <= 10^9`

# Submissions
---
**Solution 1: (DP Bottom-Up)**

dp[i] means the minimum value of subsequence with length i

```
Runtime: 3870 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        dp = [0]
        for v in map(int, s):
            if dp[-1] * 2 + v <= k:
                dp.append(dp[-1] * 2 + v)
            for i in range(len(dp) - 1, 0, -1):
                dp[i] = min(dp[i], dp[i - 1] * 2 + v)
        return len(dp) - 1
```

**Solution 2: (DP Bottom-Up)**
```
Runtime: 54 ms
Memory Usage: 6.6 MB
```
```c++
class Solution {
public:
    int longestSubsequence(string s, int k) {
        int dp[1010] = {}, j = 0;
        for (char& v : s) {
            if (dp[j] * 2 + v - '0' <= k)
                dp[++j] = dp[j] * 2 + v - '0';
            for (int i = j; i > 0; --i)
                dp[i] = min(dp[i], dp[i - 1] * 2 + v - '0');
        }
        return j;
    }
};
```
