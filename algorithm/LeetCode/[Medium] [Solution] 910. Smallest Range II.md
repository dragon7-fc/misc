910. Smallest Range II

Given an array `A` of integers, for each integer `A[i]` we need to choose either `x = -K` or `x = K`, and add `x` to `A[i]` (only once).

After this process, we have some array `B`.

Return the smallest possible difference between the maximum value of `B` and the minimum value of `B`.

 

**Example 1:**
```
Input: A = [1], K = 0
Output: 0
Explanation: B = [1]
```

**Example 2:**
```
Input: A = [0,10], K = 2
Output: 6
Explanation: B = [2,8]
```

**Example 3:**
```
Input: A = [1,3,6], K = 3
Output: 3
Explanation: B = [4,6,3]
```

**Note:**

1. `1 <= A.length <= 10000`
1. `0 <= A[i] <= 10000`
1. `0 <= K <= 10000`

# Solution
---
## Approach 1: Linear Scan
**Intuition**

As in Smallest Range I, smaller `A[i]` will choose to increase their value ("go up"), and bigger `A[i]` will decrease their value ("go down").

**Algorithm**

We can formalize the above concept: if `A[i] < A[j]`, we don't need to consider when `A[i]` goes down while `A[j]` goes up. This is because the interval `(A[i] + K, A[j] - K)` is a subset of `(A[i] - K, A[j] + K)` (here, `(a, b)` for `a > b` denotes `(b, a)` instead.)

That means that it is never worse to choose (up, down) instead of (down, up). We can prove this claim that one interval is a subset of another, by showing both `A[i] + K` and `A[j] - K` are between `A[i] - K` and `A[j] + K`.

For sorted `A`, say `A[i]` is the largest `i` that goes up. Then `A[0] + K, A[i] + K, A[i+1] - K, A[A.length - 1] - K` are the only relevant values for calculating the answer: every other value is between one of these extremal values.

```python
class Solution(object):
    def smallestRangeII(self, A, K):
        A.sort()
        mi, ma = A[0], A[-1]
        ans = ma - mi
        for i in xrange(len(A) - 1):
            a, b = A[i], A[i+1]
            ans = min(ans, max(ma-K, a+K) - min(mi+K, b-K))
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N \log N)$, where $N$ is the length of the `A`.

* Space Complexity: $O(1)$, plus the space used by the builtin sorting algorithm.

# Submissions
---
**Solution:**
```
Runtime: 168 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        mi, ma = A[0], A[-1]
        ans = ma - mi
        for i in range(len(A) - 1):
            a, b = A[i], A[i+1]
            ans = min(ans, max(ma-K, a+K) - min(mi+K, b-K))
        return ans
```