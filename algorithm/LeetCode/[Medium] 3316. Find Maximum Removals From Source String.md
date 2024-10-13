3316. Find Maximum Removals From Source String

You are given a string `source` of size `n`, a string `pattern` that is a **subsequence** of `source`, and a sorted integer array `targetIndices` that contains distinct numbers in the range `[0, n - 1]`.

We define an operation as removing a character at an index `idx` from `source` such that:

* `idx` is an element of targetIndices.
* `pattern` remains a **subsequence** of `source` after removing the character.

Performing an operation does not change the indices of the other characters in `source`. For example, if you remove `'c'`from `"acb"`, the character at index `2` would still be `'b'`.

Return the **maximum** number of operations that can be performed.

 

**Example 1:**
```
Input: source = "abbaa", pattern = "aba", targetIndices = [0,1,2]

Output: 1

Explanation:

We can't remove source[0] but we can do either of these two operations:

Remove source[1], so that source becomes "a_baa".
Remove source[2], so that source becomes "ab_aa".
```

**Example 2:**
```
Input: source = "bcda", pattern = "d", targetIndices = [0,3]

Output: 2

Explanation:

We can remove source[0] and source[3] in two operations.
```

**Example 3:**
```
Input: source = "dda", pattern = "dda", targetIndices = [0,1,2]

Output: 0

Explanation:

We can't remove any character from source.
```

**Example 4:**
```
Input: source = "yeyeykyded", pattern = "yeyyd", targetIndices = [0,2,3,4]

Output: 2

Explanation:

We can remove source[2] and source[3] in two operations.
```
 

**Constraints:**

* `1 <= n == source.length <= 3 * 10^3`
* `1 <= pattern.length <= n`
* `1 <= targetIndices.length <= n`
* `targetIndices` is sorted in ascending order.
* The input is generated such that `targetIndices` contains distinct elements in the range `[0, n - 1]`.
* `source` and `pattern` consist only of lowercase English letters.
* The input is generated such that `pattern` appears as a subsequence in `source`.

# Submissions
---
**Solution 1: (DP Bottom-Up)**
```
Runtime: 2627 ms
Memory: 197.59 MB
```
```python
class Solution:
    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
        m, n = len(source), len(pattern)
        s = set(targetIndices)
        dp = [[-float("inf")] * (n + 1) for _ in range(m + 1)]
        dp[m][n] = 0
        for i in range(m - 1, -1, -1):
            for j in range(n, -1, -1):
                if j == n: dp[i][j] = int(i in s) + dp[i + 1][j]
                else:
                    dp[i][j] = int(i in s) + dp[i + 1][j]
                    if source[i] == pattern[j]: dp[i][j] = max(dp[i][j], dp[i + 1][j + 1])
        return dp[0][0] if dp[0][0] != -float("inf") else 0
```

**Solution 2: (DP Bottom-Up)**
  
  a b a
a 1 2 3 3  V
b ~ 1 2 2  V
b ~ 0 1 1  V
a ~ ~ 0 0
a ~ ~ 0 0
        0
```
Runtime: 268 ms
Memory: 94.08 MB
```
```c++
class Solution {
public:
    int maxRemovals(string source, string pattern, vector<int>& targetIndices) {
        int m = source.size(), n = pattern.size();
        unordered_set<int> st(targetIndices.begin(), targetIndices.end());
        vector<vector<int>> dp(m+1, vector<int>(n+1, INT_MIN));
        dp[m][n] = 0;
        for (int i = m-1; i >= 0; i --) {
            for (int j = n; j >= 0; j --) {
                if (j == n) {
                    dp[i][j] = st.count(i) + dp[i+1][j];
                } else {
                    # not_taken
                    dp[i][j] = st.count(i) + dp[i+1][j];
                    # taken
                    if (source[i] == pattern[j]) {
                        dp[i][j] = max(dp[i][j], dp[i+1][j+1]);
                    }
                }
            }
        }
        return  dp[0][0] != INT_MIN ? dp[0][0] : 0;
    }
};
```
