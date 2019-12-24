1145. Binary Tree Coloring Game

Two players play a turn based game on a binary tree.  We are given the `root` of this binary tree, and the number of nodes `n` in the tree.  `n` is odd, and each node has a distinct value from `1` to `n`.

Initially, the first player names a value `x` with `1 <= x <= n`, and the second player names a value `y` with `1 <= y <= n` and `y != x`.  The first player colors the node with value `x` red, and the second player colors the node with value `y` blue.

Then, the players take turns starting with the first player.  In each turn, that player chooses a node of their color (red if player 1, blue if player 2) and colors an **uncolored** neighbor of the chosen node (either the left child, right child, or parent of the chosen node.)

If (and only if) a player cannot choose such a node in this way, they must pass their turn.  If both players pass their turn, the game ends, and the winner is the player that colored more nodes.

You are the second player.  If it is possible to choose such a `y` to ensure you win the game, return `true`.  If it is not possible, return `false`.

 

**Example 1:**

![1145_1480-binary-tree-coloring-game.png](img/1145_1480-binary-tree-coloring-game.png)
```
Input: root = [1,2,3,4,5,6,7,8,9,10,11], n = 11, x = 3
Output: true
Explanation: The second player can choose the node with value 2.
``` 

**Constraints:**

* `root` is the root of a binary tree with `n` nodes and distinct node values from `1` to `n`.
* `n` is odd.
* `1 <= x <= n <= 100`

# Submissions
---
**Solution 1:**

* Since we're following the parent pointer, treat the binary tree as a graph
* The `x` divides the graph into at most 3 subgraphs (left, right, parent)
* The optimal move is to play adjacent to x so we can colour one of the three subgraph

```
Runtime: 32 ms
Memory Usage: 12.8 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        self.l, self.r = None, None
        def numNodes(root, x):
            if not root:
                return 0 
            l = numNodes(root.left, x)
            r = numNodes(root.right, x)
            if root.val == x:
                self.l = l
                self.r = r
            return l + r + 1
        numNodes(root,x)
        return max(self.l, self.r, n - self.l - self.r - 1) > n/2
```