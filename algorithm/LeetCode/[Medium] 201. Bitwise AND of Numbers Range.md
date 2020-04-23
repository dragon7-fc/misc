201. Bitwise AND of Numbers Range

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

**Example 1:**
```
Input: [5,7]
Output: 4
```

**Example 2:**
```
Input: [0,1]
Output: 0
```

# Submissions
---
**Solution 1; (Bit Manipulation, Greedy)**
```
Runtime: 44 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while n > m:
            #next highest 1 bit
            n &= (n-1)
        return n
```

**Solution 2: (Brute Force)**
```
Runtime: 68 ms
Memory Usage: 13.6 MB
```
```python
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m <= n//2: return 0
        return functools.reduce(lambda a, b: a&b, list(range(m, n+1)))
```

**Solution 3: (Common Prefix)**
```
Runtime: 48 ms
Memory Usage: 13.7 MB
```
```python
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        k = 0
        while n != m:
            n >>= 1
            m >>= 1
            k += 1
            
        return n << k
```