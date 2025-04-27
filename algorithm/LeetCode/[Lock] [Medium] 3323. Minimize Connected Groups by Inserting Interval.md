3323. Minimize Connected Groups by Inserting Interval

You are given a 2D array `intervals`, where `intervals[i] = [starti, endi]` represents the start and the end of interval i. You are also given an integer `k`.

You must add exactly one new interval `[startnew, endnew]` to the array such that:

* The length of the new interval, `endnew - startnew`, is at most `k`.
* After adding, the number of connected groups in intervals is minimized.

A **connected group** of intervals is a maximal collection of intervals that, when considered together, cover a continuous range from the smallest point to the largest point with no gaps between them. Here are some examples:

* A group of intervals `[[1, 2], [2, 5], [3, 3]]` is connected because together they cover the range from 1 to 5 without any gaps.
* However, a group of intervals `[[1, 2], [3, 4]]` is not connected because the segment `(2, 3)` is not covered.

Return the **minimum** number of connected groups after adding **exactly one** new interval to the array.

 

**Example 1:**
```
Input: intervals = [[1,3],[5,6],[8,10]], k = 3

Output: 2

Explanation:

After adding the interval [3, 5], we have two connected groups: [[1, 3], [3, 5], [5, 6]] and [[8, 10]].
```

**Example 2:**
```
Input: intervals = [[5,10],[1,1],[3,3]], k = 1

Output: 3

Explanation:

After adding the interval [1, 1], we have three connected groups: [[1, 1], [1, 1]], [[3, 3]], and [[5, 10]].
```
 

**Constraints:**

* `1 <= intervals.length <= 10^5`
* `intervals[i] == [starti, endi]`
* `1 <= starti <= endi <= 10^9`
* `1 <= k <= 10^9`

# Submissions
---
**Solution 1: (Sort, Sliding Window)**

        1  2  3  4
        xxxx  xxxx

        1  2  3  4  5  6  7  8  9  10
        xxxxxxx     xxxx     xxxxxxxx
              -------
        ^i                     ^j

        x     x     xxxxxxxxxxxxxxxxxx

        xx xxxx   xxxx xxxx
            xxxxx  xx
              xx
                ---------

        [1,3],[15,16],[11,16],[10,15],[14,18],[7,9],[4,5], k = 1

        1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18
        xxxxxxx  xxxx                                  xxxxxx
                                       xxxxxxxxxxxxxxxxxxxxxx
                                   xxxxxxxxxxxxxxxxxxxxxx
                                                   xxxxxxxxxxxxxxxxxx
                          xxxxxxx
    ---------------------------------------------------------------------
        xxxxxxx  xxxx     xxxxxxx  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx 
        ^i        ^j

```
Runtime: 179 ms, Beats 69.23%
Memory: 196.28 MB, Beats 61.54%
```
```c++
class Solution {
public:
    int minConnectedGroups(vector<vector<int>>& intervals, int k) {
        int n, i, j, ans;
        vector<vector<int>> dp;
        sort(intervals.begin(), intervals.end());
        for (i = 0; i < intervals.size(); i ++) {
            if (dp.size() && dp.back()[1] >= intervals[i][0]) {
                dp.back()[1] = max(dp.back()[1], intervals[i][1]);
            } else {
                dp.push_back(intervals[i]);
            }
        }
        n = dp.size();
        ans = n;
        j = 0;
        for (i = 0; i < n; i ++) {
            while (j < n && dp[j][0] - dp[i][1] <= k) {
                j += 1;
            }
            ans = min(ans, i + 1 + n - j);
        }
        return ans;
    }
};
```
