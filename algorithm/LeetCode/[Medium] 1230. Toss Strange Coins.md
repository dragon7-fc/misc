1230. Toss Strange Coins

You have some coins.  The `i`-th coin has a probability `prob[i]` of facing heads when tossed.

Return the probability that the number of coins facing heads equals `target` if you toss every coin exactly once.

 

**Example 1:**
```
Input: prob = [0.4], target = 1
Output: 0.40000
```

**Example 2:**
```
Input: prob = [0.5,0.5,0.5,0.5,0.5], target = 0
Output: 0.03125
```

**Constraints:**

* `1 <= prob.length <= 1000`
* `0 <= prob[i] <= 1`
* `0 <= target <= prob.length`
* Answers will be accepted as correct if they are within `10^-5` of the correct answer.

# Submissions
---
**Solution 1:**

**Explanation:**
* `dp[c][k]` is the prob of tossing `c` first coins and get `k` faced up.
* `dp[c][k] = dp[c - 1][k] * (1 - p) + dp[c - 1][k - 1] * p)`
* where `p` is the prob for `c`-th coin.

**Complexity**
* Time $O(N^2)$
* Space $O(N)$

```
Runtime: 708 ms
Memory Usage: 13.7 MB
```
```python
class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        dp = [1] + [0] * target
        for p in prob:
            for k in range(target, -1, -1):
                dp[k] = (dp[k - 1] if k else 0) * p + dp[k] * (1 - p)
        return dp[target]
```