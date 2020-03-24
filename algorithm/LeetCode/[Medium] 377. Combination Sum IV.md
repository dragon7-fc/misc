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