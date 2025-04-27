3215. Count Triplets with Even XOR Set Bits II

Given three integer arrays `a`, `b`, and `c`, return the number of triplets `(a[i], b[j], c[k])`, such that the bitwise `XOR` between the elements of each triplet has an **even** number of **set bits**.
 

**Example 1:**
```
Input: a = [1], b = [2], c = [3]

Output: 1

Explanation:

The only triplet is (a[0], b[0], c[0]) and their XOR is: 1 XOR 2 XOR 3 = 002.
```

**Example 2:**
```
Input: a = [1,1], b = [2,3], c = [1,5]

Output: 4

Explanation:

Consider these four triplets:

(a[0], b[1], c[0]): 1 XOR 3 XOR 1 = 0112
(a[1], b[1], c[0]): 1 XOR 3 XOR 1 = 0112
(a[0], b[0], c[1]): 1 XOR 2 XOR 5 = 1102
(a[1], b[0], c[1]): 1 XOR 2 XOR 5 = 1102
```

**Constraints:**

* `1 <= a.length, b.length, c.length <= 10^5`
* `0 <= a[i], b[i], c[i] <= 10^9`

# Submissions
---
**Solution 1: (Bit Manipulations)**

        2 even -> even
        1 even -> odd
        2 odd -> even

```
Runtime: 17 ms, Beats -%
Memory: 154.55 MB, Beats 75.00%
```
```c++
class Solution {
public:
    long long tripletCount(vector<int>& a, vector<int>& b, vector<int>& c) {
        long long cnta[2] = {0}, cntb[2] = {0}, cntc[2] = {0}, cnt, ans = 0;
        for (auto num: a) {
            cnt = 0;
            while (num) {
                cnt += num&1;
                num >>= 1;
            }
            cnta[cnt%2] += 1;
        }
        for (auto num: b) {
            cnt = 0;
            while (num) {
                cnt += num&1;
                num >>= 1;
            }
            cntb[cnt%2] += 1;
        }
        for (auto num: c) {
            cnt = 0;
            while (num) {
                cnt += num&1;
                num >>= 1;
            }
            cntc[cnt%2] += 1;
        }
        ans += cnta[0] * cntb[0] * cntc[0];
        ans += cnta[1] * cntb[1] * cntc[0];
        ans += cnta[0] * cntb[1] * cntc[1];
        ans += cnta[1] * cntb[0] * cntc[1];
        return ans;
    }
};
```
