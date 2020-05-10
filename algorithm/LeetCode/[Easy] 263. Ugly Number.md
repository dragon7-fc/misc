263. Ugly Number

Write a program to check whether a given number is an ugly number.

Ugly numbers are **positive numbers** whose prime factors only include `2, 3, 5`.

**Example 1:**
```
Input: 6
Output: true
Explanation: 6 = 2 × 3
```

**Example 2:**
```
Input: 8
Output: true
Explanation: 8 = 2 × 2 × 2
```

**Example 3:**
```
Input: 14
Output: false 
Explanation: 14 is not ugly since it includes another prime factor 7.
```

**Note:**

1. `1` is typically treated as an ugly number.
1. Input is within the 32-bit signed integer range: `[−2^31,  2^31 − 1]`.

# Submissions
---
**Solution 1: (Math, DFS)**
```
Runtime: 28 ms
Memory Usage: 12.6 MB
```
```python
class Solution:
    def isUgly(self, num: int) -> bool:
        prime_factor = [2, 3, 5]
        N = len(prime_factor)
        def dfs(number):
            if number == 1:
                return True
            
            for i in range(N):
                q, r = divmod(number, prime_factor[i])
                if r == 0:
                    return dfs(q)
            return False
            
        return True if num == 1 else False if num <= 0 else dfs(num)
```

**Solution 2: (DFS)**
```
Runtime: 24 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        while not num % 2:
            num /= 2
        while not num % 3:
            num /= 3
        while not num % 5:
            num /= 5
        return num == 1
```