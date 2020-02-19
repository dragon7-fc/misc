978. Longest Turbulent Subarray

A subarray `A[i], A[i+1], ..., A[j]` of `A` is said to be turbulent if and only if:

* For `i <= k < j`, `A[k] > A[k+1]` when `k` is odd, and `A[k] < A[k+1]` when `k` is even;
* OR, for `i <= k < j`, `A[k] > A[k+1]` when `k` is even, and `A[k] < A[k+1]` when `k` is odd.

That is, the subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

Return the length of a maximum size turbulent subarray of `A`.

 

**Example 1:**
```
Input: [9,4,2,10,7,8,8,1,9]
Output: 5
Explanation: (A[1] > A[2] < A[3] > A[4] < A[5])
```

**Example 2:**
```
Input: [4,8,12,16]
Output: 2
```

**Example 3:**
```
Input: [100]
Output: 1
```

**Note:**

1. 1 <= `A.length` <= 40000
1. 0 <= `A[i]` <= 10^9

# Solution
---
## Approach 1: Sliding Window
**Intuition**

Evidently, we only care about the comparisons between adjacent elements. If the comparisons are represented by `-1, 0, 1` (for `<, =, >`), then we want the longest sequence of alternating `1, -1, 1, -1, ...` (starting with either `1` or `-1`).

These alternating comparisons form contiguous blocks. We know when the next block ends: when it is the last two elements being compared, or when the sequence isn't alternating.

For example, take an array like `A = [9,4,2,10,7,8,8,1,9]`. The comparisons are `[1,1,-1,1,-1,0,-1,1]`. The blocks are `[1], [1,-1,1,-1], [0], [-1,1]`.

**Algorithm**

Scan the array from left to right. If we are at the end of a block (last elements OR it stopped alternating), then we should record the length of that block as our candidate answer, and set the start of the new block as the next element.

```python
class Solution(object):
    def maxTurbulenceSize(self, A):
        N = len(A)
        ans = 1
        anchor = 0

        for i in xrange(1, N):
            c = cmp(A[i-1], A[i])
            if c == 0:
                anchor = i
            elif i == N-1 or c * cmp(A[i], A[i+1]) != -1:
                ans = max(ans, i - anchor + 1)
                anchor = i
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the length of `A`.

* Space Complexity: $O(1)$.

# Submissions
---
**Solution (Sliding Window)**
```
Runtime: 536 ms
Memory Usage: 18 MB
```
```python
class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        N = len(A)
        ans = 1
        anchor = 0

        for i in range(1, N):
            c = A[i-1] - A[i]
            if not c:
                anchor = i
            elif i == N-1 or not c * (A[i] - A[i+1]) < 0:
                ans = max(ans, i - anchor + 1)
                anchor = i
        return ans
```