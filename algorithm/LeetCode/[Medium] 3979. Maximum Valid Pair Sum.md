3979. Maximum Valid Pair Sum

You are given an integer array `nums` of length `n` and an integer `k`.

A pair of indices `(i, j)` is called **valid** if:

* `0 <= i < j < n`
* `j - i >= k`

Return the **maximum** value of `nums[i] + nums[j]` among all valid pairs.

 

**Example 1:**
```
Input: nums = [1,3,5,2,8], k = 2

Output: 13

Explanation:

The valid pairs are:

(0, 2): nums[0] + nums[2] = 6
(0, 3): nums[0] + nums[3] = 3
(0, 4): nums[0] + nums[4] = 9
(1, 3): nums[1] + nums[3] = 5
(1, 4): nums[1] + nums[4] = 11
(2, 4): nums[2] + nums[4] = 13
Thus, the answer is 13.
```
**Example 2:**
```
Input: nums = [5,1,9], k = 1

Output: 14

Explanation:

Since k = 1, every pair is valid.
The maximum value is obtained from a pair (0, 2)​​​​​​​, which is nums[0] + nums[2] = 5 + 9 = 14.
Thus, the answer is 14.
```

**Constraints:**

* `2 <= n == nums.length <= 10^5`
* `1 <= nums[i] <= 10^9`
* `1 <= k <= n - 1`

# Submissions
---
**Solution 1: (Prefix Sum)**
```
Runtime: 4 ms, Beats 42.86%
Memory: 215.44 MB, Beats 14.29%
```
```c++
class Solution {
public:
    int maxValidPairSum(vector<int>& nums, int k) {
        int n =nums.size();
        vector<int> right(n);
        right[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= k; i --) {
            right[i] = max(nums[i], right[i + 1]);
        }
        int left = 0;
        int ans = 0;
        for (int i = 0; i < n - k; i ++) {
            left = max(left, nums[i]);
            ans = max(ans, left + right[i + k]);
        }
        return ans;
    }
};
```

**Solution 2: (Prefix Sum, one pass)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 205.46 MB, Beats 14.29%
```
```c++
class Solution {
public:
    int maxValidPairSum(vector<int>& nums, int k) {
        int n =nums.size();
        int ans = 0;
        for (int i = 0; i < n; i ++) {
            if (i >= k) {
                ans = max(ans, nums[i] + nums[i - k]);
            }
            if (i) {
                nums[i] = max(nums[i], nums[i - 1]);
            }
        }
        return ans;
    }
};
```
