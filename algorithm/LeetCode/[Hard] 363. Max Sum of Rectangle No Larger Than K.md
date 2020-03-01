363. Max Sum of Rectangle No Larger Than K

Given a non-empty 2D matrix matrix and an integer k, find the max sum of a rectangle in the matrix such that its sum is no larger than k.

**Example:**
```
Input: matrix = [[1,0,1],[0,-2,3]], k = 2
Output: 2 
Explanation: Because the sum of rectangle [[0, 1], [-2, 3]] is 2,
             and 2 is the max number no larger than k (k = 2).
```
**Note:**

* The rectangle inside the `matrix` must have an `area > 0`.
* What if the number of rows is much larger than the number of columns?

# Submissions
---
**Solution 1: (Prefix Sum, Binary Search)**
```
Runtime: 964 ms
Memory Usage: 13.7 MB
```
```python
class Solution:
    # Overall complexity O(n^4)
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        # Validation for corner case.
        if not matrix:
            return 0

        # Traditional kadane algorithm does not work 
        # here, as that algorithm always finds max sum
        # in a sub array and disregards intermediate sums
        # which needs to be considered for evaluating <=k criteria. 
        #
        # Below function stores prefix sum values
        # in a sorted list and performs binary 
        # search on this list to get the closest
        # element whose difference with current element
        # does not exceed k. 
        # Complexity for this algorithm is O(n^2)
        def max_sum_array_no_larger_than_k(l, k):
            prefix_sums = [0]
            prefix_sum, max_sum = 0, -sys.maxsize
            for item in l:
                prefix_sum += item
                
                left = bisect.bisect_left(prefix_sums, prefix_sum - k)
                if left < len(prefix_sums):
                    max_sum = max(max_sum, prefix_sum - prefix_sums[left])
                   
               # This has a worst case complexity of O(n) 
                bisect.insort(prefix_sums, prefix_sum)
            return max_sum

        R = len(matrix)
        C = len(matrix[0])
        max_sum = float('-inf')
        
        # Below loops basically fold 2-d array into 
        # a single dimensional array, so that above 
        # function can be applied to it.
        # Here we iterate through all possible 2-d
        # arrays possible for every column. 
        for from_col in range(C):
            col_values = [0 for _ in range(R)]
            for to_col in range(from_col, C):
                for row in range(R):
                    col_values[row] = col_values[row] + matrix[row][to_col]
                curr_sum = max_sum_array_no_larger_than_k(col_values, k)
                max_sum = max(curr_sum, max_sum)
        return max_sum
```