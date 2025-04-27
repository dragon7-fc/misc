3284. Sum of Consecutive Subarrays

We call an array `arr` of length `n` consecutive if one of the following holds:

* `arr[i] - arr[i - 1] == 1 for all 1 <= i < n.`
* `arr[i] - arr[i - 1] == -1 for all 1 <= i < n.`

The **value** of an array is the sum of its elements.

For example, `[3, 4, 5]` is a consecutive array of value `12` and `[9, 8]` is another of value `17`. While `[3, 4, 3]` and `[8, 6]` are not consecutive.

Given an array of integers `nums`, return the sum of the values of all consecutive subarrays.

Since the answer may be very large, return it **modulo** `10^9 + 7`.

**Note** that an array of length 1 is also considered consecutive.

 

**Example 1:**
```
Input: nums = [1,2,3]

Output: 20

Explanation:

The consecutive subarrays are: [1], [2], [3], [1, 2], [2, 3], [1, 2, 3].
Sum of their values would be: 1 + 2 + 3 + 3 + 5 + 6 = 20.
```

**Example 2:**
```
Input: nums = [1,3,5,7]

Output: 16

Explanation:

The consecutive subarrays are: [1], [3], [5], [7].
Sum of their values would be: 1 + 3 + 5 + 7 = 16.
```

**Example 3:**
```
Input: nums = [7,6,1,2]

Output: 32

Explanation:

The consecutive subarrays are: [7], [6], [1], [2], [7, 6], [1, 2].
Sum of their values would be: 7 + 6 + 1 + 2 + 13 + 3 = 32.
```
 

**Constraints:**

* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^5`

# Submissions
---
**Solution 1: (Sliding Window)**

    1  2  3  4
    *  
       *
    *  *
          *
       *  *
    *  *  *
             *
          *  *
       *  *  *
    *  *  *  *

    1 + (1+2*2) + (5 + 3*3)

    1  2  3
cur 1  5  14
ans 1  6  20

```
Runtime: 0 ms, Beats 100.00%
Memory: 129.76 MB, Beats 36.36%
```
```c++
class Solution {
public:
    int getSum(vector<int>& nums) {
        int n = nums.size(), i = 0, j, MOD = 1e9 + 7;
        long long cur, ans = 0;
        while (i < n) {
            cur = nums[i];
            ans += cur;
            j = i+1;
            while (j < n && nums[j] - nums[j-1] == nums[i+1] - nums[i] && abs(nums[i+1] - nums[i]) == 1) {
                cur += 1LL*(j-i+1)*nums[j];
                cur %= MOD;
                ans += cur;
                ans %= MOD;
                j += 1;
            }
            if (j < n && abs(nums[j] - nums[j-1]) == 1 && nums[j] - nums[j-1] != nums[i+1] - nums[i]) {
                i = j-1;
                ans -= nums[i];
            } else {
                i = j;
            }
        }
        return ans;
    }
};
```
