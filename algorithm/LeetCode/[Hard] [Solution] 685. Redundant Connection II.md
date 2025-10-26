685. Redundant Connection II

In this problem, a rooted tree is a **directed** graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.

The given input is a directed graph that started as a rooted tree with N nodes (with distinct values `1, 2, ..., N`), with one additional directed edge added. The added edge has two different vertices chosen from `1` to `N`, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair `[u, v]` that represents a **directed** edge connecting nodes `u` and `v`, where `u` is a parent of child `v`.

Return an edge that can be removed so that the resulting graph is a rooted tree of `N` nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array.

**Example 1:**
```
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given directed graph will be like this:
  1
 / \
v   v
2-->3
```

**Example 2:**
```
Input: [[1,2], [2,3], [3,4], [4,1], [1,5]]
Output: [4,1]
Explanation: The given directed graph will be like this:
5 <- 1 -> 2
     ^    |
     |    v
     4 <- 3
```

**Note:**

* The size of the input 2D-array will be between `3` and `1000`.
* Every integer represented in the 2D-array will be between `1` and `N`, where `N` is the size of the input array.

# Solution
---
## Approach #1: Depth-First Search [Accepted]
**Intuition**

Starting from a rooted tree with `N-1` edges and `N` vertices, let's enumerate the possibilities for the added "redundant" edge. If there is no loop, then either one vertex must have two parents (or no edge is redundant.) If there is a loop, then either one vertex has two parents, or every vertex has one parent.

In the first two cases, there are only two candidates for deleting an edge, and we can try removing the last one and seeing if that works. In the last case, the last edge of the cycle can be removed: for example, when `1->2->3->4->1->5`, we want the last edge (by order of occurrence) in the cycle `1->2->3->4->1` (but not necessarily `1->5`).

**Algorithm**

We'll first construct the underlying graph, keeping track of edges coming from nodes with multiple parents. After, we either have 2 or 0 `candidates`.

If there are no candidates, then every vertex has one parent, such as in the case `1->2->3->4->1->5`. From any node, we walk towards it's parent until we revisit a node - then we must be inside the cycle, and any future seen nodes are part of that cycle. Now we take the last edge that occurs in the cycle.

Otherwise, we'll see if the graph induced by `parent` is a rooted tree. We again take the `root` by walking from any node towards the parent until we can't, then we perform a depth-first search on this `root`. If we visit every node, then removing the last of the two edge candidates is acceptable, and we should. Otherwise, we should remove the first of the two edge candidates.

In our solution, we use `orbit` to find the result upon walking from a node x towards it's `parent` repeatedly until you revisit a node or can't walk anymore. `orbit(x).node` (or `orbit(x)[0]` in Python) will be the resulting node, while `orbit(x).seen` (or `orbit(x)[1]`) will be all the nodes visited.

```python
class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        N = len(edges)
        parent = {}
        candidates = []
        for u, v in edges:
            if v in parent:
                candidates.append((parent[v], v))
                candidates.append((u, v))
            else:
                parent[v] = u

        def orbit(node):
            seen = set()
            while node in parent and node not in seen:
                seen.add(node)
                node = parent[node]
            return node, seen

        root = orbit(1)[0]

        if not candidates:
            cycle = orbit(root)[1]
            for u, v in edges:
                if u in cycle and v in cycle:
                    ans = u, v
            return ans

        children = collections.defaultdict(list)
        for v in parent:
            children[parent[v]].append(v)

        seen = [True] + [False] * N
        stack = [root]
        while stack:
            node = stack.pop()
            if not seen[node]:
                seen[node] = True
                stack.extend(children[node])

        return candidates[all(seen)]
```

**Complexity Analysis**

* Time Complexity: $O(N)$ where $N$ is the number of vertices (and also the number of edges) in the graph. We perform a depth-first search.

* Space Complexity: $O(N)$, the size of the graph.

# Submissions
---
**Solution: (Depth-First Search)**
```
Runtime: 48 ms
Memory Usage: 13.2 MB
```
```python
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        parent = {}
        candidates = []  # 0 or 2 candidates (loop start, loop end)
        for u, v in edges:
            if v in parent:
                candidates.append((parent[v], v))
                candidates.append((u, v))
            else:
                parent[v] = u

        def orbit(node):
            seen = set()
            while node in parent and node not in seen:
                seen.add(node)
                node = parent[node]
            return node, seen

        root = orbit(1)[0]

        if not candidates:
            cycle = orbit(root)[1]
            for u, v in edges:
                if u in cycle and v in cycle:
                    ans = u, v
            return ans

        children = collections.defaultdict(list)
        for v in parent:
            children[parent[v]].append(v)

        seen = [True] + [False] * N
        stack = [root]
        while stack:
            node = stack.pop()
            if not seen[node]:
                seen[node] = True
                stack.extend(children[node])

        return candidates[all(seen)]
```

**Solution 2: (Union Find)**
```
Runtime: 64 ms
Memory Usage: 13.3 MB
```
```python
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        def isloop(end):
            cur = end
            while cur in parents:
                cur = parents[cur]
                if cur == end:
                    return True
            return False
        uf = {}
        def find(x):
            uf.setdefault(x, x)
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]
        def union(x, y):
            uf[find(x)] = find(y)
        parents = {}
        unionCandidate = []
        candidates = []
        for start, end in edges:
            if end not in parents:
                parents[end] = start
            else:
                candidates = [[parents[end], end],[start, end]]
            if find(start) == find(end):
                unionCandidate = [start, end]
            else:
                union(start, end)
        if candidates:
            if isloop(candidates[0][1]):
                return candidates[0]
            return candidates[1]
        else:
            return unionCandidate
```

**Solution 3: (Union Find)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 13.56 MB, Beats 93.35%
```
```c++
class Solution {
    vector<int> p;
    bool isLoop(int u, vector<int> &g) {
        int v = u;
        while (g[v] != -1) {
            v = g[v];
            if (v == u) {
                return true;
            }
        }
        return false;
    }
    int find(int x) {
        if (p[x] != x) {
            p[x] = find(p[x]);
        }
        return p[x];
    }
    void uni(int x, int y) {
        int rx = find(x), ry = find(y);
        p[rx] = p[ry];
    }
public:
    vector<int> findRedundantDirectedConnection(vector<vector<int>>& edges) {
        int n = edges.size(), i;
        p.resize(n + 1);
        for (i = 1; i < n; i ++) {
            p[i] = i;
        }
        vector<int> g(n + 1, -1);
        vector<vector<int>> candidates;
        vector<int> unionCandidate;
        for (auto &e: edges) {
            if (g[e[1]] == -1) {
                g[e[1]] = e[0];
            } else {
                candidates = {{g[e[1]], e[1]}, {e[0], e[1]}};
            }
            if (find(e[0]) == find(e[1])) {
                unionCandidate = {e[0], e[1]};
            } else {
                uni(e[0], e[1]);
            }
        }
        if (candidates.size()) {
            if (isLoop(candidates[0][1], g)) {
                return candidates[0];
            } else {
                return candidates[1];
            }
        }
        return unionCandidate;
    }
};
```
