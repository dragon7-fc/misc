3247. Number of Subsequences with Odd Sum

Given an array `nums`, return the number of **subsequences** with an odd sum of elements.

Since the answer may be very large, return it **modulo** `10^9 + 7`.

 


**Example 1:**
```
Input: nums = [1,1,1]

Output: 4

Explanation:

The odd-sum subsequences are: [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1].
```

**Example 2:**
```
Input: nums = [1,2,2]

Output: 4

Explanation:

The odd-sum subsequences are: [1, 2, 2], [1, 2, 2], [1, 2, 2], [1, 2, 2].
```
 

**Constraints:**

* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^9`

# Submissions
---
**Solution 1: (DP Bottom-Up)**

    1  1  2  1
o   1  2  4 
e      1  3
    ^
       ^
    ^     ^
       ^^^^
             ^
    ^^^^     ^
          ^^^^
    ^^^^^^^^^^

    1  1  1
o   1  2  4
e      1  3
cnt 1
ans
    ^  
       ^
          ^
    ^^^^^^^

    1  2  2
o   1  2  4
e      1
cnt 1
ans 1
    ^
    ^^^^
    ^     ^
    ^^^^^^^

```
Runtime: 3 ms, Beats 90.00%
Memory: 110.86 MB, Beats 85.00%
```
```c++
class Solution {
public:
    int subsequenceCount(vector<int>& nums) {
        int MOD = 1e9 + 7;
        long long o = 0, e = 0, po, pe, ans = 0;
        for (auto num: nums) {
            if (num%2) {
                po = o;
                o += 1 + e;
                e += po;
            } else {
                po = o;
                o *= 2;
                e = 2*e + 1;
            }
            o %= MOD;
            e %= MOD;
        }
        return o;
    }
};
```
