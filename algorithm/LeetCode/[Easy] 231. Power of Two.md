231. Power of Two

Given an integer, write a function to determine if it is a power of two.

**Example 1:**
```
Input: 1
Output: true 
Explanation: 2^0 = 1
```

**Example 2:**
```
Input: 16
Output: true
Explanation: 2^4 = 16
```

**Example 3:**
```
Input: 218
Output: false
```

# Submissions
---
**Solution 1: (Math, Bit Manipulation)**
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

**Solution 2: (Math)**
```
Runtime: 0 ms
Memory Usage: 5.8 MB
```
```c
bool isPowerOfTwo(int n){
    if (n <= 0)
        return false;
    while (n >= 2) {
        if (n%2)
            return false;
        n >>= 1;
    }
    return n == 1 ? true : false;
}
```

**Solution 3: (Math)**
```
Runtime: 0 ms
Memory Usage: 5.7 MB
```
```c
bool isPowerOfTwo(int n){
    return n && !(n & (long)n - 1);
}
```
