3397. Maximum Number of Distinct Elements After Operations

You are given an integer array `nums` and an integer `k`.

You are allowed to perform the following operation on each element of the array at most once:

* Add an integer in the range `[-k, k]` to the element.

Return the **maximum** possible number of distinct elements in nums after performing the operations.

 

**Example 1:**
```
Input: nums = [1,2,2,3,3,4], k = 2

Output: 6

Explanation:

nums changes to [-1, 0, 1, 2, 3, 4] after performing operations on the first four elements.
```

**Example 2:**
```
Input: nums = [4,4,4,4], k = 1

Output: 3

Explanation:

By adding -1 to nums[0] and 1 to nums[1], nums changes to [3, 5, 4, 4].
```
 

**Constraints:**

* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^9`
* `0 <= k <= 10^9`

# Submissions
---
**Solution 1: (Greedy, Counting Sort)**
```
Runtime: 126 ms
Memory: 97.49 MB
```
```c++
class Solution {
public:
    int maxDistinctElements(vector<int>& nums, int k) {
        int pre = INT_MIN, ans = 0;
        sort(nums.begin(), nums.end());
        for (auto num: nums) {
            if (pre <= num+k) {
                if (pre < num-k) {
                    pre = num-k;
                }
                pre += 1;
                ans += 1;
            }
        }
        return ans;
    }
};
```

**Solution 2: (Sort)**
```
Runtime: 112 ms, Beats 85.80%
Memory: 97.52 MB, Beats 88.33%
```
```c++
class Solution {
public:
    int maxDistinctElements(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int n = nums.size(), i, pre = nums[0] - k, ans = 1;
        for (i = 1; i < n; i ++) {
            if (nums[i] + k > pre) {
                pre = max(pre + 1, nums[i] - k);
                ans += 1;
            }
        }
        return ans;
    }
};
```
