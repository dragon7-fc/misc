2505. Bitwise OR of All Subsequence Sums

Given an integer array `nums`, return the value of the bitwise **OR** of the sum of all possible **subsequences** in the array.

A **subsequence** is a sequence that can be derived from another sequence by removing zero or more elements without changing the order of the remaining elements.

 

**Example 1:**
```
Input: nums = [2,1,0,3]
Output: 7
Explanation: All possible subsequence sums that we can have are: 0, 1, 2, 3, 4, 5, 6.
And we have 0 OR 1 OR 2 OR 3 OR 4 OR 5 OR 6 = 7, so we return 7.
```

**Example 2:**
```
Input: nums = [0,0,0]
Output: 0
Explanation: 0 is the only possible subsequence sum we can have, so we return 0.
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `0 <= nums[i] <= 10^9`

# Submissions
---
**Solution 1: (prefix sum)**

__Intuition__

The set bit of the final result has two possible sources

1. set bit in one of an original number;
1. set bit as a result of a subsequence sum.
For the 2nd source where the set bit is carried over from lower bits, you can always get the it from a prefix sum. As a result, the solution is like below.

```
Runtime: 488 ms
Memory: 24.8 MB
```
```python
class Solution:
    def subsequenceSumOr(self, nums: List[int]) -> int:
        ans = prefix = 0 
        for x in nums: 
            prefix += x
            ans |= x | prefix 
        return ans
```
