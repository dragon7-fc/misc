3811. Number of Alternating XOR Partitions

You are given an integer array `nums` and two distinct integers `target1` and `target2`.

A partition of `nums` splits it into one or more contiguous, non-empty blocks that cover the entire array without overlap.

A partition is valid if the bitwise XOR of elements in its blocks alternates between `target1` and `target2`, starting with `target1`.

Formally, for blocks `b1`, `b2`, …:

* `XOR(b1) = target1`
* `XOR(b2) = target2` (if it exists)
* `XOR(b3) = target1`, and so on.

Return the number of valid partitions of nums, modulo `10^9 + 7`.

**Note**: A single block is valid if its **XOR** equals `target1`.

 

**Example 1:**
```
Input: nums = [2,3,1,4], target1 = 1, target2 = 5

Output: 1

Explanation:

The XOR of [2, 3] is 1, which matches target1.
The XOR of the remaining block [1, 4] is 5, which matches target2.
This is the only valid alternating partition, so the answer is 1.
```

**Example 2:**
```
Input: nums = [1,0,0], target1 = 1, target2 = 0

Output: 3

Explanation:

The XOR of [1, 0, 0] is 1, which matches target1.
The XOR of [1] and [0, 0] are 1 and 0, matching target1 and target2.
The XOR of [1, 0] and [0] are 1 and 0, matching target1 and target2.
Thus, the answer is 3.
```

**Example 3:**
```
Input: nums = [7], target1 = 1, target2 = 7

Output: 0

Explanation:

The XOR of [7] is 7, which does not match target1, so no valid partition exists.
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `0 <= nums[i], target1, target2 <= 10^5`
* `target1 != target2`

# Submissions
---
**Solution 1: (DP Bottom-Up, 2 DP transaction)**

    nums = [ 2, 3, 1, 4], target1 = 1, target2 = 5
    x    0   2  1  0  4
    d1       3  0  1  5
    d2       7  4  5  1
    a1       0  0  0  1 <
    a2       0  1  0  0 <
dp1:
0        1
2            0
1               0
dp2:
0                  0
2            0
1               1

    nums = [ 1, 0, 0], target1 = 1, target2 = 0
    x    0   1  1  1
    d1       0  0  0
    d2       1  1  1
    a1       0  1  2 <
    a2       1  1  1 <
dp1:
0        1
1            0  1  
dp2:
1            1  2   
```
Runtime: 55 ms, Beats 75.00%
Memory: 139.42 MB, Beats 41.67%
```
```c++
class Solution {
public:
    int alternatingXOR(vector<int>& nums, int target1, int target2) {
        int n = nums.size(), i, x = 0, d1, d2, a1, a2, MOD = 1e9 + 7;
        unordered_map<int, long long> dp1, dp2;
        dp1[0] = 1;
        for (auto &num: nums) {
            x ^= num;
            d1 = x ^ target1;
            d2 = x ^ target2;
            a1 = dp2[d2];
            a2 = dp1[d1];
            dp1[x] = (dp1[x] + a1) % MOD;
            dp2[x] = (dp2[x] + a2) % MOD;
        }
        return (a1 + a2) % MOD;
    }
};
```
