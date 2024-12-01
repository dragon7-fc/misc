3371. Identify the Largest Outlier in an Array

You are given an integer array `nums`. This array contains `n` elements, where **exactly** `n - 2` elements are **special** numbers. One of the remaining **two** elements is the sum of these **special numbers**, and the other is an **outlier**.

An **outlier** is defined as a number that is neither one of the original special numbers nor the element representing the sum of those numbers.

Note that special numbers, the sum element, and the outlier must have **distinct** indices, but may share the **same** value.

Return the **largest** potential **outlier** in `nums`.

 

**Example 1:**
```
Input: nums = [2,3,5,10]

Output: 10

Explanation:

The special numbers could be 2 and 3, thus making their sum 5 and the outlier 10.
```

**Example 2:**
```
Input: nums = [-2,-1,-3,-6,4]

Output: 4

Explanation:

The special numbers could be -2, -1, and -3, thus making their sum -6 and the outlier 4.
```

**Example 3:**
```
Input: nums = [1,1,1,1,1,5,5]

Output: 5

Explanation:

The special numbers could be 1, 1, 1, 1, and 1, thus making their sum 5 and the other 5 as the outlier.
```
 

**Constraints:**

* `3 <= nums.length <= 10^5`
* `-1000 <= nums[i] <= 1000`
* The input is generated such that at least **one** potential outlier exists in `nums`.

# Submissions
---
**Solution 1: (Math, Hash Table, try outlier on every number)**
```
Runtime: 294 ms
Memory: 181.50 MB
```
```c++
class Solution {
public:
    int getLargestOutlier(vector<int>& nums) {
        int n = nums.size(), i, cur, a = accumulate(nums.begin(), nums.end(), 0), ans = INT_MIN;
        unordered_map<int,int> dp;
        for (auto num: nums) {
            dp[num] += 1;
        }
        for (i = 0; i < n; i ++) {
            cur = a - nums[i];
            dp[nums[i]] -= 1;
            if (cur%2 == 0 && dp.count(cur/2) && dp[cur/2] >= 1) {
                ans = max(ans, nums[i]);
            }
            dp[nums[i]] += 1;
        }
        return ans;
    }
};
```
