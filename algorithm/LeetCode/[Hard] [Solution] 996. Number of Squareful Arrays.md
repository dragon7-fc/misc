996. Number of Squareful Arrays

Given an array `A` of non-negative integers, the array is squareful if for every pair of adjacent elements, their sum is a perfect square.

Return the number of permutations of `A` that are squareful.  Two permutations `A1` and `A2` differ if and only if there is some index `i` such that `A1[i] != A2[i]`.

 

**Example 1:**
```
Input: [1,17,8]
Output: 2
Explanation: 
[1,8,17] and [17,8,1] are the valid permutations.
```

**Example 2:**
```
Input: [2,2,2]
Output: 1
```

**Note:**

* `1 <= A.length <= 12`
* `0 <= A[i] <= 1e9`

# Solution
---
## Approach 1: Backtracking
**Intuition**

Construct a graph where an edge from $i$ to $j$ exists if $A[i] + A[j]$ is a perfect square. Our goal is to investigate Hamiltonian paths of this graph: paths that visit all the nodes exactly once.

**Algorithm**

Let's keep a current `count` of what values of nodes are left to visit, and a count `todo` of how many nodes left to visit.

From each node, we can explore all neighboring nodes (by value, which reduces the complexity blowup).

Please see the inline comments for more details.

```python
class Solution(object):
    def numSquarefulPerms(self, A):
        N = len(A)
        count = collections.Counter(A)

        graph = {x: [] for x in count}
        for x in count:
            for y in count:
                if int((x+y)**.5 + 0.5) ** 2 == x+y:
                    graph[x].append(y)

        def dfs(x, todo):
            count[x] -= 1
            if todo == 0:
                ans = 1
            else:
                ans = 0
                for y in graph[x]:
                    if count[y]:
                        ans += dfs(y, todo - 1)
            count[x] += 1
            return ans

        return sum(dfs(x, len(A) - 1) for x in count)
```

**Complexity Analysis**

* Time Complexity: $O(N^N)$, where $N$ is length of `A`. A tighter bound is outside the scope of this article. However, it can be shown that the underlying graph is triangle free, as well as other properties that would dramatically shrink this complexity.

* Space Complexity: $O(N)$.

## Approach 2: Dynamic Programming
**Intuition**

As in Approach 1, construct an underlying graph. Since the number of nodes is small, we can use dynamic programming with a 'visited' mask.

**Algorithm**

We construct the graph in the same method as in Approach 1.

Now, let `dfs(node, visited)` be the number of ways from `node` to visit the remaining unvisited nodes. Here, visited is a mask: `(visited >> i) & 1` is true if and only if the `i`th node has been visited.

Afterwards, we may have overcounted if there are repeated values in `A`. To account for this, for every `x` in `A`, if `A` contains `x` a total of `k` times, we divide the answer by `k!`.

```python
from functools import lru_cache

class Solution:
    def numSquarefulPerms(self, A):
        N = len(A)

        def edge(x, y):
            r = math.sqrt(x+y)
            return int(r + 0.5) ** 2 == x+y

        graph = [[] for _ in range(len(A))]
        for i, x in enumerate(A):
            for j in range(i):
                if edge(x, A[j]):
                    graph[i].append(j)
                    graph[j].append(i)

        # find num of hamiltonian paths in graph

        @lru_cache(None)
        def dfs(node, visited):
            if visited == (1 << N) - 1:
                return 1

            ans = 0
            for nei in graph[node]:
                if (visited >> nei) & 1 == 0:
                    ans += dfs(nei, visited | (1 << nei))
            return ans

        ans = sum(dfs(i, 1<<i) for i in range(N))
        count = collections.Counter(A)
        for v in count.values():
            ans //= math.factorial(v)
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N 2^N)$, where $N$ is length of `A`.

* Space Complexity: $O(N 2^N)$.

# Submissions
---
