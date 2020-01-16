1053. Previous Permutation With One Swap

Given an array `A` of positive integers (not necessarily distinct), return the lexicographically largest permutation that is smaller than `A`, that can be made with one swap (A swap exchanges the positions of two numbers `A[i]` and `A[j]`).  If it cannot be done, then return the same array.

 

**Example 1:**
```
Input: [3,2,1]
Output: [3,1,2]
Explanation: Swapping 2 and 1.
```

**Example 2:**
```
Input: [1,1,5]
Output: [1,1,5]
Explanation: This is already the smallest permutation.
```

**Example 3:**
```
Input: [1,9,4,6,7]
Output: [1,7,4,6,9]
Explanation: Swapping 9 and 7.
```

**Example 4:**
```
Input: [3,1,1,3]
Output: [1,3,1,3]
Explanation: Swapping 1 and 3.
``` 

**Note:**

1. `1 <= A.length <= 10000`
1. `1 <= A[i] <= 10000`

# Submissions
---
**Solution 1: (Greedy)**
```
Runtime: 284 ms
Memory Usage: 14.8 MB
```
```python
class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        ind = None
        # find right-most decreasing seq A[ind]
        for i in range(len(A)-1,-1,-1):
            if i-1 >= 0 and A[i-1] > A[i]:
                ind = i-1
                break   

        # If no such index, return original array A 
        if ind==None:
            return A

        mx = float('-inf')

        # find A[mxind] nearest to A[ind], from ind to end
        for i in range(ind+1, len(A)):
            if A[i] > mx and A[i] < A[ind]:
                mx = A[i]
                mxind = i

        # Simple Swap
        A[ind], A[mxind] = A[mxind], A[ind]
 
        return A
```