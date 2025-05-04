3344. Maximum Sized Array

Given a positive integer `s`, let A be a 3D array of dimensions `n × n × n`, where each element `A[i][j][k]` is defined as:

* `A[i][j][k] = i * (j OR k)`, where `0 <= i, j, k < n`.

Return the **maximum** possible value of `n` such that the **sum** of all elements in array A does not exceed `s`.

 

**Example 1:**
```
Input: s = 10

Output: 2

Explanation:

Elements of the array A for n = 2:
A[0][0][0] = 0 * (0 OR 0) = 0
A[0][0][1] = 0 * (0 OR 1) = 0
A[0][1][0] = 0 * (1 OR 0) = 0
A[0][1][1] = 0 * (1 OR 1) = 0
A[1][0][0] = 1 * (0 OR 0) = 0
A[1][0][1] = 1 * (0 OR 1) = 1
A[1][1][0] = 1 * (1 OR 0) = 1
A[1][1][1] = 1 * (1 OR 1) = 1
The total sum of the elements in array A is 3, which does not exceed 10, so the maximum possible value of n is 2.
```

**Example 2:**
```
Input: s = 0

Output: 1

Explanation:

Elements of the array A for n = 1:
A[0][0][0] = 0 * (0 OR 0) = 0
The total sum of the elements in array A is 0, which does not exceed 0, so the maximum possible value of n is 1.
```

**Constraints:**

`0 <= s <= 10^15`

# Submissions
---
**Solution 1: (Math, Binary Search)**

We can pre-compute sum of 2D matrix A[j][k] for 0 < j, k <= m in dp[m]. We can re-use the sum of m - 1 matrix to make it efficient.

> What is the maximum m we can have? The sum of 3D matrix of size m is approximatelly m ^ 5.
> So, the max m is about a fifth root of 10 ^ 15, which is 1,000 (experimentally, 1,200 is enough).

Then, the sum of 3D matrix of size m would be sum(0..m - 1) * dp[m - 1].

We can binary-search for the maximum m where the sum does not exceed s.

The complexity of this solution is amortized O(log m), where m is ~sqrt(5, n), with one-time precomputation of O(m ^ 2).

```
Runtime: 0 ms, Beats 100.00%
Memory: 8.22 MB, Beats 50.00%
```
```c++
long long dp[1200] = { 0, 0 };
class Solution {
public:
    int maxSizedArray(long long s) {
        if (dp[1] == 0)
            for (int m = 1; m < 1200; ++m) {
                int sum_row = 0;
                for (int k = 0; k < m; ++k)
                    sum_row += k | m;
                dp[m] = dp[m - 1] + 2 * sum_row + m;
                dp[m - 1] *= m * (m - 1) / 2;
            }
        return upper_bound(begin(dp), end(dp), s) - begin(dp);
    }
};
```
