2031. Count Subarrays With More Ones Than Zeros

You are given a binary array `nums` containing only the integers `0` and `1`. Return the number of **subarrays** in `nums` that have more `1`'s than `0`'s. Since the answer may be very large, return it **modulo** `10^9 + 7`.

A **subarray** is a contiguous sequence of elements within an array.

 

**Example 1:**
```
Input: nums = [0,1,1,0,1]
Output: 9
Explanation:
The subarrays of size 1 that have more ones than zeros are: [1], [1], [1]
The subarrays of size 2 that have more ones than zeros are: [1,1]
The subarrays of size 3 that have more ones than zeros are: [0,1,1], [1,1,0], [1,0,1]
The subarrays of size 4 that have more ones than zeros are: [1,1,0,1]
The subarrays of size 5 that have more ones than zeros are: [0,1,1,0,1]
```

**Example 2:**
```
Input: nums = [0]
Output: 0
Explanation:
No subarrays have more ones than zeros.
```

**Example 3:**
```
Input: nums = [1]
Output: 1
Explanation:
The subarrays of size 1 that have more ones than zeros are: [1]
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `0 <= nums[i] <= 1`

# Submissions
---
**Solution 1: (DP, Hash Table)**
```
Runtime: 1220 ms
Memory Usage: 28.7 MB
```
```python
class Solution:
    def subarraysWithMoreZerosThanOnes(self, nums: List[int]) -> int:
        MOD = 10** 9 + 7
        counts = collections.Counter({0:1})
        res = s = dp = 0
        for n in nums:
            if n:
                s += 1
                dp += counts[s - 1]
            else:
                s -= 1
                dp -= counts[s]
            res = (res + dp) % MOD
            counts[s] += 1
        
        return res % MOD
```
