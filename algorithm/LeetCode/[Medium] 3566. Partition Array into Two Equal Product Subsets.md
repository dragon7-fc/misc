3566. Partition Array into Two Equal Product Subsets

You are given an integer array `nums` containing **distinct** positive integers and an integer `target`.

Determine if you can partition `nums` into two **non-empty disjoint subsets**, with each element belonging to **exactly one** subset, such that the product of the elements in each subset is equal to `target`.

Return `true` if such a partition exists and `false` otherwise.

A **subset** of an array is a selection of elements of the array.
 

**Example 1:**
```
Input: nums = [3,1,6,8,4], target = 24

Output: true

Explanation: The subsets [3, 8] and [1, 6, 4] each have a product of 24. Hence, the output is true.
```

**Example 2:**
```
Input: nums = [2,5,3,7], target = 15

Output: false

Explanation: There is no way to partition nums into two non-empty disjoint subsets such that both subsets have a product of 15. Hence, the output is false.
```
 

Constraints:

* `3 <= nums.length <= 12`
* `1 <= target <= 10^15`
* `1 <= nums[i] <= 10^0`
* All elements of nums are **distinct**.

# Submissions
---
**Solution 1: (Brute Force)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 23.63 MB, Beats 25.00%
```
```c++
class Solution {
public:
    bool checkEqualPartitions(vector<int>& nums, long long target) {
        int n = nums.size(), i, j;
        bool flag;
        long long a, b;
        for (i = 0; i < (1<<n); i ++) {
            a = target;
            b = target;
            flag = true;
            for (j = 0; j < n; j ++) {
                if ((1<<j) & i) {
                    if (a%nums[j] == 0) {
                        a /= nums[j];
                    } else {
                        flag = false;
                        break;
                    }
                } else {
                    if (b%nums[j] == 0) {
                        b /= nums[j];
                    } else {
                        flag = false;
                        break;
                    }
                }
            }
            if (!flag) {
                continue;
            }
            if (a == 1 && b == 1) {
                return true;
            }
        }
        return false;
    }
};
```
