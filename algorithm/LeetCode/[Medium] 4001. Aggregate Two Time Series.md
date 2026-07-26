4001. Aggregate Two Time Series

You are given two 2D integer arrays `series1` and `series2`.

Each element in both series is of the form `[timestamp, value]`, where:

* `timestamp` is an integer representing the time.
* `value` is an integer representing the value at that timestamp.

Each array is sorted in **strictly increasing** order of `timestamp`.

For any timestamp **not present** in a series, its value is taken from the **next available timestamp** in the same series if one exists. Otherwise, its value is considered 0.

The **aggregated series** is formed by summing the corresponding values from both series at every timestamp that appears in either series.

Return the **aggregated series** as a 2D integer array of `[timestamp, summedValue]` pairs, sorted in **strictly increasing** order of timestamp.

 

**Example 1:**
```
Input: series1 = [[1,3],[4,1]], series2 = [[2,2],[5,2]]

Output: [[1,5],[2,3],[4,3],[5,2]]

Explanation:

Timestamp	series1	series2	summedValue
1	3	2	5
2	1	2	3
4	1	2	3
5	0	2	2
Thus, the aggregated series is [[1, 5], [2, 3], [4, 3], [5, 2]].
```

**Example 2:**
```
Input: series1 = [[1,5],[3,1]], series2 = [[2,2]]

Output: [[1,7],[2,3],[3,1]]

Explanation:

Timestamp	series1	series2	summedValue
1	5	2	7
2	1	2	3
3	1	0	1
Thus, the aggregated series is [[1, 7], [2, 3], [3, 1]].
```

**Example 3:**
```
Input: series1 = [[1,5]], series2 = [[1000000000,2]]

Output: [[1,7],[1000000000,2]]

Explanation:

At timestamp 1, the next available value in series2 is 2 at timestamp 1000000000. At timestamp 1000000000, there is no later timestamp in series1, so its value is 0. Only timestamps that appear in at least one of the two series are included.
```
 

**Constraints:**

* `1 <= series1.length, series2.length <= 10^5`
* `series1[i].length == series2[i].length == 2`
* `1 <= series1[i][0], series2[i][0] <= 10^9`
* `1 <= series1[i][1], series2[i][1] <= 10^9`
* Each series is sorted in strictly increasing order of `timestamp`.

# Submissions
---
**Solution 1: (Greedy)**
```
Runtime: 81 ms, Beats 69.25%
Memory: 350.08 MB, Beats 95.59%
```
```c++
class Solution {
public:
    vector<vector<int>> aggregateTimeSeries(vector<vector<int>>& series1, vector<vector<int>>& series2) {
        int m = series1.size();
        int n = series2.size();
        int i = 0;
        int j = 0;
        vector<vector<int>> ans;
        while (i < m && j < n) {
            ans.push_back(vector<int>(2));
            ans.back()[1] = series1[i][1] + series2[j][1];
            if (series1[i][0] == series2[j][0]) {
                ans.back()[0] = series1[i][0];
                i += 1;
                j += 1;
            } else if (series1[i][0] < series2[j][0]) {
                ans.back()[0] = series1[i][0];
                i += 1;
            } else {
                ans.back()[0] = series2[j][0];
                j += 1;
            }
        }
        while (i < m) {
            ans.push_back(series1[i]);
            i += 1;
        }
        while (j < n) {
            ans.push_back(series2[j]);
            j += 1;
        }
        return ans;
    }
};
```
