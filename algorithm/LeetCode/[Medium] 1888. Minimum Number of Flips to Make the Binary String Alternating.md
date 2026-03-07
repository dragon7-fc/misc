1888. Minimum Number of Flips to Make the Binary String Alternating

You are given a binary string `s`. You are allowed to perform two types of operations on the string in any sequence:

* **Type-1**: **Remove** the character at the start of the string `s` and **append** it to the end of the string.
* **Type-2**: **Pick** any character in `s` and **flip** its value, i.e., if its value is `'0'` it becomes `'1'` and vice-versa.

Return the **minimum** number of **type-2** operations you need to perform such that `s` becomes alternating.

The string is called **alternating** if no two adjacent characters are equal.

* For example, the strings `"010"` and `"1010"` are alternating, while the string `"0100"` is not.
 

**Example 1:**
```
Input: s = "111000"
Output: 2
Explanation: Use the first operation two times to make s = "100011".
Then, use the second operation on the third and sixth elements to make s = "101010".
```

**Example 2:**
```
Input: s = "010"
Output: 0
Explanation: The string is already alternating.
```

**Example 3:**
```
Input: s = "1110"
Output: 1
Explanation: Use the second operation on the second element to make s = "1010".
```

**Constraints:**

* `1 <= s.length <= 10^5`
* `s[i]` is either `'0'` or `'1'`.

# Submissions
---
**Solution 1: (Sliding Window, extend)**
```
Runtime: 1204 ms
Memory Usage: 16.5 MB
```
```python
class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s
        alt1, alt2 = "", ""
        for i in range(len(s)):
            alt1 += "0" if i % 2 else "1"
            alt2 += "1" if i % 2 else "0"
        
        res = len(s)
        l = 0
        diff1, diff2 = 0, 0
        for r in range(len(s)):
            if s[r] != alt1[r]:
                diff1 += 1
            if s[r] != alt2[r]:
                diff2 += 1
            
            if r - l + 1 > n:
                if s[l] != alt1[l]:
                    diff1 -=1
                if s[l] != alt2[l]:
                    diff2 -=1
                l += 1
            if r - l + 1 == n:
                res = min(res, diff1, diff2)
        return res
```

**Solution 2: (Analysis + Prefix Sum + Suffix Sum)**

    s = "1 1 1 0 0 0"
pre
0        0 1 1 1 2 2
1        0 0 1 2 2 3

```
Runtime: 298 ms, Beats 6.00%
Memory: 119.01 MB, Beats 5.20%
```
```c++
class Solution {
public:
    int minFlips(string s) {
        // Characteristic function
        auto I = [](char ch, int x) -> int { return ch - '0' == x; };

        int n = s.size();
        vector<vector<int>> pre(n, vector<int>(2));
        // Note the boundary case when i=0
        for (int i = 0; i < n; ++i) {
            pre[i][0] = (i == 0 ? 0 : pre[i - 1][1]) + I(s[i], 1);
            pre[i][1] = (i == 0 ? 0 : pre[i - 1][0]) + I(s[i], 0);
        }

        int ans = min(pre[n - 1][0], pre[n - 1][1]);
        if (n % 2 == 1) {
            // If n is an odd number, it is also necessary to calculate suf
            vector<vector<int>> suf(n, vector<int>(2));
            // Note the boundary case when i = n - 1
            for (int i = n - 1; i >= 0; --i) {
                suf[i][0] = (i == n - 1 ? 0 : suf[i + 1][1]) + I(s[i], 1);
                suf[i][1] = (i == n - 1 ? 0 : suf[i + 1][0]) + I(s[i], 0);
            }
            for (int i = 0; i + 1 < n; ++i) {
                ans = min(ans, pre[i][0] + suf[i + 1][0]);
                ans = min(ans, pre[i][1] + suf[i + 1][1]);
            }
        }

        return ans;
    }
};
```

**Solution 3: (Sliding Window, DP Bottom-Up, Brute Force)**

            s          s
        ---------- ----------
type1   .          .
        x
typw2   . . . . . 
         . . . . .

s0                           start with '0'
s1                           start with '1'

              s           s
    s =  1 1 1 0 0 0|1 1 1 0 0 0
         0 1 0 1 0 1|0 1 0 1 0 1
s0       1   2 3   4|5   5 5   5    + type2  
                    |4   4 4   4    - type1
         1 0 1 0 1 0|1 0 1 0 1 0
s1         1     2  |  3     3      + type2
                    |  2     2      - type1
ans                2
```
Runtime: 7 ms, Beats 91.60%
Memory: 14.20 MB, Beats 98.00%
```
```c++
class Solution {
public:
    int minFlips(string s) {
        int res = INT_MAX, s0 = 0, s1 = 0, sz = s.size();
        for (int i = 0; i < 2 * sz; ++i) {
            s0 += s[i % sz] != '0' + i % 2;
            s1 += s[i % sz] != '0' + (1 - i % 2);
            if (i >= sz - 1) {
                if (i >= sz) {
                    s0 -= s[i - sz] != '0' + (i - sz) % 2;
                    s1 -= s[i - sz] != '0' + (1 - (i - sz) % 2);
                }
                res = min(res, min(s0, s1));
            }
        }
        return res;
    }
};
```
