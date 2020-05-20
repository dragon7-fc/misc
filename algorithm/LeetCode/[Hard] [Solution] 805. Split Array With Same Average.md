805. Split Array With Same Average

In a given integer array A, we must move every element of A to either list B or list C. (B and C initially start empty.)

Return true if and only if after such a move, it is possible that the average value of B is equal to the average value of C, and B and C are both non-empty.

**Example :**
```
Input: 
[1,2,3,4,5,6,7,8]
Output: true
Explanation: We can split the array into [1,4,5,8] and [2,3,6,7], and both of them have the average of 4.5.
```

**Note:**

* The length of `A` will be in the range `[1, 30]`.
* `A[i]` will be in the range of `[0, 10000]`.

# Solution
---
## Approach #1: Meet in the Middle [Accepted]
**Intuition and Algorithm**

First, let's get a sense of the condition that `average(B) = average(C)`, where `B`, `C` are defined in the problem statement.

Say `A` (the input array) has `N` elements which sum to `S`, and `B` (one of the splitting sets) has `K` elements which sum to `X`. Then the equation for `average(B) = average(C)` becomes $\frac{X}{K} = \frac{S-X}{N-K}$. This reduces to $X(N-K) = (S-X)K$ which is $\frac{X}{K} = \frac{S}{N}$. That is, `average(B) = average(A)`.

Now, we could delete `average(A)` from each element `A[i]` without changing our choice for `B`. (`A[i] -= mu`, where `mu = average(A)`). This means we just want to choose a set `B` that sums to `0`.

Trying all $2^N$ sets is still too many choices, so we will create sets of sums `left, right` of the approximately $2^{N/2}$ choices on the `left` and on the `right` separately. (That is, `left` is a set of sums of every powerset in the first half of `A`, and `right` is the set of sums of every powerset in the second half of `A`). Then, it is true if we find $0$ in these powersets, or if two sums in different halves cancel out (`-x in right for x in left`), except for one minor detail below.

Care must be taken that we do not specify sets that would make the original `B` or `C` empty. If `sleft = A[0] + A[1] + ... + A[N/2 - 1]`, and `sright = A[N/2] + ... + A[N-1]`, (where `A[i]` was transformed to the new `A[i] - average(A)`) then we cannot choose both (`sleft, sright`). This is correct because if for example sleft was a sum reached by a strictly smaller powerset than {`A[0], A[1], ..., A[N/2 - 1]`}, then the difference between these sets would be non-empty and have sum `0`.

```python
class Solution(object):
    def splitArraySameAverage(self, A):
        from fractions import Fraction
        N = len(A)
        S = sum(A)
        A = [z - Fraction(S, N) for z in A]

        if N == 1: return False

        #Want zero subset sum
        left = {A[0]}
        for i in xrange(1, N/2):
            left = {z + A[i] for z in left} | left | {A[i]}
        if 0 in left: return True

        right = {A[-1]}
        for i in xrange(N/2, N-1):
            right = {z + A[i] for z in right} | right | {A[i]}
        if 0 in right: return True

        sleft = sum(A[i] for i in xrange(N/2))
        sright = sum(A[i] for i in xrange(N/2, N))

        return any(-ha in right and (ha, -ha) != (sleft, sright) for ha in left)
```

**Complexity Analysis**

* Time Complexity: $O(2^{N/2})$, where $N$ is the length of `A`.

* Space Complexity: $O(2^{N/2})$.

# Submissions
---
**Solution 1: (Meet in the Middle)**
```
Runtime: 1396 ms
Memory Usage: 17.4 MB
```
```python
class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        from fractions import Fraction
        N = len(A)
        S = sum(A)
        A = [z - Fraction(S, N) for z in A]

        if N == 1: return False

        #Want zero subset sum
        left = {A[0]}
        for i in range(1, N//2):
            left = {z + A[i] for z in left} | left | {A[i]}
        if 0 in left: return True

        right = {A[-1]}
        for i in range(N//2, N-1):
            right = {z + A[i] for z in right} | right | {A[i]}
        if 0 in right: return True

        sleft = sum(A[i] for i in range(N//2))
        sright = sum(A[i] for i in range(N//2, N))

        return any(-ha in right and (ha, -ha) != (sleft, sright) for ha in left)
```