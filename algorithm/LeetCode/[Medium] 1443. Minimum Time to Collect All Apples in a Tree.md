1443. Minimum Time to Collect All Apples in a Tree

Given an undirected tree consisting of `n` vertices numbered from `0` to `n-1`, which has some apples in their vertices. You spend `1` second to walk over one edge of the tree. Return the minimum time in seconds you have to spend in order to collect all apples in the tree starting at **vertex 0** and coming back to this vertex.

The edges of the undirected tree are given in the array edges, where `edges[i] = [fromi, toi]` means that exists an edge connecting the vertices `fromi` and `toi`. Additionally, there is a boolean array `hasApple`, where `hasApple[i] = true` means that vertex `i` has an apple, otherwise, it does not have any apple.

 

**Example 1:**

![1443_min_time_collect_apple_1.png](img/1443_min_time_collect_apple_1.png)
```
Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,true,true,false]
Output: 8 
Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.
```

**Example 2:**

![1443_min_time_collect_apple_2.png](img/1443_min_time_collect_apple_2.png)
```
Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,false,true,false]
Output: 6
Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.
```

**Example 3:**
```
Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,false,false,false,false,false]
Output: 0
```

**Constraints:**

* `1 <= n <= 10^5`
* `edges.length == n-1`
* `edges[i].length == 2`
* `fromi < toi`
* `hasApple.length == n`

# Submissions
---
**Solution 1: (DFS, postorder)**
```
Runtime: 673 ms
Memory: 50.9 MB
```
```pytho
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        g = collections.defaultdict(list)
        for a, b in edges:
            g[a] += [b]
            g[b] += [a]

        def dfs(u, p):
            rst = 0
            for v in g[u]:
                if v == p:
                    continue
                rst += dfs(v, u)
            if (hasApple[u] or rst > 0) and u != 0:
                rst += 2
            return rst

        return dfs(0, -1)
```

