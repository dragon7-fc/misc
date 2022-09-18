1770. Maximum Score from Performing Multiplication Operations

You are given two integer arrays `nums` and `multipliers` of size `n` and `m` respectively, where `n >= m`. The arrays are **1-indexed**.

You begin with a score of `0`. You want to perform exactly `m` operations. On the `i`th operation (**1-indexed**), you will:

* Choose one integer `x` from either the start or the end of the array `nums`.
* Add `multipliers[i] * x` to your score.
* Remove `x` from the array `nums`.

Return the maximum score after performing `m` operations.

 

**Example 1:**
```
Input: nums = [1,2,3], multipliers = [3,2,1]
Output: 14
Explanation: An optimal solution is as follows:
- Choose from the end, [1,2,3], adding 3 * 3 = 9 to the score.
- Choose from the end, [1,2], adding 2 * 2 = 4 to the score.
- Choose from the end, [1], adding 1 * 1 = 1 to the score.
The total score is 9 + 4 + 1 = 14.
```

**Example 2:**
```
Input: nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]
Output: 102
Explanation: An optimal solution is as follows:
- Choose from the start, [-5,-3,-3,-2,7,1], adding -5 * -10 = 50 to the score.
- Choose from the start, [-3,-3,-2,7,1], adding -3 * -5 = 15 to the score.
- Choose from the start, [-3,-2,7,1], adding -3 * 3 = -9 to the score.
- Choose from the end, [-2,7,1], adding 1 * 4 = 4 to the score.
- Choose from the end, [-2,7], adding 7 * 6 = 42 to the score. 
The total score is 50 + 15 - 9 + 4 + 42 = 102.
```

**Constraints:**

* `n == nums.length`
* `m == multipliers.length`
* `1 <= m <= 103`
* `m <= n <= 105`
* `-1000 <= nums[i], multipliers[i] <= 1000`

# Submissions
---
**Solution 1: (DP Top-Down)**
```
Runtime: 7500 ms
Memory Usage: 43.2 MB
```
```python
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        
        @lru_cache(2000)
        def fn(lo, hi, k):
            """Return max score from nums[lo:hi+1]."""
            if k == len(multipliers): return 0
            return max(nums[lo] * multipliers[k] + fn(lo+1, hi, k+1), nums[hi] * multipliers[k] + fn(lo, hi-1, k+1))
        
        return fn(0, len(nums)-1, 0)
```

**Solution 2: (DP Bottom-Up)**
```
Runtime: 5512 ms
Memory Usage: 41.3 MB
```
```python
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        dp = [[0]*m for _ in range(m+1)]
        
        for i in reversed(range(m)):
            for j in range(i, m): 
                k = i + m - j - 1
                dp[i][j] = max(nums[i] * multipliers[k] + dp[i+1][j], nums[j-m+n] * multipliers[k] + dp[i][j-1])
        
        return dp[0][-1]
```

**Solution 3: (DP Top-Down)**
```
Runtime: 777 ms
Memory Usage: 119.3 MB
```
```
class Solution {
    int m, n;
    int dfs(vector<int>& nums, vector<int>& mult, vector<vector<int>>& dp, int i, int j) {
        // i : pointer at nums
        // j : pointer at mult
        // if we have performed all operations, then return 0
        if (j == m) return 0;
        // memoizated before - return the value here
        if (dp[i][j] != INT_MIN) return dp[i][j];
        // we can either choose an integer in `nums` the start or the end of the array
        // so we try both case and take the maximum value
        // then memoize it
        return dp[i][j] = max(
            // pick from the start
            mult[j] * nums[i] + dfs(nums, mult, dp, i + 1, j + 1),
            // pick fromt the end
            mult[j] * nums[n - 1 - j + i] + dfs(nums, mult, dp, i, j + 1)
        ); 
    }
public:
    int maximumScore(vector<int>& nums, vector<int>& multipliers) {
        n = (int) nums.size(), m = (int) multipliers.size();
		// init values that couldn't be reached. -1 will cause TLE. -2 would pass but it's not supposed to pass.
        vector<vector<int>> dp(m, vector<int>(m, INT_MIN));
        // or u can return dp[0][0] after running dfs
        return dfs(nums, multipliers, dp, 0, 0);
    }
};
```

**Solution 4: (DP Bottom-Up)**
```
Runtime: 389 ms
Memory Usage: 50.6 MB
```
```c++
class Solution {
public:
    int maximumScore(vector<int>& nums, vector<int>& multipliers) {
        int n = (int) nums.size(), m = (int) multipliers.size();
        vector<int> dp(m + 1);
        // let's think backwards
        for (int i = 0; i < m; i++) {
            // at round m, we  pick the m-th multiplier
            // at round m - 1, we pick the (m - 1)-th multiplier
            // at round m - 2, we pick the (m - 2)-th multiplier
            // and so on ... 
            int mult = multipliers[m - 1 - i];
            // how many elements we need to process? 
            // at round m, there are m elements
            // at round m - 1, there are m - 1 elements
            // at round m - 2, there are m - 2 elements
            // and so on ...
            for (int j = 0; j < m - i; j++) {
                // so we take the max of
                dp[j] = max(
                    // the start
                    mult * nums[j] + dp[j + 1], 
                    // the end
                    mult * nums[j + (n - (m - i))] + dp[j]
                );
            }
        }
        return dp[0];
    }
};
```

**Solution 5: (DP Bottom-Up)**
```
Runtime: 365 ms
Memory Usage: 119.8 MB
```
```c++
class Solution {
public:
    int maximumScore(vector<int>& nums, vector<int>& multipliers) {
        // For Right Pointer
        int n = nums.size();
        // Number of Operations
        int m = multipliers.size();
        vector<vector<int>> dp(m+1, vector<int>(m+1));
        
        for (int op = m - 1; op >= 0; op--) {
            for (int left = op; left >= 0; left--) {
                dp[op][left] = max(multipliers[op] * nums[left] + dp[op + 1][left + 1],
                                   multipliers[op] * nums[n - 1 - (op - left)] + dp[op + 1][left]);
            }
        }
        
        return dp[0][0];
    }
};
```
