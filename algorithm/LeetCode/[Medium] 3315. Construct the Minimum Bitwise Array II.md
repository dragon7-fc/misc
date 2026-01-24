3315. Construct the Minimum Bitwise Array II

You are given an array `nums` consisting of `n` **prime** integers.

You need to construct an array ans of length `n`, such that, for each index `i`, the bitwise `OR` of `ans[i]` and `ans[i] + 1` is equal to `nums[i]`, i.e. `ans[i] OR (ans[i] + 1) == nums[i]`.

Additionally, you must **minimize** each value of `ans[i]` in the resulting array.

If it is not possible to find such a value for ans[i] that satisfies the condition, then set `ans[i] = -1`.

 

**Example 1:**
```
Input: nums = [2,3,5,7]

Output: [-1,1,4,3]

Explanation:

For i = 0, as there is no value for ans[0] that satisfies ans[0] OR (ans[0] + 1) = 2, so ans[0] = -1.
For i = 1, the smallest ans[1] that satisfies ans[1] OR (ans[1] + 1) = 3 is 1, because 1 OR (1 + 1) = 3.
For i = 2, the smallest ans[2] that satisfies ans[2] OR (ans[2] + 1) = 5 is 4, because 4 OR (4 + 1) = 5.
For i = 3, the smallest ans[3] that satisfies ans[3] OR (ans[3] + 1) = 7 is 3, because 3 OR (3 + 1) = 7.
```

**Example 2:**
```
Input: nums = [11,13,31]

Output: [9,12,15]

Explanation:

For i = 0, the smallest ans[0] that satisfies ans[0] OR (ans[0] + 1) = 11 is 9, because 9 OR (9 + 1) = 11.
For i = 1, the smallest ans[1] that satisfies ans[1] OR (ans[1] + 1) = 13 is 12, because 12 OR (12 + 1) = 13.
For i = 2, the smallest ans[2] that satisfies ans[2] OR (ans[2] + 1) = 31 is 15, because 15 OR (15 + 1) = 31.
```

**Constraints:**

* `1 <= nums.length <= 100`
* `2 <= nums[i] <= 10^9`
* `nums[i]` is a prime number.

# Submissions
---
**Solution 1: (Bit Manipulation)**

    01  100  011  1001  1100   1111
    10  101  100  1010  1101  10000
    11  101  111  1011  1101  11111

             110
             101

```
Runtime: 7 ms
Memory: 27.31 MB
```
```c++
class Solution {
public:
    vector<int> minBitwiseArray(vector<int>& nums) {
        int n = nums.size(), k, cur;
        vector<int> ans(n, INT_MAX);
        for (int i = 0; i < n; i ++) {
            k = 0;
            while ((1<<k) <= nums[i]) {
                if (nums[i]&(1<<k)) {
                    cur = nums[i]^(1<<k);
                    if (((cur+1)|cur) == nums[i]) {
                        ans[i] = min(ans[i], cur);
                    }
                }
                k += 1;
            }
            if (ans[i] == INT_MAX) {
                ans[i] = -1;
            }
        }
        return ans;
    }
};
```

**Solution 2: (Bit Manipulation, try unset a bit before first zero for even number)**

ans[i] OR (ans[i] + 1) == nums[i]
-> unset a bit beofre first zero

    nums = [   2,   3,   5,   7]
                        v
                   11  101  111
                   x     x  x
    ans       -1    1  100   11


     nums = [11,  13,   31]
            v     v
           1011 1101 11111
             x     x x
     ans   1001 1100  1111

```
Runtime: 0 ms, Beats 100.00%
Memory: 28.27 MB, Beats 61.17%
```
```c++
class Solution {
public:
    vector<int> minBitwiseArray(vector<int>& nums) {
        int n = nums.size(), a;
        vector<int> ans(n, -1);
        for (int i = 0; i < n; i ++) {
            if (nums[i] % 2) {
                a = 1;
                while (a & nums[i]) {
                    ans[i] = nums[i] - a;
                    a <<= 1;
                }
            }
        }
        return ans;
    }
};
```
