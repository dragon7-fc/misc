2495. Number of Subarrays Having Even Product

Given a **0-indexed** integer array `nums`, return the number of 
subarrays of `nums` having an even product.

 

**Example 1:**
```
Input: nums = [9,6,7,13]
Output: 6
Explanation: There are 6 subarrays with an even product:
- nums[0..1] = 9 * 6 = 54.
- nums[0..2] = 9 * 6 * 7 = 378.
- nums[0..3] = 9 * 6 * 7 * 13 = 4914.
- nums[1..1] = 6.
- nums[1..2] = 6 * 7 = 42.
- nums[1..3] = 6 * 7 * 13 = 546.
```

**Example 2:**
```
Input: nums = [7,3,5]
Output: 0
Explanation: There are no subarrays with an even product.
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^5`

# Submissions
---
**Solution 1: (DP)**

__Intuition__

The key insight is that a subarray with even product must contain at least one even number. So we simply count the number of subarrays with even numbers. Here, I organize the counting in this way. Given an array represented by the binary 11110111101111, at index 4 where I seen an even number (represented by 0) I update a variable to 5 indicating 5 numbers have been seen so far. Until next even number (at index 9) each number (regardless of even or odd) contributes a 5 to the final answer. In this way, the algo is summarized as

1. define a variable val starting at 0;
1. at an even number at index i, update the variable to i+1;
1. at each index, increment the answer ans by val.


```
Runtime: 692 ms
Memory: 27.5 MB
```
```python
class Solution:
    def evenProduct(self, nums: List[int]) -> int:
        N = len(nums)
        ans = cur = 0
        for i in range(N):
            if nums[i] % 2 == 0:
                cur = i+1 
            ans += cur
        return ans
```
