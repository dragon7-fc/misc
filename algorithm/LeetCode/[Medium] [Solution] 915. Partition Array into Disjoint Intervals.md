915. Partition Array into Disjoint Intervals

Given an array `A`, partition it into two (contiguous) subarrays `left` and `right` so that:

* Every element in `left` is less than or equal to every element in `right`.
* `left` and `right` are non-empty.
* `left` has the smallest possible size.
Return the length of `left` after such a partitioning.  It is guaranteed that such a partitioning exists.

**Example 1:**
```
Input: [5,0,3,8,6]
Output: 3
Explanation: left = [5,0,3], right = [8,6]
```

**Example 2:**
```
Input: [1,1,1,0,6,12]
Output: 4
Explanation: left = [1,1,1,0], right = [6,12]
``` 

**Note:**

1. `2 <= A.length <= 30000`
1. `0 <= A[i] <= 10^6`
1. It is guaranteed there is at least one way to partition `A` as described.

# Solution
---
## Approach 1: Next Array
**Intuition**

Instead of checking whether `all(L <= R for L in left for R in right)`, let's check whether `max(left) <= min(right)`.

Algorithm

Let's try to find `max(left)` for subarrays `left = A[:1]`, `left = A[:2]`, `left = A[:3]`, ... etc. Specifically, `maxleft[i]` will be the maximum of subarray `A[:i]`. They are related to each other: `max(A[:4]) = max(max(A[:3]), A[3])`, so `maxleft[4] = max(maxleft[3], A[3])`.

Similarly, `min(right)` for every possible `right` can be found in linear time.

After we have a way to query `max(left)` and `min(right)` quickly, the solution is straightforward.

# Submissions
---
**Solution**
```
Runtime: 272 ms
Memory Usage: 17.9 MB
```
```python
class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        N = len(A)
        maxleft = [None] * N
        minright = [None] * N

        m = A[0]
        for i in range(N):
            m = max(m, A[i])
            maxleft[i] = m

        m = A[-1]
        for i in range(N-1, -1, -1):
            m = min(m, A[i])
            minright[i] = m

        for i in range(1, N):
            if maxleft[i-1] <= minright[i]:
                return i
```