1007. Minimum Domino Rotations For Equal Row

In a row of dominoes, `A[i]` and `B[i]` represent the top and bottom halves of the `i`-th domino.  (A domino is a tile with two numbers from `1` to `6` - one on each half of the tile.)

We may rotate the `i`-th domino, so that `A[i]` and `B[i]` swap values.

Return the minimum number of rotations so that all the values in `A` are the same, or all the values in `B` are the same.

If it cannot be done, return `-1`.

**Example 1:**

![1007_domino](img/1007_domino.png)

```
Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
```

**Example 2:**
```
Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.
``` 

**Note:**

1. 1 <= `A[i]`, `B[i]` <= 6
1. 2 <= `A.length` == `B.length` <= 20000

# Submissions
---
**Solution 1: (Counter)**
```
Runtime: 1340 ms
Memory Usage: 14.7 MB
```
```python
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        a_counter = collections.Counter(A)
        b_counter = collections.Counter(B)
        a_most = a_counter.most_common()[0]
        b_most = b_counter.most_common()[0]
        if a_most[1] > b_most[1]:
            ans = 0
            for i in range(len(A)):
                if A[i] != a_most[0] and B[i] != a_most[0]:
                    return -1
                elif A[i] != a_most[0] and B[i] == a_most[0]:
                    ans += 1
            return ans
        else:
            ans = 0
            for i in range(len(B)):
                if B[i] != b_most[0] and A[i] != b_most[0]:
                    return -1
                elif B[i] != b_most[0] and A[i] == b_most[0]:
                    ans += 1
            return ans
```

**Solution 2: (Set)**
```
Runtime: 1296 ms
Memory Usage: 14.8 MB
```
```python
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        s, n = set([1,2,3,4,5,6]), len(A)
        for i in range(n): s &= set([A[i], B[i]])
        if not s: return -1
        flips1 = sum(A[i] == list(s)[0] for i in range(n))
        flips2 = sum(B[i] == list(s)[0] for i in range(n))
        return min(n - flips1, n - flips2)
```

**Solutin 3: (Counter, Vote)**
```
Runtime: 1112 ms
Memory Usage: 14.9 MB
```
```python
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        cntA = [0] * 7
        cntB = [0] * 7
        cntSame = [0] * 7
        for i in range(n):
            a, b = A[i], B[i]
            cntA[a] += 1
            cntB[b] += 1
            if a == b: cntSame[a] += 1
        ans = n
        for v in range(1, 7):
            if cntA[v] + cntB[v] - cntSame[v] == n:
                minSwap = min(cntA[v], cntB[v]) - cntSame[v]
                ans = min(ans, minSwap)
        return -1 if ans == n else ans
```