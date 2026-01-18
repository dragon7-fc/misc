3809. Best Reachable Tower

You are given a 2D integer array `towers`, where `towers[i] = [xi, yi, qi]` represents the coordinates `(xi, yi)` and quality factor `qi` of the `i`th tower.

You are also given an integer array `center = [cx, cy]` representing your location, and an integer radius.

A tower is **reachable** if its Manhattan distance from center is **less than or equal** to `radius`.

Among all reachable towers:

* Return the coordinates of the tower with the maximum quality factor.
* If there is a tie, return the tower with the lexicographically smallest coordinate. If no tower is reachable, return [-1, -1].

The **Manhattan Distance** between two cells `(xi, yi)` and `(xj, yj)` is `|xi - xj| + |yi - yj|`.
A coordinate `[xi, yi]` is **lexicographically smaller** than `[xj, yj]` if `xi < xj`, or `xi == xj and yi < yj`.

`|x|` denotes the absolute value of x.

 

**Example 1:**
```
Input: towers = [[1,2,5], [2,1,7], [3,1,9]], center = [1,1], radius = 2

Output: [3,1]

Explanation:

Tower [1, 2, 5]: Manhattan distance = |1 - 1| + |2 - 1| = 1, reachable.
Tower [2, 1, 7]: Manhattan distance = |2 - 1| + |1 - 1| = 1, reachable.
Tower [3, 1, 9]: Manhattan distance = |3 - 1| + |1 - 1| = 2, reachable.
All towers are reachable. The maximum quality factor is 9, which corresponds to tower [3, 1].
```

**Example 2:**
```
Input: towers = [[1,3,4], [2,2,4], [4,4,7]], center = [0,0], radius = 5

Output: [1,3]

Explanation:

Tower [1, 3, 4]: Manhattan distance = |1 - 0| + |3 - 0| = 4, reachable.
Tower [2, 2, 4]: Manhattan distance = |2 - 0| + |2 - 0| = 4, reachable.
Tower [4, 4, 7]: Manhattan distance = |4 - 0| + |4 - 0| = 8, not reachable.
Among the reachable towers, the maximum quality factor is 4. Both [1, 3] and [2, 2] have the same quality, so the lexicographically smaller coordinate is [1, 3].
```

**Example 3:**
```
Input: towers = [[5,6,8], [0,3,5]], center = [1,2], radius = 1

Output: [-1,-1]

Explanation:

Tower [5, 6, 8]: Manhattan distance = |5 - 1| + |6 - 2| = 8, not reachable.
Tower [0, 3, 5]: Manhattan distance = |0 - 1| + |3 - 2| = 2, not reachable.
No tower is reachable within the given radius, so [-1, -1] is returned.
```
 

**Constraints:**

* `1 <= towers.length <= 10^5`
* `towers[i] = [xi, yi, qi]`
* `center = [cx, cy]`
* `0 <= xi, yi, qi, cx, cy <= 10^5`
* `0 <= radius <= 10^5`

# Submissions
---
**Solution 1: (Greedy)**
```
Runtime: 39 ms, Beats 28.57%
Memory: 284.78 MB, Beats 7.14%
```
```c++
class Solution {
public:
    vector<int> bestTower(vector<vector<int>>& towers, vector<int>& center, int radius) {
        vector<int> ans = {INT_MAX, INT_MAX};
        int bestQuality = 0;

        for (auto& t : towers) {
            int dist = abs(center[0] - t[0]) + abs(center[1] - t[1]);
            if (dist <= radius) {
                if (t[2] > bestQuality) {
                    bestQuality = t[2];
                    ans = {t[0], t[1]};
                } else if (t[2] == bestQuality) {
                    ans = min(ans, {t[0], t[1]});
                }
            }
        }

        if (ans[0] == INT_MAX) return {-1, -1};
        return ans;
    }
};
```
