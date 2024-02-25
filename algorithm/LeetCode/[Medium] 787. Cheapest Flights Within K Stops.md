787. Cheapest Flights Within K Stops

There are `n` cities connected by `m` flights. Each fight starts from city `u` and arrives at `v` with a price `w`.

Now given all the cities and flights, together with starting city `src` and the destination `dst`, your task is to find the cheapest price from `src` to `dst` with up to `k` stops. If there is no such route, output `-1`.

**Example 1:**

```
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation: 
The graph looks like this:

The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
```
![787_995](img/787_995.png)


**Example 2:**

```
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
Explanation: 
The graph looks like this:

The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
```

![787_995](img/787_995.png)

**Note:**

* The number of nodes n will be in range `[1, 100]`, with nodes labeled from `0` to `n - 1`.
* The size of flights will be in range `[0, n * (n - 1) / 2]`.
* The format of each flight will be `(src, dst, price)`.
* The price of each flight will be in the range `[1, 10000]`.
k is in the range of `[0, n - 1]`.
* There will not be any duplicated flights or self cycles.

# Submissions
---
**Solution 1: (BFS, Dijkstra's algorithm)**
```
Runtime: 92 ms
Memory Usage: 20 MB
```
```python
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        dic = collections.defaultdict(list)
        for s, d, p in flights:
            dic[s].append([d, p])
        q = [[0, src, 0]]
        while q:
            price, s, hop = heapq.heappop(q)
            if s == dst:
                return price
            if hop > K: continue
            for nd, np in dic[s]:
                heapq.heappush(q, [price + np, nd, hop + 1])
        return -1
```

**Solution 2: (DFS)**
```
Runtime: 108 ms
Memory Usage: 7.7 MB
```
```c
int helper(int n, int** flights, int flightsSize, int* flightsColSize, int src, int dst, int K,int** map){
    int min_ret=50000;
    if(map[K][src]!=0){
        return map[K][src];
    }
    if(src==dst){
        return 0;
    }
    if(K==0){
        for(int i=0;i<flightsSize;i++){
            if(flights[i][0]==src&&flights[i][1]==dst){
                return flights[i][2];
            }
        }
        return min_ret;
    }
    
    for(int i=0;i<flightsSize;i++){
        if(flights[i][0]==src){
            if(map[K-1][flights[i][1]]==0){
                map[K-1][flights[i][1]]=helper(n,flights,flightsSize,flightsColSize, flights[i][1], dst, K-1,map);
            }
            int tmp=flights[i][2]+map[K-1][flights[i][1]];
            if(min_ret>tmp){
                min_ret=tmp;
                
            }
        }
    }
    return min_ret;
}

int findCheapestPrice(int n, int** flights, int flightsSize, int* flightsColSize, int src, int dst, int k){
    int** map=(int**)malloc((k+1)*sizeof(int*));
    for(int i=0;i<k+1;i++){
        map[i]=(int*)calloc(n+1,sizeof(int));
    }
    int ret=helper(n, flights, flightsSize,flightsColSize, src, dst, k,map);
    return ret>=50000?-1:ret;
}
```

**Solution 3: (BFS)**
```
Runtime: 34 ms
Memory Usage: 13.9 MB
```
```c++
class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        // adjacent list
        vector<unordered_map<int, int>> adj(n); // src: to->weight
        for(auto& f: flights)
            adj[f[0]][f[1]] = f[2];

        vector<int> dist(n, INT_MAX);
        
        queue<vector<int>> q;
        q.push({src, 0});
        
        k++;
        while(k--){
            int q_size = q.size();
            while(q_size--){
                auto x = q.front(); q.pop();
                int cur_idx = x[0];
                int cur_dist = x[1];
                
                for(auto p: adj[cur_idx]){
                    int new_dist = p.second + cur_dist;
                    if(new_dist < dist[p.first]){
                        q.push({p.first, new_dist});
                        dist[p.first] = new_dist;
                    }
                }
            }
        }
        
        return (dist[dst] == INT_MAX) ? -1 : dist[dst];
    }
};
```

**Solution 4: (BFS, Dijkstra's algorithm)**
```
Runtime: 28 ms
Memory Usage: 15.6 MB
```
```c++
class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        vector<vector<pair<int, int>>> graph(n);
        for(auto e : flights) {
            graph[e[0]].push_back({e[1], e[2]});
        }
        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;
        // {dist_from_src_node, node, number_of_stops_from_src_node}
        pq.push({0, src, 0});
        
        vector<int> stops(n, INT_MAX);
        // number of stops to reach indexth node with least possible price from src node
        // as it will be calculated once the pq.top() equals to indexth node
        
        // pq.top() will always store least cost among the pq elements so if already stop is calculated
        // and if that is greater than the cstop that means already we have a path with cheaper cost
        // as well as with less or equal number of stops
        
        while(!pq.empty()) {
            auto temp=pq.top();
            int cdist=temp[0];
            int cnode=temp[1];
            int cstop=temp[2];
            pq.pop();
            
            if(cstop>stops[cnode] || cstop>k+1)
                continue;
            
            stops[cnode]=cstop;
            if(cnode==dst) {
                return cdist;
            }
            
            for(auto a : graph[cnode]) {
                pq.push({cdist+a.second, a.first, cstop+1});
            }
        }
        return -1;
    }
};
```

**Solution 5: (Dijkstra Time: O(N + E*K*log(E*K)), Space: O(N + E*K))**
```
Runtime: 318 ms
Memory: 15.5 MB
```
```python
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = collections.defaultdict(list)
        for f, t, p in flights:
            g[f] += [(t, p)]
        hq = [(0, 0, src)]

        # can't use dist[] to recored profit, it will lost step information.
        step = [float('inf')]*n

        while hq:
            p, s, u = heapq.heappop(hq)
            if s > step[u] or s > k+1:
                continue
            step[u] = s
            if u == dst:
                return p
            for nu, np in g[u]:
                heapq.heappush(hq, (p+np, s+1, nu))
        return -1
```

**Solution 6: (BFS Time: O(N + E*K), Space: O(N + E*K))**
```
Runtime: 108 ms
Memory: 15.2 MB
```
```python
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = collections.defaultdict(list)
        for f, t, p in flights:
            g[f] += [(t, p)]
        q = collections.deque([(src, 0)])
        dist = [float('inf')]*n
        while k >= 0 and q:
            sz = len(q)
            for _ in range(sz):
                u, p = q.popleft()
                for nu, np in g[u]:
                    if p+np >= dist[nu]:
                        continue
                    dist[nu] = p+np
                    q += [(nu, dist[nu])]
            k -= 1
        return dist[dst] if dist[dst] != float('inf') else -1
```

**Solution 7: (Dijkstra, level based)**
```
Runtime: 36 ms
Memory: 17.26 MB
```
```c++
class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        vector<vector<pair<int,int>>> g(n, vector<pair<int,int>>());
        for (int i = 0; i < flights.size(); i ++) {
            g[flights[i][0]].push_back({flights[i][1], flights[i][2]});
        }
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> pq;
        vector<vector<int>> dist(n, vector<int>(k+2, INT_MAX));
        pq.push({0, src, 0});
        dist[src][0] = 0;
        int rst = INT_MAX;
        while (pq.size()) {
            auto [c, v, s] = pq.top();
            pq.pop();
            if (v == dst) {
                rst = min(rst, c);
                continue;
            }
            for (auto [nv, nc]: g[v]) {
                if (s <= k && dist[nv][s+1] > dist[v][s] + nc) {
                    dist[nv][s+1] = dist[v][s] + nc;
                    pq.push({c+nc, nv, s+1});
                }
            }
        }
        return rst != INT_MAX? rst : -1;
    }
};
```

**Solution 8: (BFS)**
```
Runtime: 20 ms
Memory: 16.80 MB
```
```c++
class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        unordered_map<int, vector<pair<int, int>>> adj;
        for (auto& flight : flights) {
            adj[flight[0]].push_back({flight[1], flight[2]});
        }

        vector<int> dist(n, INT_MAX);
        dist[src] = 0;

        queue<pair<int, int>> q;
        q.push({src, 0});
        int stops = 0;

        while (!q.empty() && stops <= k) {
            int sz = q.size();
            while (sz-- > 0) {
                auto [node, distance] = q.front();
                q.pop();
                for (auto& [neighbour, price] : adj[node]) {
                    if (price + distance >= dist[neighbour]) continue;
                    dist[neighbour] = price + distance;
                    q.push({neighbour, dist[neighbour]});
                }
            }
            stops++;
        }
        return dist[dst] == INT_MAX ? -1 : dist[dst];
    }
};
```
