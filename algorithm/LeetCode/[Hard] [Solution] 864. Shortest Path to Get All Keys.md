864. Shortest Path to Get All Keys

We are given a 2-dimensional `grid`. `"."` is an empty cell, `"#"` is a wall, `"@"` is the starting point, `("a", "b", ...)` are keys, and `("A", "B", ...)` are locks.

We start at the starting point, and one move consists of walking one space in one of the 4 cardinal directions.  We cannot walk outside the grid, or walk into a wall.  If we walk over a key, we pick it up.  We can't walk over a lock unless we have the corresponding key.

For some `1 <= K <= 6`, there is exactly one lowercase and one uppercase letter of the first `K` letters of the English alphabet in the grid.  This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.

Return the lowest number of moves to acquire all keys.  If it's impossible, return `-1`.

 

**Example 1:**
```
Input: ["@.a.#","###.#","b.A.B"]
Output: 8
```

**Example 2:**
```
Input: ["@..aA","..B#.","....b"]
Output: 6
```

**Note:**

* `1 <= grid.length <= 30`
* `1 <= grid[0].length <= 30`
* `grid[i][j]` contains only ``'.', '#', '@', 'a'-'f'` and `'A'-'F'`
* The number of keys is in `[1, 6]`.  Each key has a different letter and opens exactly one lock.

## Approach 1: Brute Force + Permutations
**Intuition and Algorithm**

We have to pick up the keys $K$ in some order, say $K_{\sigma_i}$.

For each ordering, let's do a breadth first search to find the distance to the next key.

For example, if the keys are `'abcdef'`, then for each ordering such as 'bafedc', we will try to calculate the candidate distance from `'@' -> 'b' -> 'a' -> 'f' -> 'e' -> 'd' -> 'c'`.

Between each segment of our path (and corresponding breadth-first search), we should remember what keys we've picked up. Keys that are picked up become part of a mask that helps us identify what locks we are allowed to walk through during the next breadth-first search.

Each part of the algorithm is relatively straightforward, but the implementation in total can be quite challenging. See the comments for more details.

```python
class Solution(object):
    def shortestPathAllKeys(self, grid):
        R, C = len(grid), len(grid[0])
        # location['a'] = the coordinates of 'a' on the grid, etc.
        location = {v: (r, c)
                    for r, row in enumerate(grid)
                    for c, v in enumerate(row)
                    if v not in '.#'}

        def neighbors(r, c):
            for cr, cc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
                if 0 <= cr < R and 0 <= cc < C:
                    yield cr, cc

        def bfs(source, target, keys = ()):
            sr, sc = location[source]
            tr, tc = location[target]
            seen = [[False] * C for _ in xrange(R)]
            seen[sr][sc] = True
            queue = collections.deque([(sr, sc, 0)])
            while queue:
                r, c, d = queue.popleft()
                if r == tr and c == tc: return d
                for cr, cc in neighbors(r, c):
                    if not seen[cr][cc] and grid[cr][cc] != '#':
                        if grid[cr][cc].isupper() and grid[cr][cc].lower() not in keys:
                            continue
                        queue.append((cr,cc,d+1))
                        seen[cr][cc] = True
            return float('inf')

        ans = float('inf')
        keys = "".join(chr(ord('a') + i) for i in xrange(len(location) / 2))
        for cand in itertools.permutations(keys):
            # bns : the built candidate answer, consisting of the sum
            # of distances of the segments from '@' to cand[0] to cand[1] etc.
            bns = 0
            for i, target in enumerate(cand):
                source = cand[i-1] if i > 0 else '@'
                d = bfs(source, target, cand[:i])
                bns += d
                if bns >= ans: break
            else:
                ans = bns

        return ans if ans < float('inf') else -1
```

**Complexity Analysis**

* Time Complexity: $O(R * C * \mathcal{A} * \mathcal{A}!)$, where $R, C$ are the dimensions of the grid, and $\mathcal{A}$ is the maximum number of keys ($\mathcal{A}$ because it is the "size of the alphabet".) Each bfs is performed up to $\mathcal{A} * \mathcal{A}$ times.

* Space Complexity: $O(R * C + \mathcal{A}!)$, the space for the bfs and to store the candidate key permutations.


## Approach 2: Points of Interest + Dijkstra
**Intuition and Algorithm**

Clearly, we only really care about walking between points of interest: the keys, locks, and starting position. We can use this insight to speed up our calculation.

Let's make this intuition more formal: any walk can be decomposed into primitive segments, where each segment (between two points of interest) is primitive if and only if it doesn't touch any other point of interest in between.

Then, we can calculate the distance (of a primitive segment) between any two points of interest, using a breadth first search.

Afterwards, we have some graph (where each node refers to at most $13$ places, and at most $2^6$ states of keys). We have a starting node (at `'@'` with no keys) and ending nodes (at anywhere with all keys.) We also know all the costs to go from one node to another - each node has outdegree at most 13. This shortest path problem is now ideal for using Dijkstra's algorithm.

Dijkstra's algorithm uses a priority queue to continually searches the path with the lowest cost to destination, so that when we reach the target, we know it must have been through the lowest cost path. Refer to this link for more detail.

Again, each part of the algorithm is relatively straightforward (for those familiar with BFS and Dijkstra's algorithm), but the implementation in total can be quite challenging.

```python
class Solution(object):
    def shortestPathAllKeys(self, grid):
        R, C = len(grid), len(grid[0])

        # The points of interest
        location = {v: (r, c)
                    for r, row in enumerate(grid)
                    for c, v in enumerate(row)
                    if v not in '.#'}

        def neighbors(r, c):
            for cr, cc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
                if 0 <= cr < R and 0 <= cc < C:
                    yield cr, cc

        # The distance from source to each point of interest
        def bfs_from(source):
            r, c = location[source]
            seen = [[False] * C for _ in xrange(R)]
            seen[r][c] = True
            queue = collections.deque([(r, c, 0)])
            dist = {}
            while queue:
                r, c, d = queue.popleft()
                if source != grid[r][c] != '.':
                    dist[grid[r][c]] = d
                    continue # Stop walking from here if we reach a point of interest
                for cr, cc in neighbors(r, c):
                    if grid[cr][cc] != '#' and not seen[cr][cc]:
                        seen[cr][cc] = True
                        queue.append((cr, cc, d+1))
            return dist        

        dists = {place: bfs_from(place) for place in location}
        target_state = 2 ** sum(p.islower() for p in location) - 1

        #Dijkstra
        pq = [(0, '@', 0)]
        final_dist = collections.defaultdict(lambda: float('inf'))
        final_dist['@', 0] = 0
        while pq:
            d, place, state = heapq.heappop(pq)
            if final_dist[place, state] < d: continue
            if state == target_state: return d
            for destination, d2 in dists[place].iteritems():
                state2 = state
                if destination.islower(): #key
                    state2 |= (1 << (ord(destination) - ord('a')))
                elif destination.isupper(): #lock
                    if not(state & (1 << (ord(destination) - ord('A')))): #no key
                        continue

                if d + d2 < final_dist[destination, state2]:
                    final_dist[destination, state2] = d + d2
                    heapq.heappush(pq, (d+d2, destination, state2))

        return -1
