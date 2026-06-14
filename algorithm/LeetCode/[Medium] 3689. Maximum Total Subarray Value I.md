3689. Maximum Total Subarray Value I

You are given an integer array `nums` of length `n` and an integer `k`.

You need to choose exactly `k` non-empty **subarrays** `nums[l..r]` of `nums`. Subarrays may overlap, and the exact same subarray (same `l` and `r`) can be chosen more than once.

The value of a subarray `nums[l..r]` is defined as: `max(nums[l..r]) - min(nums[l..r])`.

The total value is the sum of the values of all chosen subarrays.

Return the **maximum** possible total value you can achieve.

 

**Example 1:**
```
Input: nums = [1,3,2], k = 2

Output: 4

Explanation:

One optimal approach is:

Choose nums[0..1] = [1, 3]. The maximum is 3 and the minimum is 1, giving a value of 3 - 1 = 2.
Choose nums[0..2] = [1, 3, 2]. The maximum is still 3 and the minimum is still 1, so the value is also 3 - 1 = 2.
Adding these gives 2 + 2 = 4.
```

**Example 2:**
```
Input: nums = [4,2,5,1], k = 3

Output: 12

Explanation:

One optimal approach is:

Choose nums[0..3] = [4, 2, 5, 1]. The maximum is 5 and the minimum is 1, giving a value of 5 - 1 = 4.
Choose nums[0..3] = [4, 2, 5, 1]. The maximum is 5 and the minimum is 1, so the value is also 4.
Choose nums[2..3] = [5, 1]. The maximum is 5 and the minimum is 1, so the value is again 4.
Adding these gives 4 + 4 + 4 = 12.
```
 

**Constraints:**

* `1 <= n == nums.length <= 5 * 10^4`
* `0 <= nums[i] <= 10^9`
* `1 <= k <= 10^5`

# Submissions
---
**Solution 1: (Deque)**
```
Runtime: 11 ms, Beats 10.12%
Memory: 106.97 MB, Beats 1.56%
```
```c++
class Solution {
public:
    long long maxTotalValue(vector<int>& nums, int k) {
        long long ans = 0;
        deque<int> min_dq, max_dq;
        for (const auto &num: nums) {
            while (min_dq.size() && min_dq.back() >= num) {
                min_dq.pop_back();
            }
            min_dq.push_back(num);
            while (max_dq.size() && max_dq.back() <= num) {
                max_dq.pop_back();
            }
            max_dq.push_back(num);
            ans = max(ans, 1LL * (max_dq.front() - min_dq.front()) * k);
        }
        return ans;

    }
};
```

**Solution 2: (Greedy)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 103.81 MB, Beats 3.11%
```
```c++
class Solution {
public:
    long long maxTotalValue(vector<int>& nums, int k) {
        int mn = INT_MAX;
        int mx = INT_MIN;
        for (const auto &num: nums) {
            mn = min(mn, num);
            mx = max(mx, num);
        }
        return 1LL * (mx - mn) * k;
    }
};
```
