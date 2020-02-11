1129. Shortest Path with Alternating Colors

Consider a directed graph, with nodes labelled `0, 1, ..., n-1`.  In this graph, each edge is either red or blue, and there could be self-edges or parallel edges.

Each `[i, j]` in `red_edges` denotes a red directed edge from node `i` to node `j`.  Similarly, each `[i, j]` in `blue_edges` denotes a blue directed edge from node `i` to node `j`.

Return an array `answer` of length `n`, where each `answer[X]` is the length of the shortest path from node `0` to node `X` such that the edge colors alternate along the path (or `-1` if such a path doesn't exist).

 

**Example 1:**
```
Input: n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
Output: [0,1,-1]
```

**Example 2:**
```
Input: n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]
Output: [0,1,-1]
```

**Example 3:**
```
Input: n = 3, red_edges = [[1,0]], blue_edges = [[2,1]]
Output: [0,-1,-1]
```

**Example 4:**
```
Input: n = 3, red_edges = [[0,1]], blue_edges = [[1,2]]
Output: [0,1,2]
```

**Example 5:**
```
Input: n = 3, red_edges = [[0,1],[0,2]], blue_edges = [[1,0]]
Output: [0,1,1]
```

**Constraints:**

* `1 <= n <= 100`
* `red_edges.length <= 400`
* `blue_edges.length <= 400`
* `red_edges[i].length == blue_edges[i].length == 2`
* `0 <= red_edges[i][j], blue_edges[i][j] < n`

# Submissions
---
**Solution 1: (BFS, Graph)**
```
Runtime: 88 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        queue = [(0,0,0),(0,1,0)]
        seen = set()
        ans = [-1]*(n)

        graph = collections.defaultdict(list)

        for s,e in red_edges:
            graph[s].append((e,0))
        for s,e in blue_edges:
            graph[s].append((e,1))

        while queue:
            cur, color,depth = queue.pop(0)
            seen.add((cur, color))
            if ans[cur] == -1:
                ans[cur] = depth 
            for nei, nei_color in graph[cur]:
                if nei_color == (1-color):
                    if (nei, nei_color) not in seen:
                        queue.append((nei, nei_color, depth+1))
        return ans
```