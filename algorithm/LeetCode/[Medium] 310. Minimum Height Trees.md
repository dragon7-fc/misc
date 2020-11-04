310. Minimum Height Trees

For an undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

**Format**
The graph contains `n` nodes which are labeled from `0` to `n - 1`. You will be given the number `n` and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate `edges` will appear in edges. Since all edges are undirected, `[0, 1]` is the same as `[1, 0]` and thus will not appear together in `edges`.

**Example 1 :**
```
Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3 

Output: [1]
```

**Example 2 :**
```
Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5 

Output: [3, 4]
```

**Note:**

* According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”
* The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

**Hint**

* How many MHTs can a graph have at most?

    For the tree-alike graph, the number of centroids is no more than 2.
    * If the number of nodes is even, then there would be two centroids.
    * If the number of nodes is odd, then there would be only one centroid 

# Submissions
---
**Solution 1: (Topological Sorting, BFS from leaf to centroid)**
```
Runtime: 228 ms
Memory Usage: 18.3 MB
```
```python
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        # base cases
        if n <= 2:
            return [i for i in range(n)]

        # Build the graph with the adjacency list
        neighbors = [set() for i in range(n)]
        for start, end in edges:
            neighbors[start].add(end)
            neighbors[end].add(start)

        # Initialize the first layer of leaves
        leaves = []
        for i in range(n):
            if len(neighbors[i]) == 1:
                leaves.append(i)

        # Trim the leaves until reaching the centroids
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []
            # remove the current leaves along with the edges
            while leaves:
                leaf = leaves.pop()
                for neighbor in neighbors[leaf]:
                    neighbors[neighbor].remove(leaf)
                    if len(neighbors[neighbor]) == 1:
                        new_leaves.append(neighbor)

            # prepare for the next round
            leaves = new_leaves

        # The remaining nodes are the centroids of the graph
        return leaves
```