3804. Number of Centered Subarrays

You are given an integer array `nums`.

A subarray of `nums` is called **centered** if the sum of its elements is equal to at least one element within that same subarray.

Return the number of **centered** subarrays of `nums`.

 

**Example 1:**
```
Input: nums = [-1,1,0]

Output: 5

Explanation:

All single-element subarrays ([-1], [1], [0]) are centered.
The subarray [1, 0] has a sum of 1, which is present in the subarray.
The subarray [-1, 1, 0] has a sum of 0, which is present in the subarray.
Thus, the answer is 5.
```

**Example 2:**
```
Input: nums = [2,-3]

Output: 2

Explanation:

Only single-element subarrays ([2], [-3]) are centered.
```
 

**Constraints:**

* `1 <= nums.length <= 500`
* `-10^5 <= nums[i] <= 10^5`

# Submissions
---
**Solution 1: (Set)**
```
Runtime: 174 ms, Beats 97.87%
Memory: 64.35 MB, Beats 81.70%
```
```c++
class Solution {
public:
    int centeredSubarrays(vector<int>& nums) {
        int n = nums.size(), i, j, a, ans = 0;
        unordered_set<int> st;
        for (i = 0; i < n; i ++) {
            a = 0;
            for (j = i; j < n; j ++) {
                st.insert(nums[j]);
                a += nums[j];
                if (st.count(a)) {
                    ans += 1;
                }
            }
            st.clear();
        }
        return ans;
    }
};
```
