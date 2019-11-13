1027. Longest Arithmetic Sequence

Given an array `A` of integers, return the length of the longest arithmetic subsequence in `A`.

Recall that a subsequence of `A` is a list `A[i_1], A[i_2], ..., A[i_k]` with `0 <= i_1 < i_2 < ... < i_k <= A.length - 1`, and that a sequence `B` is arithmetic if `B[i+1] - B[i]` are all the same value (for `0 <= i < B.length - 1`).

 

**Example 1:**

```
Input: [3,6,9,12]
Output: 4
Explanation: 
The whole array is an arithmetic sequence with steps of length = 3.
```

**Example 2:**

```
Input: [9,4,7,2,10]
Output: 3
Explanation: 
The longest arithmetic subsequence is [4,7,10].
```

**Example 3:**

```
Input: [20,1,15,3,10,5,8]
Output: 4
Explanation: 
The longest arithmetic subsequence is [20,15,10,5].
```

**Note:**

1. `2 <= A.length <= 2000`
1. `0 <= A[i] <= 10000`

# Submissions
---
**Solution 1: (DP)**
```
Runtime: 1124 ms
Memory Usage: 312.4 MB
```
```python
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        for i, a2 in enumerate(A[1:], start=1):
            for j, a1 in enumerate(A[:i]):
                d = a2 - a1
                if (j, d) in dp:
                    dp[i, d] = dp[j, d] + 1
                else:
                    dp[i, d] = 2
        return max(dp.values())
```