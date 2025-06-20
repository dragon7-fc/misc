1432. Max Difference You Can Get From Changing an Integer

You are given an integer `num`. You will apply the following steps exactly two times:

* Pick a digit `x` (`0 <= x <= 9`).
* Pick another digit `y` (`0 <= y <= 9`). The digit `y` can be equal to `x`.
* Replace all the occurrences of `x` in the decimal representation of `num` by `y`.
* The new integer cannot have any leading zeros, also the new integer cannot be `0`.

Let `a` and `b` be the results of applying the operations to num the first and second times, respectively.

Return the max difference between `a` and `b`.

 

**Example 1:**
```
Input: num = 555
Output: 888
Explanation: The first time pick x = 5 and y = 9 and store the new integer in a.
The second time pick x = 5 and y = 1 and store the new integer in b.
We have now a = 999 and b = 111 and max difference = 888
```

**Example 2:**
```
Input: num = 9
Output: 8
Explanation: The first time pick x = 9 and y = 9 and store the new integer in a.
The second time pick x = 9 and y = 1 and store the new integer in b.
We have now a = 9 and b = 1 and max difference = 8
```

**Example 3:**
```
Input: num = 123456
Output: 820000
```

**Example 4:**
```
Input: num = 10000
Output: 80000
```

**Example 5:**
```
Input: num = 9288
Output: 8700
```

**Constraints:**

* `1 <= num <= 10^8`


# Submissions
---
**Solution 1: (Brute Force)**
```
Runtime: 48 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def maxDiff(self, num: int) -> int:
        num = str(num)
        maxNum, minNum = float('-inf'), float('inf')
        for i in '0123456789':
            for j in '0123456789':
                nextNum = num.replace(i, j)
                if nextNum[0] == '0' or int(nextNum) == 0:
                    continue
                maxNum = max(maxNum, int(nextNum))    
                minNum = min(minNum, int(nextNum))    
        return maxNum - minNum
```

**Solution 2: (Greedy)**

**Algorithm**

* For higher end, find the first non-9 digit and convert all such digits to 9.
* For lower end, if the first digit is not 1, then convert it to 1. Otherwise, find the first non-0 or 1 digit, and convert it to 0.

```
Runtime: 28 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def maxDiff(self, num: int) -> int:
        num = str(num)
        
        i = next((i for i in range(len(num)) if num[i] != "9"), -1) #first non-9 digit
        hi = int(num.replace(num[i], "9"))
        
        if num[0] != "1": lo = int(num.replace(num[0], "1"))
        else: 
            i = next((i for i in range(len(num)) if num[i] not in "01"), -1)
            lo = int(num.replace(num[i], "0") if i > 0 else num)
            
        return hi - lo
```

**Solution 3: (String, Greedy)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 8.30 MB, Beats 43.13%
```
```c++
class Solution {
    string repl(string &s, char rs, char rt) {
        string rst;
        for (auto c: s) {
            if (c == rs) {
                rst += rt;
            } else {
                rst += c;
            }
        }
        return rst;
    }
public:
    int maxDiff(int num) {
        string s = to_string(num), sa, sb;
        char ca = 0, cb = 0;
        int i, a, b;
        for (i = 0; i < s.length(); i ++) {
            if (s[i] != '9' && ca == 0) {
                ca = s[i];
            }
            if (s[i] > '1' && cb == 0) {
                cb = s[i];
            }
            if (ca != 0 && cb != 0) {
                break;
            }
        }
        sa = repl(s, ca, '9');
        if (s[0] != '1') {
            sb = repl(s, cb, '1');
        } else {
            if (cb) {
                sb = repl(s, cb, '0');
            } else {
                sb = s;
            }
        }
        a = stoi(sa);
        b = stoi(sb);
        return a - b;
    }
};
```
