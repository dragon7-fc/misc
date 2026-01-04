202. Happy Number

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

**Example:** 
```
Input: 19
Output: true
Explanation: 
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
```

# Submissions
---
**Solution 1: (Greedy, Hash Table)**
```
Runtime: 32 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        v = n
        while True:
            v = sum([int(i)**2 for i in str(v)])
            if v == 1:
                return True
            elif v in seen:
                return False
            else:
                seen.add(v)
```

**Solution 2: (Greedy, Hash Table)**
```
Runtime: 2 ms, Beats 25.23%
Memory: 8.35 MB, Beats 35.30%
```
```c++
class Solution {
public:
    bool isHappy(int n) {
        int a, d;
        unordered_set<int> st;
        while (!st.count(n)) {
            st.insert(n);
            a = 0;
            while (n) {
                d = n % 10;
                a += d * d;
                n /= 10;
            }
            if (a == 1) {
                return true;
            }
            n = a;
        }
        return false;
    }
};
```

**Solution 3: (Hardcoding the Only Cycle (Advanced))**
```
Runtime: 0 ms, Beats 100.00%
Memory: 7.83 MB, Beats 67.98%
```
```c++
class Solution {
    int getNext(int n) {
        int totalSum = 0;
        while (n > 0) {
            int d = n % 10;
            n = n / 10;
            totalSum += d * d;
        }
        return totalSum;
    }
public:
    bool isHappy(int n) {
        while (n != 1 && n != 4) {
            n = getNext(n);
        }
        return n == 1;
    }
};
```
