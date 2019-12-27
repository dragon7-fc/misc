974. Subarray Sums Divisible by K

Given an array `A` of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by `K`.

 

**Example 1:**
```
Input: A = [4,5,0,-2,-3,1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
``` 

**Note:**

1. 1 <= `A.length` <= 30000
1. -10000 <= `A[i]` <= 10000
1. 2 <= `K` <= 10000

# Solution
---
## Approach 1: Prefix Sums and Counting
**Intuition**

As is typical with problems involving subarrays, we use prefix sums to add each subarray. Let `P[i+1] = A[0] + A[1] + ... + A[i]`. Then, each subarray can be written as `P[j] - P[i]` (for `j > i`). Thus, we have `P[j] - P[i]` equal to `0` modulo `K`, or equivalently `P[i]` and `P[j]` are the same value modulo `K`.

**Algorithm**

Count all the `P[i]`'s modulo `K`. Let's say there are $C_x$ values $P[i] \equiv x \pmod{K}$. Then, there are $\sum_x \binom{C_x}{2}$ possible subarrays.

For example, take `A = [4,5,0,-2,-3,1]` and `K = 5`. Then `P = [0,4,9,9,7,4,5]`, and $C_0 = 2, C_2 = 1, C_4 = 4$:

* With $C_0 = 2$ (at $P[0]$, $P[6]$), it indicates $\binom{2}{2} = 1$ subarray with sum divisible by $K$, namely $A[0:6] = [4, 5, 0, -2, -3, 1]$.
* With $C_4 = 4$ (at $P[1]$, $P[2]$, $P[3]$, $P[5]$), it indicates $\binom{4}{2} = 6$ subarrays with sum divisible by $K$, namely $A[1:2]$, $A[1:3]$, $A[1:5]$, $A[2:3]$, $A[2:5]$, $A[3:5]$.

```python
class Solution(object):
    def subarraysDivByK(self, A, K):
        P = [0]
        for x in A:
            P.append((P[-1] + x) % K)

        count = collections.Counter(P)
        return sum(v*(v-1)/2 for v in count.values())
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the length of `A`.

* Space Complexity: $O(N)$. (However, the solution can be modified to use $O(K)$ space by storing only count.)

# Submissions
---
**Solution**
```
Runtime: 344 ms
Memory Usage: 17.8 MB
```
```python
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        P = [0]
        for x in A:
            P.append((P[-1] + x) % K)

        count = collections.Counter(P)
        return sum(v*(v-1)//2 for v in count.values())
```