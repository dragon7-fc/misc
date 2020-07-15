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

**Solution 2: (BFS)**
```
Runtime: 272 ms
Memory Usage: 42 MB
```
```c++
class Solution {
public:
    int numBusesToDestination(vector<vector<int>>& routes, int S, int T) {
        if(S == T) return 0; // must
        unordered_map<int, vector<int> > buses4stop; // stop_id->buses; key/stop_id is sparse
        for(int i = 0; i < routes.size(); i++)
            for(const auto& stop: routes[i])
                buses4stop[stop].emplace_back(i);
        queue<int> q{{S}};        
        vector<bool>visited(routes.size());        
                 
        for(int step = 0;!q.empty(); step++)
            for(int sz = q.size(); sz-- > 0; ){
                const int cur = q.front(); q.pop();                                
                for(const auto& bus: buses4stop[cur]){
                    if(visited[bus]) continue;
                    visited[bus] = 1;
                    for(const auto& next: routes[bus]){                       
                        if(next == T) return step+1;                
                        q.emplace(next);               
                    }
                }
            }            
        
        return -1;
    }
};
```