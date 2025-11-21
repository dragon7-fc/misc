3755. Find Maximum Balanced XOR Subarray Length

Given an integer array `nums`, return the length of the longest **subarray** that has a bitwise XOR of zero and contains an equal number of even and odd numbers. If no such subarray exists, return `0`.

 

**Example 1:**
```
Input: nums = [3,1,3,2,0]

Output: 4

Explanation:

The subarray [1, 3, 2, 0] has bitwise XOR 1 XOR 3 XOR 2 XOR 0 = 0 and contains 2 even and 2 odd numbers.
```

**Example 2:**
```
Input: nums = [3,2,8,5,4,14,9,15]

Output: 8

Explanation:

The whole array has bitwise XOR 0 and contains 4 even and 4 odd numbers.
```

**Example 3:**
```
Input: nums = [0]

Output: 0

Explanation:

No non-empty subarray satisfies both conditions.
```
 

**Constraints:**

* `1 <= nums.length <= 10^5`
* `0 <= nums[i] <= 10^9`

# Submissions
---
**Solution 1: (Hash Table, Prefix Sum, 2 element key hash table)**
```
Runtime: 797 ms, Beats 21.05%
Memory: 351.00, MB Beats 67.65%
```
```c++
class Solution {
public:
    int maxBalancedSubarray(vector<int>& nums) {
        int n = nums.size();
        map<pair<int, int>, int> mp;
        int xr = 0, odd = 0, even = 0;
        int ans = 0;
        mp[{0, 0}] = -1;
        for (int i = 0; i < n; i++) {
            xr ^= nums[i];
            if (nums[i] % 2 == 0) {
                even++;
            } else {
                odd++;
            }
            int diff = odd - even;
            pair<int, int> key = {xr, diff};
            if (mp.count(key)) {
                ans = max(ans, i - mp[key]);
            } else {
                mp[key] = i;
            }
        }
        return ans;
    }
};
```
