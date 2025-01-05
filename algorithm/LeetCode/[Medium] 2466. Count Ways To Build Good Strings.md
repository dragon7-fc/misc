2466. Count Ways To Build Good Strings

Given the integers `zero`, `one`, `low`, and `high`, we can construct a string by starting with an empty string, and then at each step perform either of the following:

* Append the character `'0'` `zero` times.
* Append the character `'1'` `one` times.

This can be performed any number of times.

A **good** string is a string constructed by the above process having a **length** between `low` and `high` (inclusive).

Return the number of **different** good strings that can be constructed satisfying these properties. Since the answer can be large, return it **modulo** `10^9 + 7`.

 

**Example 1:**
```
Input: low = 3, high = 3, zero = 1, one = 1
Output: 8
Explanation: 
One possible valid good string is "011". 
It can be constructed as follows: "" -> "0" -> "01" -> "011". 
All binary strings from "000" to "111" are good strings in this example.
```

**Example 2:**
```
Input: low = 2, high = 3, zero = 1, one = 2
Output: 5
Explanation: The good strings are "00", "11", "000", "110", and "011".
```

**Constraints:**

* `1 <= low <= high <= 10^5`
* `1 <= zero, one <= low`

# Submissions
---
**Solution 1: (DP Bottom-Up)**
```
Runtime: 746 ms
Memory: 30.1 MB
```
```python
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = Counter({0: 1})
        mod = 10 ** 9 + 7
        for i in range(1, high + 1):
            dp[i] = (dp[i - zero] + dp[i - one]) % mod
        return sum(dp[i] for i in range(low, high + 1)) % modulo
```

**Solution 2: (DP Top-Down)**

       0
       0  0   0
       ^^^^
       ^^^^^^^^
          1   1
        ^^^^^^^^
       1  1   0
       ^^^^
       ^^^^^^^^
    1  1  2   3

    dp[i] = dp[i-zero] + dp[i-one]

    1  2  4  8 

```
Runtime: 371 ms
Memory: 179.5 MB
```
```python
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 1_000_000_007

        @lru_cache(None)
        def dfs(k):
            if k == 0 : return 1
            if k < 0  : return 0
            return (dfs(k-zero) + dfs(k-one)) % mod
        
        dfs(high)
        
        return sum(dfs(k) for k in range(low,high+1)) % mod
```

**Solution 3: (DP Bottom-Up)**
```
Runtime: 2 ms
Memory: 8.65 MB
```
```c++
class Solution {
public:
    int countGoodStrings(int low, int high, int zero, int one) {
        long long dp[100001] = {0}, MOD=1e9 + 7, i;
        long long ans = 0;
        dp[0] = 1;
        for (i = 1; i <= high; i ++) {
            dp[i] = (i-zero >= 0 ? dp[i-zero] : 0) + (i - one >= 0 ? dp[i-one] : 0) % MOD;
            if (i >= low) {
                ans += dp[i];
                ans %= MOD;
            }
        }
        return ans;
    }
};
```
