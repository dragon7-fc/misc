1318. Minimum Flips to Make a OR b Equal to c

Given 3 positives numbers `a`, `b` and `c`. Return the minimum flips required in some bits of `a` and `b` to make ( `a OR b == c` ). (bitwise OR operation).
Flip operation consists of change any single bit `1` to `0` or change the bit `0` to `1` in their binary representation.

 

**Example 1:**

![1318_sample_3_1676.png](img/1318_sample_3_1676.png)
```
Input: a = 2, b = 6, c = 5
Output: 3
Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)
```

**Example 2:**
```
Input: a = 4, b = 2, c = 7
Output: 1
```

**Example 3:**
```
Input: a = 1, b = 2, c = 3
Output: 0
```

**Constraints:**

* `1 <= a <= 10^9`
* `1 <= b <= 10^9`
* `1 <= c <= 10^9`

# Submissions
---
**Solution 1: (Bit Manipulation)**
```
Runtime: 24 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        while(a or b or c):
            bit_a, bit_b, bit_c=a&1, b&1, c&1
            if (bit_a|bit_b) != bit_c:
                if bit_a == 1 and bit_b == 1:
                    count += 2
                else:
                    count += 1
            a >>= 1
            b >>= 1
            c >>= 1
            
        return count
```

**Solution 2: (Bit Manipulation)**
```
Runtime: 0 ms
Memory: 5.9 MB
```
```c++
class Solution {
public:
    int minFlips(int a, int b, int c) {
        int cur, t, ans = 0;
        while (a || b || c) {
            if ((c&1) == 0) {
                ans += ((a&1) + (b&1));
            } else {
                ans += (((a&1) | (b&1)) == 0);
            }
            a >>= 1;
            b >>= 1;
            c >>= 1;
        }
        return ans;
    }
};
```
