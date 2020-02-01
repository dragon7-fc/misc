1130. Minimum Cost Tree From Leaf Values

Given an array `arr` of positive integers, consider all binary trees such that:

* Each node has either 0 or 2 children;
* The values of `arr` correspond to the values of each leaf in an in-order traversal of the tree.  (Recall that a node is a leaf if and only if it has 0 children.)
* The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree respectively.

Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node.  It is guaranteed this sum fits into a 32-bit integer.

 

**Example 1:**

```
Input: arr = [6,2,4]
Output: 32
Explanation:
There are two possible trees.  The first has non-leaf node sum 36, and the second has non-leaf node sum 32.

    24            24
   /  \          /  \
  12   4        6    8
 /  \               / \
6    2             2   4
``` 

**Constraints:**

* `2 <= arr.length <= 40`
* `1 <= arr[i] <= 15`
* It is guaranteed that the answer fits into a 32-bit signed integer (ie. it is less than `2^31`).

# Submisssions
---
**Solution 1: (Heap, Stack)**

There are numerous ways to solve this problem, but I didn't see anyone do it with a heap. The basic premise is to walk through the array using a minheap to track the smallest leaf seen essentially and collapse it with a larger leaf strategically until we end up with just one node.

```
Runtime: 28 ms
Memory Usage: 12.6 MB
```
```python
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        cost, heap = 0, [float('inf')]
        for leaf in arr:
            while heap[0] < leaf: # join the cheapest possible leaves
                cost += heapq.heappop(heap) * min(leaf, heap[0])
            heapq.heappush(heap, leaf)
        while len(heap) > 2: # no choice but to join the remaining leaves
            cost += heapq.heappop(heap) * heap[0]
        return cost
```

**Solution 2: (DFS)**
```
Runtime: 268 ms
Memory Usage: 13.3 MB
```
```python
from functools import lru_cache

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        from functools import lru_cache
        @lru_cache(None)
        def dp(i,j):
            if j - i > 0:
                return min(dp(i,k-1) + dp(k,j) + max(arr[i:k])*max(arr[k:j+1]) for k in range(i+1,j+1))
            return 0 
        
        return dp(0,len(arr)-1)
```