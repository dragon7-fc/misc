3356. Zero Array Transformation II

You are given an integer array `nums` of length `n` and a 2D array `queries` where `queries[i] = [li, ri, vali]`.

Each `queries[i]` represents the following action on nums:

* Decrement the value at each index in the range `[li, ri]` in `nums` by at most `vali`.
* The amount by which each value is decremented can be chosen **independently** for each index.
* A **Zero Array** is an array with all its elements equal to `0`.

Return the **minimum** possible non-negative value of `k`, such that after processing the first `k` queries in **sequence**, `nums` becomes a **Zero Array**. If no such `k` exists, return `-1`.

 

**Example 1:**
```
Input: nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]]

Output: 2

Explanation:

For i = 0 (l = 0, r = 2, val = 1):
Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
The array will become [1, 0, 1].
For i = 1 (l = 0, r = 2, val = 1):
Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
The array will become [0, 0, 0], which is a Zero Array. Therefore, the minimum value of k is 2.
```

**Example 2:**
```
Input: nums = [4,3,2,1], queries = [[1,3,2],[0,2,1]]

Output: -1

Explanation:

For i = 0 (l = 1, r = 3, val = 2):
Decrement values at indices [1, 2, 3] by [2, 2, 1] respectively.
The array will become [4, 1, 0, 0].
For i = 1 (l = 0, r = 2, val = 1):
Decrement values at indices [0, 1, 2] by [1, 1, 0] respectively.
The array will become [3, 0, 0, 0], which is not a Zero Array.
```

**Constraints:**

`1 <= nums.length <= 10^5`
`0 <= nums[i] <= 5 * 10^5`
`1 <= queries.length <= 10^5`
`queries[i].length == 3`
`0 <= li <= ri < nums.length`
`1 <= vali <= 5`

# Submissions
---
**Solution 1: (Binary Search)**

     2 0 2
     ^     -
     ^     -
     2     -2
cur  2 2 2  0
     0 
    [0,2,1],  <lr
    [0,2,1],  <ans
    [1,1,3]   

    4 3 2 1
      1     -
    1     -

    [1,3,2],
    [0,2,1]
```
Runtime: 71 ms, Beats 41.44%
Memory: 345.96 MB, Beats 43.49%
```
```c++
class Solution {
    bool check(int mid, vector<int> &nums, vector<vector<int>> &queries) {
        int m = nums.size(), n = queries.size(), i, cur = 0;
        vector<int> dp(m + 1);
        for (i = 0; i <= mid; i ++) {
            dp[queries[i][0]] += queries[i][2];
            dp[queries[i][1] + 1] -= queries[i][2];
        }
        for (i = 0; i < m; i ++) {
            cur += dp[i];
            if (cur < nums[i]) {
                return false;
            }
        }
        return true;
    }
public:
    int minZeroArray(vector<int>& nums, vector<vector<int>>& queries) {
        int n = queries.size(), left = -1, right = n-1, mid, ans = n + 1;
        while (left <= right) {
            mid = left + (right-left)/2;
            if (!check(mid, nums, queries)) {
                left = mid + 1;
            } else {
                ans = mid + 1;
                right = mid - 1;
            }
        }
        return ans != n+1 ? ans : -1;
    }
};
```

**Solution 2: (Line sweep)**

      0, 8
cur 0 0
dp       4 -4
         5 -5
         9 -9
    [[0,1,4],[0,1,1],[0,1,4],[0,1,1],[1,1,5],[0,1,2],[1,1,4],[0,1,1],[1,1,3],[0,0,2],[1,1,3],[1,1,2],[0,1,5],[1,1,2],[1,1,5]]
        ^

```
Runtime: 4 ms, Beats 91.44%
Memory: 323.11 MB, Beats 68.66%
```
```c++
class Solution {
public:
    int minZeroArray(vector<int>& nums, vector<vector<int>>& queries) {
        int m = nums.size(), n = queries.size(), i = 0, j = 0, cur = 0;
        vector<int> dp(m+1);
        while (i < m) {
            while (j < n && cur + dp[i] < nums[i]) {
                if (queries[j][1] >= i) {
                    dp[max(i, queries[j][0])] += queries[j][2];
                    dp[queries[j][1] + 1] -= queries[j][2];
                }
                j += 1;
            }
            cur += dp[i];
            if (cur < nums[i]) {
                return -1;
            }
            i += 1;
        }
        return j;
    }
};
```
