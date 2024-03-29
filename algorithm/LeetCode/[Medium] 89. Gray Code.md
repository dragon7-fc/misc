89. Gray Code

The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer `n` representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with `0`.

**Example 1:**
```
Input: 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2

For a given n, a gray code sequence may not be uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence.

00 - 0
10 - 2
11 - 3
01 - 1
```

**Example 2:**
```
Input: 0
Output: [0]
Explanation: We define the gray code sequence to begin with 0.
             A gray code sequence of n has size = 2n, which for n = 0 the size is 20 = 1.
             Therefore, for n = 0 the gray code sequence is [0].
```

# Submissions
---
**Solution 1: (Bit)**
```
Runtime: 28 ms
Memory Usage: 12.6 MB
```

// 000 = 000 ^ 000  0^0
// 001 = 001 ^ 000  1^0
// 011 = 010 ^ 001  2^1
// 010 = 011 ^ 001  3^1
// 110 = 100 ^ 010  4^2
// 111 = 101 ^ 010  5^2
// 101 = 110 ^ 011  6^3
// 100 = 111 ^ 011  7^3

```python
class Solution:
    def grayCode(self, n: int) -> List[int]:
        return [i ^ (i >> 1) for i in range(2**n)]
```

**Solution 2: (Recursion)**
```
Runtime: 24 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        
        def recursion(n):
            if n == 1:
                return ['0','1']
            else:
                return ['0' + i for i in recursion(n - 1)] + ['1' + i for i in recursion(n - 1)[::-1]]
            
        return [int(i,2) for i in recursion(n)]
```
