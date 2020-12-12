865. Smallest Subtree with all the Deepest Nodes

Given a binary tree rooted at `root`, the depth of each node is the shortest distance to the root.

A node is deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is that node, plus the set of all descendants of that node.

Return the node with the largest depth such that it contains all the deepest nodes in its subtree.

 

**Example 1:**
```
Input: [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation:
```
![865_sketch1.png](img/865_sketch1.png)
```
We return the node with value 2, colored in yellow in the diagram.
The nodes colored in blue are the deepest nodes of the tree.
The input "[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]" is a serialization of the given tree.
The output "[2, 7, 4]" is a serialization of the subtree rooted at the node with value 2.
Both the input and output have TreeNode type.
```

**Note:**

* The number of nodes in the tree will be between 1 and 500.
* The values of each node are unique.

# Submissions
---
## Approach 1: Paint Deepest Nodes
**Intuition**

We try a straightforward approach that has two phases.

The first phase is to identify the nodes of the tree that are deepest. To do this, we have to annotate the depth of each node. We can do this with a depth first search.

Afterwards, we will use that annotation to help us find the answer:

* If the `node` in question has maximum depth, it is the answer.

* If both the left and right child of a `node` have a deepest descendant, then the answer is this parent node.

* Otherwise, if some child has a deepest descendant, then the answer is that child.

* Otherwise, the answer for this subtree doesn't exist.

**Algorithm**

In the first phase, we use a depth first search `dfs` to annotate our nodes.

In the second phase, we also use a depth first search `answer(node)`, returning the answer for the subtree at that node, and using the rules above to build our answer from the answers of the children of node.

Note that in this approach, the `answer` function returns answers that have the deepest nodes of the entire tree, not just the subtree being considered.

```python
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        # Tag each node with it's depth.
        depth = {None: -1}
        def dfs(node, parent = None):
            if node:
                depth[node] = depth[parent] + 1
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root)

        max_depth = max(depth.itervalues())

        def answer(node):
            # Return the answer for the subtree at node.
            if not node or depth.get(node, None) == max_depth:
                return node
            L, R = answer(node.left), answer(node.right)
            return node if L and R else L or R

        return answer(root)
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the number of nodes in the tree.

* Space Complexity: $O(N)$.

## Approach 2: Recursion
**Intuition**

We can combine both depth first searches in Approach #1 into an approach that does both steps in one pass. We will have some function `dfs(node)` that returns both the answer for this subtree, and the distance from node to the deepest nodes in this subtree.

**Algorithm**

The Result (on some subtree) returned by our (depth-first search) recursion will have two parts:

* `Result.node`: the largest depth node that is equal to or an ancestor of all the deepest nodes of this subtree.
* `Result.dist`: the number of nodes in the path from the root of this subtree, to the deepest node in this subtree.

We can calculate these answers disjointly for `dfs(node)`:

* To calculate the `Result.node` of our answer:

    * If one `childResult` has deeper nodes, then `childResult.node` will be the answer.

    * If they both have the same depth nodes, then `node` will be the answer.

The `Result.dist` of our answer is always 1 more than the largest `childResult.dist` we have.

```python
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        # The result of a subtree is:
        # Result.node: the largest depth node that is equal to or
        #              an ancestor of all the deepest nodes of this subtree.
        # Result.dist: the number of nodes in the path from the root
        #              of this subtree, to the deepest node in this subtree.
        Result = collections.namedtuple("Result", ("node", "dist"))
        def dfs(node):
            # Return the result of the subtree at this node.
            if not node: return Result(None, 0)
            L, R = dfs(node.left), dfs(node.right)
            if L.dist > R.dist: return Result(L.node, L.dist + 1)
            if L.dist < R.dist: return Result(R.node, R.dist + 1)
            return Result(node, L.dist + 1)

        return dfs(root).node
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the number of nodes in the tree.

* Space Complexity: $O(N)$.

# Submissions
---
**Solution 1: (Recursion)**
```
Runtime: 28 ms
Memory Usage: 12.9 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        # The result of a subtree is:
        # Result.node: the largest depth node that is equal to or
        #              an ancestor of all the deepest nodes of this subtree.
        # Result.dist: the number of nodes in the path from the root
        #              of this subtree, to the deepest node in this subtree.
        Result = collections.namedtuple("Result", ("node", "dist"))
        def dfs(node):
            # Return the result of the subtree at this node.
            if not node: return Result(None, 0)
            L, R = dfs(node.left), dfs(node.right)
            if L.dist > R.dist: return Result(L.node, L.dist + 1)
            if L.dist < R.dist: return Result(R.node, R.dist + 1)
            return Result(node, L.dist + 1)

        return dfs(root).node
```

**solution 2: (DFS)**
```
Runtime: 28 ms
Memory Usage: 14.5 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        def dfs(node, depth):
            if not node:
                return [depth, None]
            left_depth, left_node = dfs(node.left, depth+1)
            right_depth, right_node = dfs(node.right, depth+1)
            if left_depth > right_depth:
                return [left_depth, left_node]
            elif left_depth < right_depth:
                return [right_depth, right_node]
            else:
                return [left_depth, node]
        
        return dfs(root, 0)[1]
```