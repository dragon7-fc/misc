2571. Minimum Operations to Reduce an Integer to 0

You are given a positive integer `n`, you can do the following operation any number of times:

* Add or subtract a power of `2` from `n`.

Return the minimum number of operations to make `n` equal to `0`.

A number `x` is power of `2` if `x == 2^i` where `i >= 0`.

 

**Example 1:**
```
Input: n = 39
Output: 3
Explanation: We can do the following operations:
- Add 2^0 = 1 to n, so now n = 40.
- Subtract 2^3 = 8 from n, so now n = 32.
- Subtract 2^5 = 32 from n, so now n = 0.
It can be shown that 3 is the minimum number of operations we need to make n equal to 0.
```

**Example 2:**
```
Input: n = 54
Output: 3
Explanation: We can do the following operations:
- Add 2^1 = 2 to n, so now n = 56.
- Add 2^3 = 8 to n, so now n = 64.
- Subtract 2^6 = 64 from n, so now n = 0.
So the minimum number of operations is 3.
```

**Constraints:**

* `1 <= n <= 10^5`

# Submissions
---
**Solution 1: (Math)**
```
Runtime: 28 ms
Memory: 13.8 MB
```
```python
class Solution:
    def minOperations(self, n: int) -> int:
        res = 0
        while n != 0:
            cur = 1
            while cur < n:
                cur *= 2
            n = min(cur - n, n - cur // 2)
            res += 1
        return res
```

**Solution 2: (Bit Manipulation)**


Code
Testcase
Testcase
Test Result
All Solutions


[Java/C++/Python] 1-line Solution

lee
365 Days Badge
20813
Feb 19, 2023
C
Python
Java
Intuition
Take a look at the binary of n:

If there is an alone 1, like ..00001,
it takes at leat one operation to remove.
and we can remove it in one operation.
So we do res++ and n >>= 2,
remove two last bits.

If there are multiple 1s, like ..0000111,
we can't remove them in one single operation,
so it takes at least two operation to remove,
For example of ..0000111
we can add 1 and then remove 1000.
So we do n++ and remove the last bit 0.


Explanation
By this stratagy in intuition,
we only need to take care of the the continuous 1 in binary of n.
If it's single 1, res += 1
If it's multiple 1s, res += 2


Complexity
Time O(logn)
Space O(1)


    n = 54

    n           res
    54           0
1 1   0 1 1 0
0 1   1 0 1 1   +1
  1   1 1 0 0
  0   1 1 1 0
      0 1 1 1   +1
      1 0 0 0
      0 1 0 0
      0 0 1 0
      0 0 0 1   +1
      0 0 0 0

```
Runtime: 0 ms, Beats 100.00%
Memory: 7.87 MB, Beats 54.01%
```
```c=+
class Solution {
public:
    int minOperations(int n) {
        int res = 0;
        while (n > 0) {
            if ((n & 3) == 3) {
                n++;
                res++;
            } else {
                res += n & 1;
                n >>= 1;
            }
        }
        return res;
    }
};
```
