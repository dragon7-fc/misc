3987. Minimum Total Cost to Process All Elements

You are given an integer array `nums` and an integer `k`.

Initially, you have `k` units of resources.

You must process the elements of `nums` from left to right. To process the `i`th element, you need `nums[i]` resources.

If your available resources are less than `nums[i]`, you may perform an operation that increases your available resources by `k`. The value of `k` is fixed and does not change throughout the process. The first such operation incurs a cost of `1`, the second incurs a cost of `2`, and so on.

After processing the `i`th element, your available resources decrease by `nums[i]`.

Return an integer denoting the **minimum** total cost required to process all elements. Since the answer may be very large, return it modulo `10^9 + 7`.

 

**Example 1:**
```
Input: nums = [1,2,3,4], k = 4

Output: 3

Explanation:

After processing nums[0], we have 4 - 1 = 3 units of resources left.
After processing nums[1], we have 3 - 2 = 1 unit of resources left.
Since nums[2] = 3 and only 1 unit of resources is available, we perform the first operation costing 1. After processing nums[2], we have 1 + 4 - 3 = 2 units of resources left.
Since nums[3] = 4 and only 2 units of resources are available, we perform the second operation costing 2, to have 2 + 4 = 6 units of resources, which is enough to process nums[3].
Thus, the total cost is 1 + 2 = 3.
```

**Example 2:**
```
Input: nums = [1,1,7,14], k = 4

Output: 15

Explanation:

After processing nums[0], we have 4 - 1 = 3 units of resources left.
After processing nums[1], we have 3 - 1 = 2 units of resources left.
Since nums[2] = 7 and only 2 units of resources are available, we perform two operations costing 1 + 2 = 3. After processing nums[2], we have 2 + 4 + 4 - 7 = 3 units of resources left.
Since nums[3] = 14 and only 3 units of resources are available, we perform three operations costing 3 + 4 + 5 = 12, to have 3 + 4 + 4 + 4 = 15 units of resources, which is enough to process nums[3].
Thus, the total cost is 3 + 12 = 15.
```

**Example 3:**
```
Input: nums = [1,2,3,4], k = 10

Output: 0

Explanation:

To process all elements, we can use the initial 10 units of resources without performing any operations. Thus, the total cost required is 0.
```
 

**Constraints:**

* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^9`
* `1 <= k <= 10^9`

# Submissions
---
**Solution 1: (Greedy)**
```
Runtime: 4 ms, Beats 83.03%
Memory: 169.31 MB, Beats 65.20%
```
```c++
class Solution {
    const int MOD = 1e9 + 7;
public:
    int minimumCost(vector<int>& nums, int k) {
        long long op = 0;
        int r = k;
        for (const auto &num: nums) {
            if (num <= r) {
                r -= num;
            } else {
                int m = (num - r + (k - 1)) / k;
                op += m;
                r = r + m * k - num;
                op %= MOD;
            }
        }
        return ((1 + op) * op / 2) % MOD;
    }
};
```
