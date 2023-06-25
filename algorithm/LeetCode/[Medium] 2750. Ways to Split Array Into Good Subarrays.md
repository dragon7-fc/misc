2750. Ways to Split Array Into Good Subarrays

You are given a binary array `nums`.

A subarray of an array is **good** if it contains **exactly one** element with the value `1`.

Return an integer denoting the number of ways to split the array `nums` into **good** subarrays. As the number may be too large, return it modulo `109 + 7`.

A subarray is a contiguous **non-empty** sequence of elements within an array.

 

**Example 1:**
```
Input: nums = [0,1,0,0,1]
Output: 3
Explanation: There are 3 ways to split nums into good subarrays:
- [0,1] [0,0,1]
- [0,1,0] [0,1]
- [0,1,0,0] [1]
```

**Example 2:**
```
Input: nums = [0,1,0]
Output: 1
Explanation: There is 1 way to split nums into good subarrays:
- [0,1,0]
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `0 <= nums[i] <= 1`

# Submissions
---
**Solution 1: (Greedy, Multiply all zero counts between 1's)**
```
Runtime: 318 ms
Memory: 235.2 MB
```
```c++
class Solution {
public:
    int numberOfGoodSubarraySplits(vector<int>& nums) {
        long long ans = 1, m = 1000000007, zero  = 0;
        int i = 0;
        while(i < nums.size() && nums[i] == 0) ++i;
        if(i >= nums.size() ) return 0;
        while (i < nums.size()) {
            if (nums[i] == 1) {
                ans = (ans * (zero + 1))%m;
                zero = 0;
            } else {
                zero++;
            }
            i++;
        }
        return ans;
    }
};
```
