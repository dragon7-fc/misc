198. House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight **without alerting the police**.

**Example 1:**
```
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
```

**Example 2:**
```
Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
```

# Submissions
---
**Solution 1: (DP Bottom-Up)**
```
Runtime: 36 ms
Memory Usage: N/A
```
```python
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        n = len(nums)
        rob = [0]*(n+1)
        rob[0] = 0
        rob[1] = nums[0]
        for i in range(2, n+1):
            rob[i] = max(rob[i-1], nums[i-1]+rob[i-2])
        return rob[n]
```

**Solution 2: (DP Top-Down)**
```
Runtime: 32 ms
Memory Usage: 13.1 MB
```
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        
        @functools.lru_cache(None)
        def dp(i):
            if i >= N:
                return 0
            return max(nums[i] + dp(i+2), dp(i+1))
        
        return dfs(0)
```

**Solution 3: (DP Bottom-Up)**
```
Runtime: 0 ms
Memory Usage: 6.1 MB
```
```c
#define max(_a, _b) ((_a) > (_b) ? (_a) : (_b))
int rob(int* nums, int numsSize){
    if (numsSize == 1) {
        return nums[0];
    } else if (numsSize == 2) {
        return max(nums[0], nums[1]);
    }
    int dp0 = nums[0];
    int dp1 = max(nums[0], nums[1]);
    int dp2;
    for (int i = 2; i < numsSize; i ++) {
        dp2 = max(dp0 + nums[i], dp1);
        dp0 = dp1;
        dp1 = dp2;
    }
    return dp2;
}
```

**Solution 4: (DP Bottom-Up)**
```
Runtime: 29 ms
Memory: 13.9 MB
```
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 1:
            return nums[0]
        two = 0
        one = nums[0]
        for i in range(1, N):
            cur = max(nums[i] + two, one)
            two = one
            one = cur
        return cur
```

**Solution 5: (DP Bottom-Up)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 10.13 MB, Beats 80.12%
```
```c++
class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size(), i, a, b, c;
        if (n <= 2) {
            return *max_element(nums.begin(), nums.end());
        }
        a = nums[0], b = max(nums[0], nums[1]);
        for (i = 2; i < n; i ++) {
            c = max(b, a + nums[i]);
            a = b;
            b = c;
        }
        return c;
    }
};
```
