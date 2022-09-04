2400. Number of Ways to Reach a Position After Exactly k Steps

You are given two **positive** integers `startPos` and `endPos`. Initially, you are standing at position `startPos` on an **infinite** number line. With one step, you can move either one position to the left, or one position to the right.

Given a positive integer `k`, return the number of different ways to reach the position `endPos` starting from `startPos`, such that you perform exactly `k` steps. Since the answer may be very large, return it modulo `10^9 + 7`.

Two ways are considered different if the order of the steps made is not exactly the same.

**Note** that the number line includes negative integers.

 

**Example 1:**
```
Input: startPos = 1, endPos = 2, k = 3
Output: 3
Explanation: We can reach position 2 from 1 in exactly 3 steps in three ways:
- 1 -> 2 -> 3 -> 2.
- 1 -> 2 -> 1 -> 2.
- 1 -> 0 -> 1 -> 2.
It can be proven that no other way is possible, so we return 3.
```

**Example 2:**
```
Input: startPos = 2, endPos = 5, k = 10
Output: 0
Explanation: It is impossible to reach position 5 from position 2 in exactly 10 steps.
```

**Constraints:**

* `1 <= startPos, endPos, k <= 1000`

# Submissions
---
**Solution 1: (Math)**

**Explanation**

Two sufficient and necessary conditions from a to b with k steps:

* abs(a - b) <= k
* (a - b - k) % 2 == 0

Otherwice no ways, directly return 0.

Now two eqations

* left + right = k
* right - left = b - a

So we can have right = (b - a + k) / 2.
The combinations is to pick right steps from k steps to go right.
return result combination(k, right)


**Complexity**

* Time O(klogk)
* Space O(1)

```
Runtime: 32 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        if (startPos - endPos - k) % 2: return 0
        return comb(k, (endPos - startPos + k) // 2) % (10 ** 9 + 7)
```

**Solution 2: (Math)**
```
Runtime: 3 ms
Memory Usage: 6 MB
```
```c++
class Solution {
    int p = 1e9 + 7;
    long inv(long a) {
        if (a == 1) return 1;
        return (p - p / a) * inv(p % a) % p;
    }
public:
    int numberOfWays(int startPos, int endPos, int k) {
        if ((startPos - endPos - k) % 2) return 0;
        if (abs(startPos - endPos) > k) return 0;
        long long res = 1L;
        for (int i = 0; i < (endPos - startPos + k) / 2; ++i) {
            res = res * (k - i) % p;
            res = res * inv(i + 1) % p;
        }
        return res;
    }
};
```

**Solution 3: (DP Top-Down)**
```
Runtime: 24 ms
Memory Usage: 10.3 MB
```
```c++
class Solution {
    int dp[1000][1001] = {};
    int dfs(int d, int k) {
        if (d >= k)
            return d == k;
        if (dp[d][k] == 0)
            dp[d][k] = (1 + dfs(d + 1, k - 1) + dfs(d + (d ? -1 : 1), k - 1)) % 1000000007;
        return dp[d][k] - 1;
    } 
public:
    int numberOfWays(int startPos, int endPos, int k) {
        return dfs(abs(startPos - endPos), k);
    }
};
```
