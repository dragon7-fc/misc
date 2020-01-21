16. 3Sum Closest

Given an array `nums` of n integers and an integer `target`, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

**Example:**
```
Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
```

# Submissions
---
**Solution 1: (Two pointer, Binary search)**
```
Runtime: 124 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()                  # sort nums to perform two pointers
        result = sum(nums[:3])       # initial sum
        numsLen = len(nums)
        diff = abs(result - target)  # initial diff

        for i in range(numsLen):
            left, right = i + 1, numsLen - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                curDiff = abs(total - target)

                # compare previous diff and current diff
                # if current diff is smaller, update previous diff
                # and result to current diff and result
                if curDiff < diff:
                    diff = curDiff
                    result = total

                if total < target:   # move left pointer rightward for larger val
                    left += 1
                elif total > target: # move right pointer leftward for smaller val
                    right -= 1
                else:                # if total == target, we can directly return
                    return result

        return result
```

**Solution 2: (Two pointer, Binary search)**
```
Runtime: 104 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if not nums or len(nums) < 3:
            return 0
        
        nums.sort()
        if sum(nums[:3]) > target:
            return sum(nums[:3])
        if nums[-1] + nums[-2] + nums[-3] < target:
            return nums[-1] + nums[-2] + nums[-3] 

        rec = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                temp = nums[i] + nums[l] + nums[r]
                ans = abs(target - temp)
                if rec == [] or ans < rec[0]:
                    rec = [ans, temp]
                if temp == target:
                    return target
                elif temp < target:
                    l += 1
                else:
                    r -= 1
        
        return rec[1]
```