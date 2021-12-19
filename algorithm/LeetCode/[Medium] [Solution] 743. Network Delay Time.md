743. Network Delay Time

There are `N` network nodes, labelled `1` to `N`.

Given times, a list of travel times as **directed** edges `times[i] = (u, v, w)`, where `u` is the source node, `v` is the target node, and `w` is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node `K`. How long will it take for all nodes to receive the signal? If it is impossible, return `-1`.

**Example 1:**


```
Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2
```

**Note:**

* `N` will be in the range `[1, 100]`.
* `K` will be in the range `[1, N]`.
* The length of times will be in the range `[1, 6000]`.
* All edges `times[i] = (u, v, w)` will have `1 <= u, v <= N` and `0 <= w <= 100`.

# Solution
---
## Approach #1: Depth-First Search [Accepted]
**Intuition**

Let's record the time `dist[node]` when the signal reaches the node. If some signal arrived earlier, we don't need to broadcast it anymore. Otherwise, we should broadcast the signal.

**Algorithm**

We'll maintain `dist[node]`, the earliest that we arrived at each `node`. When visiting a `node` while `elapsed` time has elapsed, if this is the currently-fastest signal at this node, let's broadcast signals from this node.

To speed things up, at each visited node we'll consider signals exiting the node that are faster first, by sorting the edges.

```python
class Solution(object):
    def networkDelayTime(self, times, N, K):
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))

        dist = {node: float('inf') for node in xrange(1, N+1)}

        def dfs(node, elapsed):
            if elapsed >= dist[node]: return
            dist[node] = elapsed
            for time, nei in sorted(graph[node]):
                dfs(nei, elapsed + time)

        dfs(K, 0)
        ans = max(dist.values())
        return ans if ans < float('inf') else -1
```

**Complexity Analysis**

* Time Complexity: $O(N^N + E \log E)$ where $E$ is the length of times. We can only fully visit each node up to $N-1$ times, one per each other node. Plus, we have to explore every edge and sort them. Sorting each small bucket of outgoing edges is bounded by sorting all of them, because of repeated use of the inequality $x \log x + y \log y \leq (x+y) \log (x+y)$.

