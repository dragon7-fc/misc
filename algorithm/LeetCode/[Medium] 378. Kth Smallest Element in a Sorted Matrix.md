378. Kth Smallest Element in a Sorted Matrix

Given a n x n `matrix` where each of the rows and columns are sorted in ascending order, find the `k`th smallest element in the matrix.

Note that it is the `k`th smallest element in the sorted order, not the kth distinct element.

**Example:**
```
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
```

**Note:**

* You may assume `k` is always valid, `1 ≤ k ≤ n^2`.

# Submissions
---
**SOlution 1:**
```
Runtime: 168 ms
Memory Usage: 18.9 MB
```
```python
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        array = []
        for row in matrix:
            array += row
            
        return sorted(array)[k-1]
```