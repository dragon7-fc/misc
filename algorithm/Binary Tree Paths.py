""" 
Binary Tree Paths

Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


""" Solution1: 52 ms """
class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        all_path = []
        path = ""
        if root:
            self.find_path(root, all_path, path)
        return all_path
    
    def find_path(self, node, all_path, path):
        path += str(node.val)
        if not node.left and not node.right:
            all_path.append(path)
            return
        if node.left:
            path_l = path+"->"
            self.find_path(node.left, all_path, path_l)
        if node.right:
            path_r = path+"->"
            self.find_path(node.right, all_path, path_r)


""" Solution2: 44 ms """
class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        self.path_all = []
        self.DFS(root, "")
        return self.path_all
    
    def DFS(self, root, path):
        if root.left:         
            self.DFS(root.left, path + str(root.val) + "->"  )
        if root.right:
            self.DFS(root.right, path + str(root.val) + "->")
        if not root.left and not root.right:
            path += str(root.val)
            self.path_all.append(path)