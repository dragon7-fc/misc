3976. Maximum Subarray Sum After Multiplier

You are given an integer array `nums` and a positive integer `k`.

You must choose **exactly** one **subarray** of `nums` and perform **exactly** one of the following operations:

* Multiply each number in the chosen subarray by `k`.
* Divide each number in the chosen subarray by `k`.
    * When dividing a positive number by `k`, use the **floor** value of the division result.
    * When dividing a negative number by `k`, use the **ceiling** value of the division result.

Return the **maximum** possible sum of a **non-empty** subarray in the resulting array.

Note that the subarray chosen for the operation and the subarray chosen for the sum may be **different**.

 

**Example 1:**
```
Input: nums = [1,-2,3,4,-5], k = 2

Output: 14

Explanation:

Multiply each number in the subarray [3, 4] by 2.
This results in nums = [1, -2, 6, 8, -5].
The subarray with the largest sum is [6, 8], so the output is 6 + 8 = 14.
```

**Example 2:**
```
Input: nums = [-5,-4,-3], k = 2

Output: -1

Explanation:

Divide each number in the subarray [-3] by 2.
This results in nums = [-5, -4, -1].
The subarray with the largest sum is [-1], so the output is -1.
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `-10^5 <= nums[i] <= 10^5`
* `1 <= k <= 10^5`

# Submissions
---
**Solution 1: (DP Bottom-Up, kadane, can't greedy because may choose useless subarray to perform operation and sum over the other)**

Intuition
DP, the states represent the following scenarios:

dp0: The subarray has not undergone any operation .
dpb: The subarray is currently being multiplied by k.
dpc: The subarray is currently being divided by k.
dp1: The subarray has finished its operations and returned to standard elements.

Explanation
We iterate each a in array A:
We define b as a * k,
and c as a / k.
and update our dynamic programming states sequentially.

During the iteration,
we transition between these states
and update the maximum subarray sum accordingly.

Complexity
Time O(n)
Space O(1)

---------------------------------------------
    nums = [ 1,-2, 3, 4, -5], k = 2
a            1 -2  3  4  -5
b            2 -4  6  8 -10
c            0 -1  1  2  -2
dp1      0   1  0  3 10   9
dpb      0   2 -2  6 14   4
dpc      0   0  0  1  5   5
dp0      0   1 -1  3  7   2
res      ~   2     3 14
                     ans 

```
Runtime: 26 ms, Beats 87.58%
Memory: 146.83 MB, Beats 69.13%
```
```c++
class Solution {
public:
    long long maxSubarraySum(vector<int>& nums, int k) {
        long long res = -1e9, dp0 = 0, dpb = 0, dpc = 0, dp1 = 0;
        for (long long a: nums) {
            long long b = a * k, c = a / k;
            dp1 = max({dp1 + a, dpb + a, dpc + a}); // After modification completed
            dpb = max({dp0 + b, dpb + b, b});       // Inside Multiplication
            dpc = max({dp0 + c, dpc + c, c});       // Inside Division
            dp0 = max(dp0 + a, a);                  // No modification
            res = max({res, dp0, dpb, dpc, dp1});
        }
        return res;
    }
};
```
