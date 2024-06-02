3094. Guess the Number Using Bitwise Questions II

There is a number `n` between `0` and `2^30 - 1` (both inclusive) that you have to find.

There is a pre-defined API `int commonBits(int num)` that helps you with your mission. But here is the challenge, every time you call this function, n changes in some way. But keep in mind, that you have to find the initial value of `n`.

`commonBits(int num)` acts as follows:

* Calculate `count` which is the number of bits where both `n` and `num` have the same value in that position of their binary representation.
* `n = n XOR num`
* Return `count`.

Return the number `n`.

**Note**: In this world, all numbers are between `0` and `2^30 - 1` (both inclusive), thus for counting common bits, we see only the first 30 bits of those numbers.

 

**Constraints:**

* `0 <= n <= 2^30 - 1`
* `0 <= num <= 2^30 - 1`
* If you ask for some num out of the given range, the output wouldn't be reliable.

# Submissions
---
**Solution 1: (Bit Manipulation)**

We first call commonBits with 0 to count the number of zeros.

Then we try each bit (1, 2, 4, 8, ...). If that bit is in the number, commonBits result will be higher than the nubmer of zeros.

Note that we need to increase zeros when we find a matching bit.

This is because that bit will flip from 1 to 0 after the operation.

Similarly, we need to decrease zeros when there is a missmatch.

```
Runtime: 4 ms
Memory: 7.46 MB
```
```c++
/** 
 * Definition of commonBits API.
 * int commonBits(int num);
 */

class Solution {
public:
    int findNumber() {
        int res = 0, zeros = commonBits(0);
        for (int i = 1; i < (1 << 30); i <<= 1) {
            if (commonBits(i) > zeros) {
                res += i;
                ++zeros;
            }
            else
                --zeros;
        }
        return res;
    }
};
```
