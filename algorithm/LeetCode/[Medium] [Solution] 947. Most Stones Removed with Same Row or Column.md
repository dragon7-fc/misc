947. Most Stones Removed with Same Row or Column

On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point may have at most one stone.

Now, a move consists of removing a stone that shares a column or row with another stone on the grid.

What is the largest possible number of moves we can make?

 

**Example 1:**
```
Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
```

**Example 2:**
```
Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
```

**Example 3:**
```
Input: stones = [[0,0]]
Output: 0
```

**Note:**

* `1 <= stones.length <= 1000`
* `0 <= stones[i][j] < 10000`

# Solution
---
## Approach 1: Depth-First Search
**Intuition**

Let's say two stones are connected by an edge if they share a row or column, and define a connected component in the usual way for graphs: a subset of stones so that there doesn't exist an edge from a stone in the subset to a stone not in the subset. For convenience, we refer to a component as meaning a connected component.

The main insight is that we can always make moves that reduce the number of stones in each component to 1.

Firstly, every stone belongs to exactly one component, and moves in one component do not affect another component.

Now, consider a spanning tree of our component. We can make moves repeatedly from the leaves of this tree until there is one stone left.

**Algorithm**

To count connected components of the above graph, we will use depth-first search.

For every stone not yet visited, we will visit it and any stone in the same connected component. Our depth-first search traverses each node in the component.

For each component, the answer changes by ``-1 + component.size`.

```python
class Solution(object):
    def removeStones(self, stones):
        graph = collections.defaultdict(list)
        for i, x in enumerate(stones):
            for j in xrange(i):
                y = stones[j]
                if x[0]==y[0] or x[1]==y[1]:
                    graph[i].append(j)
                    graph[j].append(i)

        N = len(stones)
        ans = 0

        seen = [False] * N
        for i in xrange(N):
            if not seen[i]:
                stack = [i]
                seen[i] = True
                while stack:
                    ans += 1
                    node = stack.pop()
                    for nei in graph[node]:
                        if not seen[nei]:
                            stack.append(nei)
                            seen[nei] = True
                ans -= 1
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N^2)$, where $N$ is the length of `stones`.

* Space Complexity: $O(N^2)$.

## Approach 2: Union-Find
**Intuition**

As in Approach 1, we will need to consider components of an underlying graph. A "Disjoint Set Union" (DSU) data structure is ideal for this.

We will skip the explanation of how a DSU structure is implemented. Please refer to https://leetcode.com/problems/redundant-connection/solution/ for a tutorial on DSU.

**Algorithm**

Let's connect row `i` to column `j`, which will be represented by `j+10000`. The answer is the number of components after making all the connections.

Note that for brevity, our `DSU` implementation does not use union-by-rank. This makes the asymptotic time complexity larger.

```python
class DSU:
    def __init__(self, N):
        self.p = range(N)

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr

class Solution(object):
    def removeStones(self, stones):
        N = len(stones)
        dsu = DSU(20000)
        for x, y in stones:
            dsu.union(x, y + 10000)

        return N - len({dsu.find(x) for x, y in stones})
```

**Complexity Analysis**

* Time Complexity: $O(N \log N)$, where $N$ is the length of `stones`. (If we used union-by-rank, this can be $O(N * \alpha(N))$), where $\alpha$ is the Inverse-Ackermann function.)

* Space Complexity: $O(N)$.

# Submissions
---
**Solution:**
```
Runtime: 1616 ms
Memory Usage: 13.2 MB
```
```python
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for i, x in enumerate(stones):
            for j in range(i):
                y = stones[j]
                if x[0]==y[0] or x[1]==y[1]:
                    graph[i].append(j)
                    graph[j].append(i)

        N = len(stones)
        ans = 0

        seen = [False] * N
        for i in range(N):
            if not seen[i]:
                stack = [i]
                seen[i] = True
                while stack:
                    ans += 1
                    node = stack.pop()
                    for nei in graph[node]:
                        if not seen[nei]:
                            stack.append(nei)
                            seen[nei] = True
                ans -= 1
        return ans
```
**Solution 1:**
```
Runtime: 1636 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for i, x in enumerate(stones):
            for j in range(i):
                y = stones[j]
                if x[0]==y[0] or x[1]==y[1]:
                    graph[i].append(j)
                    graph[j].append(i)

        N = len(stones)
        ans = 0

        seen = [False] * N
        def dfs(node):
            nonlocal ans
            if not seen[node]:
                seen[node] = True
                ans += 1
                for nei in graph[node]:
                    dfs(nei)

        for i in range(N):
            if not seen[i]:
                dfs(i)
                ans -= 1
        return ans
```

**Solution:**
```
Runtime: 192 ms
Memory Usage: 13.6 MB
```
```python
class DSU:
    def __init__(self, N):
        self.p = [_ for _ in range(N)]

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr
        
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        N = len(stones)
        dsu = DSU(20000)
        for x, y in stones:
            dsu.union(x, y + 10000)

        return N - len({dsu.find(x) for x, y in stones})
```