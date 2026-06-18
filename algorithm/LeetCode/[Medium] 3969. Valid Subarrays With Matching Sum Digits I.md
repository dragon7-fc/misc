3969. Valid Subarrays With Matching Sum Digits I

You are given an integer array `nums` and an integer digit `x`.

A subarray `nums[l..r]` is considered **valid** if the sum of its elements satisfies both of the following conditions:

* The first digit of the sum is equal to `x`.
* The last digit of the sum is equal to `x`.

Return the number of valid subarrays.

 

**Example 1:**
```
Input: nums = [1,100,1], x = 1

Output: 4

Explanation:

The valid subarrays are:

nums[0..0]: sum = 1
nums[0..1]: sum = 1 + 100 = 101
nums[1..2]: sum = 100 + 1 = 101
nums[2..2]: sum = 1
Thus, the answer is 4.
```

**Example 2:**
```
Input: nums = [1], x = 2

Output: 0

Explanation:

The only subarray is nums[0..0] with a sum of 1, which does not satisfy the conditions.

Thus, the answer is 0.
```
 

**Constraints:**

* `1 <= nums.length <= 1500`
* `1 <= nums[i] <= 10^9`
* `1 <= x <= 9`

# Submissions
---
**Solution 1: (Brute Force)**
```
Runtime: 185 ms, Beats 52.85%
Memory: 32.51 MB, Beats 33.66%
```
```c++
class Solution {
public:
    int countValidSubarrays(vector<int>& nums, int x) {
        int n = nums.size();
        int ans = 0;
        for (int i = 0; i < n; i ++) {
            long long sum = 0;
            for (int j = i; j < n; j ++) {
                sum += nums[j];
                int last = sum % 10;
                if (last != x) {
                    continue;
                }
                long long t = sum;
                int first;
                while (t) {
                    first = t % 10;
                    t /= 10;
                }
                if (first == x) {
                    ans += 1;
                }
            }
        }
        return ans;
    }
};
```
