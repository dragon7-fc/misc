3660. Jump Game IX

You are given an integer array `nums`.

From any index `i`, you can jump to another index `j` under the following rules:

* Jump to index `j` where `j > i` is allowed only if `nums[j] < nums[i]`.
* Jump to index `j` where `j < i` is allowed only if `nums[j] > nums[i]`.

For each index `i`, find the maximum value in nums that can be reached by following any sequence of valid jumps starting at `i`.

Return an array `ans` where `ans[i]` is the maximum value reachable starting from index i.

 

**Example 1:**
```
Input: nums = [2,1,3]

Output: [2,2,3]

Explanation:

For i = 0: No jump increases the value.
For i = 1: Jump to j = 0 as nums[j] = 2 is greater than nums[i].
For i = 2: Since nums[2] = 3 is the maximum value in nums, no jump increases the value.
Thus, ans = [2, 2, 3].
```

**Example 2:**
```
Input: nums = [2,3,1]

Output: [3,3,3]

Explanation:

For i = 0: Jump forward to j = 2 as nums[j] = 1 is less than nums[i] = 2, then from i = 2 jump to j = 1 as nums[j] = 3 is greater than nums[2].
For i = 1: Since nums[1] = 3 is the maximum value in nums, no jump increases the value.
For i = 2: Jump to j = 1 as nums[j] = 3 is greater than nums[2] = 1.
Thus, ans = [3, 3, 3].
```
 

**Constraints:**

* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^9`

# Submissions
---
**Solution 1: (Prefix Sum)**

          v  v
    5  2  1  8  3
          ^i
    <-----
    ------------>
             <---

```
Runtime: 6 ms, Beats 87.50%
Memory: 227.33 MB, Beats 12.50%
```
```c++
class Solution {
public:
    vector<int> maxValue(vector<int>& nums) {
        int n = nums.size();
        vector<int> pre(n), suff(n), res(n);

        pre[0] = nums[0], suff[n - 1] = nums[n - 1];
        for (int i = 1; i < n; i++) {
            pre[i] = max(nums[i], pre[i - 1]);
        }

        for (int i = n - 2; i >= 0; i--) {
            suff[i] = min(nums[i], suff[i + 1]);
        }

        res[n - 1] = pre[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            res[i] = pre[i];
            if (pre[i] > suff[i + 1]) {
                res[i] = res[i + 1];
            }
        }
        return res;
    }
};
```
