397. Integer Replacement

Given a positive integer `n` and you can do operations as follow:

* If `n` is even, replace `n` with `n/2`.
* If `n` is odd, you can replace `n` with either `n + 1` or `n - 1`.

What is the minimum number of replacements needed for `n` to become `1`?

**Example 1:**
```
Input:
8

Output:
3

Explanation:
8 -> 4 -> 2 -> 1
```

**Example 2:**
```
Input:
7

Output:
4

Explanation:
7 -> 8 -> 4 -> 2 -> 1
or
7 -> 6 -> 3 -> 2 -> 1
```
# Submissions
---
**Solution 1: (DFS, DP - Top-down)**
```
Runtime: 20 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def integerReplacement(self, n: int) -> int:
        dic = {}
        def dp(num):
            if num == 1:
                return 0
            if num in dic:
                return dic[num]
            if num%2 == 0:
                res = 1 + dp(num>>1)
            else:
                res = 1 + min(dp(num+1), dp(num-1))
            dic[num] = res
            return res
        
        return dp(n)
```

**Solution 2: (Bit Manipulation)**
```
Runtime: 24 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def integerReplacement(self, n: int) -> int:
        res = 0
        m = n
        while m != 1:
            if m%2 == 0:    # if even 
                m >>= 1    # shift one bit right. This action is same as dividing the number by 2.  0010 >> 1 = 0001  ( 2 / 2 = 1 )
                res += 1
            else:  # if odd
                if m == 3:    # special case 3: 0011 -1 = 0010; 0010 >> 1 = 0001
                    res += 2    # so we add two steps
                    break
                m = m+1 if (m & 2) == 2 else m-1    # if the second bit of m is 1, we need to perform m+1, else perform m-1
                res += 1
                
        return res
```