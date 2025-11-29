3759. Count Elements With at Least K Greater Values

You are given an integer array `nums` of length `n` and an integer `k`.

An element in `nums` is said to be **qualified** if there exist **at least** `k` elements in the array that are strictly greater than it.

Return an integer denoting the total number of qualified elements in `nums`.

 

**Example 1:**
```
Input: nums = [3,1,2], k = 1

Output: 2

Explanation:

The elements 1 and 2 each have at least k = 1 element greater than themselves.
No element is greater than 3. Therefore, the answer is 2.
```

**Example 2:**
```
Input: nums = [5,5,5], k = 2

Output: 0

Explanation:

Since all elements are equal to 5, no element is greater than the other. Therefore, the answer is 0.
```
 

**Constraints:**

* `1 <= n == nums.length <= 10^5`
* `1 <= nums[i] <= 10^9`
* `0 <= k < n`

# Submissions
---
**Solution 1: (Sort)**
```
Runtime: 62 ms, Beats 60.00%
Memory: 173.98 MB, Beats 40.00%
```
```c++
class Solution {
public:
    int countElements(vector<int>& nums, int k) {
        int n = nums.size(), ans = 0;
        if (k == 0) {
            return n;
        }
        
        sort(nums.begin(), nums.end());

        // k-th largest element is at index n-k
        int threshold = nums[n - k];

        for (auto &x: nums) {
            if (x < threshold) {
                ans += 1;
            }
        }

        return ans;
    }
};
```
