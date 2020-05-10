50. Pow(x, n)

Implement `pow(x, n)`, which calculates x raised to the power `n` ($x^{n}$).

**Example 1:**
```
Input: 2.00000, 10
Output: 1024.00000
```

**Example 2:**
```
Input: 2.10000, 3
Output: 9.26100
```

**Example 3:**
```
Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
```

**Note:**

* `-100.0 < x < 100.0`
* n is a 32-bit signed integer, within the range $[−2^{31}, 2^{31} − 1]$

# Submissions
---
**Solution 1: (Math)**
```
Runtime: 28 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n < 0:
            x = 1/x
            n = -n
        
        ans = 1
        while n > 0:
            if n % 2 == 1: # current exponent is odd
                ans = ans * x
                x = x * x
                n = (n-1) / 2
            else: # current exponent is even
                x = x * x
                n = n / 2

        return ans
```

**Solution 2: (Math, DFS)**
```
Runtime: 28 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        
        if n < 0:
            x = 1/x
            n = -n

        ans = 1
        if n %2 == 1:
            ans = x * self.myPow(x*x, (n-1)/2)
        else:
            ans = self.myPow(x*x, n/2)

        return ans
```