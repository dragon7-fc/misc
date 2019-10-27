416. Partition Equal Subset Sum

Given a **non-empty** array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

**Note:**

* Each of the array element will not exceed 100.
* The array size will not exceed 200.
 

**Example 1:**
```
Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
```

**Example 2:**
```
Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
```

# Submissions
---
**Solution 1:**
```
Runtime: 664 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return True

        # in case total is odd, then there is no way for us to evenly divide the sum
        total = sum(nums)

        if total & 1:
            return False

        total >>= 1

        dp = [False] * (total + 1)
        dp[0] = True

        for num in nums:
            for s in range(total, num - 1, -1):
                dp[s] = dp[s] or dp[s - num]

        return dp[-1]
```