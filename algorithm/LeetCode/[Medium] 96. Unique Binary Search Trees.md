96. Unique Binary Search Trees

Given n, how many structurally unique **BST**'s (binary search trees) that store values 1 ... n?

**Example:**
```
Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```

# Submissions
---
**Solution 1: (DP Bottom-Up)**
```
Runtime: 40 ms
Memory Usage: N/A
```
```python
class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        arr = [0]*(n+1)
        arr[0] = 1
        arr[1] = 1
        arr[2] = 2
        for i in range(3,n+1):
            for j in range(i):
                arr[i] += arr[j]*arr[i-1-j]
        return arr[-1]
```

**Solution 2: (DP Top-Down)**
```
Runtime: 24 ms
Memory Usage: 12.9 MB
```
```python
import functools
class Solution:
    
    @functools.lru_cache(None)
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 1
        elif n == 2:
            return 2
        rst = 0
        for i in range(n):
            rst += self.numTrees(i) * self.numTrees(n - i - 1)
        return rst
```