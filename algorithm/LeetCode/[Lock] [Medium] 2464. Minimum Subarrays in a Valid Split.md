2464. Minimum Subarrays in a Valid Split

You are given an integer array `nums`.

Splitting of an integer array `nums` into subarrays is valid if:

* the greatest common divisor of the first and last elements of each subarray is **greater** than `1`, and
* each element of `nums` belongs to exactly one subarray.

Return the **minimum** number of subarrays in a valid subarray splitting of `nums`. If a valid subarray splitting is not possible, return `-1`.

**Note** that:

* The **greatest common divisor** of two numbers is the largest positive integer that evenly divides both numbers.
* A **subarray** is a contiguous non-empty part of an array.
 

**Example 1:**
```
Input: nums = [2,6,3,4,3]
Output: 2
Explanation: We can create a valid split in the following way: [2,6] | [3,4,3].
- The starting element of the 1st subarray is 2 and the ending is 6. Their greatest common divisor is 2, which is greater than 1.
- The starting element of the 2nd subarray is 3 and the ending is 3. Their greatest common divisor is 3, which is greater than 1.
It can be proved that 2 is the minimum number of subarrays that we can obtain in a valid split.
```

**Example 2:**
```
Input: nums = [3,5]
Output: 2
Explanation: We can create a valid split in the following way: [3] | [5].
- The starting element of the 1st subarray is 3 and the ending is 3. Their greatest common divisor is 3, which is greater than 1.
- The starting element of the 2nd subarray is 5 and the ending is 5. Their greatest common divisor is 5, which is greater than 1.
It can be proved that 2 is the minimum number of subarrays that we can obtain in a valid split.
```

**Example 3:**
```
Input: nums = [1,2,1]
Output: -1
Explanation: It is impossible to create valid split.
```

**Constraints:**

* `1 <= nums.length <= 1000`
* `1 <= nums[i] <= 10^5`

# Submissions
---
**Solution 1: (DP Bottom-Up)**
```
Runtime: 1157 ms
Memory: 14.1 MB
```
```python
class Solution:
    def validSubarraySplit(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [float('inf')] * (N + 1)
        dp[0] = 0
        if nums[0] != 1:
            dp[1] = 1 
        for i in range(1, N):
            for j in range(i+1):
                if math.gcd(nums[i], nums[j]) > 1:
                    dp[i+1] = min(dp[i+1], dp[j] + 1)     
        return dp[N] if dp[N] < float('inf') else -1
```

**Solution 2: (DP Top-Down)**
```
Runtime: 788 ms
Memory: 15.8 MB
```
```python
class Solution:
    def validSubarraySplit(self, nums: List[int]) -> int:
        N = len(nums)
        
        @functools.lru_cache(None)
        def dp(i):
            if i == N:
                return 0
            rst = 1001
            for j in range(i, N):
                if gcd(nums[i], nums[j]) > 1:
                    if dp(j+1) != -1:
                        rst = min(rst, 1 + dp(j+1))
            return -1 if rst == 1001 else rst
        
        return dp(0)
```
