2714. Find Shortest Path with K Hops

You are given a positive integer `n` which is the number of nodes of a 0-indexed undirected weighted connected graph and a 0-indexed 2D array `edges` where `edges[i] = [ui, vi, wi]` indicates that there is an edge between nodes `ui` and `vi` with weight `wi`.

You are also given two nodes `s` and `d`, and a positive integer `k`, your task is to find the shortest path from `s` to `d`, but you can hop over at most `k` edges. In other words, make the weight of at most `k` edges `0` and then find the shortest path from `s` to `d`.

Return the length of the shortest path from `s` to `d` with the given condition.

 

**Example 1:**
```
Input: n = 4, edges = [[0,1,4],[0,2,2],[2,3,6]], s = 1, d = 3, k = 2
Output: 2
Explanation: In this example there is only one path from node 1 (the green node) to node 3 (the red node), which is (1->0->2->3) and the length of it is 4 + 2 + 6 = 12. Now we can make weight of two edges 0, we make weight of the blue edges 0, then we have 0 + 2 + 0 = 2. It can be shown that 2 is the minimum length of a path we can achieve with the given condition.
```
![2714_1.jpg](img/2714_1.jpg)


**Example 2:**
```
Input: n = 7, edges = [[3,1,9],[3,2,4],[4,0,9],[0,5,6],[3,6,2],[6,0,4],[1,2,4]], s = 4, d = 1, k = 2
Output: 6
Explanation: In this example there are 2 paths from node 4 (the green node) to node 1 (the red node), which are (4->0->6->3->2->1) and (4->0->6->3->1). The first one has the length 9 + 4 + 2 + 4 + 4 = 23, and the second one has the length 9 + 4 + 2 + 9 = 24. Now if we make weight of the blue edges 0, we get the shortest path with the length 0 + 4 + 2 + 0 = 6. It can be shown that 6 is the minimum length of a path we can achieve with the given condition.
```
![2714_2.jpg](img/2714_2.jpg)

**Example 3:**
```
Input: n = 5, edges = [[0,4,2],[0,1,3],[0,2,1],[2,1,4],[1,3,4],[3,4,7]], s = 2, d = 3, k = 1
Output: 3
Explanation: In this example there are 4 paths from node 2 (the green node) to node 3 (the red node), which are (2->1->3), (2->0->1->3), (2->1->0->4->3) and (2->0->4->3). The first two have the length 4 + 4 = 1 + 3 + 4 = 8, the third one has the length 4 + 3 + 2 + 7 = 16 and the last one has the length 1 + 2 + 7 = 10. Now if we make weight of the blue edge 0, we get the shortest path with the length 1 + 2 + 0 = 3. It can be shown that 3 is the minimum length of a path we can achieve with the given condition.
```
![2714_3.jpg](img/2714_3.jpg)
 

**Constraints:**

* `2 <= n <= 500`
* `n - 1 <= edges.length <= min(104, n * (n - 1) / 2)`
* `edges[i].length = 3`
* `0 <= edges[i][0], edges[i][1] <= n - 1`
* `1 <= edges[i][2] <= 10^6`
* `0 <= s, d, k <= n - 1`
* `s != d`
* The input is generated such that the graph is connected and has no repeated edges or self-loops

# Submissions
---
**Solution 1: (DP, BFS)**

We run simple BFS, memorizing the best result for node i and skips cnt in dp[i][cnt].

I tried Dijkstra (prioritizing either by path or number of skips), but it did not affect the runtime.

I also tried a segment tree to query the minimum path in [cnt, k] range. The result was the same but the code was more complicated.

What helped the runtime (shaved ~100 ms) is to set dp[i][cnt - 1] every time we update dp[i][cnt].

```
Runtime: 86 ms, Beats 100.00%
Memory: 94.15 MB, Beats 75.00%
```
```c++
class Solution {
public:
    int shortestPathWithHops(int n, vector<vector<int>>& edges, int s, int d, int k) {
        vector<vector<array<int, 2>>> g(n);
        for (auto &e : edges) {
            g[e[0]].push_back({e[1], e[2]});
            g[e[1]].push_back({e[0], e[2]});
        }
        vector<vector<int>> dp(n, vector<int>(n, INT_MAX));
        dp[s][k] = 0;
        queue<array<int, 3>> q;
        q.push({s, k, 0});
        while (!q.empty()) {
            auto [i, cnt, path] = q.front();
            q.pop();
            if (dp[i][cnt] != path || i == d) {
                continue;
            }
            for (auto [j, w] : g[i]) {
                if (dp[j][cnt] > dp[i][cnt] + w) {
                    dp[j][cnt] = dp[i][cnt] + w;
                    q.push({j, cnt, dp[j][cnt]});
                    if (cnt > 0)
                        dp[j][cnt - 1] = min(dp[j][cnt - 1], dp[j][cnt]);
                }            
                if (cnt > 0 && dp[j][cnt - 1] > dp[i][cnt]) {
                    dp[j][cnt - 1] = dp[i][cnt];
                    q.push({j, cnt - 1, dp[j][cnt - 1]});
                    if (cnt - 1 > 0)
                        dp[j][cnt - 2] = min(dp[j][cnt - 2], dp[j][cnt - 1]);
                }
            }
        }
        return *min_element(begin(dp[d]), end(dp[d]));
    }
};
```
