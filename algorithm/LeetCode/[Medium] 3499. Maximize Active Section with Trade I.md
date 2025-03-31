3499. Maximize Active Section with Trade I

You are given a binary string `s` of length `n`, where:

* `'1'` represents an active section.
* `'0'` represents an inactive section.

You can perform **at most one trade** to maximize the number of active sections in `s`. In a trade, you:

* Convert a contiguous block of `'1'`s that is surrounded by `'0'`s to all `'0'`s.
* Afterward, convert a contiguous block of `'0'`s that is surrounded by `'1'`s to all `'1'`s.

Return the maximum number of active sections in `s` after making the optimal trade.

**Note**: Treat `s` as if it is augmented with a `'1'` at both ends, forming `t = '1' + s + '1'`. The augmented `'1'`s do not contribute to the final count.

 

**Example 1:**
```
Input: s = "01"

Output: 1

Explanation:

Because there is no block of '1's surrounded by '0's, no valid trade is possible. The maximum number of active sections is 1.
```

**Example 2:**
```
Input: s = "0100"

Output: 4

Explanation:

String "0100" → Augmented to "101001".
Choose "0100", convert "101001" → "100001" → "111111".
The final string without augmentation is "1111". The maximum number of active sections is 4.
```

**Example 3:**
```
Input: s = "1000100"

Output: 7

Explanation:

String "1000100" → Augmented to "110001001".
Choose "000100", convert "110001001" → "110000001" → "111111111".
The final string without augmentation is "1111111". The maximum number of active sections is 7.
```

**Example 4:**
```
Input: s = "01010"

Output: 4

Explanation:

String "01010" → Augmented to "1010101".
Choose "010", convert "1010101" → "1000101" → "1111101".
The final string without augmentation is "11110". The maximum number of active sections is 4.
```

**Constraints:**

* `1 <= n == s.length <= 10^5`
* `s[i]` is either `'0'` or `'1'`

# Submissions
---
**Solution 1: (Prefix Sum)**

      1|0 1 0|1
      1|0 1 0 1 0|1
        ^^^^^
      1|0 0 0 1 0|1
        ^^^^^
      1|1 1 1 1 0|1
        ^^^^^ ^
        
      1|0 1 0 1 0|1
            ^^^^^
      1|0 1 0 0 0|1
            ^^^^^
      1|0 1 1 1 1|1
          ^ ^^^^^

```
Runtime: 139 ms, Beats 50.00%
Memory: 151.44 MB, Beats 7.14%
```
```c++
class Solution {
public:
    int maxActiveSectionsAfterTrade(string s) {
        int n = s.size(), m, i = 0, cur, k = 0, ans = 0;
        vector<pair<int,int>> dp;
        dp.push_back({-1, -1});
        while (i < n && s[i] == '1') {
            k += 1;
            i += 1;
        }
        if (i) {
            dp.back().second = i-1;
        }
        while (i < n) {
            dp.push_back({i, i});
            k += s[i] == '1';
            while (i+1 < n && s[i+1] == s[i]) {
                k += s[i+1] == '1';
                i += 1;
            }
            dp.back().second = i;
            i += 1;
        }
        if (s[n-1] != '1') {
            dp.push_back({n, n});
        }
        m = dp.size();
        if (m <= 3) {
            return k;
        } else {
            for (i = 2; i + 2 < m; i += 2) {
                cur = dp[i+2].first - dp[i-1].first;
                ans = max(ans, k - (dp[i].second - dp[i].first + 1) + cur);
            }
        }
        return ans;
    }
};
```
