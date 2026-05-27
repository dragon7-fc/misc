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

**Solution 2: (DP Bottom-Up, Prefix Sum, Sliding Window, 2 array)**

    s = "0 1 1 0 1 0", minJump = 2, maxJump = 3
pre      1 1 1 2 2 3 
dp       1     1   1
         l r   i
           l r   i
             l r   i

```
Runtime: 16 ms, Beats 24.78%
Memory: 38.60 MB, Beats 5.42%
```
```c++
class Solution {
public:
    bool canReach(string s, int minJump, int maxJump) {
        int n = s.size();
        vector<int> dp(n), pre(n);
        dp[0] = 1;
        // since we start dynamic programming from i=minJump, we need to
        // precompute the prefix sums for the part [0, minJump)
        for (int i = 0; i < minJump; ++i) {
            pre[i] = 1;
        }
        for (int i = minJump; i < n; ++i) {
            int left = i - maxJump, right = i - minJump;
            if (s[i] == '0') {
                int total = pre[right] - (left <= 0 ? 0 : pre[left - 1]);
                dp[i] = (total != 0);
            }
            pre[i] = pre[i - 1] + dp[i];
        }
        return dp[n - 1];
    }
};
```

**Solution 3: (DP Bottom-Up, Prefix Sum, Sliding Window, count active result in previous sliding window, 1 array)**

    s = "0 1 1 0 1 0", minJump = 2, maxJump = 3
dp       1     1   1
cnt          1   0 1
         ---   ^
             ---   ^
                 

```
Runtime: 9 ms, Beats 61.62%
Memory: 19.78 MB, Beats 95.87%
```
```c++
class Solution {
public:
    bool canReach(string s, int minJump, int maxJump) {
        int n = s.length();
        // If the destination is a wall, it's impossible
        if (s[n - 1] == '1') return false;

        // dp[i] will store whether index i is reachable
        vector<bool> dp(n, false);
        dp[0] = true; // We start at index 0

        int reachableCount = 0;

        for (int i = 1; i < n; ++i) {
            // 1. Add the new element entering the window from the right side
            if (i >= minJump) {
                if (dp[i - minJump]) {
                    reachableCount++;
                }
            }

            // 2. Remove the old element exiting the window from the left side
            if (i > maxJump) {
                if (dp[i - maxJump - 1]) {
                    reachableCount--;
                }
            }

            // 3. If there is at least one reachable index in our window and current char is '0'
            if (reachableCount > 0 && s[i] == '0') {
                dp[i] = true;
            }
        }

        return dp[n - 1];
    }
};
```
