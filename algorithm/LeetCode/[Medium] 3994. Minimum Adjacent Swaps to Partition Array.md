3994. Minimum Adjacent Swaps to Partition Array

You are given an integer array `nums` and two integers `a` and `b` such that `a < b`.

An array is called **good** if it can be split into three contiguous parts, in this order, such that:

* Every element in the first part is **less than** `a`.
* Every element in the second part is in the range `[a, b]` inclusive.
* Every element in the third part is **greater than** `b`.

Any of the three parts may be empty.

In one **adjacent** swap, you may swap two neighboring elements of `nums`.

Return the **minimum** number of adjacent swaps required to make nums good. Since the answer may be very large, return it modulo `10^9 + 7`.

 

**Example 1:**
```
Input: nums = [1,3,2,4,5,6], a = 3, b = 4

Output: 1

Explanation:

Swap nums[1] and nums[2]. The array becomes [1, 2, 3, 4, 5, 6].
This array is good because it can be split into [1, 2], [3, 4], and [5, 6].
```

**Example 2:**
```
Input: nums = [9,7,5,3], a = 4, b = 8

Output: 5

Explanation:

One sequence of optimal swaps is as follows:

Swap nums[2] and nums[3]. The array becomes [9, 7, 3, 5].
Swap nums[1] and nums[2]. The array becomes [9, 3, 7, 5].
Swap nums[0] and nums[1]. The array becomes [3, 9, 7, 5].
Swap nums[1] and nums[2]. The array becomes [3, 7, 9, 5].
Swap nums[2] and nums[3]. The array becomes [3, 7, 5, 9].
This array is good because it can be split into [3], [7, 5], and [9].
```

**Example 3:**
```
Input: nums = [3,7,5,9], a = 4, b = 8

Output: 0

Explanation:

The array is already good. No swaps are needed.
```
 

**Constraints:**

* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^9`
* `1 <= a < b <= 10^9`

# Submissions
---
**Solution 1: (Greedy)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 149.09 MB, Beats 42.86%
```
```c++
class Solution {
public:
    int minAdjacentSwaps(vector<int>& nums, int a, int b) {
        int n = nums.size();
        int k0 = 0;
        int k1 = 0;
        long long ans = 0;
        for (int i = 0; i < n; i ++) {
            if (nums[i] < a) {
                ans += i - k0;
                k0 += 1;
                k1 += 1;
            } else if (nums[i] <= b) {
                ans += i - k1;
                k1 += 1;
            }
        }
        return ans % (int)(1e9 + 7);
    }
};
```