* Space Complexity: $O(N + E)$, the size of the graph $(O(E)$, plus the size of the implicit call stack in our DFS ($O(N)$).

## Approach #2: Dijkstra's Algorithm [Accepted]
**Intuition and Algorithm**

We use Dijkstra's algorithm to find the shortest path from our source to all targets. This is a textbook algorithm, refer to this link for more details.

Dijkstra's algorithm is based on repeatedly making the candidate move that has the least distance travelled.

In our implementations below, we showcase both $O(N^2)$ (basic) and $O(N \log N)$ (heap) approaches.

Basic Implementation

```python
class Solution(object):
    def networkDelayTime(self, times, N, K):
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {node: float('inf') for node in xrange(1, N+1)}
        seen = [False] * (N+1)
        dist[K] = 0

        while True:
            cand_node = -1
            cand_dist = float('inf')
            for i in xrange(1, N+1):
                if not seen[i] and dist[i] < cand_dist:
                    cand_dist = dist[i]
                    cand_node = i

            if cand_node < 0: break
            seen[cand_node] = True
            for nei, d in graph[cand_node]:
                dist[nei] = min(dist[nei], dist[cand_node] + d)

        ans = max(dist.values())
        return ans if ans < float('inf') else -1
```

Heap Implementation

```python
class Solution(object):
    def networkDelayTime(self, times, N, K):
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        pq = [(0, K)]
        dist = {}
        while pq:
            d, node = heapq.heappop(pq)
            if node in dist: continue
            dist[node] = d
            for nei, d2 in graph[node]:
                if nei not in dist:
                    heapq.heappush(pq, (d+d2, nei))

        return max(dist.values()) if len(dist) == N else -1
```

**Complexity Analysis**

* Time Complexity: $O(N^2 + E)$m where $E$ is the length of times in the basic implementation, and $O(E \log E)$ in the heap implementation, as potentially every edge gets added to the heap.

* Space Complexity: $O(N + E)$, the size of the graph ($O(E)$), plus the size of the other objects used ($O(N)$).

# Submissions
---
**Solution: (DFS, Graph)**
```
Runtime: 984 ms
Memory Usage: 16 MB
```
```python
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))

        dist = {node: float('inf') for node in range(1, N+1)}

        def dfs(node, elapsed):
            if elapsed >= dist[node]: return
            dist[node] = elapsed
            for time, nei in sorted(graph[node]):
                dfs(nei, elapsed + time)

        dfs(K, 0)
        ans = max(dist.values())
        return ans if ans < float('inf') else -1
```

**Solution: (BFS, Dijkstra's Algorithm, Graph)**
```
Runtime: 496 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        pq = [(0, K)]  # distance, node
        # heapq.heapify(pq)
        dist = {}  # visited node -> distance
        while pq:
            d, node = heapq.heappop(pq)  # get next smallest distance node
            if node in dist: continue
            dist[node] = d
            for nei, d2 in graph[node]:
                if nei not in dist:
                    heapq.heappush(pq, (d+d2, nei))  # append neighbor un-visited node

        return max(dist.values()) if len(dist) == N else -1
```

**Solution 2: (Dijkstra's Algorithm)**
```
Runtime: 131 ms
Memory Usage: 10.6 MB
```
```c
#undef INFINITY
#define INFINITY 1000
#define MAX 101
int flag[101][101]={0};
int dijkstra(int G[MAX][MAX],int n,int startnode)
{
 
	int cost[MAX][MAX],distance[MAX],pred[MAX];
	int visited[MAX],count,mindistance,nextnode,i,j;
	int ret=0;
	//pred[] stores the predecessor of each node
	//count gives the number of nodes seen so far
	//create the cost matrix
	for(i=0;i<n;i++)
		for(j=0;j<n;j++)
			if(G[i][j]==0&&flag[i][j]-1)
				cost[i][j]=INFINITY;
			else
				cost[i][j]=G[i][j];
	
	//initialize pred[],distance[] and visited[]
	for(i=0;i<n;i++)
	{
		distance[i]=cost[startnode][i];
		//pred[i]=startnode;
		visited[i]=0;
	}
	
	distance[startnode]=0;
	visited[startnode]=1;
	count=1;
	
	while(count<n)
	{
		mindistance=INFINITY;
		
		//nextnode gives the node at minimum distance
		for(i=0;i<n;i++)
			if(distance[i]<mindistance&&!visited[i])
			{
				mindistance=distance[i];
				nextnode=i;
			}
            if(distance[nextnode]>ret)
                ret=distance[nextnode];
			//check if a better path exists through nextnode			
			visited[nextnode]=1;
            if(mindistance==INFINITY)
                return -1;
			for(i=0;i<n;i++)
				if(!visited[i])
					if(mindistance+cost[nextnode][i]<distance[i])
					{
						distance[i]=mindistance+cost[nextnode][i];
						//pred[i]=nextnode;
                        
					}
		count++;
	}
    //print the path and distance of each node
	/*for(i=0;i<n;i++)
		if(i!=startnode)
		{
			printf("\nDistance of node%d=%d",i+1,distance[i]);
			printf("\nPath=%d",i+1);
			
			j=i;
			do
			{
				j=pred[j];
				printf("<-%d",j+1);
			}while(j!=startnode);
	}*/

    return ret;

}

int networkDelayTime(int** times, int timesSize, int* timesColSize, int n, int k){
    int G[101][101]={0};
    for(int i=0;i<timesSize;i++)
    {
        if(times[i][2]==0)
            flag[times[i][0]-1][times[i][1]-1]=1;
        G[times[i][0]-1][times[i][1]-1]=times[i][2];
    }
    return dijkstra(G,n,k-1);
}
```
