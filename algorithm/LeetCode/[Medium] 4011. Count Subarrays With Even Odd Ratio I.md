4011. Count Subarrays With Even Odd Ratio I

You are given an integer array `nums` and two integers `a` and `b`.

For a subarray, let:

* `x` be the number of even elements.
* `y` be the number of odd elements.

The ratio of even to odd elements in a subarray is defined as `x / y`, where ratios are compared by their exact rational values.

A subarray is considered **valid** if:

* `y > 0`, and
* `x / y <= a / b`.

Return the number of valid subarrays in `nums`.

 

**Example 1:**
```
Input: nums = [1,2,1,2], a = 3, b = 2

Output: 7

Explanation:

The following are the valid subarrays:

Subarray	Values	Even Count	Odd Count	Ratio
nums[0..0]	[1]	0	1	0 / 1
nums[0..1]	[1, 2]	1	1	1 / 1
nums[0..2]	[1, 2, 1]	1	2	1 / 2
nums[0..3]	[1, 2, 1, 2]	2	2	2 / 2
nums[1..2]	[2, 1]	1	1	1 / 1
nums[2..2]	[1]	0	1	0 / 1
nums[2..3]	[1, 2]	1	1	1 / 1
Thus, the number of valid subarrays is 7.
```

**Example 2:**
```
Input: nums = [2,2,1], a = 2, b = 1

Output: 3

Explanation:

The following are the valid subarrays:

Subarray	Values	Even Count	Odd Count	Ratio
nums[0..2]	[2, 2, 1]	2	1	2 / 1
nums[1..2]	[2, 1]	1	1	1 / 1
nums[2..2]	[1]	0	1	0 / 1
Thus, the number of valid subarrays is 3.
```

**Example 3:**
```
Input: nums = [2,2,2], a = 1, b = 1

Output: 0

Explanation:

Every subarray contains 0 odd numbers, so no subarray is valid.
```
 

**Constraints:**

* `1 <= nums.length <= 1000`
* `1 <= nums[i] <= 1000`
* `1 <= a, b <= 1000`

# Submissions
---
**Solution 1: (Brute Force)**
```
Runtime: 128 ms, Beats 5.19%
Memory: 29.74 MB, Beats 54.49%
```
```c++
class Solution {
public:
    int countRatioSubarrays(vector<int>& nums, int a, int b) {
        int n = nums.size();
        int ans = 0;
        for (int i = 0; i < n; i ++) {
            int cnt[2] = {0};
            for (int j = i; j < n; j ++) {
                cnt[nums[j] & 1] += 1;
                if (cnt[1] && b * cnt[0] <= a * cnt[1]) {
                    ans += 1;
                }
            }
        }
        return ans;
    }
};
```
