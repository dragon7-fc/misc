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

**Solution 3: (Greedy)**

Such a deceptive problem. The key is to realize that we need to take all zeros.

Then, we take as many 1 from the right as we can, before exceeding k. It can be shown that greedily using 1 from the right is always better than to skip it.

```
Runtime: 5 ms
Memory: 7.1 MB
```
```c++
public:
    int longestSubsequence(string s, int k) {
        int val = 0, cnt = 0, pow = 1;
        for (int i = s.size() - 1; i >= 0 && val + pow <= k; --i) {
            if (s[i] == '1') {
                ++cnt;
                val += pow;
            }
            pow <<= 1;
        }
        return count(begin(s), end(s), '0') + cnt;
    }
};
```

**Solution 4: (Greedy)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 9.43 MB, Beats 73.55%
```
```c++
class Solution {
public:
    int longestSubsequence(string s, int k) {
        int n = s.length(), i, a = 0, ans = 0;
        for (i = n-1; i >= 0; i --) {
            if (s[i] == '1') {
                if (n-1-i < 31 && a + (1<<(n-1-i)) <= k) {
                    a += 1<<(n-1-i);
                    ans = n-i;
                }
            } else {
                ans += 1;
            }
        }
        return ans;
    }
};
```
