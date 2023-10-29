2919. Minimum Increment Operations to Make Array Beautiful

You are given a **0-indexed** integer array `nums` having length `n`, and an integer `k`.

You can perform the following increment operation **any** number of times (including zero):

* Choose an index `i` in the range `[0, n - 1]`, and increase `nums[i]` by `1`.

An array is considered **beautiful** if, for any **subarray** with a size of `3` or more, its maximum element is greater than or equal to `k`.

Return an integer denoting the **minimum** number of increment operations needed to make `nums` **beautiful**.

A subarray is a contiguous **non-empty** sequence of elements within an array.

 

**Example 1:**
```
Input: nums = [2,3,0,0,2], k = 4
Output: 3
Explanation: We can perform the following increment operations to make nums beautiful:
Choose index i = 1 and increase nums[1] by 1 -> [2,4,0,0,2].
Choose index i = 4 and increase nums[4] by 1 -> [2,4,0,0,3].
Choose index i = 4 and increase nums[4] by 1 -> [2,4,0,0,4].
The subarrays with a size of 3 or more are: [2,4,0], [4,0,0], [0,0,4], [2,4,0,0], [4,0,0,4], [2,4,0,0,4].
In all the subarrays, the maximum element is equal to k = 4, so nums is now beautiful.
It can be shown that nums cannot be made beautiful with fewer than 3 increment operations.
Hence, the answer is 3.
```

**Example 2:**
```
Input: nums = [0,1,3,3], k = 5
Output: 2
Explanation: We can perform the following increment operations to make nums beautiful:
Choose index i = 2 and increase nums[2] by 1 -> [0,1,4,3].
Choose index i = 2 and increase nums[2] by 1 -> [0,1,5,3].
The subarrays with a size of 3 or more are: [0,1,5], [1,5,3], [0,1,5,3].
In all the subarrays, the maximum element is equal to k = 5, so nums is now beautiful.
It can be shown that nums cannot be made beautiful with fewer than 2 increment operations.
Hence, the answer is 2.
```

**Example 3:**
```
Input: nums = [1,1,2], k = 1
Output: 0
Explanation: The only subarray with a size of 3 or more in this example is [1,1,2].
The maximum element, 2, is already greater than k = 1, so we don't need any increment operation.
Hence, the answer is 0.
```

**Constraints:**

* `3 <= n == nums.length <= 10^5`
* `0 <= nums[i] <= 10^9`
* `0 <= k <= 10^9`

# Submissions
---
**Solution 1: (DP, sliding window)**
```
Runtime: 77 ms
Memory: 80.6 MB
```
```c++
class Solution {
public:
    long long minIncrementOperations(vector<int>& nums, int k) {
        long long dp1 = 0, dp2 = 0, dp3 = 0, dp;
        for (int& a: nums) {
            dp = min(dp1, min(dp2, dp3)) + max(k - a, 0);
            dp1 = dp2;
            dp2 = dp3;
            dp3 = dp;
        }
        return min(dp1, min(dp2, dp3));
    }
};
```

**Solution 2: (DP Top-Down)**
```
Runtime: 107 ms
Memory: 97.3 MB
```
```c++
class Solution {
    int n; 
    vector<long long> dp;
    long long solve(int ind,vector<int>& nums, int k)
    {
        if(ind>n-3)
            return 0;
        if(dp[ind]!=-1)
            return dp[ind];
        //option 1
        long long op1 = max(0,k-nums[ind]) + solve(ind+1,nums,k);
        //option 2
        long long op2 = max(0,k-nums[ind+1]) + solve(ind+2,nums,k);
        //option 3
        long long op3 = max(0,k-nums[ind+2]) + solve(ind+3,nums,k);
        
        return dp[ind] = min(op1,min(op2,op3));
    }
public:
    long long minIncrementOperations(vector<int>& nums, int k) {
        n = nums.size();
        dp.resize(n,-1);
        return solve(0,nums,k);
    }
};
```
