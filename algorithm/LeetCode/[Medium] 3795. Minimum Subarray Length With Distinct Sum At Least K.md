3795. Minimum Subarray Length With Distinct Sum At Least K

You are given an integer array `nums` and an integer `k`.

Return the **minimum** length of a **subarray** whose sum of the distinct values present in that subarray (each value counted once) is at least `k`. If no such subarray exists, return `-1`.

 

**Example 1:**
```
Input: nums = [2,2,3,1], k = 4

Output: 2

Explanation:

The subarray [2, 3] has distinct elements {2, 3} whose sum is 2 + 3 = 5, which is at least k = 4. Thus, the answer is 2.
```

**Example 2:**
```
Input: nums = [3,2,3,4], k = 5

Output: 2

Explanation:

The subarray [3, 2] has distinct elements {3, 2} whose sum is 3 + 2 = 5, which is at least k = 5. Thus, the answer is 2.
```
**Example 3:**
```
Input: nums = [5,5,4], k = 5

Output: 1

Explanation:

The subarray [5] has distinct elements {5} whose sum is 5, which is at least k = 5. Thus, the answer is 1.
```
 

**Constraints:**

* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^5`
* `1 <= k <= 10^9`

# Submissions
---
**Solution 1: (Sliding Window)**
```
Runtime: 302 ms, Beats 22.22%
Memory: 297.53 MB, Beats 22.22%
```
```c++
class Solution {
public:
    int minLength(vector<int>& nums, int k) {
        int n = nums.size(), i = 0, j, a = 0, ans = INT_MAX;
        vector<int> cnt(1e5 + 1);
        for (j = 0; j < n; j ++) {
            if (cnt[nums[j]] == 0) {
                a += nums[j];
            }
            cnt[nums[j]] += 1;
            while (a >= k) {
                ans = min(ans, j - i + 1);
                cnt[nums[i]] -= 1;
                if (cnt[nums[i]] == 0) {
                    a -= nums[i];
                }
                i += 1;
            }
        }
        return ans != INT_MAX ? ans : -1;
    }
};
```
