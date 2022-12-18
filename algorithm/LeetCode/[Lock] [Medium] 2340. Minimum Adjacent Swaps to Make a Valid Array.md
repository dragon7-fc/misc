2340. Minimum Adjacent Swaps to Make a Valid Array

You are given a **0-indexed** integer array `nums`.

**Swaps** of **adjacent** elements are able to be performed on nums.

A **valid** array meets the following conditions:

* The largest element (any of the largest elements if there are multiple) is at the rightmost position in the array.
* The smallest element (any of the smallest elements if there are multiple) is at the leftmost position in the array.

Return the **minimum** swaps required to make `nums` a valid array.

 

**Example 1:**
```
Input: nums = [3,4,5,5,3,1]
Output: 6
Explanation: Perform the following swaps:
- Swap 1: Swap the 3rd and 4th elements, nums is then [3,4,5,3,5,1].
- Swap 2: Swap the 4th and 5th elements, nums is then [3,4,5,3,1,5].
- Swap 3: Swap the 3rd and 4th elements, nums is then [3,4,5,1,3,5].
- Swap 4: Swap the 2nd and 3rd elements, nums is then [3,4,1,5,3,5].
- Swap 5: Swap the 1st and 2nd elements, nums is then [3,1,4,5,3,5].
- Swap 6: Swap the 0th and 1st elements, nums is then [1,3,4,5,3,5].
It can be shown that 6 swaps is the minimum swaps required to make a valid array.
```

**Example 2:**
```
Input: nums = [9]
Output: 0
Explanation: The array is already valid, so we return 0.
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^5`

# Submissions
---
**Solution 1: (Greedy)**
```
Runtime: 512 ms
Memory: 27.7 MB
```
```python
class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        N = len(nums)
        left = right = 0
        mn, mx = float('inf'), float('-inf')
        for i in range(N):
            if nums[i] >= nums[right]:
                right = i
            if nums[i] < nums[left]:
                left = i
        ans = N - 1 - right + left
        ans -= 1 if left > right else 0
        return ans
```
