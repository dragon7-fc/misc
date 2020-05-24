927. Three Equal Parts

Given an array `A` of `0`s and `1`s, divide the array into 3 non-empty parts such that all of these parts represent the same binary value.

If it is possible, return **any** `[i, j]` with `i+1 < j`, such that:

* `A[0], A[1], ..., A[i]` is the first part;
* `A[i+1], A[i+2], ..., A[j-1]` is the second part, and
* `A[j], A[j+1], ..., A[A.length - 1]` is the third part.
* `All` three parts have equal binary value.

If it is not possible, return `[-1, -1]`.

Note that the entire part is used when considering what binary value it represents.  For example, `[1,1,0]` represents `6` in decimal, not `3`.  Also, leading zeros are allowed, so `[0,1,1]` and `[1,1]` represent the same value.

 

**Example 1:**
```
Input: [1,0,1,0,1]
Output: [0,3]
```

**Example 2:**
```
Input: [1,1,0,1,1]
Output: [-1,-1]
```

**Note:**

* `3 <= A.length <= 30000`
* `A[i] == 0 or A[i] == 1`
 
# Solution
---
## Approach 1: Equal Ones
**Intuition**

Each part has to have the same number of ones in their representation. The algorithm given below is the natural continuation of this idea.

**Algorithm**

Say `S` is the number of ones in `A`. Since every part has the same number of ones, they all should have `T = S / 3` ones.

If `S` isn't divisible by 3, the task is impossible.

We can find the position of the 1st, T-th, T+1-th, 2T-th, 2T+1-th, and 3T-th one. The positions of these ones form 3 intervals: `[i1, j1], [i2, j2], [i3, j3]`. (If there are only 3 ones, then the intervals are each length `1`.)

Between them, there may be some number of zeros. The zeros after `j3` must be included in each part: say there are `z` of them (`z = S.length - j3`).

So the first part, `[i1, j1]`, is now `[i1, j1+z]`. Similarly, the second part, `[i2, j2]`, is now `[i2, j2+z]`.

If all this is actually possible, then the final answer is `[j1+z, j2+z+1]`.

```python
class Solution(object):
    def threeEqualParts(self, A):
        IMP = [-1, -1]

        S = sum(A)
        if S % 3: return IMP
        T = S / 3
        if T == 0:
            return [0, len(A) - 1]

        breaks = []
        su = 0
        for i, x in enumerate(A):
            if x:
                su += x
                if su in {1, T+1, 2*T+1}:
                    breaks.append(i)
                if su in {T, 2*T, 3*T}:
                    breaks.append(i)

        i1, j1, i2, j2, i3, j3 = breaks

        # The array is in the form W [i1, j1] X [i2, j2] Y [i3, j3] Z
        # where [i1, j1] is a block of 1s, etc.
        if not(A[i1:j1+1] == A[i2:j2+1] == A[i3:j3+1]):
            return [-1,-1]

        # x, y, z: the number of zeros after part 1, 2, 3
        x = i2 - j1 - 1
        y = i3 - j2 - 1
        z = len(A) - j3 - 1

        if x < z or y < z: return IMP
        j1 += z
        j2 += z
        return [j1, j2+1]
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the length of S.

* Space Complexity: $O(N)$.

# Submissions
---
**Solution: (Equal Ones)**
```
Runtime: 408 ms
Memory Usage: 14.6 MB
```
```python
class Solution:
    def threeEqualParts(self, A: List[int]) -> List[int]:
        IMP = [-1, -1]

        S = sum(A)
        if S % 3: return IMP
        T = S / 3
        if T == 0:
            return [0, len(A) - 1]

        breaks = []
        su = 0
        for i, x in enumerate(A):
            if x:
                su += x
                if su in {1, T+1, 2*T+1}:
                    breaks.append(i)
                if su in {T, 2*T, 3*T}:
                    breaks.append(i)

        i1, j1, i2, j2, i3, j3 = breaks

        # The array is in the form W [i1, j1] X [i2, j2] Y [i3, j3] Z
        # where [i1, j1] is a block of 1s, etc.
        if not(A[i1:j1+1] == A[i2:j2+1] == A[i3:j3+1]):
            return [-1,-1]

        # x, y, z: the number of zeros after part 1, 2, 3
        x = i2 - j1 - 1
        y = i3 - j2 - 1
        z = len(A) - j3 - 1

        if x < z or y < z: return IMP
        j1 += z
        j2 += z
        return [j1, j2+1]
```