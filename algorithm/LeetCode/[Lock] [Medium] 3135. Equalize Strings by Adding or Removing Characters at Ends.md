3135. Equalize Strings by Adding or Removing Characters at Ends

Given two strings `initial` and `target`, your task is to modify `initial` by performing a series of operations to make it equal to `target`.

In one operation, you can add or remove one character only at the beginning or the end of the string `initial`.

Return the **minimum** number of operations required to transform `initial` into `target`.

 

**Example 1:**
```
Input: initial = "abcde", target = "cdef"

Output: 3

Explanation:

Remove 'a' and 'b' from the beginning of initial, then add 'f' to the end.
```

**Example 2:**
```
Input: initial = "axxy", target = "yabx"

Output: 6

Explanation:

Operation	Resulting String
Add 'y' to the beginning	"yaxxy"
Remove from end	"yaxx"
Remove from end	"yax"
Remove from end	"ya"
Add 'b' to the end	"yab"
Add 'x' to the end	"yabx"
```

**Example 3:**
```
Input: initial = "xyz", target = "xyz"

Output: 0

Explanation:

No operations are needed as the strings are already equal.
```
 

**Constraints:**

* `1 <= initial.length, target.length <= 1000`
* `initial` and `target` consist only of lowercase English letters.

# Submissions
---
**Solution 1: (Hash Table, longest common substring)**
```
Runtime: 40 ms
Memory: 13.17 MB
```
```c++
class Solution {
public:
    int minOperations(string initial, string target) {
        int m = initial.size(), n = target.size(), cur , k, ans = m+n;
        vector<vector<int>> dp(26);
        for (int i = 0; i < n; i ++) {
            dp[target[i]-'a'].push_back(i);
        }
        for (int i = 0; i < m; i ++) {
            for (auto j: dp[initial[i]-'a']) {
                cur = 0;
                k = 0;
                while (i+k < m && j+k < n && initial[i+k] == target[j+k]) {
                    k += 1;
                }
                cur += (m-k) + (n-k);
                ans = min(ans, cur);
            }
        }
        return ans;
    }
};
```
