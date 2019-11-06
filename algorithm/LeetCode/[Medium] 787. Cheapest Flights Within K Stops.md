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
**Solution 1: (Dijkstra's algorithm)**
```
Runtime: 84 ms
Memory Usage: 20 MB
```
```python
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        dic = collections.defaultdict(list)
        for s, d, price in flights:
            dic[s].append([d, price])
        q = [[0, src, 0]]
        heapq.heapify(q)
        while q:
            price, s, hop = heapq.heappop(q)
            if s == dst:
                return price
            if hop > K: continue
            for ele in dic[s]:
                heapq.heappush(q, [price+ele[1], ele[0], hop + 1])
        return -1
```