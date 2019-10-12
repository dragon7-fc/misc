1031. Maximum Sum of Two Non-Overlapping Subarrays

Given an array `A` of non-negative integers, return the maximum sum of elements in two non-overlapping (contiguous) subarrays, which have lengths `L` and `M`.  (For clarification, the `L`-length subarray could occur before or after the `M`-length subarray.)

Formally, return the largest `V` for which `V = (A[i] + A[i+1] + ... + A[i+L-1]) + (A[j] + A[j+1] + ... + A[j+M-1])` and either:

* `0 <= i < i + L - 1 < j < j + M - 1 < A.length`, or
* `0 <= j < j + M - 1 < i < i + L - 1 < A.length`.
 

**Example 1:**
```
Input: A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2
Output: 20
Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length 2.
```

**Example 2:**
```
Input: A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2
Output: 29
Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with length 2.
```

**Example 3:**
```
Input: A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3
Output: 31
Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [3,8] with length 3.
```

**Note:**

1. `L >= 1`
1. `M >= 1`
1. `L + M <= A.length <= 1000`
1. `0 <= A[i] <= 1000`

# Submissions
---
**Solution 1:**
```
Runtime: 104 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        N = len(A)
        l_sum, m_sum = [], []
        lm_max = ml_max = 0
        for i in range(N):
            if i+L <= N: l_sum.append(sum(A[i:i+L]))
            if i+M <= N: m_sum.append(sum(A[i:i+M]))
        for i in range(N):
            if i+L+M <= N:
                lm_max = max(lm_max, l_sum[i] + max(m_sum[i+L:]))
                ml_max = max(ml_max, m_sum[i] + max(l_sum[i+M:]))
        return max(lm_max, ml_max)
```