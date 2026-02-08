3835. Count Subarrays With Cost Less Than or Equal to K

You are given an integer array `nums`, and an integer `k`.

For any subarray `nums[l..r]`, define its cost as:

`cost = (max(nums[l..r]) - min(nums[l..r])) * (r - l + 1).`

Return an integer denoting the number of subarrays of `nums` whose cost is less than or equal to `k`.

 

**Example 1:**
```
Input: nums = [1,3,2], k = 4

Output: 5

Explanation:

We consider all subarrays of nums:

nums[0..0]: cost = (1 - 1) * 1 = 0
nums[0..1]: cost = (3 - 1) * 2 = 4
nums[0..2]: cost = (3 - 1) * 3 = 6
nums[1..1]: cost = (3 - 3) * 1 = 0
nums[1..2]: cost = (3 - 2) * 2 = 2
nums[2..2]: cost = (2 - 2) * 1 = 0
There are 5 subarrays whose cost is less than or equal to 4.
```

**Example 2:**
```
Input: nums = [5,5,5,5], k = 0

Output: 10

Explanation:

For any subarray of nums, the maximum and minimum values are the same, so the cost is always 0.

As a result, every subarray of nums has cost less than or equal to 0.

For an array of length 4, the total number of subarrays is (4 * 5) / 2 = 10.
```

**Example 3:**
```
Input: nums = [1,2,3], k = 0

Output: 3

Explanation:

The only subarrays of nums with cost 0 are the single-element subarrays, and there are 3 of them.
```
 

**Constraints:**

* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^9`
* `0 <= k <= 10^15`

# Submissions
---
**Solution 1: (Sliding Window, Deque)**
```
Runtime: 55 ms, Beats 62.26%
Memory: 185.85 MB, Beats 78.07%
```
```c++
class Solution {
public:
    long long countSubarrays(vector<int>& nums, long long k) {
        long long ans = 0, j = 0;
        deque<int> mx, mn;

        for (int i = 0; i < nums.size(); i++) {
            while (mx.size() && nums[mx.back()] <= nums[i]) {
                mx.pop_back();
            }
            while (mn.size() && nums[mn.back()] >= nums[i]) {
                mn.pop_back();
            }
            mx.push_back(i);
            mn.push_back(i);
            while (j <= i && (nums[mx.front()] - nums[mn.front()]) * (i - j + 1) > k) {
                if (mx.front() == j) {
                    mx.pop_front();
                }
                if (mn.front() == j) {
                    mn.pop_front();
                }
                j += 1;
            }
            ans += i - j + 1;
        }
        return ans;
    }
};
```
