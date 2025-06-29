3599. Partition Array to Minimize XOR

You are given an integer array `nums` and an integer `k`.

Your task is to partition `nums` into `k` non-empty subarrays. For each subarray, compute the bitwise **XOR** of all its elements.

Return the **minimum** possible value of the maximum XOR among these k subarrays.

 

**Example 1:**
```
Input: nums = [1,2,3], k = 2

Output: 1

Explanation:

The optimal partition is [1] and [2, 3].

XOR of the first subarray is 1.
XOR of the second subarray is 2 XOR 3 = 1.
The maximum XOR among the subarrays is 1, which is the minimum possible.
```

**Example 2:**
```
Input: nums = [2,3,3,2], k = 3

Output: 2

Explanation:

The optimal partition is [2], [3, 3], and [2].

XOR of the first subarray is 2.
XOR of the second subarray is 3 XOR 3 = 0.
XOR of the third subarray is 2.
The maximum XOR among the subarrays is 2, which is the minimum possible.
```

**Example 3:**
```
Input: nums = [1,1,2,3,1], k = 2

Output: 0

Explanation:

The optimal partition is [1, 1] and [2, 3, 1].

XOR of the first subarray is 1 XOR 1 = 0.
XOR of the second subarray is 2 XOR 3 XOR 1 = 0.
The maximum XOR among the subarrays is 0, which is the minimum possible.
```
 

**Constraints:**

* `1 <= nums.length <= 250`
* `1 <= nums[i] <= 10^9`
* `1 <= k <= n`

# Submissions
---
**Solution 1: (DP Top-Down, Prefix Sum)**
```
Runtime: 714 ms, Beats 29.26%
Memory: 49.22 MB, Beats 42.24%
```
```c++
class Solution {
    int dfs(int i, int k, vector<vector<int>> &dp, vector<int> &pre) {
        if (k == 1) {
            return pre.back()^pre[i];
        }
        if (dp[i][k] != -1) {
            return dp[i][k];
        }
        int rst = INT_MAX;
        for (int j = i+1; j < dp.size(); j ++) {
            rst = min(rst, max(pre[j]^pre[i], dfs(j, k-1, dp, pre)));
        }
        dp[i][k] = rst;
        return rst;
    }
public:
    int minXor(vector<int>& nums, int k) {
        int n = nums.size(), i;
        vector<int> pre(n+1);
        vector<vector<int>> dp(n, vector<int>(k+1, -1));
        for (i = 0; i < n; i ++) {
            pre[i+1] = pre[i]^nums[i];
        }
        return dfs(0, k, dp, pre);
    }
};
```

**Solution 2: (DP Bottom-Up)**

    nums = [1, 2, 3], k = 2
 -----------------------------
     pre = [0  1  3  0]  
               ^s    ^e
            xx-p1 -p2--
                  ^s ^e
            xx-p1--- p2
dp
           k
       0 1 2
         0
    1    1
    2    3
n   3    0 1
    

```
Runtime: 492 ms, Beats 68.04%
Memory: 49.22 MB, Beats 42.24%
```
```c++
class Solution {
int dp[251][251];
public:
    int minXor(vector<int>& nums, int k, int i = 0) {
        int n = nums.size();

        // Step 1: Prefix XOR
        vector<int> pfix(n + 1, 0);
        for (int i = 1; i <= n; i++) {
            pfix[i] = pfix[i - 1] ^ nums[i - 1];
        }

        // Step 2: Initialize DP
        vector<vector<int>> dp(n + 1, vector<int>(k + 1, INT_MAX));
        for (int i = 0; i <= n; i++) {
            dp[i][1] = pfix[i];  // Base case
        }

        // Step 3: Fill DP table
        for (int parts = 2; parts <= k; parts++) {
            for (int end = parts; end <= n; end++) {
                for (int split = parts - 1; split < end; split++) {
                    int segmentXOR = pfix[end] ^ pfix[split];
                    int maxXOR = max(dp[split][parts - 1], segmentXOR);
                    dp[end][parts] = min(dp[end][parts], maxXOR);
                }
            }
        }

        return dp[n][k];
    }
};
```

**Solution 2: (DP Top-Down, no prefix sum)**
```
Runtime: 187 ms, Beats 99.18%
Memory: 32.25 MB, Beats 99.70%
```
```c++
class Solution {
int dp[251][251];
public:
    int minXor(vector<int>& nums, int k, int i = 0) {
        if (i == 0)
            memset(dp, -1, sizeof(dp));
        if (i == nums.size())
            return 0;
        if (nums.size() - i < k || k <= 0)
           return INT_MAX;            
        if (dp[i][k] < 0) {
            int x = 0, res = INT_MAX;
            for (int j = i; j + k - 1 < nums.size(); ++j) {
                x ^= nums[j];
                if (x < res)
                    res = min(res, max(x, minXor(nums, k - 1, j + 1)));
            }
            dp[i][k] = res;
        }
        return dp[i][k];
    }
};
```
