371. Sum of Two Integers

Calculate the sum of two integers a and b, but you are **not allowed** to use the operator `+` and `-`.

**Example 1:**
```
Input: a = 1, b = 2
Output: 3
```

**Example 2:**
```
Input: a = -2, b = 3
Output: 1
```

# Submissions
---
**Solution 1: (Array)**
```
Runtime: 28 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        return sum([a, b])
```

**Solution 2: (Math, log(a*b) = loga + logb)**
```
Runtime: 40 ms
Memory Usage: 14.2 MB
```
```python
class Solution:
    def getSum(self, a: int, b: int) -> int:
        return int(math.log2(pow(2,a)*pow(2,b)))
```

**Solution 3: (Bit Manipulation**
```
Runtime: 0 ms
Memory: 7.17 MB
```
```c++
class Solution {
public:
    int getSum(int a, int b) {
        while(b!=0){
            int carry = a&b;
            a = a^b;
            b = carry<<1;
        }
        return a;
    }
};
```
