1513. Number of Substrings With Only 1s

Given a binary string `s` (a string consisting only of '0' and '1's).

Return the number of substrings with all characters 1's.

Since the answer may be too large, return it modulo 10^9 + 7.

 

**Example 1:**
```
Input: s = "0110111"
Output: 9
Explanation: There are 9 substring in total with only 1's characters.
"1" -> 5 times.
"11" -> 3 times.
"111" -> 1 time.
```

**Example 2:**
```
Input: s = "101"
Output: 2
Explanation: Substring "1" is shown 2 times in s.
```

**Example 3:**
```
Input: s = "111111"
Output: 21
Explanation: Each substring contains only 1's characters.
```

**Example 4:**
```
Input: s = "000"
Output: 0
```

**Constraints:**

* `s[i] == '0' or s[i] == '1'`
* `1 <= s.length <= 10^5`

# Submissions
---
**Solution 1: (Groupby)**
```
Runtime: 56 ms
Memory Usage: 14.8 MB
```
```python
class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        ans = 0
        for k, g in itertools.groupby(s):
            if k == '1':
                n = len(list(g))
                ans += n + n*(n-1)//2
        
        return ans % MOD
```

**Solution 2: (Greedy)**
```
Runtime: 44 ms
Memory Usage: 8.7 MB
```
```c++
class Solution {
public:
    int numSub(string s) {
        int res = 0, count = 0, mod = 1e9 + 7;
        for (char c: s) {
            count = c == '1' ? count + 1 : 0;
            res = (res + count) % mod;
        }
        return res;
    }
};
```

**Solution 2: (Greedy)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 11.78 MB, Beats 11.57%
```
```c++
class Solution {
public:
    int numSub(string s) {
        int a = 0, ans = 0, MOD = 1e9 + 7;
        for (auto c: s) {
            if (c == '1') {
                a += 1;
            } else {
                a = 0;
            }
            ans = (ans + a) % MOD;
        }
        return ans;
    }
};
```
