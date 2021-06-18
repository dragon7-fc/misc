795. Number of Subarrays with Bounded Maximum

We are given an array `A` of positive integers, and two positive integers `L` and `R` `(L <= R)`.

Return the number of (contiguous, non-empty) subarrays such that the value of the maximum array element in that subarray is at least `L` and at most `R`.

**Example :**
```
Input: 
A = [2, 1, 4, 3]
L = 2
R = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].
```

**Note:**

* `L`, `R`  and `A[i]`` will be an integer in the range `[0, $10^9$]`.
* The length of A will be in the range of `[1, 50000]`.

# Submissions
---
**Solution: (Greedy, Two Pointers)**
```
Runtime: 384 ms
Memory Usage: 15.2 MB
```
```python
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        start = 0
        last = -1
        count = 0
        for i in range(len(nums)):
            if nums[i] > right:
                start = i + 1
            else:
                if nums[i] >= left:
                    last = i
                if last >= start:
                    count += last - start + 1

        return count
```
