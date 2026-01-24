213. House Robber II

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are **arranged in a circle**. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight **without alerting the police**.

**Example 1:**
```
Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
```

**Example 2:**
```
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
```

# Submissions
---
**Solution 1: (DP Bottom-Up)**
```
Runtime: 32 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob(nums):
            N = len(nums)
            rob = [0]*(N+1)
            rob[0] = 0
            rob[1] = nums[0]
            for i in range(2, N+1):
                rob[i] = max(rob[i-1], nums[i-1]+rob[i-2])
            return rob[N]
        
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums)==2:
            return max(nums)
        return max([rob(nums[:-1]), rob(nums[1:])])
```

**Solution 2: (DP Bottom-Up)**
```
Runtime: 28 ms
Memory Usage: 14.1 MB
```
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1: return nums[0]
        dp, dp2 = [0]*N, [0]*N
        dp[1] = nums[0]
        for i in range(1, N-1):
            dp[i+1] = max(dp[i], dp[i-1] + nums[i])
        dp2[1] = nums[1]
        for i in range(2, N):
            dp2[i] = max(dp2[i-1], dp2[i-2] + nums[i])
        
        return max(dp[-1], dp2[-1])
```

**Solution 3: (DP Top-Down)**
```
Runtime: 24 ms
Memory Usage: 13.1 MB
```
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 0:
            return 0
        elif N == 1:
            return nums[0]
        elif N == 2:
            return max(nums)
        
        @functools.lru_cache(None)
        def dfs(i, j):
            if i >= j:
                return 0
            return max(nums[i] + dfs(i+2, j), dfs(i+1, j))
        
        #rob the first house, can't rob the last house
        return max(dfs(0, N-1), dfs(1, N))
```

**Solution 4: (DP Bottom-Up, 2 step, split to 2 sub problem)**

             0  1  2  3
    nums = [ 1, 2, 3, 1]
dpx:        [1  2  4]     
                   ^---------|
------------------------    max = 4
dp0:           [2  3  3]     |
                      ^------|
```
Runtime: 0 ms, Beats 100.00%
Memory: 10.92 MB, Beats 20.68%
```
```c++
class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size(), i, j, ans;
        if (n == 1) {
            return nums[0];
        }
        ans = max(nums[0], nums[1]);
        if (n == 2) {
            return ans;
        }
        vector<int> dp(n);
        dp[0] = nums[0];
        dp[1] = ans;
        for (i = 2; i < n-1; i ++) {
            dp[i] = max(dp[i-1], nums[i] + dp[i-2]);
        }
        ans = dp[n-2];
        dp[0] = 0;
        dp[1] = nums[1];
        for (i = 2; i < n; i ++) {
            dp[i] = max(dp[i-1], nums[i] + dp[i-2]);
        }
        ans = max(ans, dp[n-1]);
        return ans;
    }
};
```
