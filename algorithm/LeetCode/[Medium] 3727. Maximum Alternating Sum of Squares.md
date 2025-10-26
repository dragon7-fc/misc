3727. Maximum Alternating Sum of Squares

You are given an integer array `nums`. You may rearrange the elements in any order.

The **alternating score** of an array arr is defined as:

* `score = arr[0]2 - arr[1]2 + arr[2]2 - arr[3]2 + ...`

Return an integer denoting the **maximum** possible **alternating score** of `nums` after rearranging its elements.

 

**Example 1:**
```
Input: nums = [1,2,3]

Output: 12

Explanation:

A possible rearrangement for nums is [2,1,3], which gives the maximum alternating score among all possible rearrangements.

The alternating score is calculated as:

score = 22 - 12 + 32 = 4 - 1 + 9 = 12
```

**Example 2:**
```
Input: nums = [1,-1,2,-2,3,-3]

Output: 16

Explanation:

A possible rearrangement for nums is [-3,-1,-2,1,3,2], which gives the maximum alternating score among all possible rearrangements.

The alternating score is calculated as:

score = (-3)2 - (-1)2 + (-2)2 - (1)2 + (3)2 - (2)2 = 9 - 1 + 4 - 1 + 9 - 4 = 16
```
 

**Constraints:**

* `1 <= nums.length <= 10^5`
* `-4 * 10^4 <= nums[i] <= 4 * 10^4`

# Submissions
---
**Solution 1: (Sort)**
```
Runtime: 50 ms, Beats 81.82%
Memory: 176.01 MB, Beats 9.09%
```
```c++
class Solution {
public:
    long long maxAlternatingSum(vector<int>& nums) {
        int n = nums.size(), i;
        long long ans = 0;
        sort(nums.begin(), nums.end(), [](auto a, auto b){
            return a*a > b*b;
        });
        for (i = 0; i < (n + 1) / 2; i ++) {
            ans += nums[i] * nums[i];
        }
        while (i < n) {
            ans -= nums[i] * nums[i];
            i += 1;
        }
        return ans;
    }
};
```
