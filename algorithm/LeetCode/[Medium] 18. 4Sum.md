18. 4Sum

Given an array `nums` of n integers and an integer `target`, are there elements a, b, c, and d in `nums` such that `a + b + c + d = target`? Find all unique quadruplets in the array which gives the sum of `target`.

Note:

The solution set must not contain duplicate quadruplets.

**Example:**
```
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
```

# Submissions
---
**Solution 1:**
```
Runtime: 172 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if nums == None or len(nums) == 0:
            return nums
        
        nums.sort()
        ans = []
        
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                two_sum = target - nums[i] - nums[j]
                min_sum = nums[j+1] + nums[j+2]
                max_sum = nums[len(nums)-1] + nums[len(nums)-2]
                if two_sum < min_sum or two_sum > max_sum:
                    continue
                left = j+1
                right = len(nums)-1
                while left<right:
                    tmp_sum = nums[left]+nums[right]
                    if tmp_sum == two_sum:
                        l = [nums[i], nums[j], nums[left], nums[right]]
                        ans.append(l)
                        left += 1
                        right -= 1
                    elif tmp_sum < two_sum:
                        left += 1
                    elif tmp_sum > two_sum:
                        right -= 1
                        
        # remove duplicate
        ans = set([tuple(sorted(x)) for x in ans])
        return ans
```