```

**Complexity Analysis**

* Time Complexity: $O(RC(2\mathcal{A} + 1) + \mathcal{E} \log \mathcal{N})$, where $R, C$ are the dimensions of the grid, and $\mathcal{A}$ is the maximum number of keys, $\mathcal{N} = (2\mathcal{A} + 1) * 2^\mathcal{A}$ is the number of nodes when we perform Dijkstra's, and $\mathcal{E} = \mathcal{N} * (2 \mathcal{A} + 1)$ is the maximum number of edges.

* Space Complexity: $O(\mathcal{N})$.

# Submissions
---
**Soluti0on 1: (Brute Force + Permutations)**
```
Runtime: 11256 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        R, C = len(grid), len(grid[0])
        # location['a'] = the coordinates of 'a' on the grid, etc.
        location = {v: (r, c)
                    for r, row in enumerate(grid)
                    for c, v in enumerate(row)
                    if v not in '.#'}

        def neighbors(r, c):
            for cr, cc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
                if 0 <= cr < R and 0 <= cc < C:
                    yield cr, cc

        def bfs(source, target, keys = ()):
            sr, sc = location[source]
            tr, tc = location[target]
            seen = [[False] * C for _ in range(R)]
            seen[sr][sc] = True
            queue = collections.deque([(sr, sc, 0)])
            while queue:
                r, c, d = queue.popleft()
                if r == tr and c == tc: return d
                for cr, cc in neighbors(r, c):
                    if not seen[cr][cc] and grid[cr][cc] != '#':
                        if grid[cr][cc].isupper() and grid[cr][cc].lower() not in keys:
                            continue
                        queue.append((cr,cc,d+1))
                        seen[cr][cc] = True
            return float('inf')

        ans = float('inf')
        keys = "".join(chr(ord('a') + i) for i in range(len(location) // 2))
        for cand in itertools.permutations(keys):
            # bns : the built candidate answer, consisting of the sum
            # of distances of the segments from '@' to cand[0] to cand[1] etc.
            bns = 0
            for i, target in enumerate(cand):
                source = cand[i-1] if i > 0 else '@'
                d = bfs(source, target, cand[:i])
                bns += d
                if bns >= ans: break
            else:
                ans = bns

        return ans if ans < float('inf') else -1
```

**Solution 2: (Points of Interest + Dijkstra)**
```
Runtime: 152 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        R, C = len(grid), len(grid[0])

        # The points of interest
        location = {v: (r, c)
                    for r, row in enumerate(grid)
                    for c, v in enumerate(row)
                    if v not in '.#'}

        def neighbors(r, c):
            for cr, cc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
                if 0 <= cr < R and 0 <= cc < C:
                    yield cr, cc

        # The distance from source to each point of interest
        def bfs_from(source):
            r, c = location[source]
            seen = [[False] * C for _ in range(R)]
            seen[r][c] = True
            queue = collections.deque([(r, c, 0)])
            dist = {}
            while queue:
                r, c, d = queue.popleft()
                if source != grid[r][c] != '.':
                    dist[grid[r][c]] = d
                    continue # Stop walking from here if we reach a point of interest
                for cr, cc in neighbors(r, c):
                    if grid[cr][cc] != '#' and not seen[cr][cc]:
                        seen[cr][cc] = True
                        queue.append((cr, cc, d+1))
            return dist        

        dists = {place: bfs_from(place) for place in location}
        target_state = 2 ** sum(p.islower() for p in location) - 1

        #Dijkstra
        pq = [(0, '@', 0)]
        final_dist = collections.defaultdict(lambda: float('inf'))
        final_dist['@', 0] = 0
        while pq:
            d, place, state = heapq.heappop(pq)
            if final_dist[place, state] < d: continue
            if state == target_state: return d
            for destination, d2 in dists[place].items():
                state2 = state
                if destination.islower(): #key
                    state2 |= (1 << (ord(destination) - ord('a')))
                elif destination.isupper(): #lock
                    if not(state & (1 << (ord(destination) - ord('A')))): #no key
                        continue

                if d + d2 < final_dist[destination, state2]:
                    final_dist[destination, state2] = d + d2
                    heapq.heappush(pq, (d+d2, destination, state2))

        return -1
```