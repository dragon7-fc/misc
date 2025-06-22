2966. Divide Array Into Arrays With Max Difference

You are given an integer array `nums` of size `n` and a positive integer `k`.

Divide the array into one or more arrays of size `3` satisfying the following conditions:

* **Each** element of `nums` should be in exactly one array.
* The difference between any two elements in one array is less than or equal to `k`.

Return a 2D array containing all the arrays. If it is impossible to satisfy the conditions, return an empty array. And if there are multiple answers, return any of them.

 

**Example 1:**
```
Input: nums = [1,3,4,8,7,9,3,5,1], k = 2
Output: [[1,1,3],[3,4,5],[7,8,9]]
Explanation: We can divide the array into the following arrays: [1,1,3], [3,4,5] and [7,8,9].
The difference between any two elements in each array is less than or equal to 2.
Note that the order of elements is not important.
```

**Example 2:**
```
Input: nums = [1,3,3,2,7,3], k = 3
Output: []
Explanation: It is not possible to divide the array satisfying all the conditions.
```

**Constraints:**

* `n == nums.length`
* `1 <= n <= 105`
* `n` is a multiple of 3.
* `1 <= nums[i] <= 10^5`
* `1 <= k <= 10^5`

# Submissions
---
**Solution 1: (Counter)**
```
Runtime: 224 ms, Beats 5.50%
Memory: 135.65 MB, Beats 14.83%
```
```c++
class Solution {
public:
    vector<vector<int>> divideArray(vector<int>& nums, int k) {
        int n = nums.size(), i, cnt[100001] = {0}, ck = 0;
        vector<vector<int>> ans;
        for (i = 0; i < n; i ++) {
            cnt[nums[i]] += 1;
        }
        for (i = 1; i <= 100000; i ++) {
            while (cnt[i]) {
                if (ck == 0) {
                    ans.push_back({});
                }
                ans.back().push_back(i);
                if (ans.back().back() - ans.back()[0] > k) {
                    return {};
                }
                cnt[i] -= 1;
                ck = (ck+1)%3;
            }
        }
        return ans;
    }
};
```

**Solution 2: (Sort)**
```
Runtime: 43 ms, Beats 84.69%
Memory: 120.06 MB, Beats 64.59%
```
```c++
class Solution {
public:
    vector<vector<int>> divideArray(vector<int>& nums, int k) {
        int n = nums.size(), i;
        vector<vector<int>> ans;
        sort(nums.begin(), nums.end());
        for (i = 0; i < n; i += 3) {
            if (nums[i+2] - nums[i] > k) {
                return {};
            }
            ans.push_back({nums[i], nums[i+1], nums[i+2]});
        }
        return ans;
    }
};
```
