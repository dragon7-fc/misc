487. Max Consecutive Ones II

Given a binary array `nums`, return the maximum number of consecutive `1`'s in the array if you can flip at most one `0`.

 

**Example 1:**
```
Input: nums = [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the maximum number of consecutive 1s. After flipping, the maximum number of consecutive 1s is 4.
```

**Example 2:**
```
Input: nums = [1,0,1,1,0,1]
Output: 4
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `nums[i]` is either `0` or `1`.

# Submissions
---
**Solution 1: (Sliding Window)**
```
Runtime: 420 ms
Memory Usage: 14.6 MB
```
```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest_sequence = 0
        left, right = 0, 0
        num_zeroes = 0

        while right < len(nums):   # while our window is in bounds
            if nums[right] == 0:    # add the right most element into our window
                num_zeroes += 1

            while num_zeroes == 2:   # if our window is invalid, contract our window
                if nums[left] == 0:    
                    num_zeroes -= 1
                left += 1

            longest_sequence = max(longest_sequence, right - left + 1)   # update our longest sequence answer
            right += 1   # expand our window

        return longest_sequence
```