689. Maximum Sum of 3 Non-Overlapping Subarrays

In a given array `nums` of positive integers, find three non-overlapping subarrays with maximum sum.

Each subarray will be of size `k`, and we want to maximize the sum of all `3*k` entries.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

**Example:**
```
Input: [1,2,1,2,6,7,5,1], 2
Output: [0, 3, 5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
```

**Note:**

* `nums.length` will be between `1` and `20000`.
* `nums[i]` will be between `1` and `65535`.
* `k` will be between `1` and `floor(nums.length / 3)`.

# Solution
---
## Approach #1: Ad-Hoc [Accepted]
**Intuition**

It is natural to consider an array `W` of each interval's sum, where each interval is the given length `K`. To create `W`, we can either use prefix sums, or manage the sum of the interval as a window slides along the array.

From there, we approach the reduced problem: Given some array `W` and an integer `K`, what is the lexicographically smallest tuple of indices `(i, j, k)` with `i + K <= j` and `j + K <= k` that maximizes `W[i] + W[j] + W[k]`?

**Algorithm**

Suppose we fixed `j`. We would like to know on the intervals $i \in [0, j-K]$ and $k \in [j+K, \text{len}(W)-1]$, where the largest value of $W[i]$ (and respectively $W[k]$) occurs first. (Here, first means the smaller index.)

We can solve these problems with dynamic programming. For example, if we know that $i$ is where the largest value of $W[i]$ occurs first on $[0, 5]$, then on $[0, 6]$ the first occurrence of the largest $W[i]$ must be either $i$ or $6$. If say, $6$ is better, then we set `best = 6`.

At the end, `left[z]` will be the first occurrence of the largest value of `W[i]` on the interval $i \in [0, z]$, and `right[z]` will be the same but on the interval $i \in [z, \text{len}(W) - 1]$. This means that for some choice `j`, the candidate answer must be `(left[j-K], j, right[j+K]).` We take the candidate that produces the maximum `W[i] + W[j] + W[k]`.

```python
class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, K):
        W = [] #array of sums of windows
        sum_ = 0
        for i, x in enumerate(nums):
            sum_ += x
            if i >= K: sum_ -= nums[i-K]
            if i >= K-1: W.append(sum_)

        left = [0] * len(W)
        best = 0
        for i in range(len(W)):
            if W[i] > W[best]:
                best = i
            left[i] = best

        right = [0] * len(W)
        best = len(W) - 1
        for i in range(len(W) - 1, -1, -1):
            if W[i] >= W[best]:
                best = i
            right[i] = best

        ans = None
        for j in xrange(K, len(W) - K):
            i, k = left[j-K], right[j+K]
            if ans is None or (W[i] + W[j] + W[k] >
                    W[ans[0]] + W[ans[1]] + W[ans[2]]):
                ans = i, j, k
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the length of the array. Every loop is bounded in the number of steps by $N$, and does $O(1)$ work.

* Space complexity: $O(N)$. W, left, and right all take $O(N)$ memory.

# Submissions
---
**Solution 1: (Ad-Hoc, Prefix Sum, DP)**
```
Runtime: 212 ms
Memory Usage: 15.3 MB
```
```python
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], K: int) -> List[int]:
        W = [] #array of sums of windows
        sum_ = 0
        for i, x in enumerate(nums):
            sum_ += x
            if i >= K: sum_ -= nums[i-K]
            if i >= K-1: W.append(sum_)

        left = [0] * len(W)
        best = 0
        for i in range(len(W)):
            if W[i] > W[best]:
                best = i
            left[i] = best

        right = [0] * len(W)
        best = len(W) - 1
        for i in range(len(W) - 1, -1, -1):
            if W[i] >= W[best]:
                best = i
            right[i] = best

        ans = None
        for j in range(K, len(W) - K):
            i, k = left[j-K], right[j+K]
            if ans is None or (W[i] + W[j] + W[k] >
                    W[ans[0]] + W[ans[1]] + W[ans[2]]):
                ans = i, j, k
        return ans
```