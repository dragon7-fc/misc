""" 
Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


""" Solution1: 52 ms (recursive)"""
class Solution:
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isMirror(left_node, right_node):
            if not left_node and not right_node:
                return True
            if not left_node:
                return False
            if not right_node:
                return False

            return left_node.val == right_node.val and isMirror(left_node.left, right_node.right) and isMirror(left_node.right, right_node.left)
        
        if not root:
            return True
        
        return isMirror(root.left, root.right)


""" Solution2: 44 ms (iterative, BFS) """
class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        q = collections.deque([root, root])
        while len(q):
            t1 = q.popleft()
            t2 = q.popleft()
            if not t1 and not t2:
                continue
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False
            q.append(t1.left)
            q.append(t2.right)
            q.append(t1.right)
            q.append(t2.left)
        return True