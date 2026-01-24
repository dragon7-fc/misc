3228. Maximum Number of Operations to Move Ones to the End

You are given a **binary string** `s`.

You can perform the following operation on the string **any** number of times:

* Choose any index `i` from the string where `i + 1 < s.length` such that `s[i] == '1'` and `s[i + 1] == '0'`.
* Move the character `s[i]` to the **right** until it reaches the end of the string or another `'1'`. For example, for `s = "010010"`, if we choose `i = 1`, the resulting string will be `s = "000110"`.

Return the **maximum** number of operations that you can perform.

 

**Example 1:**
```
Input: s = "1001101"

Output: 4

Explanation:

We can perform the following operations:

Choose index i = 0. The resulting string is s = "0011101".
Choose index i = 4. The resulting string is s = "0011011".
Choose index i = 3. The resulting string is s = "0010111".
Choose index i = 2. The resulting string is s = "0001111".
```

**Example 2:**
```
Input: s = "00111"

Output: 0
```
 

**Constraints:**

* `1 <= s.length <= 10^5`
* `s[i]` is either `'0'` or `'1'`.

# Submissions
---
**Solution 1: (Sliding Window)**
```
Runtime: 20 ms
Memory: 14.30 MB
```
```c++
class Solution {
public:
    int maxOperations(string s) {
        int n = s.size(), i = 0, cnt = 0, ans = 0;
        while (i < n) {
            while (i < n && s[i] == '1') {
                cnt += 1;
                i += 1;
            }
            if (i == n) {
                break;
            }
            while (i < n && s[i] == '0') {
                i += 1;
            }
            ans += cnt;
        }
        return ans;
    }
};
```

**Solution 2: (Greedy + Counting)**
```
Runtime: 4 ms, Beats 71.38%
Memory: 15.93 MB, Beats 26.09%
```
```c++
class Solution {
public:
    int maxOperations(string s) {
        int countOne = 0;
        int ans = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '0') {
                while ((i + 1) < s.length() && s[i + 1] == '0') {
                    i++;
                }
                ans += countOne;
            } else {
                countOne++;
            }
        }
        return ans;
    }
};
```

**Solution 3: (Greedy + Counting)**

          0  1  2  3  4  5  6
    s = " 1  0  0  1  1  0  1"
one       1        2  3     4
z         f  t     f  f  t
ans               +1       +3
```
Runtime: 7 ms, Beats 43.12%
Memory: 15.76 MB, Beats 75.00%
```
```c++
class Solution {
public:
    int maxOperations(string s) {
        int n = s.size(), i, one = 0, ans = 0;
        bool z = false;
        for (i = 0; i < n; i ++) {
            if (s[i] == '1') {
                if (z) {
                    ans += one;
                }
                one += 1;
                z = false;
            } else {
                z = true;
            }
            if (i == n - 1 && z) {
                ans += one;
            }
        }
        return ans;
    }
};
```
