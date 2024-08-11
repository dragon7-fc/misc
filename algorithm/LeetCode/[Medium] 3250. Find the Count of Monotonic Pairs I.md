3250. Find the Count of Monotonic Pairs I

You are given an array of **positive** integers `nums` of length `n`.

We call a pair of **non-negative** integer arrays `(arr1, arr2)` **monotonic** if:

* The lengths of both arrays are `n`.
* `arr1` is monotonically **non-decreasing**, in other words, `arr1[0] <= arr1[1] <= ... <= arr1[n - 1]`.
* `arr2` is monotonically **non-increasing**, in other words, `arr2[0] >= arr2[1] >= ... >= arr2[n - 1]`.
* `arr1[i] + arr2[i] == nums[i] for all 0 <= i <= n - 1`.

Return the count of **monotonic** pairs.

Since the answer may be very large, return it **modulo** `10^9 + 7`.

 

**Example 1:**
```
Input: nums = [2,3,2]

Output: 4

Explanation:

The good pairs are:

([0, 1, 1], [2, 2, 1])
([0, 1, 2], [2, 2, 0])
([0, 2, 2], [2, 1, 0])
([1, 2, 2], [1, 1, 0])
```

**Example 2:**
```
Input: nums = [5,5,5,5]

Output: 126
```
 

**Constraints:**

* `1 <= n == nums.length <= 2000`
* `1 <= nums[i] <= 50`

# Submissions
---
**Solution 1: (DP Top-Down)**
```
Runtime: 973 ms
Memory: 55.20 MB
```
```c++
class Solution {
    int MOD = 1e9+7;
    int dp[2001][52][52];
    int solve(int i, int n, vector<int>&nums, int prev1,int prev2) {
        if (i == n)
            return 1;
        if (dp[i][prev1][prev2] != -1)
            return dp[i][prev1][prev2];
        int rst = 0;
        for (int j = prev1; j <= nums[i]; j++) {
            int x1 = j;
            int x2 = nums[i]-j;
            if (x1 >= prev1 && x2 <= prev2) {
                rst = (rst + solve(i+1, n, nums, x1, x2))%MOD;
            } 
        }
        return dp[i][prev1][prev2] = rst;
    }
public:
    int countOfPairs(vector<int>& nums) {
        int n = nums.size();
        memset(dp,-1,sizeof(dp));
        int ans = solve(0, n, nums, 0, 50);
        return ans;
    }
};
```

**Solution 2: (DP Top-Down)**
```
Runtime: 210 ms
Memory: 378.00 MB
```
```c++
class Solution {
    const int mod = 1e9 + 7;
    int f(int i, int prev, vector<int> &nums, vector<vector<int>> &dp){
        if (i >= nums.size())
            return 1;
        if (dp[i][prev] != -1)
            return dp[i][prev];
        int c = 0;
        for (int val = prev; val <= nums[i]; val++){
            int k = nums[i] - val;
            if (i == 0 || k <= nums[i -1] - prev){
                c = (c + f(i + 1, val, nums,dp)) % mod;
            }
        }
        return dp[i][prev] = c;
    }
public:
    int countOfPairs(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> dp(n, vector<int>(1001, - 1));
        return f(0, 0, nums, dp);
    }
};
```

**Solution 3: (DP Bottom-Up)**
```
Runtime: 185 ms
Memory: 39.97 MB
```
```c++
class Solution {
    const int mod = 1e9 + 7;
public:
    int countOfPairs(vector<int>& nums) {
        int n = nums.size();
        long long cnt = 0;
        int dp[n][1001];
        memset(dp, 0, sizeof(dp));
        for(int i = 0; i<= nums[0]; i++){
            dp[0][i] = 1;
        }
        for (int i = 1; i < n; i++){
            for (int prev = 0; prev <= nums[i-1]; prev++){
                for (int k = prev; k <= nums[i]; k++){
                    int val = nums[i] - k;
                    if (val <= nums[i-1] - prev)
                        dp[i][k] = (dp[i][k] + dp[i-1][prev]) % mod;
                }
            }
        }
        for (int i = 0; i <= nums[n-1]; i++){
            cnt = (cnt + dp[n-1][i]) % mod;
        }
        return cnt;
    }
};
```
