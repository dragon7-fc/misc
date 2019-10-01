746. Min Cost Climbing Stairs

On a staircase, the `i`-th step has some non-negative cost `cost[i]` assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

**Example 1:**
```
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
```

**Example 2:**
```
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
```

**Note:**
* cost will have a length in the range `[2, 1000]`.
* Every `cost[i]` will be an integer in the range `[0, 999]`.

# Solution
---
## Approach #1: Dynamic Programming [Accepted]
**Intuition**

There is a clear recursion available: the final cost `f[i]` to climb the staircase from some step `i` is `f[i] = cost[i] + min(f[i+1], f[i+2])`. This motivates dynamic programming.

**Algorithm**

Let's evaluate f backwards in order. That way, when we are deciding what `f[i]` will be, we've already figured out `f[i+1]` and `f[i+2]`.

We can do even better than that. At the `i`-th step, let `f1`, `f2` be the old value of `f[i+1]`, `f[i+2]`, and update them to be the new values `f[i]`, `f[i+1]`. We keep these updated as we iterate through `i` backwards. At the end, we want `min(f1, f2)`.

```python
class Solution(object):
    def minCostClimbingStairs(self, cost):
        f1 = f2 = 0
        for x in reversed(cost):
            f1, f2 = x + min(f1, f2), f1
        return min(f1, f2)
```

**Complexity Analysis**

* Time Complexity: $O(N)$ where $N$ is the length of cost.

* Space Complexity: $O(1)$, the space used by `f1`, `f2`.

# Submissions
---
**Solution 1:**
```
Runtime: 60 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        f1 = f2 = 0
        for x in reversed(cost):
            f1, f2 = x + min(f1, f2), f1
        return min(f1, f2)
```

**Solution 2:**
```
Runtime: 28 ms
Memory Usage: N/A
```
```python
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        dp = [0]*n
        
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
            
        return min(dp[n-1], dp[n-2])
        
```