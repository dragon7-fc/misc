1329. Sort the Matrix Diagonally

Given a `m * n` matrix `mat` of integers, sort it diagonally in ascending order from the top-left to the bottom-right then return the sorted array.

 

**Example 1:**

![1329_1482_example_1_2.png](img/1329_1482_example_1_2.png)
```
Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
```

__Hint1:__

Use a data structure to store all values of each diagonal.

__Hint2:__

How to index the data structure with the id of the diagonal?

__Hint3:__

All cells in the same diagonal (i,j) have the same difference so we can get the diagonal of a cell using the difference i-j.

**Constraints:**

* `m == mat.length`
* `n == mat[i].length`
* `1 <= m, n <= 100`
* `1 <= mat[i][j] <= 100`

**Solution 1: (Hash Table)**

**Explanation** 

* `A[i][j]` on the same diagonal have same value of `i - j`
* For each diagonal, put its elements together, sort, and set them back.


**Complexity**

* Time O(MN)
* Space O(MN)

```
Runtime: 88 ms
Memory Usage: 13 MB
```
```python
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        R, C = len(mat), len(mat[0])
        d = collections.defaultdict(list)
        for r in range(R):
            for c in range(C):
                d[r - c].append(mat[r][c])
        for k in d:
            d[k].sort(reverse=1)
        for r in range(R):
            for c in range(C):
                mat[r][c] = d[r - c].pop()
        return mat
```