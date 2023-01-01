2387. Median of a Row Wise Sorted Matrix

Given an `m x n` matrix grid containing an **odd** number of integers where each row is sorted in **non-decreasing** order, return the **median** of the matrix.

You must solve the problem in less than `O(m * n)` time complexity.

 

**Example 1:**
```
Input: grid = [[1,1,2],[2,3,3],[1,3,4]]
Output: 2
Explanation: The elements of the matrix in sorted order are 1,1,1,2,2,3,3,3,4. The median is 2.
```

**Example 2:**
```
Input: grid = [[1,1,3,3,4]]
Output: 3
Explanation: The elements of the matrix in sorted order are 1,1,3,3,4. The median is 3.
```

**Constraints:**

* `m == grid.length`
* `n == grid[i].length`
* `1 <= m, n <= 500`
* `m` and `n` are both odd.
* `1 <= grid[i][j] <= 10^6`
* `grid[i]` is sorted in non-decreasing order.

# Submissions
---
**Solution 1: (Binary Search)**
```
Runtime: 899 ms
Memory: 47.4 MB
```
```python
class Solution:
    def matrixMedian(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        left, right = float('inf'), float('-inf')
        for r in grid:
            left = min(left, r[0])
            right = max(right, r[-1])

        def check(m):
            cur = 0
            for r in grid:
                cur += bisect.bisect_right(r, m)
            return cur < M*N//2 + 1

        while left < right:
            mid = left + (right-left)//2
            if check(mid):
                left = mid+1
            else:
                right = mid

        return left
```
