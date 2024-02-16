3040. Maximum Number of Operations With the Same Score II

Given an array of integers called `nums`, you can perform any of the following operation while `nums` contains **at least** `2` elements:

* Choose the first two elements of `nums` and delete them.
* Choose the last two elements of `nums` and delete them.
* Choose the first and the last elements of `nums` and delete them.

The **score** of the operation is the sum of the deleted elements.

Your task is to find the **maximum** number of operations that can be performed, such that **all operations have the same score**.

Return the **maximum** number of operations possible that satisfy the condition mentioned above.

 

**Example 1:**
```
Input: nums = [3,2,1,2,3,4]
Output: 3
Explanation: We perform the following operations:
- Delete the first two elements, with score 3 + 2 = 5, nums = [1,2,3,4].
- Delete the first and the last elements, with score 1 + 4 = 5, nums = [2,3].
- Delete the first and the last elements, with score 2 + 3 = 5, nums = [].
We are unable to perform any more operations as nums is empty.
```

**Example 2:**
```
Input: nums = [3,2,6,1,4]
Output: 2
Explanation: We perform the following operations:
- Delete the first two elements, with score 3 + 2 = 5, nums = [6,1,4].
- Delete the last two elements, with score 1 + 4 = 5, nums = [6].
It can be proven that we can perform at most 2 operations.
```

**Constraints:**

* `2 <= nums.length <= 2000`
* `1 <= nums[i] <= 1000`

# Submissions
---
**Solution 1: (DP Top-Down)**
```
Runtime: 116 ms
Memory: 147.30 MB
```
```c++
class Solution {
    int dfs(int i, int j, int num, vector<vector<int>> &dp, vector<int>& nums) {
        if (j >= nums.size() || j-i < 1) {
            return 0;
        }
        if (dp[i][j] != 0) {
            return dp[i][j];
        }
        if (nums[i] + nums[i+1] == num) {
            dp[i][j] = max(dp[i][j], 1 + dfs(i+2, j, num, dp, nums));
        }
        if (nums[j-1] + nums[j] == num) {
            dp[i][j] = max(dp[i][j], 1 + dfs(i, j-2, num, dp, nums));
        }
        if (nums[i] + nums[j] == num) {
            dp[i][j] = max(dp[i][j], 1 + dfs(i+1, j-1, num, dp, nums));
        }
        return dp[i][j];
    }
public:
    int maxOperations(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> dp(n, vector<int>(n));
        return 1 + max({dfs(2, n-1, nums[0] + nums[1], dp, nums),
                        dfs(0, n-3, nums[n-2] + nums[n-1], dp, nums),
                        dfs(1, n-2, nums[0] + nums[n-1], dp, nums)
                        });
    }
};
```

**Solution 2: (DP Bottom-Up)**
```
Runtime: 334 ms
Memory: 391.63 MB
```
```c++
class Solution {
    int findWays(vector<int>& nums,int sum){
        int n=  nums.size();
        vector<vector<int>>dp(n,vector<int>(n,0));
        if(n<2)return 0;
        for(int i=0;i<n-1;i++){
            if(nums[i]+nums[i+1]==sum) {
                dp[i][i+1]=1;
            }
        }
        for(int i= n-2;i>=0;i--){
            for(int j=i+2;j<n;j++){
                if(nums[i]+nums[j]==sum){
                    dp[i][j]=max(dp[i][j], (1+dp[i+1][j-1]));
                }
                if(nums[i]+nums[i+1]==sum){
                    dp[i][j]= max(dp[i][j],(1+dp[i+2][j]));
                }
                if(nums[j]+nums[j-1]==sum){
                     dp[i][j]=max(dp[i][j],(1+dp[i][j-2]));
                }
            }
        }
        return dp[0][n-1]; 
    }
public:
    int maxOperations(vector<int>& nums) {
        int n= nums.size();
        vector<int>v;
        for(int i=2;i<n;i++){
            v.push_back(nums[i]);
        }
        int a = findWays(v,nums[0]+nums[1])+1;
        v.clear();
        for(int i=1;i<n-1;i++){
            v.push_back(nums[i]);
        }
        int b= findWays(v,nums[0]+nums[n-1])+1;
         v.clear();
        for(int i=0;i<n-2;i++){
            v.push_back(nums[i]);
        }
        int c= findWays(v,nums[n-2]+nums[n-1])+1;
        return max(a,max(b,c));
    }
};
```
