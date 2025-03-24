1976. Number of Ways to Arrive at Destination

You are in a city that consists of n intersections numbered from 0 to n - 1 with bi-directional roads between some intersections. The inputs are generated such that you can reach any intersection from any other intersection and that there is at most one road between any two intersections.

You are given an integer n and a 2D integer array roads where roads[i] = [ui, vi, timei] means that there is a road between intersections ui and vi that takes timei minutes to travel. You want to know in how many ways you can travel from intersection 0 to intersection n - 1 in the shortest amount of time.

Return the number of ways you can arrive at your destination in the shortest amount of time. Since the answer may be large, return it modulo 109 + 7.

 

Example 1:


Input: n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
Output: 4
Explanation: The shortest amount of time it takes to go from intersection 0 to intersection 6 is 7 minutes.
The four ways to get there in 7 minutes are:
- 0 ➝ 6
- 0 ➝ 4 ➝ 6
- 0 ➝ 1 ➝ 2 ➝ 5 ➝ 6
- 0 ➝ 1 ➝ 3 ➝ 5 ➝ 6
Example 2:

Input: n = 2, roads = [[1,0,10]]
Output: 1
Explanation: There is only one way to go from intersection 0 to intersection 1, and it takes 10 minutes.
 

**Constraints:**

* `1 <= n <= 200`
* `n - 1 <= roads.length <= n * (n - 1) / 2`
* `roads[i].length == 3`
* `0 <= ui, vi <= n - 1`
* `1 <= timei <= 10^9`
* `ui != vi`
* There is at most one road connecting any two intersections.
* You can reach any intersection from any other intersection.

# Submissions
---
**Solution 1: (Dijkstra)**
```
Runtime: 304 ms
Memory Usage: 20.9 MB
```
```python
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, time in roads:
            graph[u].append([v, time])
            graph[v].append([u, time])

        def dijkstra(src):
            dist = [math.inf] * n
            ways = [0] * n
            minHeap = [(0, src)]  # dist, src
            dist[src] = 0
            ways[src] = 1
            while minHeap:
                d, u = heappop(minHeap)
                if dist[u] < d: continue  # Skip if `d` is not updated to latest version!
                for v, time in graph[u]:
                    if dist[v] > dist[u] + time:
                        dist[v] = dist[u] + time
                        ways[v] = ways[u]
                        heappush(minHeap, (dist[v], v))
                    elif dist[v] == dist[u] + time:
                        ways[v] = (ways[v] + ways[u]) % 1_000_000_007
            return ways[n - 1]
        
        return dijkstra(0)
```

**Solution 2: (Floyd-Warshall)**

             0
         1 /   \ 4
         1  -  2
            2
init
          0    1     2
    0  {0,0} {1,1} {4,1}
    1  {1,1} {0,0} {2,1}
    2  {4,1} {2,1} {0,0}
mid 0:
          0    1     2
    0  {0,1} {1,1} {4,1}
    1  {1,1} {0,1} {2,1}
    2  {4,1} {2,1} {0,1}
mid 1:
          0    1     2
    0               {3,1}
    1  
    2  {3,1} 
mid 2
          0    1     2
    0               
    1  
    2  

```
Runtime: 295 ms, Beats 5.29%
Memory: 39.65 MB, Beats 25.13%
```
```c++
class Solution {
public:
    int countPaths(int n, vector<vector<int>>& roads) {
        vector<vector<pair<long long,long long>>> dp(n, vector<pair<long long, long long>>(n, {1e12, 0}));
        int MOD = 1e9 + 7, i, j, k;
        for (i = 0; i < n; i ++) {
            dp[i][i] = {0, 1};
        }
        for (auto r: roads) {
            dp[r[0]][r[1]] = {r[2], 1};
            dp[r[1]][r[0]] = {r[2], 1};
        }
        for (k = 0; k < n; k ++) {
            for (i = 0; i < n; i ++) {
                for (j = 0; j < n; j ++) {
                    if (i != k && j != k) {
                        if (dp[i][j].first > dp[i][k].first + dp[k][j].first) {
                            dp[i][j].first = dp[i][k].first + dp[k][j].first;
                            dp[i][j].second = (dp[i][k].second * dp[k][j].second) % MOD;
                        } else if (dp[i][j].first == dp[i][k].first + dp[k][j].first) {
                            dp[i][j].second = (dp[i][j].second + dp[i][k].second * dp[k][j].second) % MOD;
                        }
                    }
                }
            }
        }
        return dp[0][n-1].second;
    }
};
```

**Solution 3: (Dijkstra, DP Bottom-Up)**

               0  <
            5/ | 2\
           /  7|     1  <
          4 <  |   3/ \3
           \   |   3 <  2 <
           2\  | 3/ \1 /1
             \ | /   \/
             > 6 --- 5 
                  1

dist    0     1     2     3     4     5     6
      {0,1} 
            {2,1}             {5,1}        {7,1}
                  {5,1} {5,1}
                                           {7,2}
                                    {6,2}
                                           {7,3}
pq
      {0,0}
        ^
      {5,4} {7,6} {2,1}
                    ^
      {5,4} {7,6} {5,3} {5,2}
       ^
      {7,6} {7,6} {5,3} {5,2}
                   ^
      {7,6} {7,6} {6,5} {5,2}
                          ^
      {7,6} {7,6} {6,5}
                    ^

```
Runtime: 15 ms, Beats 34.98%
Memory: 37.29 MB, Beats 56.38%
```
```c++
class Solution {
public:
    int countPaths(int n, vector<vector<int>>& roads) {
        vector<vector<pair<int,int>>> g(n);
        priority_queue<pair<long long,int>, vector<pair<long long,int>>, greater<pair<long long,int>>> pq;
        vector<pair<long long,long long>> dist(n, {LONG_LONG_MAX, 0});
        long long nt;
        int MOD = 1e9 + 7;
        for (auto r: roads) {
            g[r[0]].push_back({r[1], r[2]});
            g[r[1]].push_back({r[0], r[2]});
        }
        dist[0] = {0, 1};
        pq.push({0, 0});
        while (pq.size()) {
            auto [t, u] = pq.top();
            pq.pop();
            if (t > dist[u].first) {
                continue;
            }
            for (auto [v, w]: g[u]) {
                nt = t + w;
                if (nt < dist[v].first) {
                    dist[v].first = nt;
                    dist[v].second = dist[u].second;
                    pq.push({nt, v});
                } else if (nt == dist[v].first) {
                    dist[v].second += dist[u].second;
                    dist[v].second %= MOD;
                }
            }
        }
        return dist[n-1].second;
    }
};
```
