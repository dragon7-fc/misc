3334. Find the Maximum Factor Score of Array

You are given an integer array `nums`.

The **factor score** of an array is defined as the product of the LCM and GCD of all elements of that array.

Return the **maximum factor score** of `nums` after removing **at most** one element from it.

**Note** that both the LCM and GCD of a single number are the number itself, and the factor score of an **empty** array is 0.

The term `lcm(a, b)` denotes the **least common multiple** of `a` and `b`.

The term `gcd(a, b)` denotes the **greatest common divisor** of `a` and `b`.

 

**Example 1:**
```
Input: nums = [2,4,8,16]

Output: 64

Explanation:

On removing 2, the GCD of the rest of the elements is 4 while the LCM is 16, which gives a maximum factor score of 4 * 16 = 64.
```

**Example 2:**
```
Input: nums = [1,2,3,4,5]

Output: 60

Explanation:

The maximum factor score of 60 can be obtained without removing any elements.
```

**Example 3:**
```
Input: nums = [3]

Output: 9
```
 

**Constraints:**

* `1 <= nums.length <= 100`
* `1 <= nums[i] <= 30`

# Submissions
---
**Solution 1: (Prefix Sum)**
```
Runtime: 3 ms
Memory: 25.60 MB
```
```c++
class Solution {
public:
    long long maxScore(vector<int>& nums) {
        int n =nums.size();
        long long dp[n], dp2[n], left = 0, left2, ans = 0;
        dp[n-1] = dp2[n-1] = nums[n-1];
        for (int i = n-2; i >= 0; i --) {
            dp[i] = gcd(nums[i], dp[i+1]);
            dp2[i] = lcm(nums[i], dp2[i+1]);
        }
        ans = max(ans, dp[0]*dp2[0]);
        for (int i = 0; i < n; i ++) {
            if (i && i < n-1) {
                ans = max(ans, gcd(left, dp[i+1]) * lcm(left2, dp2[i+1]));
                left = gcd(left, nums[i]);
                left2 = lcm(left2, nums[i]);
            } else if (i == n-1) {
                ans = max(ans, left*left2);
            } else {
                ans = max(ans, dp[i+1] * dp2[i+1]);
                left = nums[i];
                left2 = nums[i];
            }
            
        }
        return ans;
    }
};
```
