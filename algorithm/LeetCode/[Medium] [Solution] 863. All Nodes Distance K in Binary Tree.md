863. All Nodes Distance K in Binary Tree

We are given a binary tree (with root node `root`), a `target` node, and an integer value `K`.

Return a list of the values of all nodes that have a distance `K` from the `target` node.  The answer can be returned in any order.

 

**Example 1:**
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.
```
![863_sketch0.png](img/863_sketch0.png)
```
Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.
```

**Note:**

* The given tree is non-empty.
* Each node in the tree has unique values `0 <= node.val <= 500`.
* The `target` node is a node in the tree.
* `0 <= K <= 1000`.

# Solution
---
## Approach 1: Annotate Parent
**Intuition**

If we know the parent of every node `x`, we know all nodes that are distance `1` from `x`. We can then perform a breadth first search from the `target` node to find the answer.

**Algorithm**

We first do a depth first search where we annotate every node with information about it's parent.

After, we do a breadth first search to find all nodes a distance `K` from the `target`.

```python
class Solution(object):
    def distanceK(self, root, target, K):
        def dfs(node, par = None):
            if node:
                node.par = par
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)

        queue = collections.deque([(target, 0)])
        seen = {target}
        while queue:
            if queue[0][1] == K:
                return [node.val for node, d in queue]
            node, d = queue.popleft()
            for nei in (node.left, node.right, node.par):
                if nei and nei not in seen:
                    seen.add(nei)
                    queue.append((nei, d+1))

        return []
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the number of nodes in the given tree.

* Space Complexity: $O(N)$.

## Approach 2: Percolate Distance
**Intuition**

From `root`, say the `target` node is at depth `3` in the left branch. It means that any nodes that are distance `K - 3` in the right branch should be added to the answer.

**Algorithm**

Traverse every node with a depth first search `dfs`. We'll add all nodes `x` to the answer such that node is the node on the path from `x` to `target` that is closest to the `root`.

To help us, `dfs(node)` will return the distance from node to the `target`. Then, there are 4 cases:

1. If `node == target`, then we should add nodes that are distance `K` in the subtree rooted at `target`.

1. If `target` is in the left branch of `node`, say at distance `L+1`, then we should look for nodes that are distance `K - L - 1` in the right branch.

1. If `target` is in the right branch of `node`, the algorithm proceeds similarly.

1. If `target` isn't in either branch of `node`, then we stop.

In the above algorithm, we make use of the auxillary function `subtree_add(node, dist)` which adds the nodes in the subtree rooted at `node` that are distance `K - dist` from the given `node`.

```python
class Solution(object):
    def distanceK(self, root, target, K):
        ans = []

        # Return distance from node to target if exists, else -1
        # Vertex distance: the # of vertices on the path from node to target
        def dfs(node):
            if not node:
                return -1
            elif node is target:
                subtree_add(node, 0)
                return 1
            else:
                L, R = dfs(node.left), dfs(node.right)
                if L != -1:
                    if L == K: ans.append(node.val)
                    subtree_add(node.right, L + 1)
                    return L + 1
                elif R != -1:
                    if R == K: ans.append(node.val)
                    subtree_add(node.left, R + 1)
                    return R + 1
                else:
                    return -1

        # Add all nodes 'K - dist' from the node to answer.
        def subtree_add(node, dist):
            if not node:
                return
            elif dist == K:
                ans.append(node.val)
            else:
                subtree_add(node.left, dist + 1)
                subtree_add(node.right, dist + 1)

        dfs(root)
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the number of nodes in the given tree.

* Space Complexity: $O(N)$.

# Submissions
---
**Solution 1: (DFS, BFS)**
```
Runtime: 32 ms
Memory Usage: 13.1 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        graph = collections.defaultdict(list)
        def dfs(node):
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                dfs(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                dfs(node.right)
        
        dfs(root)
        level = [target.val]
        ans = []
        visited = set(level)
        while level and K > 0:
            level = [nei for node in level for nei in graph[node] if nei not in visited]
            visited = visited | set(level)
            K -= 1
        return level if K == 0 else []
```