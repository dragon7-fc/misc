3819. Rotate Non Negative Elements

You are given an integer array `nums` and an integer `k`.

Rotate only the **non-negative** elements of the array to the left by `k` positions, in a cyclic manner.

All **negative** elements must stay in their original positions and must not move.

After rotation, place the **non-negative** elements back into the array in the new order, filling only the positions that originally contained non-negative values and skipping all negative positions.

Return the resulting array.

 

**Example 1:**
```
Input: nums = [1,-2,3,-4], k = 3

Output: [3,-2,1,-4]

Explanation:

The non-negative elements, in order, are [1, 3].
Left rotation with k = 3 results in:
[1, 3] -> [3, 1] -> [1, 3] -> [3, 1]
Placing them back into the non-negative indices results in [3, -2, 1, -4].
```

**Example 2:**
```
Input: nums = [-3,-2,7], k = 1

Output: [-3,-2,7]

Explanation:

The non-negative elements, in order, are [7].
Left rotation with k = 1 results in [7].
Placing them back into the non-negative indices results in [-3, -2, 7].
```

**Example 3:**
```
Input: nums = [5,4,-9,6], k = 2

Output: [6,5,-9,4]

Explanation:

The non-negative elements, in order, are [5, 4, 6].
Left rotation with k = 2 results in [6, 5, 4].
Placing them back into the non-negative indices results in [6, 5, -9, 4].
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `-10^5 <= nums[i] <= 10^5`
* `0 <= k <= 10^5`

# Submissions
---
**Solution 1: (Array)**
```
Runtime: 23 ms, Beats 70.89%
Memory: 314.49 MB, Beats 38.26%
```
```c++
class Solution {
public:
    vector<int> rotateElements(vector<int>& nums, int k) {
        vector<int> dp, dp2;
        for (auto &num: nums) {
            if (num >= 0) {
                dp.push_back(num);
            }
        }
        if (dp.size() == 0) {
            return nums;
        }
        dp2 = vector<int>(dp.begin() + (k % dp.size()), dp.end());
        dp2.insert(dp2.end(), dp.begin(), dp.begin() + (k % dp.size()));
        int i, j = 0, n = nums.size();
        for (i = 0; i < n; i ++) {
            if (nums[i] >= 0) {
                nums[i] = dp2[j];
                j += 1;
            }
        }
        return nums;
    }
};
```
