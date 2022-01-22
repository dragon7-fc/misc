1712. Ways to Split Array Into Three Subarrays

A split of an integer array is **good** if:

* The array is split into three non-empty contiguous subarrays - named `left`, `mid`, `right` respectively from left to right.
* The sum of the elements in `left` is less than or equal to the sum of the elements in `mid`, and the sum of the elements in `mid` is less than or equal to the sum of the elements in `right`.

Given `nums`, an array of **non-negative** integers, return the number of **good** ways to split `nums`. As the number may be too large, return it **modulo** `10^9 + 7`.

 

**Example 1:**
```
Input: nums = [1,1,1]
Output: 1
Explanation: The only good way to split nums is [1] [1] [1].
```

**Example 2:**
```
Input: nums = [1,2,2,2,5,0]
Output: 3
Explanation: There are three good ways of splitting nums:
[1] [2] [2,2,5,0]
[1] [2,2] [2,5,0]
[1,2] [2,2] [5,0]
```

**Example 3:**
```
Input: nums = [3,2,1]
Output: 0
Explanation: There is no good way to split nums.
```

**Constraints:**

* `3 <= nums.length <= 10^5`
* `0 <= nums[i] <= 10^4`

# Submissions
---
**Solution 1: (Binary Search)**
```
Runtime: 1552 ms
Memory Usage: 26.3 MB
```
```python
class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        mod, pre_sum = int(1e9+7), [nums[0]]
        for num in nums[1:]:                               # create prefix sum array
            pre_sum.append(pre_sum[-1] + num)
        ans, n = 0, len(nums)
        for i in range(n):                                 # pre_sum[i] is the sum of the 1st segment
            prev = pre_sum[i]                              # i+1 is the starting index of the 2nd segment
            if prev * 3 > pre_sum[-1]: break               # break loop if first segment is larger than the sum of 2 & 3 segments
                
            j = bisect.bisect_left(pre_sum, prev * 2, i+1) # j is the first possible ending index of 2nd segment
                
            middle = (prev + pre_sum[-1]) // 2             # last possible ending value of 2nd segment
            k = bisect.bisect_right(pre_sum, middle, j+1)  # k-1 is the last possible ending index of 2nd segment
            if k-1 >= n or pre_sum[k-1] > middle: continue # make sure the value satisfy the condition since we are using bisect_right here
            ans = (ans + min(k, n - 1) - j) % mod          # count & handle edge case
        return ans
```
