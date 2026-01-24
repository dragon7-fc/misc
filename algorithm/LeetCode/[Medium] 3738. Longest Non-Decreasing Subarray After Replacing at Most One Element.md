3738. Longest Non-Decreasing Subarray After Replacing at Most One Element

You are given an integer array `nums`.

You are allowed to replace at most one element in the array with any other integer value of your choice.

Return the length of the **longest non-decreasing subarray** that can be obtained after performing at most one replacement.

An array is said to be non-decreasing if each element is greater than or equal to its previous one (if it exists).

 

**Example 1:**
```
Input: nums = [1,2,3,1,2]

Output: 4

Explanation:

Replacing nums[3] = 1 with 3 gives the array [1, 2, 3, 3, 2].

The longest non-decreasing subarray is [1, 2, 3, 3], which has a length of 4.
```

**Example 2:**
```
Input: nums = [2,2,2,2,2]

Output: 5

Explanation:

All elements in nums are equal, so it is already non-decreasing and the entire nums forms a subarray of length 5.
```
 

**Constraints:**

* `1 <= nums.length <= 10^5`
* `-10^9 <= nums[i] <= 10^9`

# Submissions
---
**Solution 1: (Prefix Sum, left and right)**

     nums = [ 1, 2, 3, 1, 2]
    left      1  2  3  1  2
    right     3  2  1  2  1
    ans     4           

```
Runtime: 35 ms, Beats 25.00%
Memory: 190.31 MB, Beats 25.00%
```
```c++
class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int n = nums.size(), i, ans;
        vector<int> left(n, 1), right(n, 1);
        for (i = 1; i < n; i++)
            if (nums[i - 1] <= nums[i])
                left[i] = left[i - 1] + 1;
        for (i = n - 2; i >= 0; i--)
            if (nums[i] <= nums[i + 1])
                right[i] = right[i + 1] + 1;
        ans = min(n, *max_element(left.begin(), left.end()) + 1);
        for (i = 1; i < n - 1; i++)
            if (nums[i - 1] <= nums[i + 1])
                ans = max(ans, left[i - 1] + 1 + right[i + 1]);
        return ans;
    }
};
```
