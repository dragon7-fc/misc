3952. Maximum Total Value of Covered Indices

You are given an integer array `nums` of length `n` and a binary string `s` of length `n`, where `s[i] == '1'` means index `i` initially contains a token and `s[i] == '0'` means it does not.

You may perform the following operation any number of times:

* Choose a token currently located at index `i`, where `i > 0`, such that this token has not been moved before.
* Move this token from index `i` to index `i - 1`.

An index is considered covered if it contains a token after all moves.

Return an integer denoting the **maximum** total value of `nums` at the covered indices after optimally performing the operations.

 

**Example 1:**
```
Input: nums = [9,2,6,1], s = "0101"

Output: 15

Explanation:

Initially, indices 1 and 3 contain tokens.
Move the token from index 3 to index 2.
Move the token from index 1 to index 0.
The covered indices are [0, 2], so the total value is nums[0] + nums[2] = 9 + 6 = 15.
```

**Example 2:**
```
Input: nums = [5,1,4], s = "001"

Output: 4

Explanation:

Initially, only index 2 contains a token.
It is optimal to leave the token at index 2.
The covered index is [2], so the total value is nums[2] = 4.
```

**Example 3:**
```
Input: nums = [9,3,5], s = "011"

Output: 14

Explanation:

Initially, indices 1 and 2 contain tokens.
Move the token from index 1 to index 0.
The covered indices are [0, 2], so the total value is nums[0] + nums[2] = 9 + 5 = 14.
```

**Constraints:**

* `1 <= n == nums.length == s.length <= 10^5`
* `1 <= nums[i] <= 10^5`
* `s[i]` is either `'0'` or `'1'`

# Submissions
---
**Solution 1: (Greedy, Simulation)**
```
Runtime: 11 ms, Beats 66.67%
Memory: 190.51 MB, Beats 83.33%
```
```c++
class Solution {
public:
    long long maxTotal(vector<int>& nums, string s) {
        int n = nums.size();
        long long ans = 0;
        if (s[0] == '1') {
            ans += nums[0];
        }
        for (int i = 1; i < n; i ++) {
            if (s[i] == '1') {
                if (s[i - 1] == '0') {
                    ans += max(nums[i], nums[i - 1]);
                    nums[i] = min(nums[i], nums[i - 1]);
                    swap(s[i], s[i - 1]);
                } else {
                    ans += nums[i];
                }
            }
        }
        return ans;
    }
};
```
