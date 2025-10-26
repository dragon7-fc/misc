3346. Maximum Frequency of an Element After Performing Operations I

You are given an integer array `nums` and two integers `k` and `numOperations`.

You must perform an **operawtion** `numOperations` times on `nums`, where in each operation you:

* Select an index `i` that was not selected in any previous operations.
* Add an integer in the range `[-k, k]` to `nums[i]`.

Return the **maximum** possible **frequency** of any element in `nums` after performing the **operations**.

 

**Example 1:**
```
Input: nums = [1,4,5], k = 1, numOperations = 2

Output: 2

Explanation:

We can achieve a maximum frequency of two by:

Adding 0 to nums[1]. nums becomes [1, 4, 5].
Adding -1 to nums[2]. nums becomes [1, 4, 4].
```

**Example 2:**
```
Input: nums = [5,11,20,20], k = 5, numOperations = 1

Output: 2

Explanation:

We can achieve a maximum frequency of two by:

Adding 0 to nums[1].
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^5`
* `0 <= k <= 10^5`
* `0 <= numOperations <= nums.length`

# Submissions
---
**Solution 1: (Binary Search, brute force all possible)**
```
Runtime: 276 ms, Beats 41.75%
Memory: 153.35 MB, Beats 36.41%
```
```c++
class Solution {
public:
    int maxFrequency(vector<int>& nums, int k, int numOperations) {
        int n = nums.size(), i, j, a, b = *max_element(nums.begin(), nums.end()), ans = 0;
        sort(nums.begin(), nums.end());
        unordered_map<int, int> cnt;
        for (auto num: nums) {
            cnt[num] += 1;
        }
        for (a = 1; a <= b; a ++) {
            i = lower_bound(nums.begin(), nums.end(), a - k) - nums.begin();
            j = lower_bound(nums.begin(), nums.end(), a + k + 1) - nums.begin();
            ans = max(ans, min(j - i - cnt[a], numOperations) + cnt[a]);
        }
        return ans;
    }
};
```

**Solution 2: (Sliding Window)**
```
Runtime: 164 ms, Beats 55.83%
Memory: 122.25 MB, Beats 65.29%
```c++
class Solution {
public:
    int maxFrequency(vector<int>& nums, int k, int numOperations) {
        int n = nums.size(), ans = 0, left = 0, right = 0;
        sort(nums.begin(), nums.end());  // Sort the array for sliding window approach

        // HashMap to store frequency of each number
        unordered_map<int, int> count;
        for (int num : nums) {
            count[num]++;
        }

        // First pass: choose an existing number as the reference point
        for (int mid = 0; mid < n; mid++) {
            // Adjust left pointer to keep nums[mid] - nums[left] within `k`
            while (nums[mid] - nums[left] > k) {
                left++;
            }

            // Adjust right pointer to keep nums[right] - nums[mid] within `k`
            while (right < n - 1 && nums[right + 1] - nums[mid] <= k) {
                right++;
            }

            int total = right - left + 1;  // Calculate range size
            // Update ans with maximum achievable frequency for nums[mid] as the target
            ans = max(ans, min(total - count[nums[mid]], numOperations) + count[nums[mid]]);
        }

        // Second pass: choose a non-existent number as reference point
        left = 0;
        for (right = 0; right < n; right++) {
            int mid = (nums[left] + nums[right]) / 2;  // Calculate hypothetical midpoint

            // Adjust left pointer to ensure midpoint is within `k` range from both ends
            while (mid - nums[left] > k || nums[right] - mid > k) {
                left++;
                mid = (nums[left] + nums[right]) / 2;
            }

            // Update ans with maximum achievable frequency with the hypothetical midpoint
            ans = max(ans, min(right - left + 1, numOperations));
        }

        return ans;
    }
};
```
