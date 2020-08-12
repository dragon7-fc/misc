259. 3Sum Smaller

Given an array of n integers `nums` and a `target`, find the number of index triplets `i, j, k` with `0 <= i < j < k < n` that satisfy the condition `nums[i] + nums[j] + nums[k] < target`.

**Example:**
```
Input: nums = [-2,0,1,3], and target = 2
Output: 2 
Explanation: Because there are two triplets which sums are less than 2:
             [-2,0,1]
             [-2,0,3]
```

* Follow up: Could you solve it in O(n^2) runtime?

# Solution
---
**Solution 1: (Array, Sort, Two Pointers)**
```
Runtime: 140 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        N = len(nums)
        if not nums or len(nums) < 3:
            return 0
        count = 0
        nums.sort()
        for firstIndex in range(N - 3 + 1):
            lo, hi = firstIndex + 1, N - 1
            while lo < hi:
                threeSum = nums[firstIndex] + nums[lo] + nums[hi]
                if threeSum < target:
                    count += (hi - lo)
                    lo += 1
                else:
                    hi -= 1
        
        return count
```