3914. Minimum Operations to Make Array Non Decreasing

You are given an integer array `nums` of length `n`.

In one operation, you may choose any subarray `nums[l..r]` and increase each element in that subarray by `x`, where `x` is any **positive** integer.

Return the **minimum** possible sum of the values of `x` across all operations required to make the array **non-decreasing**.

An array is **non-decreasing** if `nums[i] <= nums[i + 1]` for all `0 <= i < n - 1`.

 

**Example 1:**
```
Input: nums = [3,3,2,1]

Output: 2

Explanation:

One optimal set of operations:

Choose subarray [2..3] and add x = 1 resulting in [3, 3, 3, 2]
Choose subarray [3..3] and add x = 1 resulting in [3, 3, 3, 3]
The array becomes non-decreasing, and the total sum of chosen x values is 1 + 1 = 2.
```

**Example 2:**
```
Input: nums = [5,1,2,3]

Output: 4

Explanation:

One optimal set of operations:

Choose subarray [1..3] and add x = 4 resulting in [5, 5, 6, 7]
The array becomes non-decreasing, and the total sum of chosen x values is 4.
```
 

**Constraints:**

* `1 <= n == nums.length <= 10^5`
* `1 <= nums[i] <= 10^9`

# Submissions
---
**Solution 1: (Greedy, simulation, try to increase every element)**
```
Runtime: 4 ms, Beats 44.44%
Memory: 136.78 MB, Beats 88.89%
```
```c++
class Solution {
public:
    long long minOperations(vector<int>& nums) {
        int n = nums.size(), i;
        long long pre = nums[0], d = 0, dd, ans = 0;
        for (i = 1; i < n; i ++) {
            if (nums[i] + d < pre) {
                dd = pre - nums[i] - d;
                ans += dd;
                d += dd;
            } else if (nums[i] >= pre + d) {
                d = 0;
            }
            pre = max(pre, nums[i] + d);
        }
        return ans;
    }
};
```

**Solution 2: (Greedy, try to remove every drop, increase at index i "carries over" to all indices > i)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 136.99 MB, Beats 34.15%
```
```c++
class Solution {
public:
    long long minOperations(vector<int>& nums) {
        long long ans = 0;
        for (int i = 0; i + 1 < nums.size(); i ++) {
            ans += max(0, nums[i] - nums[i + 1]);
        }
        return ans;
    }
};
```
