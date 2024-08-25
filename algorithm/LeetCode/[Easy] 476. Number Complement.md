476. Number Complement

Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

**Note:** 
* The given integer is guaranteed to fit within the range of a 32-bit signed integer.
* You could assume no leading zero bit in the integer’s binary representation.

**Example 1:**
```
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
```

**Example 2:**
```
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
```

# Submissions
---
**Solution 1: (Bit Manipulation)**
```
Runtime: 28 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def findComplement(self, num: int) -> int:
         return int(''.join(chr(ord('0') + ord('1') - ord(ch)) for ch in bin(num)[2:]),2)
```

**Solution 2: (Bit Manipulation)**
```
Runtime: 0 ms
Memory Usage: 5.4 MB
```
```c


int findComplement(int num){
    int temp = num, c = 0;
    while(temp>0)
    {
        c = (c<<1)|1;
        temp >>= 1;
    }  
    return num ^ c;
}
```

**Solution 2: (Bit Manipulation)**
```
Runtime: 0 ms
Memory: 7.53 MB
```
```c++
class Solution {
public:
    int findComplement(int num) {
        int b = 0;
        while (b < 31 && (1<<b) <= num) {
            num ^= (1<<b);
            b += 1;
        }
        return num;
    }
};
```
