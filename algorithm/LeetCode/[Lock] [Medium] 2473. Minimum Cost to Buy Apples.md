2473. Minimum Cost to Buy Apples

You are given a positive integer `n` representing `n` cities numbered from `1` to `n`. You are also given a **2D** array roads, where `roads[i] = [ai, bi, costi]` indicates that there is a **bidirectional** road between cities `ai` and `bi` with a cost of traveling equal to `costi`.

You can buy apples in any city you want, but some cities have different costs to buy apples. You are given the array `appleCost` where `appleCost[i]` is the cost of buying one apple from city `i`.

You start at some city, traverse through various roads, and eventually buy **exactly** one apple from **any** city. After you buy that apple, you have to return back to the city you **started** at, but now the cost of all the roads will be **multiplied** by a given factor `k`.

Given the integer `k`, return an array `answer` of size `n` where `answer[i]` is the minimum total cost to buy an apple if you start at city `i`.

 

**Example 1:**

![2473_graph55.png](img/2473_graph55.png)
```
Input: n = 4, roads = [[1,2,4],[2,3,2],[2,4,5],[3,4,1],[1,3,4]], appleCost = [56,42,102,301], k = 2
Output: [54,42,48,51]
Explanation: The minimum cost for each starting city is the following:
- Starting at city 1: You take the path 1 -> 2, buy an apple at city 2, and finally take the path 2 -> 1. The total cost is 4 + 42 + 4 * 2 = 54.
- Starting at city 2: You directly buy an apple at city 2. The total cost is 42.
- Starting at city 3: You take the path 3 -> 2, buy an apple at city 2, and finally take the path 2 -> 3. The total cost is 2 + 42 + 2 * 2 = 48.
- Starting at city 4: You take the path 4 -> 3 -> 2 then you buy at city 2, and finally take the path 2 -> 3 -> 4. The total cost is 1 + 2 + 42 + 1 * 2 + 2 * 2 = 51.
```

**Example 2:**

![2473_graph4.png](img/2473_graph4.png)
```
Input: n = 3, roads = [[1,2,5],[2,3,1],[3,1,2]], appleCost = [2,3,1], k = 3
Output: [2,3,1]
Explanation: It is always optimal to buy the apple in the starting city.
```

**Constraints:**

* `2 <= n <= 1000`
* `1 <= roads.length <= 1000`
* `1 <= ai, bi <= n`
* `ai != bi`
* `1 <= costi <= 10^5`
* `appleCost.length == n`
* `1 <= appleCost[i] <= 10^5`
* `1 <= k <= 100`
* There are no repeated edges.

# Submissions
---
**Solution 1: (Dijkstra)**
```
Runtime: 737 ms
Memory: 14.6 MB
```
```python
class Solution:
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:
        g = collections.defaultdict(list)
        for a, b, cost in roads:
            g[a-1] += [[b-1, cost]]
            g[b-1] += [[a-1, cost]]
        ans = appleCost[:]
        for i in range(n):
            hq = [[0, i]]
            seen = set()
            while hq:
                c, u = heapq.heappop(hq)
                if u in seen:
                    continue
                seen.add(u)
                ans[i] = min(ans[i], c*(k+1) + appleCost[u])
                for v, vc in g[u]:
                    if not v in seen and (c + vc)*(k+1) < ans[i]:
                        heapq.heappush(hq, [c + vc, v])
                
        return ans
```

**Solution 2: (Dijkstra)**
```
Runtime: 1254 ms
Memory: 14.7 MB
```
```python
class Solution:
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:
        g = collections.defaultdict(list)
        for a, b, cost in roads:
            g[a-1] += [[b-1, cost]]
            g[b-1] += [[a-1, cost]]
        ans = [0]*n
        for i in range(n):
            hq = [[0, i]]
            dist = [float('inf')]*n
            while hq:
                c, u = heapq.heappop(hq)
                if c*(k+1) + appleCost[u] >= dist[u]:
                    continue
                dist[u] = c*(k+1) + appleCost[u]
                dist[i] = min(dist[i], c*(k+1) + appleCost[u])
                for v, vc in g[u]:
                    if (c + vc)*(k+1) < dist[i]:
                        heapq.heappush(hq, [c + vc, v])
            ans[i] = dist[i]
                
        return ans
```

