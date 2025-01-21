3428. Maximum and Minimum Sums of at Most Size K Subsequences

You are given an integer array `nums` and a positive integer `k`. Return the sum of the **maximum** and **minimum** elements of all **subsequences** of `nums` with at most `k` elements.

Since the answer may be very large, return it modulo `10^9 + 7`.

 

**Example 1:**
```
Input: nums = [1,2,3], k = 2

Output: 24

Explanation:

The subsequences of nums with at most 2 elements are:

Subsequence	Minimum	Maximum	Sum
[1]	1	1	2
[2]	2	2	4
[3]	3	3	6
[1, 2]	1	2	3
[1, 3]	1	3	4
[2, 3]	2	3	5
Final Total	 	 	24
The output would be 24.
```

**Example 2:**
```
Input: nums = [5,0,6], k = 1

Output: 22

Explanation:

For subsequences with exactly 1 element, the minimum and maximum values are the element itself. Therefore, the total is 5 + 5 + 0 + 0 + 6 + 6 = 22.
```

**Example 3:**
```
Input: nums = [1,1,1], k = 2

Output: 12

Explanation:

The subsequences [1, 1] and [1] each appear 3 times. For all of them, the minimum and maximum are both 1. Thus, the total is 12.
```
 

**Constraints:**

* `1 <= nums.length <= 10^5`
* `0 <= nums[i] <= 10^9`
* `1 <= k <= min(100, nums.length)`

# Submissions
---
**Solution 1: (Combination)**
```
Runtime: 340 ms
Memory: 254.40 MB
```
```c++
class Solution {
public:
    int minMaxSums(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int ans = 0;
        int MOD = 1e9 + 7;
        vector<vector<int>> ncr(nums.size() + 1, vector<int> (k + 1,0));
        
        ncr[0][0] = 1;
        for (int n = 1; n <= nums.size(); n++) {
            ncr[n][0] = 1;
            for (int r = 1; r <= k; r++) 
                ncr[n][r] = (ncr[n - 1][r - 1] + ncr[n - 1][r]) % MOD;
        } 

        for(int n = 0; n < nums.size(); n ++) {
            int numberOfSubsequences = 0;
            for(int r = 0; r <= k - 1; r ++) 
                if(n >= r) numberOfSubsequences = (numberOfSubsequences + ncr[n][r]) % MOD;
            ans = (ans + (long long)(nums[n] + nums[nums.size() - n - 1]) * numberOfSubsequences) % MOD;
        }
        return ans;
    }
};
```
