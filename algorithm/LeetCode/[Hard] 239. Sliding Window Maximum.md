239. Sliding Window Maximum

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

**Example:**
```
Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```

**Note:**

* You may assume `k` is always valid, `1 ≤ k ≤ input array's size` for non-empty array.

**Follow up:**

* Could you solve it in linear time?

# Submissions
---
**Solution 1: (Sliding Window)**
```
Runtime: 688 ms
Memory Usage: 19.4 MB
```
```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        return [max(nums[i: i + k]) for i in range(len(nums) - (k -1))] if nums else []
```

**Solution 2: (Sliding Window)**
```
Runtime: 152 ms
Memory Usage: 19.8 MB
```
```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        num_cur = nums[:k]
        ans = [max(num_cur)]
        for i, v in enumerate(nums[k:]):
            num_cur += [v]
            if ans[-1] != num_cur.pop(0) and k > 1:
                ans += max(ans[-1], v),                
            else:                
                ans += [max(num_cur)]
        return ans
```