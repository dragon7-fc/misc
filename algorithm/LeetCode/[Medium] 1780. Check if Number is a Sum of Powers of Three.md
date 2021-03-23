1780. Check if Number is a Sum of Powers of Three

Given an integer `n`, return `true` if it is possible to represent `n` as the sum of distinct powers of three. Otherwise, return `false`.

An integer `y` is a power of three if there exists an integer `x` such that `y == 3^x`.

 

**Example 1:**
```
Input: n = 12
Output: true
Explanation: 12 = 31 + 32
```

**Example 2:**
```
Input: n = 91
Output: true
Explanation: 91 = 30 + 32 + 34
```

**Example 3:**
```
Input: n = 21
Output: false
```

**Constraints:**s

* `1 <= n <= 10^7`

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 32 ms
Memory Usage: 14.1 MB
```
```python
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        if n%3 == 2:return False
        if n == 1:return True
        return Solution.checkPowersOfThree(self, int(n/3))
```

**Solution 2: (Math)**
```
Runtime: 28 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n>0:
            if n%3==0:
                n = int(n/3)
            elif n%3==1:
                n = int(n/3)
            else:
                return False
        return True
```