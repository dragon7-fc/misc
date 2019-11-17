1186. Maximum Subarray Sum with One Deletion

Given an array of integers, return the maximum sum for a **non-empty** subarray (contiguous elements) with at most one element deletion. In other words, you want to choose a subarray and optionally delete one element from it so that there is still at least one element left and the sum of the remaining elements is maximum possible.

Note that the subarray needs to be non-empty after deleting one element.

 

**Example 1:**

```
Input: arr = [1,-2,0,3]
Output: 4
Explanation: Because we can choose [1, -2, 0, 3] and drop -2, thus the subarray [1, 0, 3] becomes the maximum value.
```

**Example 2:**

```
Input: arr = [1,-2,-2,3]
Output: 3
Explanation: We just choose [3] and it's the maximum sum.
```

**Example 3:**

```
Input: arr = [-1,-1,-1,-1]
Output: -1
Explanation: The final subarray needs to be non-empty. You can't choose [-1] and delete -1 from it, then get an empty subarray to make the sum equals to 0.
```

**Constraints:**

* `1 <= arr.length <= 10^5`
* `-10^4 <= arr[i] <= 10^4`

# Submissions
---
**Solution 1:**

Define `dp(i, d)` as maximum subarray sum on `arr[:i + 1]` with `d` times deletions.
We'll get this recursion:
* `dp(i, 0) = max(arr[i], dp(i - 1, 0) + arr[i])`
* `dp(i, 1) = max(dp(i - 1, 0), dp(i - 1, 1) + arr[i])`.

```
Runtime: 364 ms
Memory Usage: 32.6 MB
```
```python
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        N = len(arr)
        dp = [[float('-inf')] * 2 for _ in range(N)]
        res = float('-inf')
        for i, a in enumerate(arr):
            dp[i][0] = max(a, dp[i - 1][0] + a)
            dp[i][1] = max(dp[i - 1][0], dp[i - 1][1] + a)
            res = max(res, *dp[i])
        return res
```

**Solution 2:**
```
Runtime: 276 ms
Memory Usage: 22.8 MB
```
```python
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        x = y = res = float('-inf')
        for a in arr:
            x, y = max(a, x + a), max(x, y + a)
            res = max(res, x, y)
        return res
```