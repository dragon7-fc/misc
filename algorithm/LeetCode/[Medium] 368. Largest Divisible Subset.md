368. Largest Divisible Subset

Given a set of **distinct** positive integers, find the largest subset such that every pair $(S_i, S_j)$ of elements in this subset satisfies:

$S_i \% S_j = 0$ or $S_j \% S_i = 0.$

If there are multiple solutions, return any subset is fine.

**Example 1:**

```
Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)
```

**Example 2:**
```
Input: [1,2,4,8]
Output: [1,2,4,8]
```

# Submissions
---
**Solution 1: (DP Bottom-Up)**
```
Runtime: 424 ms
Memory Usage: 14.1 MB
```
```python
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums.sort()
        n = len(nums)
        # (previous divisible index, length of divisible subset)
        dp = [(-1, 1)] * n
        # (last divisible index, maximum length of divisible subsets)
        maxl = (0, 1)
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[i][1] < dp[j][1] + 1:
                        dp[i] = (j, dp[j][1] + 1)
                        if maxl[1] < dp[i][1]:
                            maxl = (i, dp[i][1])
        ret = []
        x = maxl[0]
        while x > -1:
            ret.append(nums[x])
            x = dp[x][0]
        return ret[::-1]
```

**Solution 2: (DP Bottom-Up)**
```
Runtime: 456 ms
Memory Usage: 14.1 MB
```
```python
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        if len(nums) ==0: return []
        result = [nums[0]]
        dp = [[nums[i]] for i in range(len(nums))]
        for i in range(len(dp)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if len(dp[j]) + 1 > len(dp[i]):
                        dp[i] = dp[j] + [nums[i]]
            if len(dp[i]) > len(result):
                result = dp[i]
        return result
```

**Solution 3: (DP Top-Down)**
```
Runtime: 3432 ms
Memory Usage: 101.8 MB
```
```python
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        N = len(nums)
        if N == 0: return []
        nums.sort()
        
        @functools.lru_cache(None)
        def dfs(prevIndex, curPos):
            if curPos == N:
                return []
            taken, not_taken = [], []
            if prevIndex == -1 or nums[curPos] % nums[prevIndex] == 0:
                taken = [nums[curPos]] + dfs(curPos, curPos+1)
            not_taken = dfs(prevIndex, curPos+1)
            if len(taken) > len(not_taken):
                return taken
            else:
                return not_taken
        
        return dfs(-1, 0)
```

**Solution 4: (DP Bottom-Up)**
```
Runtime: 30 ms
Memory: 13.94 MB
```
```c++
class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) {
            return {};
        }
        sort(nums.begin(), nums.end());
        vector<vector<int>> dp(n);
        for (int i = 0; i < n; i ++) {
            dp[i].push_back(nums[i]);
        }
        vector<int> ans = {nums[0]};
        for (int j = 0; j < n; j ++) {
            for (int i = 0; i < j; i ++) {
                if (nums[j]%nums[i] == 0) {
                    if (dp[i].size() + 1 > dp[j].size()) {
                        dp[j] = dp[i];
                        dp[j].push_back(nums[j]);
                    }
                }
            }
            if (dp[j].size() > ans.size()) {
                ans = dp[j];
            }
        }
        return ans;
    }
};
```

**Solution 5: (DP Bottom-Up)**

          nums
          1      2      3
nums dp                              stk
1    0   {1,0}     k                  x
2    1   (1,1)  (2,0)     k           x
3    2k  (1,2)         (3,1)          x
                        mx

         nums
         1     2      4       8
nums dp                              stk
1    0   (1,0)    k                   x 
2    1   (1,1) (2,0)     k            x
4    2   (1,2)        (3,1)      k    x
8    3k  (1,3)                (4,2)   x
                               mx

```
Runtime: 7 ms, Beats 94.70%
Memory: 12.65 MB, Beats 47.06%
```
```c++
class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        int n = nums.size(), i, j, k = 0, mx = 1;
        vector<int> ans;
        vector<pair<int,int>> dp(n);
        stack<int>stk;
        for (i = 0; i < n; i ++) {
            dp[i] = {1, i};
        }
        sort(nums.begin(), nums.end());
        for (j = 1; j < n; j ++) {
            for (i = 0; i < j; i ++) {
                if (nums[j]%nums[i] == 0 && dp[i].first + 1 > dp[j].first) {
                    dp[j] = {dp[i].first + 1, i};
                    if (dp[j].first > mx) {
                        mx = dp[j].first;
                        k = j;
                    }
                }
            }
        }
        while (dp[k].first != 1) {
            stk.push(nums[k]);
            k = dp[k].second;
        }
        stk.push(nums[k]);
        while (stk.size()) {
            ans.push_back(stk.top());
            stk.pop();
        }
        return ans;
    }
};
```
