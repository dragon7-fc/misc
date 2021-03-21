1802. Maximum Value at a Given Index in a Bounded Array

You are given three positive integers `n`, `index` and `maxSum`. You want to construct an array `nums` (**0-indexed**) that satisfies the following conditions:

* `nums.length == n`
* `nums[i]` is a positive integer where `0 <= i < n`.
* `abs(nums[i] - nums[i+1]) <= 1` where `0 <= i < n-1`.
* The sum of all the elements of `nums` does not exceed `maxSum`.
* `nums[index]` is maximized.

Return `nums[index]` of the constructed array.

Note that `abs(x)` equals `x` if `x >= 0`, and `-x` otherwise.

 

**Example 1:**
```
Input: n = 4, index = 2,  maxSum = 6
Output: 2
Explanation: The arrays [1,1,2,1] and [1,2,2,1] satisfy all the conditions. There are no other valid arrays with a larger value at the given index.
```

**Example 2:**
```
Input: n = 6, index = 1,  maxSum = 10
Output: 3
```

**Constraints:**

* `1 <= n <= maxSum <= 109`
* `0 <= index < n`

# Submissions
---
**Solution 1: (Binary Search)**

**Explanation**

We first do maxSum -= n,
then all elements needs only to valid A[i] >= 0

We binary search the final result between left and right,
where left = 0 and right = maxSum.

For each test, we check minimum sum if A[index] = a.
The minimum case would be A[index] is a peak in A.
It's arithmetic sequence on the left of A[index] with difference is 1.
It's also arithmetic sequence on the right of A[index] with difference is -1.

On the left, A[0] = max(a - index, 0),
On the right, A[n - 1] = max(a - ((n - 1) - index), 0),

The sum of arithmetic sequence {b, b+1, ....a},
equals to (a + b) * (a - b + 1) / 2.

```
Runtime: 36 ms
Memory Usage: 14.2 MB
```
```python
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def test(a):
            b = max(a - index, 0)
            res = (a + b) * (a - b + 1) / 2
            b = max(a - ((n - 1) - index), 0)
            res += (a + b) * (a - b + 1) / 2
            return res - a

        maxSum -= n
        left, right = 0, maxSum
        while left < right:
            mid = (left + right + 1) // 2
            if test(mid) <= maxSum:
                left = mid
            else:
                right = mid - 1
        return left + 1
```