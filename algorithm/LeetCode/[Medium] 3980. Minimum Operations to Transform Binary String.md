3980. Minimum Operations to Transform Binary String

You are given two binary strings `s1` and `s2` of the same length `n`.

You can perform the following operations on `s1` any number of times, in any order:

* Choose an index `i` such that `s1[i] == '0'`, and change it to `'1'`.
* Choose an index `i` such that `0 <= i < n - 1`, and both `s1[i]` and `s1[i + 1]` are `'1'`. Change both characters to `'0'`.

Return the **minimum** number of operations required to make `s1` equal to `s2`. If it is impossible, return `-1`.

 

**Example 1:**
```
Input: s1 = "11", s2 = "00"

Output: 1

Explanation:

Change indices 0 and 1 from '1' to '0' in one operation, so "11" becomes "00". Thus, the answer is 1.
```

**Example 2:**
```
Input: s1 = "01", s2 = "10"

Output: 3

Explanation:

Change index 0 from '0' to '1', so "01" becomes "11".
Change indices 0 and 1 from '1' to '0', so "11" becomes "00".
Change index 0 from '0' to '1', so "00" becomes "10".
Thus, the answer is 3.
```

**Example 3:**
```
Input: s1 = "1", s2 = "0"

Output: -1

Explanation:

The first operation cannot change '1' to '0', and the second operation requires two adjacent characters. Therefore, it is impossible.
```
 

**Constraints:**

* `1 <= n == s1.length == s2.length <= 10^5`
* `s1` and `s2` consist only of `'0'` and `'1'`.

# Submissions
---
**Solution 1: (Greedy, Simulation)**
```
Runtime: 12 ms, Beats 83.33%
Memory: 30.19 MB, Beats 58.33%
```
```c++
class Solution {
public:
    int minOperations(string s1, string s2) {
       if (s1 == "1" && s2 == "0") {
            return -1;
        }
        int res = 0, n = s1.length();
        for (int i = 0; i < n; i++) {
            if (s1[i] == s2[i]) {
                continue;
            }
            res++;
            // s1[i] == '0' && s2[i] == '1'
            if (s1[i] == '0') {
                s1[i] = '1';

            // s1[i] == '1' && s2[i] == '0'
            } else {
                // replace s1[i - 1: i] = '11'
                if (i == n - 1) {
                    res += s1[i - 1] == '0';
                    res += s2[i - 1] == '1';

                // replace s1[i: i + 1] = '11' 
                } else {
                    res += s1[i + 1] == '0';
                    s1[i] = '0';
                    s1[i + 1] = '0';
                }
            }
        }
        return res;
    }
};
```
