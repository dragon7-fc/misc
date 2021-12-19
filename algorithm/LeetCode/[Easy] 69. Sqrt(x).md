69. Sqrt(x)

Implement `int sqrt(int x)`.

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

**Example 1:**
```
Input: 4
Output: 2
```

**Example 2:**
```
Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
```

# Submissions
---
**Solution 1: (Math)**
```
Runtime: 28 ms
Memory Usage: N/A
```
```python
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(math.sqrt(x))
```

**Solution 2: (Math, Binary Search)**
```
Runtime: 28 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid > x:
                right = mid - 1
            elif mid * mid < x:
                left = mid + 1
            else:
                return mid
        return right
```

**Solution 3: (Binary Search)**
```
Runtime: 0 ms
Memory Usage: 5.7 MB
```
```c
int mySqrt(int x){
    if (x <= 1)
        return x;
    long left = 0, right = x, mid;
    while (left <= right) {
        mid = (left+right)/2;
        if (mid*mid == x)
            return mid;
        else if (mid*mid > x)
            right = mid-1;
        else
            left = mid+1;
    }
    return right;
}
```
