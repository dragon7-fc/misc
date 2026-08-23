4031. Find All Numbers Disappeared in an Array II

You are given an integer array `nums` and two integers `lower` and `upper`.

A missing integer is an integer in the inclusive range `[lower, upper]` that does not appear in `nums`.

Return a 2D integer array where each element is of the form `[start, end]`, representing a contiguous range of missing integers. Return the ranges in **increasing** order. If there are no missing integers, return an empty array.

Note: Consecutive missing integers should be grouped into a single range.

 

**Example 1:**
```
Input: nums = [3,9,7], lower = 1, upper = 12

Output: [[1,2],[4,6],[8,8],[10,12]]

Explanation:

The missing integers are [1, 2, 4, 5, 6, 8, 10, 11, 12].
Grouping the missing integers into the minimum number of contiguous ranges, we get [1, 2], [4, 6], [8, 8], and [10, 12].
Therefore, the answer is [[1, 2], [4, 6], [8, 8], [10, 12]].
```

**Example 2:**
```
Input: nums = [1,1], lower = 5, upper = 7

Output: [[5,7]]

Explanation:

The missing integers are [5, 6, 7].
Grouping the missing integers into the minimum number of contiguous ranges, we get [5, 7].
Therefore, the answer is [[5, 7]].
```

**Example 3:**
```
Input: nums = [2,3,5], lower = 2, upper = 3

Output: []

Explanation:

There are no missing integers.
Therefore, the answer is [].
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^5`
* `1 <= lower <= upper <= 10^5`

# Submissions
---
**Solution 1: (Greedy)**
```
Runtime: 76 ms, Beats 87.80%
Memory: 242.01 MB, Beats 93.54%
```
```c++
class Solution {
public:
    vector<vector<int>> findDisappearedNumbers(vector<int>& nums, int lower, int upper) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int cur = lower;
        vector<vector<int>> ans;
        for (const auto &num: nums) {
            if (num < lower) {
                continue;
            }
            if (num > upper) {
                break;
            }
            if (cur < num) {
                ans.push_back({cur, num - 1});
            }
            cur = max(cur, num + 1);
        }
        if (cur <= upper) {
            ans.push_back({cur, upper});
        }
        return ans;
    }
};
```
