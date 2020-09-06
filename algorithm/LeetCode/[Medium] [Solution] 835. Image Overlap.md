835. Image Overlap

Two images `A` and `B` are given, represented as binary, square matrices of the same size.  (A binary matrix has only 0s and 1s as values.)

We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  After, the overlap of this translation is the number of positions that have a 1 in both images.

(Note also that a translation does **not** include any kind of rotation.)

What is the largest possible overlap?

**Example 1:**
```
Input: A = [[1,1,0],
            [0,1,0],
            [0,1,0]]
       B = [[0,0,0],
            [0,1,1],
            [0,0,1]]
Output: 3
Explanation: We slide A to right by 1 unit and down by 1 unit.
```
**Notes:** 

1. `1 <= A.length = A[0].length = B.length = B[0].length <= 30`
1. `0 <= A[i][j], B[i][j] <= 1`

# Solution
---
## Approach #1: Translate by Delta [Accepted]
**Intuition and Algorithm**

For each translation `delta`, we calculate the candidate answer `overlap(delta)`, which is the size of the overlap if we shifted the matrix `A` by delta.

We only need to check `delta` for which some point in `A` maps to some point in `B`, since a candidate overlap must be at least 1. Using a Set `seen`, we remember if we've calculated `overlap(delta)`, so that we don't perform this expensive check more than once per `delta`.

We use `java.awt.Point` (or `complex` in Python) to handle our 2D vectors gracefully. We could have also mapped a vector `delta = (x, y)` (which has coordinates between `-(N-1)` and `N-1`) to `2*N x + y` for convenience. Note that we cannot map it to `N*dx, dy` as there would be interference: `(0, N-1)` and `(1, -1)` would map to the same point.

```python
class Solution(object):
    def largestOverlap(self, A, B):
        N = len(A)
        A2 = [complex(r, c) for r, row in enumerate(A)
              for c, v in enumerate(row) if v]
        B2 = [complex(r, c) for r, row in enumerate(B)
              for c, v in enumerate(row) if v]
        Bset = set(B2)
        seen = set()
        ans = 0
        for a in A2:
            for b in B2:
                d = b-a
                if d not in seen:
                    seen.add(d)
                    ans = max(ans, sum(x+d in Bset for x in A2))
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N^6)$, where $N$ is the length of `A` or `B`.

* Space Complexity: $O(N^2)$.

## Approach #2: Count by Delta [Accepted]
**Intuition and Algorithm**

We can do the reverse of Approach #1: count every possible `delta = b - a` we see. If we see say, 5 of the same `delta = b - a`, then the translation by `delta` must have overlap 5.

```python
class Solution(object):
    def largestOverlap(self, A, B):
        N = len(A)
        count = collections.Counter()
        for i, row in enumerate(A):
            for j, v in enumerate(row):
                if v:
                    for i2, row2 in enumerate(B):
                        for j2, v2 in enumerate(row2):
                            if v2:
                                count[i-i2, j-j2] += 1
        return max(count.values() or [0])
```

## Complexity Analysis

* Time Complexity: $O(N^4)$, where $N$ is the length of A or B.

* Space Complexity: $O(N^2)$.

# Submissions
---
**Solution: (Count by Delta)**
```
Runtime: 680 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        N = len(A)
        count = collections.Counter()
        for i, row in enumerate(A):
            for j, v in enumerate(row):
                if v:
                    for i2, row2 in enumerate(B):
                        for j2, v2 in enumerate(row2):
                            if v2:
                                count[i-i2, j-j2] += 1
                                
        return max(count.values() or [0])
```

**Solution 2: (Delta Hash Table Counter)**
```
Runtime: 348 ms
Memory Usage: 14.2 MB
```
```python
class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        A_points, B_points, d = [], [], collections.defaultdict(int)

        # Filter points having 1 for each matrix respectively.
        for r in range(len(A)):
            for c in range(len(A[0])):
                if A[r][c]:
                    A_points.append((r, c))

                if B[r][c]:
                    B_points.append((r, c))
 
        # For every point in filtered A, calculate the
        # linear transformation vector with all points of filtered B
        # count the number of the pairs that have the same transformation vector
        for r_a, c_a in A_points:
            for r_b, c_b in B_points:
                d[(r_b - r_a, c_b - c_a)] += 1

        return max(d.values() or [0])
```