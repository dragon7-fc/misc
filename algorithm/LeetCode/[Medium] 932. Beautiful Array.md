932. Beautiful Array

For some fixed `N`, an array `A` is beautiful if it is a permutation of the integers `1, 2, ..., N`, such that:

For every `i < j`, there is **no** `k` with `i < k < j` such that `A[k] * 2 = A[i] + A[j]`.

Given `N`, return **any** beautiful array `A`.  (It is guaranteed that one exists.)

 

**Example 1:**
```
Input: 4
Output: [2,1,4,3]
```

**Example 2:**
```
Input: 5
Output: [3,1,2,5,4]
```

**Note:**

* `1 <= N <= 1000`

# Submissions
---
**Solution 1: (Divide and Conquer)**

Example:
1,2,3,4,5,6,7,8,9
-->
1,3,5,7,9,2,4,6,8
-->
1,5,9,3,7,2,6,4,8
-->
1,9,5,3,7,2,6,4,8

```
Runtime: 36 ms
Memory Usage: 12.6 MB
```
```python
class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        def dfs(lst):
            if len(lst) <= 2:
                return lst
            return dfs(lst[::2]) + dfs(lst[1::2])
        
        return dfs([_ for _ in range(1,N+1)])
```