1008. Construct Binary Search Tree from Preorder Traversal

Return the root node of a binary search tree that matches the given `preorder` traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a `value < node.val`, and any descendant of node.right has a `value > node.val`.  Also recall that a preorder traversal displays the `value` of the node first, then traverses `node.left`, then traverses `node.right`.)

 

**Example 1:**
```
Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]
```
![1008_1266.png](img/1008_1266.png)
 

**Note:** 

* `1 <= preorder.length <= 100`
* The values of preorder are distinct.

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
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if preorder:
            val = preorder[0]
            root = TreeNode(val)
            i = 1
            while i < len(preorder) and preorder[i] < val:
                i += 1
            root.left = self.bstFromPreorder(preorder[1:i])
            root.right = self.bstFromPreorder(preorder[i:])
            return root
```

**Solution 2: (Iterative)**
```
Runtime: 32 ms
Memory Usage: 13.6 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        """
        This method uses iteration to construct a binary search tree from the
        input list.  The only preorder characteristic of the list that it uses
        is that the first element of the list is the value of the root node.

        :param preorder:
        :type preorder:
        :return:
        :rtype:
        """
        if preorder == []:
            return None
        head = TreeNode(preorder[0])
        for value in preorder[1:]:
            new_node = TreeNode(value)
            new_node_not_added = True
            node = head
            while new_node_not_added:
                if value < node.val:
                    if node.left:
                        node = node.left
                    else:
                        node.left = new_node
                        new_node_not_added = False
                elif value > node.val:
                    if node.right:
                        node = node.right
                    else:
                        node.right = new_node
                        new_node_not_added = False
        return head
```