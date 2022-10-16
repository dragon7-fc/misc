2443. Sum of Number and Its Reverse

Given a **non-negative** integer `num`, return `true` if `num` can be expressed as the sum of any **non-negative** integer and its reverse, or `false` otherwise.

 

**Example 1:**
```
Input: num = 443
Output: true
Explanation: 172 + 271 = 443 so we return true.
```

**Example 2:**
```
Input: num = 63
Output: false
Explanation: 63 cannot be expressed as the sum of a non-negative integer and its reverse so we return false.
```

**Example 3:**
```
Input: num = 181
Output: true
Explanation: 140 + 041 = 181 so we return true. Note that when a number is reversed, there may be leading zeros.
```

**Constraints:**

* `0 <= num <= 10^5`

# Submissions
---
**Solution 1: (Brute Force)**
```
Runtime: 4247 ms
Memory: 13.9 MB
```
```python
class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        ### make sure to check num as well (for case num=0), so we go from 0 to num+1
        for n in range(0,num+1):
            strN = str(n)		### convert int to string
            strR = strN[::-1]	### reverse the digits
            ### make sure to convert the string back to int.
            if int(strN)+int(strR)==num:
                return True
        return False
```

**Solution 2: (Brute Force)**
```
Runtime: 41 ms
Memory: 5.9 MB
```
```c++
class Solution {
public:
    bool sumOfNumberAndReverse(int num) {
        int n1 = num / 2;
        auto rev = [](int n) {
            int rn = 0;
            for (; n; n /= 10)
                rn = rn * 10 + n % 10;
            return rn;
        };  
        for (int n1 = num / 2; n1 <= num; ++n1)
            if (n1 + rev(n1) == num)
                return true;
        return false;
    }
};
```
