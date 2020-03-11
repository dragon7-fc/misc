867. Transpose Matrix

Given a matrix `A`, return the transpose of `A`.

The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.

![867_hint_transpose.png](img/867_hint_transpose.png)

**Example 1:**
```
Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
```

**Example 2:**
```
Input: [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
```

**Note:**

* 1 <= A.length <= 1000
* 1 <= A[0].length <= 1000

# Solution
---
## Approach 1: Copy Directly
**Intuition and Algorithm**

The transpose of a matrix `A` with dimensions `R x C` is a matrix ans with dimensions `C x R` for which `ans[c][r] = A[r][c]`.

Let's initialize a new matrix ans representing the answer. Then, we'll copy each entry of the matrix as appropriate.

```python
class Solution(object):
    def transpose(self, A):
        R, C = len(A), len(A[0])
        ans = [[None] * R for _ in xrange(C)]
        for r, row in enumerate(A):
            for c, val in enumerate(row):
                ans[c][r] = val
        return ans

        #Alternative Solution:
        #return zip(*A)
```

**Complexity Analysis**

* Time Complexity: $O(R * C)$, where $R$ and $C$ are the number of rows and columns in the given matrix `A`.

* Space Complexity: $O(R * C)$, the space used by the answer.

# Submissions
---
**Solution 1: (Copy Directly)**
```
Runtime: 80 ms
Memory Usage: N/A
```
```python
class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        AT = [[0 for _ in range(len(A))] for _ in range(len(A[0]))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                AT[j][i] = A[i][j]
        return AT
```

**Solution 2: ()**
```
Runtime: 72 ms
Memory Usage: 13.4 MB
```
```python
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return zip(*A)
```