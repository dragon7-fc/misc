3919. Minimum Cost to Move Between Indices

You are given an integer array `nums` where `nums` is **strictly increasing**.

For each index `x`, let `closest(x)` be the adjacent index such that `abs(nums[x] - nums[y])` is **minimized**. If both adjacent indices exist and give the same difference, choose the smaller index.

From any index `x`, you can move in two ways:

* To any index `y` with cost `abs(nums[x] - nums[y])`, or
* To `closest(x)` with cost 1.

You are also given a 2D integer array `queries`, where each `queries[i] = [li, ri]`.

For each query, calculate the **minimum total cost** to move from index `li` to index `ri`.

Return an integer array `ans`, where `ans[i]` is the answer for the `i`th query.

An array is said to be **strictly increasing** if each element is **strictly greater** than its previous one.

The **absolute difference** between two values `x` and `y` is defined as `abs(x - y)`.

 

**Example 1:**
```
Input: nums = [-5,-2,3], queries = [[0,2],[2,0],[1,2]]

Output: [6,2,5]

Explanation:

The closest indices are [1, 0, 1] respectively.
For [0, 2], the path 0 → 1 → 2 uses a closest move from index 0 to 1 with cost 1 and a move from index 1 to 2 with cost |-2 - 3| = 5, giving total 1 + 5 = 6.
For [2, 0], the path 2 → 1 → 0 uses two closest moves from index 2 to 1 and from index 1 to 0, each with cost 1, giving total 2.
For [1, 2], the direct move from index 1 to index 2 has cost |-2 - 3| = 5, which is optimal.
Thus, ans = [6, 2, 5].
```

**Example 2:**
```
Input: nums = [0,2,3,9], queries = [[3,0],[1,2],[2,0]]

Output: [4,1,3]

Explanation:

The closest indices are [1, 2, 1, 2] respectively.
For [3, 0], the path 3 → 2 → 1 → 0 uses closest moves from index 3 to 2 and from 2 to 1, each with cost 1, and a move from 1 to 0 with cost |2 - 0| = 2, giving total 1 + 1 + 2 = 4.
For [1, 2], the closest move from index 1 to 2 has cost 1.
For [2, 0], the path 2 → 1 → 0 uses a closest move from index 2 to 1 with cost 1 and a move from 1 to 0 with cost |2 - 0| = 2, giving total 1 + 2 = 3.
Thus, ans = [4, 1, 3].
```
 

**Constraints:**

* `2 <= nums.length <= 10^5`
* `-10^9 <= nums[i] <= 10^9`
* `nums` is strictly increasing
* `1 <= queries.length <= 10^5`
* `queries[i] = [li, ri]`
* `0 <= li, ri < nums.length`

# Submissions
---
**Solution 1: (Prefix Sum)**
```
Runtime: 9 ms, Beats 87.30%
Memory: 229.17 MB, Beats 82.57%
```
```c++
class Solution {
public:
    vector<int> minCost(vector<int>& nums, vector<vector<int>>& queries) {
        int m = nums.size(), n = queries.size(), i;
        vector<long long> left(m), right(m);
        vector<int> ans(n);
        for (i = 0; i < m - 1; i ++) {
            if (i == 0) {
                left[i + 1] = left[i] + 1;
            } else {
                if (nums[i + 1] - nums[i] < nums[i] - nums[i - 1]) {
                    left[i + 1] = left[i] + 1;
                } else {
                    left[i + 1] = left[i] + nums[i + 1] - nums[i];
                }
            }
        }
        for (i = m - 1; i > 0; i --) {
            if (i == m - 1) {
                right[i - 1] = right[i] + 1;
            } else {
                if (nums[i] - nums[i - 1] <= nums[i + 1] - nums[i]) {
                    right[i - 1] = right[i] + 1;
                } else {
                    right[i - 1] = right[i] + nums[i] - nums[i - 1];
                }
            }
        }
        for (i = 0; i < n; i ++) {
            auto &l = queries[i][0];
            auto &r = queries[i][1];
            if (r > l) {
                ans[i] = left[r] - left[l];
            } else {
                ans[i] = right[r] - right[l];
            }
        }
        return ans;
    }
};
```
