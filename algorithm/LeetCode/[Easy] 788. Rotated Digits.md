788. Rotated Digits

X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.

Now given a positive number `N`, how many numbers `X` from `1` to `N` are good?

**Example:**
```
Input: 10
Output: 4
Explanation: 
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
```

**Note:**

* `N`  will be in range `[1, 10000]`.

# Submissions
---
**Solution 1: (Set)**
```
Runtime: 100 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def rotatedDigits(self, N: int) -> int:
        valid = {'2','5','6','9'}
        invalid = {'3','4','7'}
        result = 0
        for num in range(2, N+1):
            s = set(str(num))
            if s & invalid:
                continue
            elif s & valid:
                result += 1
        return result
```

**Solution 2: (Brute Force)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 7.85 MB, Beats 66.14%
```
```c++
class Solution {
public:
    int rotatedDigits(int n) {
        int a, b, e, d, nd, ans = 0;
        bool flag;
        vector<int> mp = {0,1,5,-1,-1,2,9,-1,8,6};
        for (a = 1; a <= n; a ++) {
            b = 0;
            e = 1;
            flag = true;
            while (e <= a) {
                d = (a / e) % 10;
                nd = mp[d];
                if (nd < 0) {
                    flag = false;
                    break;
                }
                b += nd * e;
                e *= 10;
            }
            if (flag && b != a) {
                ans += 1;
            }
        }
        return ans;
    }
};
```
