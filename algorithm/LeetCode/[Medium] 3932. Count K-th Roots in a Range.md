3932. Count K-th Roots in a Range

You are given three integers `l`, `r`, and `k`.

An integer `y` is said to be a perfect kth power if there exists an integer `x` such that `y = x^k`.

Return the number of integers `y` in the range `[l, r]` (inclusive) that are perfect kth powers.

 

**Example 1:**
```
Input: l = 1, r = 9, k = 3

Output: 2

Explanation:

The perfect cubes in the range [1, 9] are:
1 = 13
8 = 23
Hence, the answer is 2.
```

**Example 2:**
```
Input: l = 8, r = 30, k = 2

Output: 3

Explanation:

The perfect squares in the range [8, 30] are:
9 = 32
16 = 42
25 = 52
Hence, the answer is 3.
```

**Constraints:**

* `0 <= l <= r <= 10^9`
* `1 <= k <= 30`

# Submissions
---
**Solution 1: (Math, Brute Force)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 8.92 MB, Beats 22.66%
```
```c++
class Solution {
public:
    int countKthRoots(int l, int r, int k) {
        if (k == 1) {
            return r - l + 1;
        }
        int left = 0, right;
        while (pow(left, k) < l) {
            left += 1;
        }
        right = left;
        while (pow(right, k) <= r) {
            right += 1;
        }
        return right - left;
    } 
};
```
