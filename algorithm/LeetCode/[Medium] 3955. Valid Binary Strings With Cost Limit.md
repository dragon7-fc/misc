3955. Valid Binary Strings With Cost Limit

You are given two integers `n` and `k`.

The cost of a binary string `s` is defined as the sum of all indices `i` (0-based) such that `s[i] == '1'`.

A binary string is considered valid if:

* It does not contain two consecutive `'1'` characters.
* Its cost is less than or equal to `k`.

Return a list of all valid binary strings of length `n` in any order.

 

**Example 1:**
```
Input: n = 3, k = 1

Output: ["000","010","100"]

Explanation:

The binary strings of length 3 without consecutive '1' characters are:

"000" : cost = 0
"100" : cost = 0
"010" : cost = 1
"001" : cost = 2
"101" : cost = 0 + 2 = 2
Among these, the strings with cost less than or equal to k = 1 are "000", "010" and "100".

Thus, the valid strings are ["000", "010", "100"].
```

**Example 2:**
```
Input: n = 1, k = 0

Output: ["0","1"]

Explanation:

The valid binary strings of length 1 are "0" and "1".

Thus the answer is ["0", "1"].
```
 

**Constraints:**

* `1 <= n <= 12`
* `0 <= k <= n * (n - 1) / 2`

# Submissions
---
**Solution 1: (Brute Force, Bitmask)**
```
Runtime: 112 ms, Beats 12.91%
Memory: 29.30 MB, Beats 83.90%
```
```c++
class Solution {
public:
    vector<string> generateValidStrings(int n, int k) {
        vector<string> ans;
        for (int x = 0; x < 1 << n; x ++) {
            string s = string(n, '0');
            for (int i = 0; i < n; i ++) {
                if ((1 << i) & x) {
                    s[i] = '1';
                }
            }
            int cost = 0;
            bool oneone = false;
            for (int i = 1; i < n; i ++) {
                if (s[i] == '1') {
                    if (s[i - 1] == '0') {
                        cost += i;
                    } else {
                        oneone = true;
                    }
                }
            }
            if (oneone == false && cost <= k) {
                ans.push_back(s);
            }
        }
        return ans;
    }
};
```
