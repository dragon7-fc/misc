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
Memory: 5.8 MB
```
```c++
class Solution {
    int countSetBits(int n)
    {
        int count = 0;
        while (n)
        {
            n &= (n - 1);
            count++;
        }
        return count;
    }
public:
    int minimizeXor(int num1, int num2) {
        int cnt1 = countSetBits(num1), cnt2 = countSetBits(num2);
        if (cnt1 == cnt2)
        {
            return num1;
        }
        else if (cnt1 > cnt2)
        {
            int diff = cnt1 - cnt2;
            for (int bit = 0; bit < 31; bit++)
            {
                if (diff == 0)
                    break;
                else if ((num1 & (1 << bit)) != 0)
                {
                    diff--;
                    num1 ^= (1 << bit);
                }
            }
            return num1;
        }
        else
        {
            int diff = cnt2 - cnt1;
            for (int bit = 0; bit < 31; bit++)
            {
                if (diff == 0)
                    break;
                else if ((num1 & (1 << bit)) == 0)
                {
                    diff--;
                    num1 |= (1 << bit);
                }
            }
            return num1;
        }
    }
};
```
