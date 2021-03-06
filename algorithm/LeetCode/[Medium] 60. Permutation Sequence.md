60. Permutation Sequence

The set `[1,2,3,...,n]` contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for `n = 3`:
```
"123"
"132"
"213"
"231"
"312"
"321"
```
Given `n` and `k`, return the $k^{th}$ permutation sequence.


**Note:**

* Given n will be between `1` and `9` inclusive.
* Given k will be between `1` and `n!` inclusive.

**Example 1:**
```
Input: n = 3, k = 3
Output: "213"
```

**Example 2:**
```
Input: n = 4, k = 9
Output: "2314"
```

# Submissions
---
**Solution 1: (Math, itertools)**
```
Runtime: 2128 ms
Memory Usage: 56.1 MB
```
```python
class Solution:    
    def getPermutation(self, n: int, k: int) -> str:
        return ''.join(list(map(str, list(itertools.permutations([_ for _ in range(1, n+1)]))[k-1])))
```

**Solution 2: (Math, DFS)**
```
Runtime: 28 ms
Memory Usage: 12.7 MB
```
```python
class Solution:    
    def getPermutation(self, n: int, k: int) -> str:
        def permutate(nums, n, k) -> str:
            if n == 1:
                return str(nums[0])

            base = math.factorial(n - 1)
            for num in nums:
                if k - base > 0:
                    k -= base
                else:
                    nums.remove(num)
                    return str(num) + permutate(nums, n - 1, k)
                
        seq = [_ for _ in range(1, n+1)]
        return permutate(seq, n, k)
```

**Solution 3: (Math)**
```
Runtime: 24 ms
Memory Usage: 12.6 MB
```
```python
class Solution:    
    def getPermutation(self, n: int, k: int) -> str:
        rst, k, nums = '', k-1, list(range(1, n+1))
        for i in range(n, 0, -1):
            ind, k = divmod(k, math.factorial(i-1))
            rst += str(nums[ind])
            del nums[ind]
        return rst
```