3858. Minimum Bitwise OR From Grid

You are given a 2D integer array `grid` of size `m x n`.

You must select **exactly** one integer from each row of the `grid`.

Return an integer denoting the **minimum** possible bitwise OR of the selected integers from each row.

 

**Example 1:**
```
Input: grid = [[1,5],[2,4]]

Output: 3

Explanation:

Choose 1 from the first row and 2 from the second row.
The bitwise OR of 1 | 2 = 3, which is the minimum possible.
```

**Example 2:**
```
Input: grid = [[3,5],[6,4]]

Output: 5

Explanation:

Choose 5 from the first row and 4 from the second row.
The bitwise OR of 5 | 4 = 5, which is the minimum possible.
```

**Example 3:**
```
Input: grid = [[7,9,8]]

Output: 7

Explanation:

Choosing 7 gives the minimum bitwise OR.
```

**Constraints:**

* `1 <= m == grid.length <= 10^5`
`1 <= n == grid[i].length <= 10^5`
`m * n <= 10^5`
`1 <= grid[i][j] <= 10^5`

# Submissions
---
**Solution 1: (Bit Manipulation, High Bit to Low, try un-set every bit in every row)**

Intuition
Use a greedy strategy from the highest bit to the lowest bit.

Explanation
For each bit,
we check if it is possible to
achieve the target OR without setting it.

A bit must be included in the result
if there is at least one row
where every element contains either that bit
or a higher bit we already decided to skip.

By iterating from high to low,
we minimize the final result
by only setting bits that
are absolutely necessary to satisfy all rows.

Complexity
Time O(20mn)
Space O(1)

    grid = [[   1,   5],
          bi
    3  2  1  0
1:  0  0  0  1
5:  0  1  0  1
res          1
            [   2,   4]]
2:  0  0  1  0
4:  0  1  0  0
res       1
ans       1  1    

------------------------------
    grid = [[   3,   5],
    3  2  1  0
3:  0  0  1  1
5:  0  1  0  1
res          1
            [   6,   4]]
6:  0  1  1  0
4:  0  1  0  0
res    1
ans    1  0  1

```
Runtime: 4 ms, Beats 84.68%
Memory: 125.84 MB, Beats 75.62%
```
```c++
class Solution {
public:
    int minimumOR(vector<vector<int>>& grid) {
        int res = 0;
        for (int bi = 20; bi >= 0; --bi) {
            int b = 1 << bi;
            int mask = res | (b - 1);
            for (auto& r : grid) {
                bool row_all_bad = true;
                for (int a : r) {
                    if ((a & mask) == a) {
                        row_all_bad = false;
                        break;
                    }
                }
                if (row_all_bad) {
                    res |= b;
                    break;
                }
            }
        }
        return res;
    }
};
```
