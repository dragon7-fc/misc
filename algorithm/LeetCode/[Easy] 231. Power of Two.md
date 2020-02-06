231. Power of Two

Given an integer, write a function to determine if it is a power of two.

**Example 1:**
```
Input: 1
Output: true 
Explanation: 20 = 1
```

**Example 2:**
```
Input: 16
Output: true
Explanation: 24 = 16
```

**Example 3:**
```
Input: 218
Output: false
```

# Submissions
---
**Solution 1: (Bit Manipulation)**
```
Runtime: 28 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        
        while n >= 2:
            n, r = divmod(n, 2)
            if r:
                return False
        
        return True
```