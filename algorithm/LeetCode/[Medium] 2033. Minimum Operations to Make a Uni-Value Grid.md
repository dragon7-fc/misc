2033. Minimum Operations to Make a Uni-Value Grid

You are given a 2D integer `grid` of size `m x n` and an integer `x`. In one operation, you can **add** `x` to or **subtract** `x` from any element in the `grid`.

A **uni-value grid** is a grid where all the elements of it are equal.

Return the **minimum** number of operations to make the grid **uni-value**. If it is not possible, return `-1`.

 

**Example 1:**
![img/2033_gridtxt.png](img/2033_gridtxt.png)
```
Input: grid = [[2,4],[6,8]], x = 2
Output: 4
Explanation: We can make every element equal to 4 by doing the following: 
- Add x to 2 once.
- Subtract x from 6 once.
- Subtract x from 8 twice.
A total of 4 operations were used.
```

**Example 2:**

![2033_gridtxt-1.png](img/2033_gridtxt-1.png)
```
Input: grid = [[1,5],[2,3]], x = 1
Output: 5
Explanation: We can make every element equal to 3.
```

**Example 3:**

![2033_gridtxt-2.png](img/2033_gridtxt-2.png)
```
Input: grid = [[1,2],[3,4]], x = 2
Output: -1
Explanation: It is impossible to make every element equal.
```

**Constraints:**

* `m == grid.length`
* `n == grid[i].length`
* `1 <= m, n <= 10^5`
* `1 <= m * n <= 10^5`
* `1 <= x, grid[i][j] <= 10^4`

# Submissions
---
**Solution 1: (Medium)**
```
Runtime: 1748 ms
Memory Usage: 49.5 MB
```
```python
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = sorted([v for row in grid for v in row])
        N = len(nums)
        mid_left = nums[N//2-1]
        mid_right = nums[N//2]
        left = 0
        for i in range(N):
            d, r = divmod(abs(mid_left - nums[i]), x)
            if r:
                return -1
            left += d
        right = 0
        for i in range(N):
            d, r = divmod(abs(mid_right - nums[i]), x)
            if r:
                return -1
            right += d
        return min(left, right)
```

**Solution 2: (DP)**
```
Runtime: 272 ms
Memory Usage: 90.2 MB
```
```c++
class Solution {
public:
    int minOperations(vector<vector<int>>& grid, int x) {
        int res = INT_MAX, ops = 0;
        vector<int> v, dp(grid.size() * grid[0].size());
        for (auto &row : grid)
            v.insert(end(v), begin(row), end(row));
        sort(begin(v), end(v));
        for (int i = 0; i < v.size() - 1; ++i) {
            if ((v[i + 1] - v[i]) % x)
                return -1;
            dp[i + 1] = dp[i] + (i + 1) * (v[i + 1] - v[i]) / x;
        }
        for (int i = v.size() - 1; i > 0; --i) {
            ops += (v.size() - i) * (v[i] - v[i - 1]) / x;
            res = min(res, ops + dp[i - 1]);
        }
        return res == INT_MAX ? 0 : res;
    }
};
``` 

**Solution 3: (Math, Medium)**

    a + px = b + qx
-> (a + px)%x = (b + qx)%x
-> a%x = b%x

```
Runtime: 63 ms, Beats 10.94%
Memory: 99.88 MB, Beats 6.38%
```
```c++
class Solution {
public:
    int minOperations(vector<vector<int>>& grid, int x) {
        int m, ans = 0;
        vector<int> dp;
        for (auto r: grid) {
            for (auto c: r) {
                dp.push_back(c);
            }
        }
        sort(dp.begin(), dp.end());
        m = dp[dp.size()/2];
        for (auto a: dp) {
            if (a%x != m%x) {
                return -1;
            }
            ans += abs(a-m)/x;
        }
        return ans;
    }
};
```

**Solution 4: (Sort, Prefix and Suffix Sums)**
```
Runtime: 39 ms, Beats 66.87%
Memory: 94.71 MB, Beats 10.64%
```
```c++
class Solution {
public:
    int minOperations(vector<vector<int>>& grid, int x) {
        // Initialize an empty array to store all numbers
        vector<int> numsArray;
        int result = INT_MAX;

        // Flatten the grid into numsArray and check if all elements have the
        // same remainder when divided by x
        for (int row = 0; row < grid.size(); row++) {
            for (int col = 0; col < grid[0].size(); col++) {
                // If remainder of any element doesn't match the first element,
                // return -1
                if (grid[row][col] % x != grid[0][0] % x) return -1;
                numsArray.push_back(grid[row][col]);
            }
        }

        // Sort numsArray in non-decreasing order to easily calculate operations
        sort(numsArray.begin(), numsArray.end());

        int length = numsArray.size();
        vector<int> prefixSum(length, 0);
        vector<int> suffixSum(length, 0);

        // Calculate the prefix sum up to each index (excluding the current
        // element)
        for (int index = 1; index < length; index++) {
            prefixSum[index] = prefixSum[index - 1] + numsArray[index - 1];
        }

        // Calculate the suffix sum from each index (excluding the current
        // element)
        for (int index = length - 2; index >= 0; index--) {
            suffixSum[index] = suffixSum[index + 1] + numsArray[index + 1];
        }

        // Iterate through numsArray to calculate the number of operations for
        // each potential common value
        for (int index = 0; index < length; index++) {
            int leftOperations =
                (numsArray[index] * index - prefixSum[index]) / x;

            int rightOperations =
                (suffixSum[index] - numsArray[index] * (length - index - 1)) /
                x;

            // Update the result with the minimum operations needed
            result = min(result, leftOperations + rightOperations);
        }

        return result;
    }
};
```

