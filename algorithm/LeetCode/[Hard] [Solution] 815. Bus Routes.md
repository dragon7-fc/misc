815. Bus Routes

We have a list of bus routes. Each `routes[i]` is a bus route that the `i`-th bus repeats forever. For example if `routes[0] = [1, 5, 7]`, this means that the first bus (0-th indexed) travels in the sequence `1->5->7->1->5->7->1->...` forever.

We start at bus stop `S` (initially not on a bus), and we want to go to bus stop `T`. Travelling by buses only, what is the least number of buses we must take to reach our destination? Return -1 if it is not possible.

**Example:**
```
Input: 
routes = [[1, 2, 7], [3, 6, 7]]
S = 1
T = 6
Output: 2
Explanation: 
The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
```

**Constraints:**

* `1 <= routes.length <= 500`.
* `1 <= routes[i].length <= 10^5`.
* `0 <= routes[i][j] < 10 ^ 6`.

# Solution
---
## Approach #1: Breadth First Search [Accepted]
**Intuition**

Instead of thinking of the stops as nodes (of a graph), think of the buses as nodes. We want to take the least number of buses, which is a shortest path problem, conducive to using a breadth-first search.

**Algorithm**

We perform a breadth first search on bus numbers. When we start at `S`, originally we might be able to board many buses, and if we end at `T` we may have many targets for our goal state.

One difficulty is to efficiently decide whether two buses are connected by an edge. They are connected if they share at least one bus stop. Whether two lists share a common value can be done by set intersection (HashSet), or by sorting each list and using a two pointer approach.

To make our search easy, we will annotate the depth of each node: `info[0] = node, info[1] = depth`.

```python
class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        if S == T: return 0
        routes = map(set, routes)
        graph = collections.defaultdict(set)
        for i, r1 in enumerate(routes):
            for j in xrange(i+1, len(routes)):
                r2 = routes[j]
                if any(r in r2 for r in r1):
                    graph[i].add(j)
                    graph[j].add(i)

        seen, targets = set(), set()
        for node, route in enumerate(routes):
            if S in route: seen.add(node)
            if T in route: targets.add(node)

        queue = [(node, 1) for node in seen]
        for node, depth in queue:
            if node in targets: return depth
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, depth+1))
        return -1
```

**Complexity Analysis**

* Time Complexity: Let $N$ denote the number of buses, and $b_i$ be the number of stops on the $i$th bus.

To create the graph, in Python we do $O(\sum (N - i) b_i)$ work (we can improve this by checking for which of r1, r2 is smaller), while in Java we did a $O(\sum b_i \log b_i)$ sorting step, plus our searches are $O(N \sum b_i)$ work.

Our (breadth-first) search is on $N$ nodes, and each node could have $N$ edges, so it is $O(N^2)$.

* Space Complexity: $O(N^2 + \sum b_i)$ additional space complexity, the size of graph and routes. In Java, our space complexity is $O(N^2)$ because we do not have an equivalent of routes. Dual-pivot quicksort (as used in `Arrays.sort(int[])`) is an in-place algorithm, so in Java we did not increase our space complexity by sorting.

# Submissions
---
**Solution 1: (Breadth First Search)**
```
Runtime: 1336 ms
Memory Usage: 22.1 MB
```
```python
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T: return 0
        routes = list(map(set, routes))
        graph = collections.defaultdict(set)
        for i, r1 in enumerate(routes):
            for j in range(i+1, len(routes)):
                r2 = routes[j]
                if any(r in r2 for r in r1):
                    graph[i].add(j)
                    graph[j].add(i)

        seen, targets = set(), set()
        for node, route in enumerate(routes):
            if S in route: seen.add(node)
            if T in route: targets.add(node)

        queue = [(node, 1) for node in seen]
        for node, depth in queue:
            if node in targets: return depth
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, depth+1))
        return -1
```

**Solution 2: (BFS, route as key)**
```
Runtime: 685 ms
Memory: 55.5 MB
```
```c++
class Solution {
public:
    int numBusesToDestination(vector<vector<int>>& routes, int source, int target) {
        if (source == target) {
            return 0;
        }

        unordered_map<int, vector<int>> adjList;
        // Create a map from the bus stop to all the routes that include this stop.
        for (int route = 0; route < routes.size(); route++) {
            for (auto stop : routes[route]) {
                // Add all the routes that have this stop.
                adjList[stop].push_back(route);
            }
        }

        queue<int> q;
        vector<bool> vis(routes.size());
        // Insert all the routes in the queue that have the source stop.
        for (auto route : adjList[source]){
            q.push(route);
            vis[route] = true;
        }

        int busCount = 1;
        while (q.size()) {
            int size = q.size();

            for (int i = 0; i < size; i++) {
                int route = q.front(); q.pop();

                // Iterate over the stops in the current route.
                for (auto stop: routes[route]) {
                    // Return the current count if the target is found.
                    if (stop == target) {
                        return busCount;
                    }

                    // Iterate over the next possible routes from the current stop.
                    for (auto nextRoute : adjList[stop]) {
                        if (!vis[nextRoute]) {
                            vis[nextRoute] = true;
                            q.push(nextRoute);
                        }
                    }
                }
            }
            busCount++;
        }
        return -1;
    }
};
```

**Solution 3: (BFS, stop as key)**
```
Runtime: 280 ms
Memory: 121.1 MB
```
```c++
class Solution {
public:
    int numBusesToDestination(vector<vector<int>>& routes, int source, int target) {
        int n = routes.size();
        unordered_map<int, unordered_set<int>> g;
        for (int i = 0; i < n; i ++) {
            for (int j = 0; j < routes[i].size(); j ++) {
                g[routes[i][j]].insert(i);
            }
        }
        queue<pair<int,int>> q;
        unordered_set<int> visited;
        q.push({source, 0});
        visited.insert(source);
        while (q.size()) {
            auto [u, s] = q.front();
            q.pop();
            if (u == target) {
                return s;
            }
            for (auto route: g[u]) {
                for (auto stop: routes[route]) {
                    if (!visited.count(stop)) {
                        visited.insert(stop);
                        q.push({stop, s+1});
                    }
                }
                routes[route].clear();
            }
        }
        return -1;
    }
};
```
