3473. Sum of K Subarrays With Length at Least M

You are given an integer array `nums` and two integers, `k` and `m`.

Return the maximum sum of `k` non-overlapping subarrays of `nums`, where each subarray has a length of **at least** `m`.

 

**Example 1:**
```
Input: nums = [1,2,-1,3,3,4], k = 2, m = 2

Output: 13

Explanation:

The optimal choice is:

Subarray nums[3..5] with sum 3 + 3 + 4 = 10 (length is 3 >= m).
Subarray nums[0..1] with sum 1 + 2 = 3 (length is 2 >= m).
The total sum is 10 + 3 = 13.
```

**Example 2:**
```
Input: nums = [-10,3,-1,-2], k = 4, m = 1

Output: -10

Explanation:

The optimal choice is choosing each element as a subarray. The output is (-10) + 3 + (-1) + (-2) = -10.
```
 

**Constraints:**

* `1 <= nums.length <= 2000`
* `-104 <= nums[i] <= 10^4`
* `1 <= k <= floor(nums.length / m)`
* `1 <= m <= 3`

# Submissions
---
**Solution 1: (Prefix Sum, DP Bottom-Up)** 

    nums = [1, 2,-1, 3, 3, 4],   k = 2, m = 2
            ^^^^     ^^^^^^^
-----------------------------------------
prefix   = [0, 1, 3, 2, 5, 8,12]
                               

dp[i][j]: maximum sum achievable using i subarrays from the first j elements of the array.
dp[i+1][j] = max(
    dp[i+1][j]
    dp[i+1][j-1]
    dp[i][j-m] + (prefix[j] - prefix[j-m]) = prefix[j] + (dp[i][j-m] - prefix[j-m])
                                                         ^^^^^^^^^^^^^^^^^^^^^^^^^^
                                                                   best
)

dp
           [1, 2,-1, 3, 3, 4]
            0  1  2  3  4  5  6
           ---------------------
        0 | 0  0  0  0  0  0  0
        1 | ~  ~  3  3  5  8 12
best  ~           0  0  0  0  0
        2 | ~  ~  ~  ~  5  9 13
best  ~     ~  ~  ~  ~  0  1  1

```
Runtime: 223 ms, Beats 100.00%
Memory: 130.34 MB, Beats 100.00%
```
```c++
class Solution {
public:
    int maxSum(vector<int>& nums, int k, int m) {
        int n = nums.size();
        vector<int> prefix(n + 1, 0);

        partial_sum(nums.begin(),nums.end(),prefix.begin()+1);
        
        vector<vector<int>> dp(k + 1, vector<int>(n + 1, -1e9));
        
        for (int j = 0; j <= n; j++) {
            dp[0][j] = 0;
        }
        
        for (int i = 0; i < k; i++) {
            int best = -1e9;
            for (int j = 0; j <= n; j++) {
                if (j > 0)
                    dp[i + 1][j] = max(dp[i + 1][j], dp[i + 1][j - 1]);
                
                if (j - m >= 0)
                    best = max(best, dp[i][j - m] - prefix[j - m]);
                
                if (best != -1e9)
                    dp[i + 1][j] = max(dp[i + 1][j], prefix[j] + best);
            }
        }
        
        return dp[k][n];
    }
};
```
