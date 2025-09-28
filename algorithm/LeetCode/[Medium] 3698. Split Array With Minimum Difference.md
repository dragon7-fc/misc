3698. Split Array With Minimum Difference

You are given an integer array `nums`.

Split the array into exactly two subarrays, `left` and `right`, such that `left` is **strictly increasing** and `right` is **strictly decreasing**.

Return the **minimum possible absolute difference** between the sums of `left` and `right`. If no valid split exists, return `-1`.

 

**Example 1:**
```
Input: nums = [1,3,2]

Output: 2

Explanation:

i	left	right	Validity	left sum	right sum	Absolute difference
0	[1]	[3, 2]	Yes	1	5	|1 - 5| = 4
1	[1, 3]	[2]	Yes	4	2	|4 - 2| = 2
Thus, the minimum absolute difference is 2.
```

**Example 2:**
```
Input: nums = [1,2,4,3]

Output: 4

Explanation:

i	left	right	Validity	left sum	right sum	Absolute difference
0	[1]	[2, 4, 3]	No	1	9	-
1	[1, 2]	[4, 3]	Yes	3	7	|3 - 7| = 4
2	[1, 2, 4]	[3]	Yes	7	3	|7 - 3| = 4
Thus, the minimum absolute difference is 4.
```

**Example 3:**
```
Input: nums = [3,1,2]

Output: -1

Explanation:

No valid split exists, so the answer is -1.
```
 

**Constraints:**

* `2 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^5`

# Submissions
---
**Solution 1: (Prefix Sum)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 184.21 MB, Beats 68.30%
```
```c++
class Solution {
public:
    long long splitArray(vector<int>& nums) {
        int n = nums.size(), i;
        vector<long long> dp(n);
        long long a = 0, ans = LONG_LONG_MAX;
        dp[n - 1] = nums[n - 1];
        for (i = n - 2; i >= 0; i --) {
            if (nums[i] > nums[i + 1]) {
                dp[i] = nums[i] + dp[i + 1];
            } else {
                break;
            }
        }
        a = 0;
        i = 0;
        while (i == 0 || i < n - 1 && nums[i] > nums[i - 1]) {
            a += nums[i];
            if (dp[i + 1]) {
                ans = min(ans, abs(a - dp[i + 1]));
            }
            i += 1;
        }
        if (ans != LONG_LONG_MAX) {
            return ans;
        }
        return -1;
    }
};
```
