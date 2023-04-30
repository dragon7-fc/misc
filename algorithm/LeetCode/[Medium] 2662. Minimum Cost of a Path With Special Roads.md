2662. Minimum Cost of a Path With Special Roads

You are given an array `start` where `start = [startX, startY]` represents your initial position `(startX, startY)` in a 2D space. You are also given the array `target` where `target = [targetX, targetY]` represents your target position `(targetX, targetY)`.

The cost of going from a position `(x1, y1)` to any other position in the space `(x2, y2)` is `|x2 - x1| + |y2 - y1|`.

There are also some special roads. You are given a 2D array `specialRoads` where `specialRoads[i] = [x1i, y1i, x2i, y2i, costi]` indicates that the `i`th special road can take you from `(x1i, y1i)` to `(x2i, y2i)` with a cost equal to `costi`. You can use each special road any number of times.

Return the minimum cost required to go from `(startX, startY)` to `(targetX, targetY)`.

 

**Example 1:**
```
Input: start = [1,1], target = [4,5], specialRoads = [[1,2,3,3,2],[3,4,4,5,1]]
Output: 5
Explanation: The optimal path from (1,1) to (4,5) is the following:
- (1,1) -> (1,2). This move has a cost of |1 - 1| + |2 - 1| = 1.
- (1,2) -> (3,3). This move uses the first special edge, the cost is 2.
- (3,3) -> (3,4). This move has a cost of |3 - 3| + |4 - 3| = 1.
- (3,4) -> (4,5). This move uses the second special edge, the cost is 1.
So the total cost is 1 + 2 + 1 + 1 = 5.
It can be shown that we cannot achieve a smaller total cost than 5.
```

**Example 2:**
```
Input: start = [3,2], target = [5,7], specialRoads = [[3,2,3,4,4],[3,3,5,5,5],[3,4,5,6,6]]
Output: 7
Explanation: It is optimal to not use any special edges and go directly from the starting to the ending position with a cost |5 - 3| + |7 - 2| = 7.
```

**Constraints:**

* `start.length == target.length == 2`
* `1 <= startX <= targetX <= 10^5`
* `1 <= startY <= targetY <= 10^5`
* `1 <= specialRoads.length <= 200`
* `specialRoads[i].length == 5`
* `startX <= x1i, x2i <= targetX`
* `startY <= y1i, y2i <= targetY`
* `1 <= costi <= 105`

# Submissions
---
**Solution 1: (Dijkstras)**
```
Runtime: 169 ms
Memory: 72.3 MB
```
```c++
class Solution {
public:
    int minimumCost(vector<int>& start, vector<int>& target, vector<vector<int>>& specialRoads) {
        // use dijkstras algorithm
        int sx = start[0], sy = start[1];
        int tx = target[0], ty = target[1];
        priority_queue<pair<long long ,pair<int, int>>, vector<pair<long long ,pair<int, int>>>,greater<pair<long long ,pair<int, int>>>> pq;
        long long INF = 1e12;
        map<pair<int, int>, long long> distance;
        auto dist = [&](int x, int y) {
            if(not distance.count({x, y})) distance[{x, y}] = INF;
            return distance[{x, y}];
        };
        pq.push({0, {sx, sy}});
        distance[{sx, sy}] = 0;
        while (!pq.empty()) {
            long long d = pq.top().first;
            auto [cx, cy] = pq.top().second;
            pq.pop();
            if (cx == tx and cy == ty) {
                return d;
            }
            
            // directly go to target
            long long direct = d + abs(cx-tx) + abs(cy-ty);
            pq.push({direct, {tx, ty}});

            // take some road
            for (vector<int> &road : specialRoads) {
                int fromx = road[0], fromy = road[1];
                int tox  = road[2], toy = road[3];
                long long cost = road[4];
                long long val = d + cost + abs(cx-fromx) + abs(cy-fromy);
                if (dist(tox, toy) > val) {
                    distance[{tox, toy}] = val;
                    pq.push({val, {tox, toy}});
                }
            }
        }
        
        return -1;
    }
};
```
