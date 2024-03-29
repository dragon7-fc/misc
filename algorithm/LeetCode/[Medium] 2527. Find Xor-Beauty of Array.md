2527. Find Xor-Beauty of Array

You are given a **0-indexed** integer array `nums`.

The **effective value** of three indices `i`, `j`, and `k` is defined as `((nums[i] | nums[j]) & nums[k])`.

The **xor-beauty** of the array is the XORing of **the effective values of all the possible triplets** of indices `(i, j, k)` where `0 <= i, j, k < n`.

Return the xor-beauty of `nums`.

**Note** that:

* `val1 | val2` is bitwise OR of `val1` and `val2`.
* `val1 & val2` is bitwise AND of `val1` and `val2`.
 

**Example 1:**
```
Input: nums = [1,4]
Output: 5
Explanation: 
The triplets and their corresponding effective values are listed below:
- (0,0,0) with effective value ((1 | 1) & 1) = 1
- (0,0,1) with effective value ((1 | 1) & 4) = 0
- (0,1,0) with effective value ((1 | 4) & 1) = 1
- (0,1,1) with effective value ((1 | 4) & 4) = 4
- (1,0,0) with effective value ((4 | 1) & 1) = 1
- (1,0,1) with effective value ((4 | 1) & 4) = 4
- (1,1,0) with effective value ((4 | 4) & 1) = 0
- (1,1,1) with effective value ((4 | 4) & 4) = 4 
Xor-beauty of array will be bitwise XOR of all beauties = 1 ^ 0 ^ 1 ^ 4 ^ 1 ^ 4 ^ 0 ^ 4 = 5.
```

**Example 2:**
```
Input: nums = [15,45,20,2,34,35,5,44,32,30]
Output: 34
Explanation: The xor-beauty of the given array is 34.
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^9`

# Submissions
---
**Solution 1: (Greedy)**

The key observation is that the triplets ((nums[i] | nums[j]) & nums[k]) occurs in pairs except when i=j=ki=j=ki=j=k.

* when i=j=ki = j = ki=j=k, the result ((nums[i] | nums[j]) & nums[k]) is the the number itself.
* when i=j but i≠k, we would have nums[i] & nums[k] and nums[k] & nums[i] be valid triplets for each pair of number in nums. XORing them would give 0.
* otherwise, for each nums[k], ((nums[i] | nums[j]) & nums[k]) and ((nums[j] | nums[i]) & nums[k]) would both be a valid triplets and be considered in the final result. Obviously they are the same and XORing them in the last step would make them 0.

Hence, the result is just the XOR of all numbers in the array.

```
Runtime: 385 ms
Memory: 27.7 MB
```
```python
class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        return functools.reduce(operator.xor, nums)
```
