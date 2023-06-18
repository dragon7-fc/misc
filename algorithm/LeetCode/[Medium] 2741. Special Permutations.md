2741. Special Permutations

You are given a **0-indexed** integer array `nums` containing `n` **distinct** positive integers. A permutation of nums is called special if:

For all indexes `0 <= i < n - 1`, either `nums[i] % nums[i+1] == 0` or `nums[i+1] % nums[i] == 0`.

Return the total number of special permutations. As the answer could be large, return it **modulo** `10^9 + 7`.

 

**Example 1:**
```
Input: nums = [2,3,6]
Output: 2
Explanation: [3,6,2] and [2,6,3] are the two special permutations of nums.
```

**Example 2:**
```
Input: nums = [1,4,3]
Output: 2
Explanation: [3,1,4] and [4,1,3] are the two special permutations of nums.
```

**Constraints:**

* `2 <= nums.length <= 14`
* `1 <= nums[i] <= 10^9`

# Submissions
---
**Solution 1: (Bitmask DP)**
```
Runtime: 4471 ms
Memory: 219.5 MB
```
```python
class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        N = len(nums)
        MOD = 10**9 + 7
        
        @functools.lru_cache(None)
        def bt(i, cur):
            if cur == ((1<<N) - 1):
                return 1
            rst = 0
            for j in range(N):
                if cur & (1<<j) == 0:
                    if nums[i]%nums[j] == 0 or nums[j]%nums[i] == 0:
                        rst += bt(j, cur + (1<<j))
                        rst %= MOD
            return rst
            
        ans = 0
        for i in range(N):
            ans += bt(i, 1<<i)
            ans %= MOD
        return ans
```

**Solution 2: (Bitmask DP)**
```
Runtime: 303 ms
Memory: 18.9 MB
```
```c++
class Solution {
    int dp[14][16383];
    int dfs(int i, int mask, vector<int>& nums) {
        if (mask == (1 << nums.size()) - 1)
            return 1;
        if (dp[i][mask] == -1) {
            dp[i][mask] = 0;
            for (int j = 0; j < nums.size(); ++j) {
                if ((mask & (1 << j)) == 0 && (mask == 0 || nums[i] % nums[j] == 0 || nums[j] % nums[i] == 0)) {
                    dp[i][mask] = (dp[i][mask] + dfs(j, mask + (1 << j), nums)) % 1000000007;
                }
            }
        }
        return dp[i][mask];
    }
public:
    int specialPerm(vector<int>& nums) {
        memset(dp, -1, sizeof(dp));
        return dfs(0, 0, nums);
    }
};
```
