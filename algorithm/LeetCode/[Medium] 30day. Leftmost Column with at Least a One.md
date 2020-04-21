Leftmost Column with at Least a One

(This problem is an interactive problem.)

A binary matrix means that all elements are `0` or `1`. For each individual row of the matrix, this row is sorted in non-decreasing order.

Given a row-sorted binary matrix `binaryMatrix`, return leftmost column index(0-indexed) with at least a `1` in it. If such index doesn't exist, return `-1`.

**You can't access the Binary Matrix directly**.  You may only access the matrix using a `BinaryMatrix` interface:

* `BinaryMatrix.get(x, y)` returns the element of the matrix at index `(x, y)` (0-indexed).
* `BinaryMatrix.dimensions()` returns a list of 2 elements `[n, m]`, which means the matrix is `n * m`.

Submissions making more than `1000` calls to `BinaryMatrix.get` will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.

For custom testing purposes you're given the binary matrix `mat` as input in the following four examples. You will not have access the binary matrix directly.

 

**Example 1:**

![30day_21_untitled-diagram-5.jpg](img/30day_21_untitled-diagram-5.jpg)
```
Input: mat = [[0,0],[1,1]]
Output: 0
```

**Example 2:**

![30day_21_untitled-diagram-4.jpg](img/30day_21_untitled-diagram-4.jpg)
```
Input: mat = [[0,0],[0,1]]
Output: 1
```

**Example 3:**

![30day_21_untitled-diagram-3.jpg](img/30day_21_untitled-diagram-3.jpg)
```
Input: mat = [[0,0],[0,0]]
Output: -1
```

**Example 4:**

![30day_21_untitled-diagram-6.jpg](img/30day_21_untitled-diagram-6.jpg)
```
Input: mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
Output: 1
``` 

**Constraints:**

* `1 <= mat.length, mat[i].length <= 100`
* `mat[i][j]` is either `0` or `1`.
* `mat[i]` is sorted in a non-decreasing way.

**Hint**

1. (Binary Search) For each row do a binary search to find the leftmost one on that row and update the answer.
1. (Optimal Approach) Imagine there is a pointer p(x, y) starting from top right corner. p can only move left or down. If the value at p is 0, move down. If the value at p is 1, move left. Try to figure out the correctness and time complexity of this algorithm.

# Submissions
---
**Solution 1: (2D Binary Search)**

(Optimal Approach) Imagine there is a pointer p(x, y) starting from top right corner. p can only move left or down. If the value at p is 0, move down. If the value at p is 1, move left. Try to figure out the correctness and time complexity of this algorithm.

```
Runtime: 104 ms
Memory Usage: 14.2 MB
```
```python
# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        R, C = binaryMatrix.dimensions()
        
        def search(r, c):
            if r == R and c == C-1:
                return -1
            elif r == R:
                return c+1
            elif c < 0:
                return 0
            upper_right = binaryMatrix.get(r, c)
            if upper_right == 1:
                return search(r, c - 1)
            elif upper_right == 0:
                return search(r + 1, c)

        return search(0, C-1)

```