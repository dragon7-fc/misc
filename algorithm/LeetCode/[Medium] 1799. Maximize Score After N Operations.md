1799. Maximize Score After N Operations

You are given `nums`, an array of positive integers of size `2 * n`. You must perform `n` operations on this array.

In the `i`th operation (1-indexed), you will:

* Choose two elements, `x` and `y`.
* Receive a score of `i * gcd(x, y)`.
* Remove `x` and `y` from nums.

Return the maximum score you can receive after performing `n` operations.

The function `gcd(x, y)` is the greatest common divisor of `x` and `y`.

 

**Example 1:**
```
Input: nums = [1,2]
Output: 1
Explanation: The optimal choice of operations is:
(1 * gcd(1, 2)) = 1
```

**Example 2:**
```
Input: nums = [3,4,6,8]
Output: 11
Explanation: The optimal choice of operations is:
(1 * gcd(3, 6)) + (2 * gcd(4, 8)) = 3 + 8 = 11
```

**Example 3:**
```
Input: nums = [1,2,3,4,5,6]
Output: 14
Explanation: The optimal choice of operations is:
(1 * gcd(1, 5)) + (2 * gcd(2, 4)) + (3 * gcd(3, 6)) = 1 + 4 + 9 = 14
```

**Constraints:**

* `1 <= n <= 7`
* `nums.length == 2 * n`
* `1 <= nums[i] <= 10^6`

# Submissions
---
**Solution 1: (DP Top-Down)**

We need to do the full search for this one. For each i, we try every pair from the remaining numbers. Fortunately, the number of pairs in this problem is limited to 7.

Nonetheless, we need to do memoisation to avoid TLE. We can track numbers that we used using a bit mask, and also use that bitmask for the memoisation. For 14 numbers, we will have 2 ^ 14 = 16384 possible combinations.

```
Runtime: 1988 ms
Memory Usage: 24.8 MB
```
```python
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dfs(i: int, mask: int) -> int:
            if i > len(nums) // 2:
                return 0;
            res = 0
            for j in range(len(nums)):
                for k in range(j + 1, len(nums)):
                    new_mask = (1 << j) + (1 << k)
                    if not mask & new_mask:
                        res = max(res, i * gcd(nums[j], nums[k]) + dfs(i + 1, mask + new_mask))
            return res
        return dfs(1, 0)
```