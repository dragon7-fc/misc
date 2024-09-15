3290. Maximum Multiplication Score

You are given an integer array `a` of size 4 and another integer array `b` of size at least 4.

You need to choose 4 indices `i0`, `i1`, `i2`, and `i3` from the array `b` such that `i0 < i1 < i2 < i3`. Your score will be equal to the value `a[0] * b[i0] + a[1] * b[i1] + a[2] * b[i2] + a[3] * b[i3]`.

Return the **maximum** score you can achieve.

 

**Example 1:**
```
Input: a = [3,2,5,6], b = [2,-6,4,-5,-3,2,-7]

Output: 26

Explanation:
We can choose the indices 0, 1, 2, and 5. The score will be 3 * 2 + 2 * (-6) + 5 * 4 + 6 * 2 = 26.
```

**Example 2:**
```
Input: a = [-1,4,5,-2], b = [-5,-1,-3,-2,-4]

Output: -1

Explanation:
We can choose the indices 0, 1, 3, and 4. The score will be (-1) * (-5) + 4 * (-1) + 5 * (-2) + (-2) * (-4) = -1.
```
 

**Constraints:**

* `a.length == 4`
* `4 <= b.length <= 105`
* `-10^5 <= a[i], b[i] <= 10^5`

# Submissions
---
**Solution 1: (DP Top-Down)**
```
Runtime: 230 ms
Memory: 181.75 MB
```
```c++
class Solution {
    long long dfs(int i, int j, vector<vector<long long>> &dp, vector<int> &a, vector<int> &b, int n) {
        if (i == 4) {
            return 0;
        }
        if (j == n) {
            return INT_MIN;
        }
        if (dp[i][j] != INT_MIN) {
            return dp[i][j];
        }
        long long rst = INT_MIN;
        rst = max(rst, dfs(i, j+1, dp, a, b, n));
        rst = max(rst, (long long)a[i]*b[j] + dfs(i+1, j+1, dp, a, b, n));
        dp[i][j] = rst;
        return rst;
    }
public:
    long long maxScore(vector<int>& a, vector<int>& b) {
        int n = b.size();
        vector<vector<long long>> dp(4, vector<long long>(n, INT_MIN));
        return dfs(0, 0, dp, a, b, n);
    }
};
```

**Solution 2: (DP Bottom-Up)**
```
Runtime: 134 ms
Memory: 128.26 MB
```
```c++
class Solution {
public:
    long long maxScore(vector<int>& a, vector<int>& b) {
        vector<long long> t(4, INT_MIN);
        for (long long num : b) {
            t[3] = max(t[3], t[2] + num * a[3]);
            t[2] = max(t[2], t[1] + num * a[2]);
            t[1] = max(t[1], t[0] + num * a[1]);
            t[0] = max(t[0], num * a[0]);
        }
        return t[3];
    }
};
```
