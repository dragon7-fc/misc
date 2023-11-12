2930. Number of Strings Which Can Be Rearranged to Contain Substrin

You are given an integer `n`.

A string s is called **good** if it contains only lowercase English characters and it is possible to rearrange the characters of `s` such that the new string contains `"leet"` as a substring.

For example:

* The string `"lteer"` is good because we can rearrange it to form `"leetr"` .
* `"letl"` is not good because we cannot rearrange it to contain `"leet"` as a substring.

Return the **total** number of good strings of length `n`.

Since the answer may be large, return it modulo `10^9 + 7`.

A **substring** is a contiguous sequence of characters within a string.

 
 

**Example 1:**
```
Input: n = 4
Output: 12
Explanation: The 12 strings which can be rearranged to have "leet" as a substring are: "eelt", "eetl", "elet", "elte", "etel", "etle", "leet", "lete", "ltee", "teel", "tele", and "tlee".
```

**Example 2:**
```
Input: n = 10
Output: 83943898
Explanation: The number of strings with length 10 which can be rearranged to have "leet" as a substring is 526083947580. Hence the answer is 526083947580 % (109 + 7) = 83943898.
```

**Constraints:**

* `1 <= n <= 10^5`

# Submissions
---
**Solution 1: (Math)**
```
Runtime: 41 ms
Memory: 16.3 MB
```
```python
class Solution:
    def stringCount(self, n: int) -> int:
        mod = 10 ** 9 + 7
        if n < 4:
            return 0

        # total combination:
        ans = pow(26, n, mod)
        
        # l = 0
        sub = (pow(25, n, mod)) % mod
        # t = 0
        sub += (pow(25, n, mod)) % mod
        # e = 0, 1
        sub += (pow(25, n, mod) + n * pow(25, n-1, mod)) % mod
        # l = 0, t = 0
        sub -= pow(24, n, mod)
        # l = 0, e < 2
        sub -= (pow(24, n, mod) + n * pow(24, n-1, mod)) % mod
        # t = 0, e < 2
        sub -= (pow(24, n, mod) + n * pow(24, n-1, mod)) % mod
        # l = 0, t = 0, e < 2
        sub += (pow(23, n, mod) + n * pow(23, n-1, mod)) % mod
        return (ans - sub) % mod
```

# Submissions
---
**Solution 1: (DP Top-Down)**
```
Runtime: 383 ms
Memory: 27.9 MB
```
```c++
class Solution {
    long long mod = 1e9+7;
    long long dp[100001][3][2][2];
    long long dfs(int index, int n, int e, int l, int t){
        if (index == n) {
            if (e >= 2 && l >= 1 && t >= 1) {
                return 1;
            }
            return 0;
        }
        if (dp[index][e][l][t] != - 1) {
            return dp[index][e][l][t];
        }
        long long rst = 0;
        for (int i = 0; i < 26; i++) {
            if (i == 4 && e < 2) {
                // 'e'
                rst = (rst + dfs(index+1, n, e+1, l, t))%mod;
            } else if (i == 11 && l < 1){
                // 'l'
                rst = (rst + dfs(index+1, n, e, l+1, t))%mod;
            } else if (i == 19 && t < 1){
                // 't'
                rst = (rst + dfs(index+1, n, e, l, t+1))%mod;
            } else {
                rst = (rst + dfs(index+1, n, e, l, t))%mod;
            }
            
        }
        return dp[index][e][l][t] = rst;
    }
public:
    int stringCount(int n) {
        memset(dp,-1,sizeof(dp));
        return (int)(dfs(0,n,0,0,0)%mod);
    }
};
```