**Solution 3: (Dijkstra, O(n*(n+e)*Log(n)))**
```
Runtime: 2717 ms
Memory: 567.42 MB
```
```c++
class Solution {
    // Finds the minimum cost to buy an apple from the start city
    long long shortestPath(int startCity, vector<vector<pair<int, int>>> graph,
                           vector<int>& appleCost, int k, int n) {
        // Stores the travel cost reach each city from the start city
        vector<int> travelCosts(n, INT_MAX);
        travelCosts[startCity] = 0;

        // Initialize the heap (priority queue) with the starting city
        // Each element of the heap is an array with the cost and city
        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> heap;
        heap.push({0, startCity});
        long long minCost = INT_MAX;

        while (!heap.empty()) {
            // Remove the city with the minimum cost from the top of the heap
            auto current = heap.top();
            heap.pop();
            int travelCost = current[0];
            int currCity = current[1];

            // Update the min cost if the curr city has a smaller total cost
            minCost = min(minCost, 
                    static_cast<long long>(appleCost[currCity]) + (k + 1) * travelCost);

            // Add each neighboring city to the heap if an apple is cheaper
            for (auto& [neighbor, cost] : graph[currCity]) {
                int nextCost = travelCost + cost;
                if (nextCost < travelCosts[neighbor]) {
                    travelCosts[neighbor] = nextCost;
                    heap.push({nextCost, neighbor});
                }
            }
        }
        return minCost;
    }
public:
    vector<long long> minCost(int n, vector<vector<int>>& roads, vector<int>& appleCost, int k) {
        // Store the graph as a list of lists
        // The rows represent the cities (vertices)
        // The columns store an adjacency list of road, cost pairs (edge, weight)
        vector<vector<pair<int, int>>> graph(n, vector<pair<int, int>>());

        // Add each road to the graph using adjacency lists
        // Store each city at graph[city - 1]
        for (auto& road : roads) {
            int city_a = road[0] - 1, city_b = road[1] - 1, cost = road[2];
            graph[city_a].push_back({city_b, cost});
            graph[city_b].push_back({city_a, cost});
        }

        // Find the minimum cost to buy an apple starting in each city
        vector<long long> result(n);
        for (int startCity = 0; startCity < n; startCity++) {
            result[startCity] = shortestPath(startCity, graph, appleCost, k, n);
        }

        return result;
    }
};
```

**Solution 3: (Dijkstra, one pass, O((n+e)*Log(n+e)))**
```
Runtime: 21 ms
Memory: 18.08 MB
```
```c++
class Solution {
public:
    vector<long long> minCost(int n, vector<vector<int>>& roads, vector<int>& appleCost, int k) {
        vector<vector<pair<int, int>>> g(n);
        for (auto& r : roads) {
            g[r[0]-1].push_back({r[1]-1, r[2]});
            g[r[1]-1].push_back({r[0]-1, r[2]});
        }
        vector<long long> ans(appleCost.begin(), appleCost.end());
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        for (int i = 0; i < n; i++) {
            pq.push({appleCost[i], i});
        }
        while (!pq.empty()) {
            auto [c, i] = pq.top();
            pq.pop();
            if (ans[i] < c)
                continue;
            for (auto [ni, nc] : g[i]) {
                if (ans[ni] > ans[i] + (k + 1) * nc) {
                    ans[ni] = ans[i] + (k + 1) * nc;
                    pq.push({ans[ni], ni});
                }
            }
        }
        return ans;
    }
};
```
