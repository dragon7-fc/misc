230. Kth Smallest Element in a BST

Given a binary search tree, write a function `kthSmallest` to find the **k**th smallest element in it.

**Note:**

You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

**Example 1:**
```
Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
```

**Example 2:**
```
Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
```

**Follow up:**

What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

# Solution
---
## How to traverse the tree
There are two general strategies to traverse a tree:

* Depth First Search (`DFS`)

In this strategy, we adopt the `depth` as the priority, so that one would start from a root and reach all the way down to certain leaf, and then back to root to reach another branch.

The DFS strategy can further be distinguished as `preorder`, `inorder`, and `postorder` depending on the relative order among the root node, left node and right node.

* Breadth First Search (`BFS`)

We scan through the tree level by level, following the order of height, from top to bottom. The nodes on higher level would be visited before the ones with lower levels.

On the following figure the nodes are numerated in the order you visit them, please follow `1-2-3-4-5` to compare different strategies.

![230_bfs_dfs.png](img/230_bfs_dfs.png)

>To solve the problem, one could use the property of BST : inorder traversal of BST is an array sorted in the ascending order.

## Approach 1: Recursion
It's a very straightforward approach with $\mathcal{O}(N)$ time complexity. The idea is to build an inorder traversal of BST which is an array sorted in the ascending order. Now the answer is the `k - 1`th element of this array.

![230_inorder.png](img/230_inorder.png)

```python
class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
    
        return inorder(root)[k - 1]
```

**Complexity Analysis**

* Time complexity : $\mathcal{O}(N)$ to build a traversal.

* Space complexity : $\mathcal{O}(N)$ to keep an inorder traversal.

## Approach 2: Iteration
The above recursion could be converted into iteration, with the help of stack. This way one could speed up the solution because there is no need to build the entire inorder traversal, and one could stop after the kth element.

![230_iteration.png](img/230_iteration.png)

```python
class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right
```

**Complexity Analysis**

* Time complexity : $\mathcal{O}(H + k)$, where $H$ is a tree height. This complexity is defined by the stack, which contains at least $H + k$ elements, since before starting to pop out one has to go down to a leaf. This results in $\mathcal{O}(\log N + k)$ for the balanced tree and $\mathcal{O}(N + k)$ for completely unbalanced tree with all the nodes in the left subtree.
* Space complexity : $\mathcal{O}(H + k)$, the same as for time complexity, $\mathcal{O}(N + k)$ in the worst case, and $\mathcal{O}(\log N + k)$ in the average case.

**Follow up**

>What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

Insert and delete in a BST were discussed last week, the time complexity of these operations is $\mathcal{O}(H)$, where $H$ is a height of binary tree, and $H = \log N$ for the balanced tree.

Hence without any optimisation insert/delete + search of kth element has $\mathcal{O}(2H + k)$ complexity. How to optimise that?

That's a design question, basically we're asked to implement a structure which contains a BST inside and optimises the following operations :

* Insert

* Delete

* Find kth smallest

Seems like a database description, isn't it? Let's use here the same logic as for LRU cache design, and combine an indexing structure (we could keep BST here) with a double linked list.

Such a structure would provide:

* $\mathcal{O}(H)$ time for the insert and delete.

* $\mathcal{O}(k)$ for the search of kth smallest.

![230_linked_list2.png](img/230_linked_list2.png)

The overall time complexity for insert/delete + search of kth smallest is $\mathcal{O}(H + k)$ instead of $\mathcal{O}(2H + k)$.

**Complexity Analysis**

* Time complexity for insert/delete + search of kth smallest: $\mathcal{O}(H + k)$, where $H$ is a tree height. $\mathcal{O}(\log N + k)$ in the average case, $\mathcal{O}(N + k)$ in the worst case.

* Space complexity : $\mathcal{O}(N)$ to keep the linked list.

# Submissions
---
**Solution:**
```
Runtime: 52 ms
Memory Usage: 16.8 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
    
        return inorder(root)[k - 1]
```

**Solution:**
```
Runtime: 48 ms
Memory Usage: 16.7 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right
```