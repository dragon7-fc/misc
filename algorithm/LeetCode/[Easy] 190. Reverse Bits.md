190. Reverse Bits

Reverse bits of a given 32 bits signed integer.

 

**Example 1:**
```
Input: n = 43261596

Output: 964176192

Explanation:

Integer	Binary
43261596	00000010100101000001111010011100
964176192	00111001011110000010100101000000
```

**Example 2:**
```
Input: n = 2147483644

Output: 1073741822

Explanation:

Integer	Binary
2147483644	01111111111111111111111111111100
1073741822	00111111111111111111111111111110
```

**Constraints:**

* `0 <= n <= 2^31 - 2`
* `n is even`.
 

**Follow up**: If this function is called many times, how would you optimize it?

# Submissions
---
**Solution 1: (String)**
```
Runtime: 24 ms
Memory Usage: N/A
```
```python
class Solution:
    def reverseBits(self, n):
        return int('{:032b}'.format(n)[::-1], 2)
```

**Solution 2: (Bit Manipulations)**
```
Runtime: 8 ms
Memory Usage: 6.2 MB
```
```c++
class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t res = 0;
        for (int i = 0; i < 31; i++) {
            res = (n % 2) + res << 1;
            n >>= 1;
        }
        return res + n % 2;
    }
};
```

**Solution 2: (Math)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 8.20 MB, Beats 73.18%
```
```c++
class Solution {
public:
    int reverseBits(int n) {
        int i = 31, j = 0, ans = 0;
        while (i >= 0) {
            if ((1 << i) & n) {
                ans += (1 << j);
            }
            j += 1;
            i -= 1;
        }
        return ans;
    }
};
```
