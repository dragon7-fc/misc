2802. Find The K-th Lucky Number

We know that `4` and `7` are lucky digits. Also, a number is called lucky if it contains only lucky digits.

You are given an integer `k`, return the `k`th lucky number represented as a string.

 

**Example 1:**
```
Input: k = 4
Output: "47"
Explanation: The first lucky number is 4, the second one is 7, the third one is 44 and the fourth one is 47.
```

**Example 2:**
```
Input: k = 10
Output: "477"
Explanation: Here are lucky numbers sorted in increasing order:
4, 7, 44, 47, 74, 77, 444, 447, 474, 477. So the 10th lucky number is 477.
```

**Example 3:**
```
Input: k = 1000
Output: "777747447"
Explanation: It can be shown that the 1000th lucky number is 777747447.
```

**Constraints:**

* `1 <= k <= 10^9`

# Submissions
---
**Solution 1: (Math)**
```
Runtime: 15 ms
Memory: 10.17 MB
```
```c++
class Solution {
public:
    string kthLuckyNumber(int k) {
        int c = 1, a = 0, d;
        while (a < k) {
            c <<= 1;
            a += c;
        }
        a -= c;
        c >>= 1;
        d = k - a;
        string ans;
        while (c) {
            if (d > c) {
                d -= c;
                ans += "7";
            } else {
                ans += "4";
            }
            c >>= 1;
        }
        return ans;
    }
};
```

**Solution 2: (Math)**
```
Runtime: 20 ms
Memory: 11.75 MB
```
```c++
class Solution {
public:
    string kthLuckyNumber(int k) {
        string res;
        k += 1;
        for (k; k != 1; k /= 2) 
            res = (k&1 ? '7' : '4') + res;
        return res;
    }
};
```
