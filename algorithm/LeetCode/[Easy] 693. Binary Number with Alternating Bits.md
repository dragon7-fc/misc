693. Binary Number with Alternating Bits

Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

**Example 1:**
```
Input: 5
Output: True
Explanation:
The binary representation of 5 is: 101
```

**Example 2:**
```
Input: 7
Output: False
Explanation:
The binary representation of 7 is: 111.
```

**Example 3:**
```
Input: 11
Output: False
Explanation:
The binary representation of 11 is: 1011.
```

**Example 4:**
```
Input: 10
Output: True
Explanation:
The binary representation of 10 is: 1010.
```

# Submissions
---
**Solution 1: (Bit Manipulation)**
```
Runtime: 20 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        return not ('11' in bin(n)[2:] or '00' in bin(n)[2:])
```

**Solution 2: (Bit Manipulation)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 7.80 MB, Beats 30.66%
```
```c++
class Solution {
public:
    bool hasAlternatingBits(int n) {
        if (n <= 2) {
            return true;
        }
        long long a = 2;
        while (a <= n) {
            if (((a & n) != 0) == (((a >> 1) & n) != 0)) {
                return false;
            }
            a <<= 1;
        }
        return true;
    }
};
```

**Solution 3: (Bit Manipulation)**

    n = 6
        0b110
            ^n%2 = cur
           ^(n/2)%2
-------------
cur    0
n      3
-------------
cur    1
n      1

```
Runtime: 0 ms, Beats 100.00%
Memory: 7.81 MB, Beats 30.66%
```
```c++
class Solution {
public:
    bool hasAlternatingBits(int n) {
        int cur = n % 2;
        n /= 2;
        while (n > 0) {
            if (cur == n % 2) return false;
            cur = n % 2;
            n /= 2;
        }
        return true;
    }
};
```
