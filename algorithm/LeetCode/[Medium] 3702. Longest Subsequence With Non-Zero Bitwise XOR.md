3702. Longest Subsequence With Non-Zero Bitwise XOR

You are given an integer array `nums`.

Return the length of the **longest subsequence** in `nums` whose bitwise **XOR** is **non-zero**. If no such **subsequence** exists, return 0.

 

**Example 1:**
```
Input: nums = [1,2,3]

Output: 2

Explanation:

One longest subsequence is [2, 3]. The bitwise XOR is computed as 2 XOR 3 = 1, which is non-zero.
```

**Example 2:**
```
Input: nums = [2,3,4]

Output: 3

Explanation:

The longest subsequence is [2, 3, 4]. The bitwise XOR is computed as 2 XOR 3 XOR 4 = 5, which is non-zero.
```
 

**Constraints:**

* `1 <= nums.length <= 10^5`
* `0 <= nums[i] <= 10^9`

# Submissions
---
**Solution 1: (Case Study, all xor != 0 then n else n - 1)**

can't use dp
-> dp[value] = length
     ^^^^^^^
      2^n

```
Runtime: 3 ms, Beats 43.09%
Memory: 171.15 MB, Beats 88.49%
```
```c++
class Solution {
public:
    int longestSubsequence(vector<int>& nums) {
        int n = nums.size();
        int a = 0;
        bool all_zero = true;
        for (auto &num: nums) {
            a ^= num;
            if (num) {
                all_zero = false;
            }
        }
        if (a) {
            return n;
        }
        return all_zero ? 0 : n - 1;
    }
};
```
