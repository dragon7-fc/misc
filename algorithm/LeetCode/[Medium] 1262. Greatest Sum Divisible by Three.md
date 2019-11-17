1262. Greatest Sum Divisible by Three

Given an array `nums` of integers, we need to find the maximum possible sum of elements of the array such that it is divisible by three.

 

**Example 1:**

```
Input: nums = [3,6,5,1,8]
Output: 18
Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).
```

**Example 2:**

```
Input: nums = [4]
Output: 0
Explanation: Since 4 is not divisible by 3, do not pick any number.
```

**Example 3:**

```
Input: nums = [1,2,3,4,4]
Output: 12
Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).
```

**Constraints:**

* `1 <= nums.length <= 4 * 10^4`
* `1 <= nums[i] <= 10^4`

# Submissions
---
**Solution 1:**

`f[i]` is the biggest value can possibly have after ith iteration, with remainder 0,1,2.
```
For example, the input is 3,6,5,1,8. The initial f would be
[[3,0,0],
[0,0,0],
[0,0,0],
[0,0,0],
[0,0,0]].
After the first iteration, which the ith value is 6. The f would become
[[3,0,0],
[9,0,0],
[0,0,0],
[0,0,0],
[0,0,0]].
After 2nd iteration, when ith value is 5, f becomes
[[3,0,0],
[9,0,0],
[9,0,14], (14 is from 9 + 5)
[0,0,0],
[0,0,0]].
Then, ith value is 1
[[3,0,0],
[9,0,0],
[9,0,14],
[15,10,14], (15 is from 14 + 1, 10 is from 9 + 1)
[0,0,0]].
And finally, ith value is 8
[[3,0,0],
[9,0,0],
[9,0,14],
[15,10,14],
[18,22,23]]. (18 is from 10 + 8, 22 is from 14 + 8, 23 is from 15 + 8)
```
```
Runtime: 524 ms
Memory Usage: 22.9 MB
```
```python
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [[0]*3 for _ in range(len(nums))]
        dp[0][nums[0] % 3] = nums[0]
        for i in range(1, len(nums)):
            for j in range(3):
                include = dp[i - 1][(j - nums[i]) % 3] + nums[i]
                if include % 3 == j:
                    dp[i][j] = max(dp[i-1][j], include)
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][0]
```