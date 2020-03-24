410. Split Array Largest Sum

Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

**Note:**

If n is the length of array, assume the following constraints are satisfied:
* 1 ≤ n ≤ 1000
* 1 ≤ m ≤ min(50, n)

**Examples:**
```
Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
```

# Submissions
---
**Solution 1: (DP Top-Down)**
```
Runtime: 4920 ms
Memory Usage: 18.1 MB
```
```python
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        prefixSum = [0]
        for a in nums:
            prefixSum.append(a + prefixSum[-1])

        @lru_cache(None)
        def dp(i, j):
            # i is number of elements from A
            # j is number of splits
            if j == 1: return prefixSum[i]
            res = float('inf')
            for k in range(j - 1, i):
                res = min(res, max(dp(k, j - 1),
                                   prefixSum[i] - prefixSum[k]))
            return res

        return dp(len(nums), m)
```

**Solution 2: (Binary Search)**
```
Runtime: 44 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        class Lazy:
            def __getitem__(self, sm):
                splits = 1
                cur = 0
                for a in nums:
                    if a > sm: return False
                    if cur + a > sm:
                        splits += 1
                        cur = 0
                    cur += a
                return splits <= m
        return bisect_left(Lazy(), True, 0, int(1e18))
```