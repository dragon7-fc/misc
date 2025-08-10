377. Combination Sum IV

Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

**Example:**
```
nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
 ```

**Follow up:**

* What if negative numbers are allowed in the given array?
* How does it change the problem?
* What limitation we need to add to the question to allow negative numbers?

**Credits:**
Special thanks to @pbrother for adding this problem and creating all test cases.

# Submissions
---
**Solution 1: (DP Bottom-Up)**
```
Runtime: 56 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for _ in range(target+1)]
        dp[0] = 1
        for i in range(1, target+1):
            dp[i] = sum([dp[i-num] for num in nums if i-num >= 0])
        return dp[target]
```

**Solution 2: (DP Top-Down)**
```
Runtime: 44 ms
Memory Usage: 17.8 MB
```
```python
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        @functools.lru_cache(None)
        def dfs(s):
            if s == 0:
                return 1
            elif s < 0:
                return 0
            rst = 0
            for num in nums:
                rst += dfs(s - num)
            return rst
            
        return dfs(target)
```

**Solution 3: (DP Top-Down)**
```
Runtime: 0 ms
Memory Usage: 6.8 MB
```
```c++
class Solution {
    vector<int> dp;
    int help(vector<int> &nums, int T, int n){
		// base case: if target is 0, we found combination then return 1
        if(T==0) return 1;
        int ans=0; 
		
		// memoisation
        if(dp[T]!=-1) return dp[T];
		
		// picking up each elements less than target and 
		// calling this function recursively
        for(int i=0; i<n; i++){
            if(nums[i]<=T){
                ans+=help(nums, T-nums[i], n);
            }
        }
        return dp[T]= ans;
    }
public:
    int combinationSum4(vector<int>& nums, int target) {
        int n=nums.size();
		// resizing the dp array to store values from 0 to target
        dp.resize(target+1,-1);
        return help(nums, target, n);
    }
};
```

**Solution 4: (DP Bottom-Up)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 9.14 MB, Beats 68.42%
```
```c++
class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        int n = nums.size(), i, a;
        vector<unsigned int> dp(target + 1);
        dp[0] = 1;
        for (a = 1; a <= target; a ++) {
            for (i = 0; i < n; i ++) {
                if (a - nums[i] >= 0) {
                    dp[a] += dp[a - nums[i]];
                }
            }
        }
        return dp[target];
    }
};
```
