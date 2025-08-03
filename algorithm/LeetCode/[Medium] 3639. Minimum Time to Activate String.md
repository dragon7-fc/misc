3639. Minimum Time to Activate String

You are given a string `s` of length `n` and an integer array `order`, where order is a permutation of the numbers in the range `[0, n - 1]`.

Starting from time t = 0, replace the character at index `order[t]` in `s` with `'*'` at each time step.

A **substring** is **valid** if it contains at least one `'*'`.

A string is **active** if the total number of **valid** substrings is greater than or equal to `k`.

Return the **minimum** time `t` at which the string `s` becomes active. If it is impossible, return `-1`.

Note:

A permutation is a rearrangement of all the elements of a set.
A substring is a contiguous non-empty sequence of characters within a string.
 

**Example 1:**
```
Input: s = "abc", order = [1,0,2], k = 2

Output: 0

Explanation:

t	order[t]	Modified s	Valid Substrings	Count	Active
(Count >= k)
0	1	"a*c"	"*", "a*", "*c", "a*c"	4	Yes
The string s becomes active at t = 0. Thus, the answer is 0.
```

**Example 2:**
```
Input: s = "cat", order = [0,2,1], k = 6

Output: 2

Explanation:

t	order[t]	Modified s	Valid Substrings	Count	Active
(Count >= k)
0	0	"*at"	"*", "*a", "*at"	3	No
1	2	"*a*"	"*", "*a", "*a*", "a*", "*"	5	No
2	1	"***"	All substrings (contain '*')	6	Yes
The string s becomes active at t = 2. Thus, the answer is 2.
```

**Example 3:**
```
Input: s = "xy", order = [0,1], k = 4

Output: -1

Explanation:

Even after all replacements, it is impossible to obtain k = 4 valid substrings. Thus, the answer is -1.
```
 

**Constraints:**

* `1 <= n == s.length <= 105`
* `order.length == n`
* `0 <= order[i] <= n - 1`
* `s` consists of lowercase English letters.
* `order` is a permutation of integers from `0` to `n - 1`.
* `1 <= k <= 109`

# Submissions
---
**Solution 1: (Binary Search)**
```
Runtime: 89 ms, Beats 56.25%
Memory: 279.59 MB, Beats 18.75%
```
```c++
class Solution {
    bool check(int mid, string &s, vector<int> &order, int k) {
        int n = s.length(), i;
        long long ck = 0;
        string cs = s;
        vector<int> dp(n);
        for (i = 0; i <= mid; i ++) {
            cs[order[i]] = '*';
        }
        dp[n-1] = n;
        if (cs[n-1] == '*') {
            dp[n-1] = n-1;
        }
        ck += n - dp[n-1];
        for (i = n-2; i >= 0; i --) {
            dp[i] = dp[i+1];
            if (cs[i] == '*') {
                dp[i] = i;
            }
            ck += n - dp[i];
        }
        return ck >= k;
    }
public:
    int minTime(string s, vector<int>& order, int k) {
        int n = s.size(), left = 0, right = n-1, mid, ans = -1;
        while (left <= right) {
            mid = left + (right - left)/2;
            if (!check(mid, s, order, k)) {
                left = mid + 1;
            } else {
                ans = mid;
                right = mid - 1;
            }
        }
        return ans;
    }
};
```
