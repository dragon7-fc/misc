2962. Count Subarrays Where Max Element Appears at Least K Times

You are given an integer array `nums` and a positive integer `k`.

Return the number of subarrays where the **maximum** element of `nums` appears at least `k` times in that subarray.

A **subarray** is a contiguous sequence of elements within an array.

 

**Example 1:**
```
Input: nums = [1,3,2,3,3], k = 2
Output: 6
Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].
```

**Example 2:**
```
Input: nums = [1,4,2,1], k = 3
Output: 0
Explanation: No subarray contains the element 4 at least 3 times.
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^6`
* `1 <= k <= 10^5`

# Submissions
---
**Solution 1: (Sliding Window, conly consider first element)**
```
Runtime: 136 ms
Memory: 120.8 MB
```
```c++
class Solution {
public:
    long long countSubarrays(vector<int>& nums, int k) {
        int mx = *max_element(nums.begin(), nums.end());
        long long ans = 0, cnt = 0;
        vector<int> dp;
        dp.push_back(0);
        for (int i = 0; i < nums.size(); i ++) {
            if (nums[i] == mx) {
                cnt += 1;
                dp.push_back(i);
            }
            if (cnt >= k) {
                ans += dp[cnt-k+1]+1;
            }
        }
        return ans;
    }
};
```

**Solution 2: (Sliding Window, consider first and last element)**
```
Runtime: 112 ms
Memory: 123.60 MB
```
```c++
class Solution {
public:
    long long countSubarrays(vector<int>& nums, int k) {
        int n = nums.size(), mx = *max_element(nums.begin(), nums.end());
        vector<int> dp;
        dp.push_back(-1);
        for (int i = 0; i < n; i ++) {
            if (nums[i] == mx) {
                dp.push_back(i);
            }
        }
        long long ans = 0;
        for (int i = 1; i+k <= dp.size(); i ++) {
            ans += (dp[i]-dp[i-1]) * (long long)(n-dp[i+k-1]);   }
        return ans;
    }
};
```

**Solution 3: (Sliding Window)**
```
Runtime: 7 ms, Beats 44.58%
Memory: 121.76 MB, Beats 48.26%
```
```c++
class Solution {
public:
    long long countSubarrays(vector<int>& nums, int k) {
        int n = nums.size(), i = 0, j, a = *max_element(nums.begin(), nums.end()), cnt = 0;
        long long ans = 0;
        for (j = 0; j < n; j ++) {
            cnt += nums[j] == a;
            while (cnt >= k) {
                ans += n - j;
                cnt -= nums[i] == a;
                i += 1;
            }
        }
        return ans;
    }
};
```
