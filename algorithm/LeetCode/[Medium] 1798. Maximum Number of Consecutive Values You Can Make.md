1798. Maximum Number of Consecutive Values You Can Make

You are given an integer array `coins` of length `n` which represents the `n` coins that you own. The value of the ith coin is `coins[i]`. You can make some value `x` if you can choose some of your `n` coins such that their values sum up to `x`.

Return the maximum number of consecutive integer values that you can make with your coins starting from and including `0`.

Note that you may have multiple coins of the same value.

 

**Example 1:**
```
Input: coins = [1,3]
Output: 2
Explanation: You can make the following values:
- 0: take []
- 1: take [1]
You can make 2 consecutive integer values starting from 0.
```

**Example 2:**
```
Input: coins = [1,1,1,4]
Output: 8
Explanation: You can make the following values:
- 0: take []
- 1: take [1]
- 2: take [1,1]
- 3: take [1,1,1]
- 4: take [4]
- 5: take [4,1]
- 6: take [4,1,1]
- 7: take [4,1,1,1]
You can make 8 consecutive integer values starting from 0.
```

**Example 3:**
```
Input: nums = [1,4,10,3,1]
Output: 20
```

**Constraints:**

* `coins.length == n`
* `1 <= n <= 4 * 10^4`
* `1 <= coins[i] <= 4 * 10^4`

# Submissions
---
**Solution 1: (Math)**

The intuition for this one is cool. Got a few TLE before figuring it out.

This is the realization: if we reached number i, that means that we can make all numbers 0...i. So, if we add a coin with value 5, we can also make numbers 8..12 (i + 5).

The only case when we can have a gap is the coin value is greater than i + 1. So we sort the coins to make sure we process smaller coins first.

```
Runtime: 820 ms
Memory Usage: 19.7 MB
```
```python
class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        max_val = 1
        for c in sorted(coins):
            if c > max_val:
                break
            max_val += c
        return max_val
```