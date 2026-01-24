3818. Minimum Prefix Removal to Make Array Strictly Increasing

You are given an integer array `nums`.

You need to remove exactly one prefix (possibly empty) from `nums`.

Return an integer denoting the **minimum** length of the removed prefix such that the remaining array is **strictly increasing**.

 

**Example 1:**
```
Input: nums = [1,-1,2,3,3,4,5]

Output: 4

Explanation:

Removing the prefix = [1, -1, 2, 3] leaves the remaining array [3, 4, 5] which is strictly increasing.
```

**Example 2:**
```
Input: nums = [4,3,-2,-5]

Output: 3

Explanation:

Removing the prefix = [4, 3, -2] leaves the remaining array [-5] which is strictly increasing.
```

**Example 3:**
```
Input: nums = [1,2,3,4]

Output: 0

Explanation:

The array nums = [1, 2, 3, 4] is already strictly increasing so removing an empty prefix is sufficient.
```
 

**Constraints:**

* `1 <= nums.length <= 10^5`
* `-10^9 <= nums[i] <= 10^9`

# Submissions
---
**Solution 1: (Greedy, walk backward)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 193.51 MB, Beats 15.31%
```
```c++
class Solution {
public:
    int minimumPrefixLength(vector<int>& nums) {
        int n = nums.size(), i = n - 2, ans = n - 1;
        while (i >= 0 && nums[i] < nums[i + 1]) {
            ans = i;
            i -= 1;
        }
        return ans;
    }
};
```
