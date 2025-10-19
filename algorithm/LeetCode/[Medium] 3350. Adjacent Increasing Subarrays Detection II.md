3350. Adjacent Increasing Subarrays Detection II

Given an array nums of n integers, your task is to find the **maximum** value of `k` for which there exist two **adjacent subarrays** of length `k` each, such that both subarrays are **strictly increasing**. Specifically, check if there are **two** subarrays of length `k` starting at indices `a` and `b` (`a < b`), where:

* Both subarrays `nums[a..a + k - 1]` and `nums[b..b + k - 1]` are **strictly increasing**.
* The subarrays must be **adjacent**, meaning `b = a + k`.

Return the **maximum** possible value of `k`.

A **subarray** is a contiguous **non-empty** sequence of elements within an array.

 

**Example 1:**
```
Input: nums = [2,5,7,8,9,2,3,4,3,1]

Output: 3

Explanation:

The subarray starting at index 2 is [7, 8, 9], which is strictly increasing.
The subarray starting at index 5 is [2, 3, 4], which is also strictly increasing.
These two subarrays are adjacent, and 3 is the maximum possible value of k for which two such adjacent strictly increasing subarrays exist.
```

**Example 2:**
```
Input: nums = [1,2,3,4,4,4,4,5,6,7]

Output: 2

Explanation:

The subarray starting at index 0 is [1, 2], which is strictly increasing.
The subarray starting at index 2 is [3, 4], which is also strictly increasing.
These two subarrays are adjacent, and 2 is the maximum possible value of k for which two such adjacent strictly increasing subarrays exist.
```

**Constraints:**

* `2 <= nums.length <= 2 * 10^5`
* `-10^9 <= nums[i] <= 10^9`

# Submissions
---
**Solution 1: (Binary Search)**
```
Runtime: 725 ms
Memory: 180.42 MB
```
```c++
class Solution {
    bool check(vector<int> &nums, int k, vector<int> &dp) {
        for (int i = 0; i + 2*k <= nums.size(); i ++) {
            if (dp[i] >= k && dp[i+k] >= k) {
                return true;
            }
        }
        return false;
    }
public:
    int maxIncreasingSubarrays(vector<int>& nums) {
        int n = nums.size(), i, left, right, mid;
        vector<int> dp(n);
        dp[n-1] = 1;
        i = n-2;
        while (i >= 0) {
            if (nums[i] < nums[i+1]) {
                dp[i] = dp[i+1] + 1;
            } else {
                dp[i] = 1;
            }
            cout << dp[i] << endl;
            i -= 1;
        }
        left = 1, right = n/2;
        while (left < right) {
            mid = right - (right-left)/2;
            cout << left << ", " << right << ", " << mid << endl;
            if (!check(nums, mid, dp)) {
                right = mid-1;
            } else {
                left = mid;
            }
        }
        return left;
    }
};
```

**Solution 2: (Prefix Sum)**
```
Runtime: 217 ms
Memory: 172.82 MB
```
```c++
class Solution {
public:
    int maxIncreasingSubarrays(vector<int>& nums) {
        int n = nums.size(), up = 1, pre_max_up = 0, res = 0;
        for (int i = 1; i < n; ++i) {
            if (nums[i] > nums[i - 1]) {
                up++;
            } else {
                pre_max_up = up;
                up = 1;
            }
            res = max({res, up / 2, min(pre_max_up, up)});
        }
        return res;
    }
};
```

**Solution 3: (Prefix Sum)**
```
Runtime: 244 ms, Beats 25.56%
Memory: 173.64 MB, Beats 81.58%
```
```c++
class Solution {
public:
    int maxIncreasingSubarrays(vector<int>& nums) {
        int n = nums.size(), i, pre = 0, a = 1, ans = 0;
        for (i = 1; i < n; i ++) {
            if (nums[i] > nums[i - 1]) {
                a += 1;
            } else {
                pre = a;
                a = 1;
            }
            ans = max({ans, a / 2, min(pre, a)});
        }
        return ans;
    }
};
```