**Solution 5: (Sort, Two Pointers)**
```
Runtime: 39 ms, Beats 66.87%
Memory: 87.08 MB, Beats 72.64%
```
```c++
class Solution {
public:
    int minOperations(vector<vector<int>>& grid, int x) {
        // Initialize an empty array to store all numbers from the grid
        vector<int> numsArray;
        int result = 0;

        // Flatten the grid into numsArray
        for (int row = 0; row < grid.size(); row++) {
            for (int col = 0; col < grid[0].size(); col++) {
                // If any element has a different remainder than the first
                // element, it is impossible to make all elements equal, so
                // return -1
                if (grid[row][col] % x != grid[0][0] % x) return -1;
                numsArray.push_back(grid[row][col]);
            }
        }

        // Sort numsArray in non-decreasing order to facilitate efficient
        // operations
        sort(numsArray.begin(), numsArray.end());

        int length = numsArray.size();
        int prefixIndex = 0;
        int suffixIndex = length - 1;

        // Gradually move prefixIndex and suffixIndex towards the middle
        while (prefixIndex < suffixIndex) {
            // If the prefix of equal elements is shorter than the suffix
            if (prefixIndex < length - suffixIndex - 1) {
                // Calculate the number of operations required to extend the
                // prefix
                int prefixOperations =
                    (prefixIndex + 1) *
                    (numsArray[prefixIndex + 1] - numsArray[prefixIndex]) / x;

                result += prefixOperations;
                // Move the prefix index forward
                prefixIndex++;
            } else {
                // Calculate the number of operations required to extend the
                // suffix
                int suffixOperations =
                    (length - suffixIndex) *
                    (numsArray[suffixIndex] - numsArray[suffixIndex - 1]) / x;

                result += suffixOperations;
                // Move the suffix index backward
                suffixIndex--;
            }
        }

        return result;
    }
};
```

**Solution 6: (Sort, Prefix and Suffix Sums)**

      0  1  2  3  4
     --------------
      2  4  6  8
pre   0  2  6  12 20
suf  20 18 14  8  0
         ^
cur  (2*0 - pre[0])/2 +
     (suf[1] - 2*(4-1))/2 = 6
         (4*1 - 2)/2 +
         (14 - 4*2)/2 = 4

               /.
             /...
           /.....
    ------a......
        /........
      /..........
    /............
    ^^^^^  ^^^^^^
      pre    suf

```
Runtime: 56, ms Beats 19.76%
Memory: 96.84 MB, Beats 8.51%
```
```c++
class Solution {
public:
    int minOperations(vector<vector<int>>& grid, int x) {
        int m = grid.size(), n = grid[0].size(), i, j, a, b, ans = INT_MAX;
        vector<int> dp, pre(m*n + 1), suf(m*n + 1);
        for (i = 0; i < m; i ++) {
            for (j = 0; j < n; j ++) {
                if (grid[i][j]%x != grid[0][0]%x) {
                    return -1;
                }
                dp.push_back(grid[i][j]);
            }
        }
        sort(dp.begin(), dp.end());
        for (i = 0; i < m*n ; i ++) {
            pre[i+1] = pre[i] + dp[i];
        }
        for (i = m*n-1; i >= 0; i --) {
            suf[i] = suf[i+1] + dp[i];
        }
        for (i = 0; i < m*n; i ++) {
            a = (dp[i]*i - pre[i])/x;
            b = (suf[i] - dp[i]*(m*n-i))/x;
            ans = min(ans, a+b);
        }
        return ans;
    }
};
```

**Solution 7: (Sort, Two Pointers)**

      2   4   6   8
      ^i          ^j
      ----     ----
         1      1
            2
        a = (i+1)*(dp[i+1]-dp[i])/x
                b = (n-j)*(dp[j]-dp[j-])/x

```
Runtime: 47 ms, Beats 42.86%
Memory: 86.84 MB, Beats 81.76%
```
```c++
class Solution {
public:
    int minOperations(vector<vector<int>>& grid, int x) {
        int m = grid.size(), n = grid[0].size(), i, j, a, b, ans = 0;
        vector<int> dp;
        for (i = 0; i < m; i ++) {
            for (j = 0; j < n; j ++) {
                if (grid[i][j]%x != grid[0][0]%x) {
                    return -1;
                }
                dp.push_back(grid[i][j]);
            }
        }
        sort(dp.begin(), dp.end());
        i = 0;
        j = m*n-1;
        while (i < j) {
            if (i <= m*n-1-j) {
                a = (i+1) * (dp[i+1]-dp[i]) / x;
                ans += a;
                i += 1;
            } else {
                b = (m*n-j) * (dp[j]-dp[j-1]) / x;
                ans += b;
                j -= 1;
            }
        }
        return ans;
    }
};
```
