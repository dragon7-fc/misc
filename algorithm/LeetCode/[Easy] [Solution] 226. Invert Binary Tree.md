226. Invert Binary Tree

Invert a binary tree.

**Example:**
```
Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
```

**Trivia:**

This problem was inspired by this original tweet by Max Howell:

>Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.

# Solution
---
## Approach #1 (Recursive) [Accepted]
This is a classic tree problem that is best-suited for a recursive approach.

**Algorithm**

The inverse of an empty tree is the empty tree. The inverse of a tree with root $r$, and subtrees $\mbox{right}$ and $\mbox{left}$, is a tree with root $r$, whose right subtree is the inverse of $\mbox{left}$, and whose left subtree is the inverse of $\mbox{right}$.

```Java
public TreeNode invertTree(TreeNode root) {
    if (root == null) {
        return null;
    }
    TreeNode right = invertTree(root.right);
    TreeNode left = invertTree(root.left);
    root.left = right;
    root.right = left;
    return root;
}
```
**Complexity Analysis**

Since each node in the tree is visited only once, the time complexity is $O(n)$, where $n$ is the number of nodes in the tree. We cannot do better than that, since at the very least we have to visit each node to invert it.

Because of recursion, $O(h)$ function calls will be placed on the stack in the worst case, where $h$ is the height of the tree. Because $h\in O(n)$, the space complexity is $O(n)$.


## Approach #2 (Iterative) [Accepted]
Alternatively, we can solve the problem iteratively, in a manner similar to breadth-first search.

**Algorithm**

The idea is that we need to swap the left and right child of all nodes in the tree. So we create a queue to store nodes whose left and right child have not been swapped yet. Initially, only the root is in the queue. As long as the queue is not empty, remove the next node from the queue, swap its children, and add the children to the queue. Null nodes are not added to the queue. Eventually, the queue will be empty and all the children swapped, and we return the original root.

```Java
public TreeNode invertTree(TreeNode root) {
    if (root == null) return null;
    Queue<TreeNode> queue = new LinkedList<TreeNode>();
    queue.add(root);
    while (!queue.isEmpty()) {
        TreeNode current = queue.poll();
        TreeNode temp = current.left;
        current.left = current.right;
        current.right = temp;
        if (current.left != null) queue.add(current.left);
        if (current.right != null) queue.add(current.right);
    }
    return root;
}
```

**Complexity Analysis**

Since each node in the tree is visited / added to the queue only once, the time complexity is $O(n)$, where $n$ is the number of nodes in the tree.

Space complexity is $O(n)$, since in the worst case, the queue will contain all nodes in one level of the binary tree. For a full binary tree, the leaf level has $\lceil \frac{n}{2}\rceil=O(n)$ leaves.

# Submissions
---
**Solution 1:**
```
Runtime: 28 ms
Memory Usage: 12.7 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root
```

**Solution 2:**
```
Runtime: 28 ms
Memory Usage: 12.6 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        q = collections.deque([root])
        while(q):
            current = q.popleft()
            current.left, current.right = current.right, current.left
            if current.right:
                q.append(current.right)
            if current.left:
                q.append(current.left)
        return root
```