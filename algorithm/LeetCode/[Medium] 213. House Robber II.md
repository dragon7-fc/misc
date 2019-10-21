213. House Robber II

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are **arranged in a circle**. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight **without alerting the police**.

**Example 1:**
```
Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
```

**Example 2:**
```
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
```

# Submissions
---
**Solution 1:**
```
Runtime: 32 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob(nums):
            N = len(nums)
            rob = [0]*(N+1)
            rob[0] = 0
            rob[1] = nums[0]
            for i in range(2, N+1):
                rob[i] = max(rob[i-1], nums[i-1]+rob[i-2])
            return rob[N]
        
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums)==2:
            return max(nums)
        return max([rob(nums[:-1]), rob(nums[1:])])
```