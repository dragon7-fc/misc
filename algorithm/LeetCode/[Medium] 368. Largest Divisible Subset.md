368. Largest Divisible Subset

Given a set of **distinct** positive integers, find the largest subset such that every pair $(S_i, S_j)$ of elements in this subset satisfies:

$S_i \% S_j = 0$ or $S_j \% S_i = 0.$

If there are multiple solutions, return any subset is fine.

**Example 1:**

```
Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)
```

**Example 2:**
```
Input: [1,2,4,8]
Output: [1,2,4,8]
```

# Submissions
---
**Solution 1:**
```
Runtime: 424 ms
Memory Usage: 14.1 MB
```
```python
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums.sort()
        n = len(nums)
        # (previous divisible index, length of divisible subset)
        dp = [(-1, 1)] * n
        # (last divisible index, maximum length of divisible subsets)
        maxl = (0, 1)
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[i][1] < dp[j][1] + 1:
                        dp[i] = (j, dp[j][1] + 1)
                        if maxl[1] < dp[i][1]:
                            maxl = (i, dp[i][1])
        ret = []
        x = maxl[0]
        while x > -1:
            ret.append(nums[x])
            x = dp[x][0]
        return ret[::-1]
```

**Solution 2:**
```
Runtime: 456 ms
Memory Usage: 14.1 MB
```
```python
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        if len(nums) ==0: return []
        result = [nums[0]]
        dp = [[nums[i]] for i in range(len(nums))]
        for i in range(len(dp)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if len(dp[j]) + 1 > len(dp[i]):
                        dp[i] = dp[j] + [nums[i]]
            if len(dp[i]) > len(result):
                result = dp[i]
        return result
```