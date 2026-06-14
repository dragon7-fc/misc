3961. Maximize Sum of Device Ratings

You are given a 2D integer array units of size `m × n` where `units[i][j]` represents the capacity of the `j`th unit in the `i`th device. Each device contains exactly `n` units.

The **rating** of a device is the **minimum** capacity among all its units.

You may perform the following operation any number of times (including zero):

* Choose a device `i` that has not been used as a source before.
* Remove exactly one unit from device `i` and add it to any different device.
* Then mark device `i` as used, so it cannot be chosen again as a source.

Return the **maximum** possible sum of the ratings of all devices after any number of such operations.

**Note**:

* Devices can receive units from multiple devices, regardless of whether they have been selected.
* The rating of an empty device is `0`.
 

**Example 1:**
```
Input: units = [[1,3],[2,2]]

Output: 4

Explanation:

Select device i = 0 and transfer units[0][0] = 1 to device i = 1.
After the transfer, the ratings are:
Device 0 = [3]: rating[0] = 3
Device 1 = [2, 2, 1]: rating[1] = 1
Thus, the sum of ratings is 3 + 1 = 4.
```

**Example 2:**
```
Input: units = [[1,2,3],[4,5,6]]

Output: 6

Explanation:

Select device i = 1 and transfer units[1][0] = 4 to device i = 0.
After the transfer, the ratings are:
Device 0 = [1, 2, 3, 4]: rating[0] = 1
Device 1 = [5, 6]: rating[1] = 5
Thus, the sum of ratings is 1 + 5 = 6.
```

**Example 3:**
```
Input: units = [[5,5,5],[1,1,1]]

Output: 6

Explanation:

No transfers increase the sum of ratings. Thus, the sum of ratings is 5 + 1 = 6.
```

**Constraints:**

* `1 <= m == units.length <= 10^5`
* `1 <= n == units[i].length <= 10^5`
* `m * n <= 2 * 10^5`
* `1 <= units[i][j] <= 10^5`

# Submissions
---
**Solution 1: (Case Study, move all device smallest unit to global device smallest second smallest unit to minimize lost)**

unit |  a2
     |  a1               
     |           c1               
     |       b1 < samllest 2nd smallest unit
     |           c0
     |       b0
     |  a0
     |       global device smallest second smallest unit
        ------------
        a    b   c
          device

ans:
unit |  a2
     |  a1 <
     |           c1 <
     |       b1 x     |
     |       c0       | min diff
     |       b0       |
     |       a0 <     |
        ------------
        a    b   c
          device   
```
Runtime: 9 ms. Beats 70.36%
Memory: 156.72 MB, Beats 85.28%
```
```c++
class Solution {
public:
    long long maxRatings(vector<vector<int>>& units) {
        if (all_of(units.begin(), units.end(), [](const auto &unit){
            return unit.size() == 1;
        })) {
            int ans = 0;
            for (const auto &unit: units) {
                ans += unit[0];
            }
            return ans;
        }
        int g_mn0 = INT_MAX;
        int g_mn1 = INT_MAX;
        long long ans = 0;
        for (int i = 0; i < units.size(); i ++) {
            int mn0 = INT_MAX;
            int mn1 = INT_MAX;
            for (const auto &a: units[i]) {
                if (a < mn0) {
                    mn1 = mn0;
                    mn0 = a;
                } else if (a < mn1) {
                    mn1 = a;
                }
            }
            g_mn0 = min(g_mn0, mn0);
            if (units[i].size() > 1) {
                ans += mn1;
                g_mn1 = min(g_mn1, mn1);
            }
        }
        return ans + g_mn0 - g_mn1;
    }
};
```
