3965. Finish Time of Tasks I

You are given an integer n representing the number of tasks in a project, numbered from 0 to `n - 1`. These tasks are connected as a tree rooted at task 0. This is represented by a 2D integer array edges of length `n - 1`, where `edges[i] = [ui, vi]` indicates that task `ui` is the parent of task `vi`.

You are also given an array `baseTime` of length `n`, where `baseTime[i]` represents the time to complete task `i`.

The finish time of each task is calculated as follows:

* Leaf task: The finish time is `baseTime[i]`.
* Non-leaf task:
    * Let `earliest` be the **minimum** finish time among its children, and `latest` be the **maximum** finish time among its children.
    * Let `ownDuration` be `(latest - earliest) + baseTime[i]`.
    * The finish time of task `i` is `latest + ownDuration`.

Return the finish time of the root task 0.

 

**Example 1:**
```
Input: n = 3, edges = [[0,1],[1,2]], baseTime = [9,5,3]

Output: 17

Explanation:
```
    0 - 1 - 2
    9   5   3
```
Task 2 is a leaf, so its finish time is baseTime[2] = 3.
Task 1 has one child task 2:
earliest = latest = 3
ownDuration = (latest - earliest) + baseTime[1] = 5
Finish time of task 1 is 3 + 5 = 8
Task 0 has one child with finish time 8:
earliest = latest = 8
ownDuration = (latest - earliest) + baseTime[0] = 9
Finish time of task 0 is 8 + 9 = 17
```

**Example 2:**
```
Input: n = 3, edges = [[0,1],[0,2]], baseTime = [4,7,6]

Output: 12

Explanation:
```
            0 4
          /   \
         1     2
         7     6
```
Task 1 is a leaf, so its finish time is baseTime[1] = 7.
Task 2 is a leaf, so its finish time is baseTime[2] = 6.
Task 0 has two children with finish times 7 and 6:
earliest = 6, latest = 7
ownDuration = (latest - earliest) + baseTime[0] = (7 - 6) + 4 = 5
Finish time of task 0 is latest + ownDuration = 7 + 5 = 12
```

**Example 3:**
```
Input: n = 4, edges = [[0,1],[0,2],[2,3]], baseTime = [5,8,2,1]

Output: 18

Explanation:

Task 1 is a leaf, so its finish time is baseTime[1] = 8.
Task 3 is a leaf, so its finish time is baseTime[3] = 1.
Task 2 has one child task 3:
earliest = latest = 1
ownDuration = (latest - earliest) + baseTime[2] = 0 + 2 = 2
Finish time of task 2 is latest + ownDuration = 1 + 2 = 3
Task 0 has two children with finish times 8 and 3:
earliest = 3, latest = 8
ownDuration = (latest - earliest) + baseTime[0] = (8 - 3) + 5 = 10
Finish time of task 0 is latest + ownDuration = 8 + 10 = 18
```

**Constraints:**

* `1 <= n <= 10^5`
* `edges.length = n - 1`
* `edges[i] == [ui, vi]`
* `0 <= ui, vi <= n - 1`
* `ui != vi`
* The input is generated such that edges represents a valid tree.
* `baseTime.length == n`
* `1 <= baseTime[i] <= 10^5`

# Submissions
---
**Solution 1: (DFS, postorder)**
```
Runtime: 199 ms, Beats 42.86%
Memory: 350.74 MB, Beats 42.86%
```
```c++
class Solution {
    long long dfs(int u, int p, vector<vector<int>> &g, vector<int> &baseTime) {
        long long earliest = LONG_LONG_MAX;
        long long latest = 0;
        for (const auto &v: g[u]) {
            if (v == p) {
                continue;
            }
            long long t = dfs(v, u, g, baseTime);
            earliest = min(earliest, t);
            latest = max(latest, t);
        }
        if (latest != 0) {
            long long ownDuration = (latest - earliest) + baseTime[u];
            return latest + ownDuration;
        }
        return baseTime[u];
    }
public:
    long long finishTime(int n, vector<vector<int>>& edges, vector<int>& baseTime) {
        vector<vector<int>> g(n);
        for (const auto &e: edges) {
            auto u = e[0];
            auto v = e[1];
            g[u].push_back(v);
            g[v].push_back(u);
        }
        return dfs(0, -1, g, baseTime);
    }
};
```
