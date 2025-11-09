3737. Count Subarrays With Majority Element I

You are given an integer array `nums` and an integer `target`.

Return the number of subarrays of `nums` in which `target` is the majority element.

The **majority** element of a subarray is the element that appears **strictly** more than half of the times in that subarray.

 

**Example 1:**
```
Input: nums = [1,2,2,3], target = 2

Output: 5

Explanation:

Valid subarrays with target = 2 as the majority element:

nums[1..1] = [2]
nums[2..2] = [2]
nums[1..2] = [2,2]
nums[0..2] = [1,2,2]
nums[1..3] = [2,2,3]
So there are 5 such subarrays.
```

**Example 2:**
```
Input: nums = [1,1,1,1], target = 1

Output: 10

Explanation:

All 10 subarrays have 1 as the majority element.
```

**Example 3:**
```
Input: nums = [1,2,3], target = 4

Output: 0

Explanation:

target = 4 does not appear in nums at all. Therefore, there cannot be any subarray where 4 is the majority element. Hence the answer is 0.
```
 

**Constraints:**

* `1 <= nums.length <= 1000`
* `1 <= nums[i] <= 10^9`
* `1 <= target <= 10^9`

# Submissions
---
**Solution 1: (Brute Force)**
```
Runtime: 2155 ms, Beats 11.11%
Memory: 453.70 MB, Beats 11.11%
```
```c++
class Solution {
public:
    int countMajoritySubarrays(vector<int>& nums, int target) {
        int n = nums.size(), i, j, ans = 0;
        unordered_map<int, int> cnt;
        for (j = 0; j < n; j ++) {
            for (i = j; i >= 0; i --) {
                cnt[nums[i]] += 1;
                if (cnt[target] > (j - i + 1) / 2) {
                    ans += 1;
                }
            }
            cnt.clear();
        }
        return ans;
    }
};
```
