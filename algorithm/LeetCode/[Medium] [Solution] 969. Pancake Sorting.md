969. Pancake Sorting

Given an array `A`, we can perform a pancake flip: We choose some positive integer `k <= A.length`, then reverse the order of the first `k` elements of `A`.  We want to perform zero or more pancake flips (doing them one after another in succession) to sort the array `A`.

Return the `k`-values corresponding to a sequence of pancake flips that sort `A`.  Any valid answer that sorts the array within `10 * A.length` flips will be judged as correct.

**Example 1:**
```
Input: [3,2,4,1]
Output: [4,2,4,3]
Explanation: 
We perform 4 pancake flips, with k values 4, 2, 4, and 3.
Starting state: A = [3, 2, 4, 1]
After 1st flip (k=4): A = [1, 4, 2, 3]
After 2nd flip (k=2): A = [4, 1, 2, 3]
After 3rd flip (k=4): A = [3, 2, 1, 4]
After 4th flip (k=3): A = [1, 2, 3, 4], which is sorted. 
```

**Example 2:**
```
Input: [1,2,3]
Output: []
Explanation: The input is already sorted, so there is no need to flip anything.
Note that other answers, such as [3, 3], would also be accepted.
``` 

**Note:**

1. `1 <= A.length <= 100`
1. `A[i]` is a permutation of `[1, 2, ..., A.length]`

# Solution
---
## Approach 1: Sort Largest to Smallest
**Intuition**

We can place the largest element (in location `i`, 1-indexed) by flipping `i` to move the element to the first position, then `A.length` to move it to the last position. Afterwards, the largest element is in the correct position, so we no longer need to pancake-flip by `A.length` or more.

We can repeat this process until the array is sorted. Each move will use 2 flips per element.

**Algorithm**

First, sort the locations from largest value of `A` to smallest value of `A`.

For each element (from largest to smallest) with location `i`, we will first simulate where this element actually is, based on the pancake flips we have done. For a pancake flip `f`, if `i <= f`, then the element has moved from location `i` to `f+1 - i`.

After, we flip by `i` then `N--` to put this element in the correct position.

```python
class Solution(object):
    def pancakeSort(self, A):
        ans = []

        N = len(A)
        B = sorted(range(1, N+1), key = lambda i: -A[i-1])
        for i in B:
            for f in ans:
                if i <= f:
                    i = f+1 - i
            ans.extend([i, N])
            N -= 1

        return ans
```
**Complexity Analysis**

* Time Complexity: $O(N^2)$, where $N$ is the length of `A`.

* Space Complexity: $O(N)$.

# Submissions
---
**Solution 1: (Sort)**
```
Runtime: 44 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        ans = []
        
        for i in range(len(A)-1, 0, -1):
            if A[i] != i+1:
                vi = A.index(i+1)
                if vi != 0:
                    A[:vi + 1] = A[vi::-1]
                    A[:i+1] = A[i::-1]
                    ans.append(vi +1)
                    ans.append(i+1)
                else:
                    A[:i+1] = A[i::-1]
                    ans.append(i+1)
        return ans
```