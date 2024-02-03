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
**Solution 1: (DP Bottom-Up)**
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

**Solution 2: (DP Bottom-Up)**
```
Runtime: 7 ms
Memory: 10.95 MB
```
```c++
class Solution {
public:
    int maxSumAfterPartitioning(vector<int>& arr, int k) {
        int n = arr.size(), cur, ans = 0;
        vector<int> dp(n+1);
        for (int j = 0; j < n; j ++) {
            cur = 0;
            for (int i = j; i >= j-k+1 && i >= 0; i --) {
                cur = max(cur, arr[i]);
                dp[j+1] = max(dp[j+1], cur*(j-i+1) + dp[i]);
            }
        }
        return dp[n];
    }
};
```
