1871. Jump Game VII

You are given a **0-indexed** binary string `s` and two integers `minJump` and `maxJump`. In the beginning, you are standing at index `0`, which is equal to `'0'`. You can move from index `i` to index `j` if the following conditions are fulfilled:

* `i + minJump <= j <= min(i + maxJump, s.length - 1)`, and
* `s[j] == '0'`.

Return `true` if you can reach index `s.length - 1` in `s`, or `false` otherwise.

 

**Example 1:**
```
Input: s = "011010", minJump = 2, maxJump = 3
Output: true
Explanation:
In the first step, move from index 0 to index 3. 
In the second step, move from index 3 to index 5.
```

**Example 2:**
```
Input: s = "01101110", minJump = 2, maxJump = 3
Output: false
```

**Constraints:**

* `2 <= s.length <= 10^5`
* `s[i]` is either `'0'` or `'1'`.
* `s[0] == '0'`
* `1 <= minJump <= maxJump < s.length`

# Submissions
---
**Solution 1: (BFS)**
```
Runtime: 388 ms
Memory Usage: 24.4 MB
```
```python
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        queue = collections.deque([0])
        visited, mx = set([0]), 0
        while queue:
            i = queue.popleft()
            for j in range(max(i + minJump, mx + 1), min(i + maxJump + 1, len(s))):
                if s[j] == '0' and j not in visited:
                    if j == len(s) - 1: return True
                    queue.append(j)
                    visited.add(j)
            mx = max(mx, i + maxJump)
        return False
```

**Solution 1: (DP Bottom-Up, prefix sum)**

dp[i] = true if we can reach s[i].
pre means the number of previous position that we can jump from.

```
Runtime: 75 ms
Memory: 17.1 MB
```
```c++
class Solution {
public:
    bool canReach(string s, int minJump, int maxJump) {
        int n = s.size(), pre = 0;
        vector<bool> dp(n, false);
        dp[0] = true;
        for (int i = 1; i < n; ++i) {
            if (i >= minJump)
                pre += dp[i - minJump];
            if (i > maxJump)
                pre -= dp[i - maxJump - 1];
            dp[i] = pre > 0 && s[i] == '0';
        }
        return dp[n - 1];
    }
};
```
