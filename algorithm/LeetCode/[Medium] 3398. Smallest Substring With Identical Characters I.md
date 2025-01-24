3398. Smallest Substring With Identical Characters I

You are given a binary string `s` of length `n` and an integer `numOps`.

You are allowed to perform the following operation on `s` at most `numOps` times:

* Select any index `i` (where `0 <= i < n`) and **flip** `s[i]`. If `s[i] == '1'`, change `s[i] to '0'` and vice versa.
You need to **minimize** the length of the **longest substring** of `s` such that all the characters in the substring are **identical**.

Return the **minimum** length after the operations.

 

**Example 1:**
```
Input: s = "000001", numOps = 1

Output: 2

Explanation: 

By changing s[2] to '1', s becomes "001001". The longest substrings with identical characters are s[0..1] and s[3..4].
```

**Example 2:**
```
Input: s = "0000", numOps = 2

Output: 1

Explanation: 

By changing s[0] and s[2] to '1', s becomes "1010".

Example 3:

Input: s = "0101", numOps = 0

Output: 1
```
 

**Constraints:**

* `1 <= n == s.length <= 1000`
* `s` consists only of `'0'` and `'1'`.
* `0 <= numOps <= n`

# Submissions
---
**Solution 1: (Binary Search)**
```
Runtime: 0 ms
Memory: 9.90 MB
```
```c++
class Solution {
    bool check(int mid, string &s, int numOps) {
        int n = s.size(), i, j = 0;
        if (mid == 1) {
            int op = 0, op2 = 0;
            for (i = 0; i < n; i ++) {
                op += s[i] == ('0' + i%2);
                op2 += s[i] == ('0' + (i+1)%2);
            }
            return min(op, op2) <= numOps;
        }
        int cnt = 0;
        string cs = s;
        i = 0;
        while (j < n) {
            j = i+1;
            while (j < n && j-i < mid && cs[j] == cs[i]) {
                j += 1;
            }
            if (j < n && j == i+mid) {
                if (j < n-1 && cs[j] == cs[i] && cs[j+1] != cs[i]) {
                    cnt += 1;
                } else {
                    cnt += cs[j] == cs[i];
                    cs[j] = '0' + (cs[i]-'0')^1;
                }
            }
            i = j;
        }
        return  cnt <= numOps;
    }
public:
    int minLength(string s, int numOps) {
        int left = 1, right = s.size(), mid, ans;
        while (left <= right) {
            mid = left + (right-left)/2;
            if (!check(mid, s, numOps)) {
                left = mid+1;
            } else {
                ans = mid;
                right = mid-1;
            }
        }
        return ans;
    }
};
```
