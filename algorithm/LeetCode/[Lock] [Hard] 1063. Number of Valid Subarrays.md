1063. Number of Valid Subarrays

Given an integer array `nums`, return the number of non-empty **subarrays** with the leftmost element of the subarray not larger than other elements in the subarray.

A **subarray** is a contiguous part of an array.

 

**Example 1:**
```
Input: nums = [1,4,2,5,3]
Output: 11
Explanation: There are 11 valid subarrays: [1],[4],[2],[5],[3],[1,4],[2,5],[1,4,2],[2,5,3],[1,4,2,5],[1,4,2,5,3].
```

**Example 2:**
```
Input: nums = [3,2,1]
Output: 3
Explanation: The 3 valid subarrays are: [3],[2],[1].
```

**Example 3:**
```
Input: nums = [2,2,2]
Output: 6
Explanation: There are 6 valid subarrays: [2],[2],[2],[2,2],[2,2],[2,2,2].
```

**Constraints:**

* `1 <= nums.length <= 5 * 10^4`
* `0 <= nums[i] <= 10^5`

# Submissions
---
**Solution 1: (Monostack)**
```
Runtime: 53 ms
Memory: 43.4 MB
```
```c++
class Solution {
public:
    int validSubarrays(vector<int>& nums) {
        vector<int> stk;
        int ans = 0;
        for (int i = 0; i < nums.size(); i ++) {
            while (!stk.empty() && stk.back() > nums[i]) {
                stk.pop_back();
            }
            stk.push_back(nums[i]);
            ans += stk.size();
        }
        return ans;
    }
};
```
