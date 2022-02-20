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
Runtime: 39 ms
Memory Usage: 14.4 MB
```
```c++
class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        // Create Graph
        map<int, vector<pair<int, int>>> graph;
        
        for (vector<int> flight : flights) {
            int u = flight[0];
            int v = flight[1];
            int p = flight[2];
            
            if (graph.find(u) == graph.end()) graph[u] = vector<pair<int, int>>();
            
            graph[u].push_back({v, p});
        }
        
        // { cost, node, stops }
        priority_queue< tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>> > pq;
        vector<int> discovery(n + 1, INT_MAX); // To Avoid TLE
        
        pq.push({0, src, 0});
        
        while (!pq.empty()) {
            auto top = pq.top();
            pq.pop();
            
            auto [cost, curr, stops] = top;
            
            if(stops > discovery[curr]) continue;  // To Avoid TLE
		    discovery[curr] = stops;
            
            if (curr == dst) return cost;
            
            if (stops > k) continue;
            
            for (auto it : graph[curr]) {
                auto [n, c] = it;
                
                pq.push({cost + c, n, stops + 1});
            }
        }
        
        return -1;
    }
};
```
