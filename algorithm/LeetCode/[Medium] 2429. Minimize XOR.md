2429. Minimize XOR

Given two positive integers `num1` and `num2`, find the integer `x` such that:

* `x` has the same number of set bits as `num2`, and
* The value `x XOR num1` is **minimal**.

Note that `XOR` is the bitwise XOR operation.

Return the integer `x`. The test cases are generated such that `x` is **uniquely determined**.

The number of **set bits** of an integer is the number of `1`'s in its binary representation.

 

**Example 1:**
```
Input: num1 = 3, num2 = 5
Output: 3
Explanation:
The binary representations of num1 and num2 are 0011 and 0101, respectively.
The integer 3 has the same number of set bits as num2, and the value 3 XOR 3 = 0 is minimal.
```

**Example 2:**
```
Input: num1 = 1, num2 = 12
Output: 3
Explanation:
The binary representations of num1 and num2 are 0001 and 1100, respectively.
The integer 3 has the same number of set bits as num2, and the value 3 XOR 1 = 2 is minimal.
```

**Constraints:**

* `1 <= num1, num2 <= 10^9`

# Submissions
---
**Solution 1: (Bit Manipulation)**
```
Runtime: 35 ms
Memory: 13.8 MB
```
```python
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bits = bin(num2)[2:].count('1')
        r = bin(num1)[2:].count('1')
        ans = 0
        i = 31
        while bits > 0 and r > 0 and i >= 0:
            if num1&(1<<i):
                ans |= 1<<i;
                r -= 1
                bits -= 1
            i -= 1
        i = 0
        while bits > 0:
            if ans&(1<<i) == 0:
                ans |= 1<<i
                bits -= 1
            i += 1
        return ans
```

**Solution 2: (Bit Manipulation)**
```
Runtime: 0 ms
Memory: 8.11 MB
```
```c++
class Solution {
public:
    int minimizeXor(int num1, int num2) {
        int cnt = 0, k = 0, cur = num2, ans;
        while (cur) {
            cnt += cur&1;
            cur >>= 1;
        }
        cur = num1;
        while (cur) {
            k += cur&1;
            cur >>= 1;
        }
        ans = num1;
        cur = 1;
        while (k > cnt) {
            if (ans&cur) {
                k -= 1;
                ans ^= cur;
            }
            cur <<= 1;
        }
        cur = 1;
        while (k < cnt) {
            if ((ans&cur) == 0) {
                ans ^= cur;
                k += 1;
            }
            cur <<= 1;
        }
        return ans;
    }
};
```

**Solution 3: (Building the Answer)**
```
Runtime: 0 ms
Memory: 7.96 MB
```
```c++
class Solution {
    // Helper function to check if the given bit position in x is set (1).
    bool isSet(int x, int bit) { return x & (1 << bit); }

    // Helper function to set the given bit position in x to 1.
    void setBit(int &x, int bit) { x |= (1 << bit); }
public:
    int minimizeXor(int num1, int num2) {
         int result = 0;

        int targetSetBitsCount = __builtin_popcount(num2);
        int setBitsCount = 0;
        int currentBit = 31;  // Start from the most significant bit.

        // While x has fewer set bits than num2
        while (setBitsCount < targetSetBitsCount) {
            // If the current bit of num1 is set or we must set all remaining
            // bits in result
            if (isSet(num1, currentBit) ||
                (targetSetBitsCount - setBitsCount > currentBit)) {
                setBit(result, currentBit);
                setBitsCount++;
            }
            currentBit--;  // Move to the next bit.
        }

        return result;
    }
};

```
