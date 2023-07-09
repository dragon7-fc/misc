2767. Partition String Into Minimum Beautiful Substrings


Given a binary string `s`, partition the string into one or more **substrings** such that each substring is **beautiful**.

A string is **beautiful** if:

* It doesn't contain leading zeros.
* It's the **binary** representation of a number that is a power of `5`.

Return the **minimum number** of substrings in such partition. If it is impossible to partition the string s into beautiful substrings, return `-1`.

A **substring** is a contiguous sequence of characters in a string.

 

**Example 1:**
```
Input: s = "1011"
Output: 2
Explanation: We can paritition the given string into ["101", "1"].
- The string "101" does not contain leading zeros and is the binary representation of integer 51 = 5.
- The string "1" does not contain leading zeros and is the binary representation of integer 50 = 1.
It can be shown that 2 is the minimum number of beautiful substrings that s can be partitioned into.
```

**Example 2:**
```
Input: s = "111"
Output: 3
Explanation: We can paritition the given string into ["1", "1", "1"].
- The string "1" does not contain leading zeros and is the binary representation of integer 50 = 1.
It can be shown that 3 is the minimum number of beautiful substrings that s can be partitioned into.
```

**Example 3:**
```
Input: s = "0"
Output: -1
Explanation: We can not partition the given string into beautiful substrings.
```

**Constraints:**

* `1 <= s.length <= 15`
* `s[i]` is either `'0'` or `'1'`.

# Submissions
---
**Solution 1: (DP Top-Down)**
```
Runtime: 82 ms
Memory: 16.5 MB
```
```python
class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        n = len(s)
        
        @functools.lru_cache(None)
        def dp(i):
            if i == n:
                return 0
            if (s[i] == '0'):
                return float('inf')
            rst = float('inf')
            cur = 0
            for j in range(i, n):
                cur <<= 1
                cur += 1 if s[j] == '1' else 0
                k = 0
                while 5**k < cur:
                    k += 1
                if 5**k == cur:
                    rst = min(rst, 1 + dp(j+1))
            return rst
            
        ans = dp(0)
        return ans if ans != float('inf') else -1
```

**Solution 2: (DP Bottom-Up)**
```
Runtime: 55 ms
Memory: 16.4 MB
```
```python
class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        seen = set(5 ** i for i in range(16))
        n = len(s)
        dp = [0] + [inf] * n
        for i in range(n):
            if s[i] == '0':
                continue
            cur = 0
            for j in range(i, n):
                cur = cur * 2 + int(s[j])
                if cur in seen:
                    dp[j + 1] = min(dp[j + 1], dp[i] + 1)
        return dp[n] if dp[n] < inf else -1
```

**Solution 3: (DP Bottom-Up)**
```
Runtime: 5 ms
Memory: 6.4 MB
```
```c++
class Solution {
public:
    int minimumBeautifulSubstrings(string s) {
        unordered_set<int> p5{ 1, 5, 25, 125, 625, 3125, 15625 };  
        vector<int> dp(s.size() + 1, s.size() + 1);
        dp[s.size()] = 0;
        for (int i = s.size() - 1; i >= 0; --i) {
            for (int j = i, val = 0; s[i] != '0' && j < s.size(); ++j) {
                val = val * 2 + s[j] - '0';
                if (p5.count(val))
                    dp[i] = min(dp[i], 1 + dp[j + 1]);
            }
        }
        return dp[0] > s.size() ? -1 : dp[0];
    }
};
```
