326. Power of Three

Given an integer, write a function to determine if it is a power of three.

**Example 1:**
```
Input: 27
Output: true
```

**Example 2:**
```
Input: 0
Output: false
```

**Example 3:**
```
Input: 9
Output: true
```

**Example 4:**
```
Input: 45
Output: false
```

**Follow up:**

Could you do it without using any loop / recursion?

# Submissions
---
**Solution 1: (Math, Greedy)**
```
Runtime: 80 ms
Memory Usage: 12.5 MB
```
```python
class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        while n%3 == 0:
            n = n/3
        return True if n == 1 else False
```

**Solution 2: (Math)**
```
Runtime: 32 ms
Memory Usage: 6 MB
```
```c++
class Solution {
public:
    bool isPowerOfThree(int n) {
        return fmod((log10(n) / log10(3)), 1) == 0;
    }
};
```

**Solution 3: (Math)**


         n = 3^x
    log3(n) = log3(3^x) = x
    log3(n) = x
   ^^^^^^^^
log(n)/log(3)

```
Runtime: 7 ms, Beats 23.24%
Memory: 8.88 MB, Beats 76.82%
```
```c++
class Solution {
public:
    bool isPowerOfThree(int n) {
        int e = log(INT_MAX)/log(3);
        int N = pow(3, e);
        return n > 0 && N%n == 0;
    }
};
```
