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

a = 2 = 0b   1 0
b = 3 = 0b   1 1
-----------------
carry   0b   1 0  (a & b)
a       0b   0 1  (a ^ b) = sum
b       0b 1 0 0  (carry << 1)
-----------------
carry   0b 0 0 0
a       0b 1 0 1
b       0b 0 0 0

```
Runtime: 0 ms, Beats 100.00%
Memory: 7.91 MB, Beats 1.96%
```
```c++
class Solution {
public:
    int getSum(int a, int b) {
        int carry;
        while (b){
            carry = a & b;
            a = a ^ b;
            b = carry << 1;
        }
        return a;
    }
};
```
