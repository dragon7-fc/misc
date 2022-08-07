2369. Check if There is a Valid Partition For The Array

You are given a **0-indexed** integer array `nums`. You have to partition the array into one or more contiguous subarrays.

We call a partition of the array **valid** if each of the obtained subarrays satisfies **one** of the following conditions:

1. The subarray consists of **exactly** `2` equal elements. For example, the subarray `[2,2]` is good.
1. The subarray consists of **exactly** `3` equal elements. For example, the subarray `[4,4,4]` is good.
* The subarray consists of **exactly** `3` consecutive increasing elements, that is, the difference between adjacent elements is `1`. For example, the subarray `[3,4,5]` is good, but the subarray `[1,3,5]` is not.

Return `true` if the array has **at least** one valid partition. Otherwise, return `false`.

 

**Example 1:**
```
Input: nums = [4,4,4,5,6]
Output: true
Explanation: The array can be partitioned into the subarrays [4,4] and [4,5,6].
This partition is valid, so we return true.
```

**Example 2:**
```
Input: nums = [1,1,1,2]
Output: false
Explanation: There is no valid partition for this array.
```

**Constraints:**

* `2 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^6`

# Submissions
---
**Solution 1: (DP Top-Down)**
```
Runtime: 1279 ms
Memory Usage: 123.2 MB
```
```python
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        
        @functools.lru_cache(None)
        def dp(i):
            if i == N:
                return True
            if i <= N-2:
                if nums[i] == nums[i+1]:
                    if dp(i+2):
                        return True
            if i <= N-3:
                if nums[i] == nums[i+1] == nums[i+2] or nums[i+1] == nums[i]+1 and nums[i+2] == nums[i]+2:
                    if dp(i+3):
                        return True
            return False
        
        return dp(0)
```

**Solution 2: (DP Bottom-Up)**
```
Runtime: 279 ms
Memory Usage: 83.8 MB
```
```c++
class Solution {
public:
    bool validPartition(vector<int>& nums) {
        int n = nums.size(), dp[4] = {0, 0, 0, 1};
        for (int i = 0; i < n; ++i) {
            dp[i % 4] = 0;
            if (i - 1 >= 0 && nums[i] == nums[i - 1])
                dp[i % 4] |= dp[(i + 2) % 4];
            if (i - 2 >= 0 && nums[i] == nums[i - 1] && nums[i - 1] == nums[i - 2])
                dp[i % 4] |= dp[(i + 1) % 4];
            if (i - 2 >= 0 && nums[i] - 1 == nums[i - 1] && nums[i - 1] == nums[i - 2] + 1)
                dp[i % 4] |= dp[(i + 1) % 4];
        }
        return dp[(n - 1) % 4];
    }
};
```
