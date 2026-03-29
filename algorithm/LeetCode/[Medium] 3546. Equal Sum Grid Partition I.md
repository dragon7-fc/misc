3546. Equal Sum Grid Partition I

You are given an `m x n` matrix `grid` of positive integers. Your task is to determine if it is possible to make either one horizontal or one vertical cut on the grid such that:

* Each of the two resulting sections formed by the cut is **non-empty**.
* The sum of the elements in both sections is **equal**.

Return `true` if such a partition exists; otherwise return `false`.

 

**Example 1:**
```
Input: grid = [[1,4],[2,3]]

Output: true

Explanation:
```
![3546_lc.jpeg](img/3546_lc.jpeg)
```
A horizontal cut between row 0 and row 1 results in two non-empty sections, each with a sum of 5. Thus, the answer is true.
```

**Example 2:**
```
Input: grid = [[1,3],[2,4]]

Output: false

Explanation:

No horizontal or vertical cut results in two non-empty sections with equal sums. Thus, the answer is false.
```
 

**Constraints:**

* `1 <= m == grid.length <= 10^5`
* `1 <= n == grid[i].length <= 10^5`
* `2 <= m * n <= 10^5`
* `1 <= grid[i][j] <= 10^5`

# Submissions
---
**Solution 1: (Prefix Sum)**
```
Runtime: 4 ms, Beats 91.73%
Memory: 126.43 MB, Beats 85.61%
```
```c++
class Solution {
public:
    bool canPartitionGrid(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size(), i, j;
        long long left, right = 0, target;
        for (i = 0; i < m; i ++) {
            for (j = 0; j < n; j ++) {
                right += grid[i][j];
            }
        }
        if (right % 2) {
            return false;
        }
        target = right / 2;
        left = 0;
        for (i = 0; i < m - 1; i ++) {
            for (j = 0; j < n; j ++) {
                left += grid[i][j];
            }
            if (left == target) {
                return true;
            } else if (left > target) {
                break;
            }
        }
        left = 0;
        for (j = 0; j < n - 1; j ++) {
            for (i = 0; i < m; i ++) {
                left += grid[i][j];
            }
            if (left == target) {
                return true;
            } else if (left > target) {
                break;
            }
        }
        return false;
    }
};
```
