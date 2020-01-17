1253. Reconstruct a 2-Row Binary Matrix

Given the following details of a matrix with n columns and 2 rows :

* The matrix is a binary matrix, which means each element in the matrix can be `0` or `1`.
* The sum of elements of the `0`-th(upper) row is given as `upper`.
* The sum of elements of the `1`-st(lower) row is given as `lower`.
* The sum of elements in the `i`-th column(0-indexed) is `colsum[i]`, where `colsum` is given as an integer array with length `n`.

Your task is to reconstruct the matrix with upper, lower and colsum.

Return it as a 2-D integer array.

If there are more than one valid solution, any of them will be accepted.

If no valid solution exists, return an empty 2-D array.

 

**Example 1:**

```
Input: upper = 2, lower = 1, colsum = [1,1,1]
Output: [[1,1,0],[0,0,1]]
Explanation: [[1,0,1],[0,1,0]], and [[0,1,1],[1,0,0]] are also correct answers.
```

**Example 2:**

```
Input: upper = 2, lower = 3, colsum = [2,2,1,1]
Output: []
```

**Example 3:**

```
Input: upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1]
Output: [[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]
```

**Constraints:**

* `1 <= colsum.length <= 10^5`
* `0 <= upper, lower <= colsum.length`
* `0 <= colsum[i] <= 2`

# Submissions
---
**Solution 1: (Greedy)**
```
Runtime: 728 ms
Memory Usage: 22.9 MB
```
```python
class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        if upper + lower != sum(colsum):
            return []
        
        R = 2
        C = len(colsum)
        ans = [[0]*C for _ in range(R)]

        for c in range(C):
            if colsum[c] == 2:
                if not upper > 0 or not lower > 0:
                    return []
                for r in range(R):
                    ans[r][c] = 1
                upper -= 1
                lower -= 1
                
        for c in range(C):
            if colsum[c] == 1:
                if upper > 0:
                    ans[0][c] = 1
                    upper -= 1
                elif lower > 0:
                    ans[1][c] = 1
                    lower -= 1
                else:
                    return []
        
        return ans
        
```