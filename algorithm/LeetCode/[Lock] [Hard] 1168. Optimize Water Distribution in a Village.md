1168. Optimize Water Distribution in a Village

There are `n` houses in a village. We want to supply water for all the houses by building wells and laying pipes.

For each house `i`, we can either build a well inside it directly with cost `wells[i - 1]` (note the `-1` due to **0-indexing**), or pipe in water from another well to it. The costs to lay pipes between houses are given by the array `pipes` where each `pipes[j] = [house1j, house2j, costj]` represents the cost to connect `house1j` and `house2j` together using a pipe. Connections are bidirectional, and there could be multiple valid connections between the same two houses with different costs.

Return the minimum total cost to supply water to all houses.

 

**Example 1:**

![1168_1359_ex1.png](img/1168_1359_ex1.png)
```
Input: n = 3, wells = [1,2,2], pipes = [[1,2,1],[2,3,1]]
Output: 3
Explanation: The image shows the costs of connecting houses using pipes.
The best strategy is to build a well in the first house with cost 1 and connect the other houses to it with cost 2 so the total cost is 3.
```

**Example 2:**
```
Input: n = 2, wells = [1,1], pipes = [[1,2,1],[1,2,2]]
Output: 2
Explanation: We can supply water with cost two using one of the three options:
Option 1:
  - Build a well inside house 1 with cost 1.
  - Build a well inside house 2 with cost 1.
The total cost will be 2.
Option 2:
  - Build a well inside house 1 with cost 1.
  - Connect house 2 with house 1 with cost 1.
The total cost will be 2.
Option 3:
  - Build a well inside house 2 with cost 1.
  - Connect house 1 with house 2 with cost 1.
The total cost will be 2.
Note that we can connect houses 1 and 2 with cost 1 or with cost 2 but we will always choose the cheapest option. 
```

**Constraints:**

* `2 <= n <= 10^4`
* `wells.length == n`
* `0 <= wells[i] <= 10^5`
* `1 <= pipes.length <= 10^4`
* `pipes[j].length == 3`
* `1 <= house1j, house2j <= n`
* `0 <= costj <= 10^5`
* `house1j != house2j`

# Submissions
---
**Solution 1: (Union Find, Hidden Well in House 0)**

__Intuition__
I take it this way:
We cannot build any well.
There is one and only one hidding well in my house (house 0).
The cost to lay pipe between house[i] and my house is wells[i].

In order to supply water to the whole village,
we need to make the village a coonected graph.


__Explanation__
Merge all costs of pipes together and sort by key.
Greedily lay the pipes if it can connect two seperate union.
Appply union find to record which houses are connected.


__Complexity__
Time O(ElogE)
Space O(N)

```
Runtime: 25 ms, Beats 70.37%
Memory: 42.12 MB, Beats 82.96%
```
```c++
class Solution {
    vector<int> uf;
    int find(int x) {
        if (x != uf[x]) uf[x] = find(uf[x]);
        return uf[x];
    }
public:
    int minCostToSupplyWater(int n, vector<int>& wells, vector<vector<int>>& pipes) {
        uf.resize(n + 1, 0);
        for (auto& p : pipes) swap(p[0], p[2]);
        for (int i = 0; i < n; ++i) {
            uf[i + 1] = i + 1;
            pipes.push_back({wells[i], 0, i + 1});
        }
        sort(pipes.begin(), pipes.end());

        int res = 0;
        for (int i = 0; n > 0; ++i) {
            int x = find(pipes[i][1]), y = find(pipes[i][2]);
            if (x != y) {
                res += pipes[i][0];
                uf[x] = y;
                --n;
            }
        }
        return res;
    }
};
```
