400. Nth Digit

Find the $n^{th}$ digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

**Note:**

n is positive and will fit within the range of a 32-bit signed integer (n < $2^{31}$).

**Example 1:**
```
Input:
3

Output:
3
```

**Example 2:**
```
Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
```

# Submissions
---
**Solution 1: (Math)**
```
Runtime: 28 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def findNthDigit(self, n: int) -> int:
        s, d = 0, 0
        while s < n:
            s += (d+1)*9*10**d
            d += 1
        n -= s-d*9*10**(d-1)
        r, q = n % d, 10**(d-1) + n//d
        return str(q)[r-1] if r > 0 else str(q-1)[-1]
```