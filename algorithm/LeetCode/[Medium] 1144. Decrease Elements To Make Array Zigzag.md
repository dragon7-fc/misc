1144. Decrease Elements To Make Array Zigzag

Given an array `nums` of integers, a move consists of choosing any element and **decreasing it by 1**.

An array `A` is a zigzag array if either:

* Every even-indexed element is greater than adjacent elements, ie. `A[0] > A[1] < A[2] > A[3] < A[4] > ...`
* OR, every odd-indexed element is greater than adjacent elements, ie. `A[0] < A[1] > A[2] < A[3] > A[4] < ...`

Return the minimum number of moves to transform the given array `nums` into a zigzag array.

 

**Example 1:**
```
Input: nums = [1,2,3]
Output: 2
Explanation: We can decrease 2 to 0 or 3 to 1.
```

**Example 2:**
```
Input: nums = [9,6,1,6,2]
Output: 4
```

# Submissions
---
**Solution 1: (Greedy)**
```
Runtime: 40 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        def countMoves(nums, isGreater):
            count = 0
            for i in range(len(nums) - 1):
                if isGreater:
                    ## nums[i] should be > nums[i + 1]
                    if nums[i] <= nums[i + 1]: 
                        count += nums[i + 1] - nums[i] + 1
                        nums[i + 1] = nums[i] - 1

                else:
                    ## nums[i] should be < nums[i + 1]
                    if nums[i] >= nums[i + 1]:
                        count += nums[i] - nums[i + 1] + 1
                        nums[i] = nums[i + 1] - 1

                isGreater = not isGreater

            return count
        
        return min(countMoves(nums.copy(), True), countMoves(nums.copy(), False))
        
    
        
```