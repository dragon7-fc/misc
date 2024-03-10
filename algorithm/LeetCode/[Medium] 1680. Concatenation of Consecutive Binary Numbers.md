1680. Concatenation of Consecutive Binary Numbers

Given an integer `n`, return the **decimal value** of the binary string formed by concatenating the binary representations of `1` to `n` in order, modulo `10^9 + 7`.

 

**Example 1:**
```
Input: n = 1
Output: 1
Explanation: "1" in binary corresponds to the decimal value 1. 
```

**Example 2:**
```
Input: n = 3
Output: 27
Explanation: In binary, 1, 2, and 3 corresponds to "1", "10", and "11".
After concatenating them, we have "11011", which corresponds to the decimal value 27.
```

**Example 3:**
```
Input: n = 12
Output: 505379714
Explanation: The concatenation results in "1101110010111011110001001101010111100".
The decimal value of that is 118505380540.
After modulo 109 + 7, the result is 505379714.
```

**Constraints:**

* `1 <= n <= 10^5`

# Submissions
---
**Solution 1: (String)**
```
Runtime: 1260 ms
Memory Usage: 24.4 MB
```
```python
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        return int(''.join(bin(i)[2 :] for i in range(1, n + 1)), 2) % (10 ** 9 + 7)
```

**Solution 2: (Math, Bit Manipulation, simulation)**
```
Runtime: 22 ms
Memory Usage: 5.9 MB
```
```c++
class Solution {
public:
    int concatenatedBinary(int n) {
        long ans = 0, mod = 1e9+7, length = 0;
        for (int i = 1; i <= n; ++i) {
            
            if ((i & (i - 1)) == 0) length++;
            ans = ((ans << length) + i) % mod;
        }
        return ans;
    }
};
```
