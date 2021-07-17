18. 4Sum

Given an array `nums` of n integers and an integer `target`, are there elements a, b, c, and d in `nums` such that `a + b + c + d = target`? Find all unique quadruplets in the array which gives the sum of `target`.

**Note:**

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
**Solution 1: (Two Pointers)**

* Time: O(N^3)
* Space: O(N)

```
Runtime: 84 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            res = []
            if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
                return res
            if k == 2:
                return twoSum(nums, target)
            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for _, set in enumerate(kSum(nums[i + 1:], target - nums[i], k - 1)):
                        res.append([nums[i]] + set)
            return res

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            res = []
            lo, hi = 0, len(nums) - 1
            while (lo < hi):
                sum = nums[lo] + nums[hi]
                if sum < target or (lo > 0 and nums[lo] == nums[lo - 1]):
                    lo += 1
                elif sum > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                    hi -= 1
                else:
                    res.append([nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
            return res

        nums.sort()
        return kSum(nums, target, 4)
```

**Solution 2: (Hash Set)**

* Time: O(N^3)
* Space: O(N)

```
Runtime: 92 ms
Memory Usage: 14.4 MB
```
```python
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
                return []
            if k == 2:
                return twoSum(nums, target)
            res = []
            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for _, set in enumerate(kSum(nums[i + 1:], target - nums[i], k - 1)):
                        res.append([nums[i]] + set)
            return res

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            res = []
            s = set()
            for i in range(len(nums)):
                if len(res) == 0 or res[-1][1] != nums[i]:
                    if target - nums[i] in s:
                        res.append([target - nums[i], nums[i]])
                s.add(nums[i])
            return res

        nums.sort()
        return kSum(nums, target, 4)
```

**Solution 3: (Two Pointers)**
```
Runtime: 120 ms
Memory Usage: 14.4 MB
```
```python
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if nums == None or len(nums) == 0:
            return nums
        N = len(nums)
        nums.sort()
        ans = []
        for i in range(N-3):
            for j in range(i+1, N-2):
                t = target - nums[i] -  nums[j]
                min_sum = nums[j+1] + nums[j+2]
                max_sum = nums[-1] + nums[-2]
                if t < min_sum or t > max_sum:
                    continue
                left = j+1
                right = N-1
                while left < right:
                    cur = nums[left] + nums[right]
                    if cur == t:
                        ans += [[nums[i], nums[j], nums[left], nums[right]]]
                        left += 1
                        right -= 1
                    elif cur < t:
                        left += 1
                    else:
                        right -= 1
        ans = set([tuple(x) for x in ans])
        return ans
```
