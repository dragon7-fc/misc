3824. Minimum K to Reduce Array Within Limit

You are given a positive integer array `nums`.

For a positive integer `k`, define `nonPositive(nums, k)` as the minimum number of operations needed to make every element of nums **non-positive**. In one operation, you can choose an index `i` and reduce `nums[i]` by `k`.

Return an integer denoting the **minimum** value of `k` such that `nonPositive(nums, k) <= k^2`.

 

**Example 1:**
```
Input: nums = [3,7,5]

Output: 3

Explanation:

When k = 3, nonPositive(nums, k) = 6 <= k2.

Reduce nums[0] = 3 one time. nums[0] becomes 3 - 3 = 0.
Reduce nums[1] = 7 three times. nums[1] becomes 7 - 3 - 3 - 3 = -2.
Reduce nums[2] = 5 two times. nums[2] becomes 5 - 3 - 3 = -1.
```

**Example 2:**
```
Input: nums = [1]

Output: 1

Explanation:

When k = 1, nonPositive(nums, k) = 1 <= k2.

Reduce nums[0] = 1 one time. nums[0] becomes 1 - 1 = 0.
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^5`

# Submissions
---
**Solution 1: (Binary Search)**
```
Runtime: 41 ms, Beats 100.00%
Memory: 187.77 MB, Beats 5.56%
```
```c++
class Solution {
    bool check(long long mid, vector<int> &nums) {
        long long a = 0;
        for (auto &num: nums) {
            a += num / mid + ((num % mid) > 0);
        }
        return a <= mid * mid;
    }
public:
    int minimumK(vector<int>& nums) {
        long long a = accumulate(begin(nums), end(nums), 0LL);
        long long left = 1, right = ceil(sqrt(a)), mid, ans;
        while (left <= right) {
            mid = left + (right - left) / 2;
            if (!check(mid, nums)) {
                left = mid + 1;
            } else {
                ans = mid;
                right = mid - 1;
            }
        }
        return ans;
    }
};
```
