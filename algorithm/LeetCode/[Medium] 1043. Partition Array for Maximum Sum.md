1043. Partition Array for Maximum Sum

Given an integer array `A`, you partition the array into (contiguous) subarrays of length at most `K`.  After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning.

 

**Example 1:**
```
Input: A = [1,15,7,9,2,5,10], K = 3
Output: 84
Explanation: A becomes [15,15,15,9,10,10,10]
``` 

**Note:**

* `1 <= K <= A.length <= 500`
* `0 <= A[i] <= 10^6`

# Submissions
---
**Solution 1: (DP)**
```
Runtime: 688 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        N = len(A)
        dp = [0] * (N+1)
        for i in range(1, N+1):
            curMax = float('-inf')
            for j in range(K):
                if i - j - 1 >= 0:
                    curMax = max(curMax, A[i - j - 1])
                    dp[i] = max(dp[i], dp[i - j - 1] + (j + 1)*curMax)
        
        return dp[N]
```