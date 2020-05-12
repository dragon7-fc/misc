396. Rotate Function

Given an array of integers `A` and let n to be its length.

Assume $B_k$ to be an array obtained by rotating the array $A_k$ positions clock-wise, we define a "rotation function" `F` on `A` as follow:

$F(k) = 0 * B_k[0] + 1 * B_k[1] + ... + (n-1) * B_k[n-1]$.

Calculate the maximum value of `F(0), F(1), ..., F(n-1)`.

**Note:**

* `n` is guaranteed to be less than `10^5`.

**Example:**
```
A = [4, 3, 2, 6]

F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26

So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.
```

# Submisssions
---
**Solution 1: (Math)**
```
Runtime: 80 ms
Memory Usage: 14.5 MB
```
```python
class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        t = sum(A)
        N = len(A)
        largest = f = sum([i*d for i,d in enumerate(A)])
        for index in range(N-1, 0, -1):
            f = f + t - N*A[index]
            largest = max(largest, f)
        return largest
```