3618. Split Array by Prime Indices

You are given an integer array `nums`.

Split `nums` into two arrays `A` and `B` using the following rule:

* Elements at **prime** indices in `nums` must go into array `A`.
* All other elements must go into array `B`.

Return the absolute difference between the sums of the two arrays: `|sum(A) - sum(B)|`.

**Note**: An empty array has a sum of 0.

 

**Example 1:**
```
Input: nums = [2,3,4]

Output: 1

Explanation:

The only prime index in the array is 2, so nums[2] = 4 is placed in array A.
The remaining elements, nums[0] = 2 and nums[1] = 3 are placed in array B.
sum(A) = 4, sum(B) = 2 + 3 = 5.
The absolute difference is |4 - 5| = 1.
```

**Example 2:**
```
Input: nums = [-1,5,7,0]

Output: 3

Explanation:

The prime indices in the array are 2 and 3, so nums[2] = 7 and nums[3] = 0 are placed in array A.
The remaining elements, nums[0] = -1 and nums[1] = 5 are placed in array B.
sum(A) = 7 + 0 = 7, sum(B) = -1 + 5 = 4.
The absolute difference is |7 - 4| = 3.
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `-10^9 <= nums[i] <= 10^9`

# Submissions
---
**Solution 1: (Math)**
```
Runtime: 8 ms, Beats 83.49%
Memory: 131.28 MB, Beats 7.14%
```
```c++
class Solution {
public:
    long long splitArray(vector<int>& nums) {
        int n = nums.size(), i, j;
        if (n < 2) {
            return abs(accumulate(nums.begin(), nums.end(), 0));
        }
        long long a = 0, b = 0;
        vector<int> dp(n);
        dp[0] = 1;
        dp[1] = 1;
        for (i = 2; i <= sqrt(n); i ++) {
            if (dp[i] == 0) {
                for (j = i+i; j < n; j += i) {
                    dp[j] = 1;
                }
            }
        }
        for (i = 0; i < n; i ++) {
            if (dp[i] == 0) {
                a += nums[i];
            } else {
                b += nums[i];
            }
        }
        return abs(a - b);
    }
};
```
