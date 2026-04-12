3900. Longest Balanced Substring After One Swap

You are given a binary string `s` consisting only of characters `'0'` and `'1'`.

A string is **balanced** if it contains an equal number of `'0'`s and `'1'`s.

You can perform **at most one** swap between any two characters in s. Then, you select a **balanced substring** from `s`.

Return an integer representing the **maximum** length of the **balanced** substring you can select.

 

**Example 1:**
```
Input: s = "100001"

Output: 4

Explanation:

Swap "100001". The string becomes "101000".
Select the substring "101000", which is balanced because it has two '0's and two '1's.
```

**Example 2:**
```
Input: s = "111"

Output: 0

Explanation:

Choose not to perform any swaps.
Select the empty substring, which is balanced because it has zero '0's and zero '1's.
```

**Constraints:**

* `1 <= s.length <= 10^5`
* `s` consists only of the characters `'0'` and `'1'`.

# Submissions
---
**Solution 1: (Hash Table, prefix state index)**
```
Runtime: 718 ms, Beats 51.71%
Memory: 243.72 MB, Beats 56.25%
```
```c++
class Solution {
public:
    int longestBalanced(string s) {
        int n = s.length(), i, k, b = 0, one = 0, zero = 0, k_one, k_zero, ans = 0;
        unordered_map<int, vector<int>> mp;
        zero = count_if(s.begin(), s.end(), [](auto &c){return c == '0';});
        one = n - zero;
        mp[0].push_back(-1);
        for (i = 0; i < n; i ++) {
            b += s[i] == '1' ? 1 : -1;
            if (mp.count(b)) {
                ans = max(ans, i - mp[b][0]);
            }
            if (mp.count(b - 2)) {
                auto &dp = mp[b - 2];
                for (auto &j: dp) {
                    k = i - j;
                    k_zero = (k - 2) / 2;
                            //   ^^^
                            //   b-2 -> b
                            //   need 2 '1'
                    if (zero > k_zero) {
                        ans = max(ans, k);
                        break;
                    }
                }
            }
            if (mp.count(b + 2)) {
                auto &dp = mp[b + 2];
                for (auto &j: dp) {
                    k = i - j;
                    k_one = (k - 2) / 2;
                    if (one > k_one) {
                        ans = max(ans, k);
                        break;
                    }
                }
            }
            mp[b].push_back(i);
        }
        return ans;
    }
};
```
