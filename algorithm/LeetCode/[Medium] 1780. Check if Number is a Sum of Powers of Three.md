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

**Solution 3: (Math)**

         9  3  1
         ^  ^
cur  27  9  3  
r    12  3  0


        81 27 9 3 1
         ^    ^   ^
cur 243 81 27 9 3 1
r    91 10    1   0


        9 3 1
        ^ ^  
cur 27  9 3 1
r   21 18 6 5

```
Runtime: 0 ms, Beats 100.00%
Memory: 7.75 MB, Beats 67.84%
```
```c++
class Solution {
public:
    bool checkPowersOfThree(int n) {
        int r = n, cur = 1;
        while (cur < r) {
            cur *= 3;
        }
        while (r && cur) {
            if (r >= cur) {
                r -= cur;
            }
            cur /= 3;
        }
        return r == 0;
    }
};
```

**Solution 4: (Ternary Representation)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 7.71 MB, Beats 67.84%
```
```c++
class Solution {
public:
    bool checkPowersOfThree(int n) {
        while (n > 0) {
            // Check if this power should be used twice
            if (n % 3 == 2) return false;

            // Divide n by 3 to move to the next greater power
            n /= 3;
        }

        // The ternary representation of n consists only of 0s and 1s
        return true;
    }
};
```
