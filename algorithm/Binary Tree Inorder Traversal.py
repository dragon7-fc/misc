""" 
Binary Tree Inorder Traversal

Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


""" Solution1: 64 ms """
class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        if not root:
            return []
        ans += self.inorderTraversal(root.left)
        ans.append(root.val)
        ans += self.inorderTraversal(root.right)
        return ans


""" Solution2: 44 ms """
class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        s = []
        cur = root
        while cur or len(s) > 0:
            while cur:
                s.append(cur)
                cur = cur.left
            cur = s.pop()
            ans.append(cur.val)
            cur = cur.right
        return ans


""" Solution3: 36 ms """
class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        else:
            return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right)
            