144. Binary Tree Preorder Traversal

Given a binary tree, return the preorder traversal of its nodes' values.

**Example:**
```
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
```
**Follow up:** Recursive solution is trivial, could you do it iteratively?

# Submissions
---
**Solution 1: (DFS)**
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
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        if root:
            # DFS with preorder:
            # current, current.left, current.right   
            ans += [root.val]
            ans += self.preorderTraversal(root.left)
            ans += self.preorderTraversal(root.right)
            
        return ans
```

**Solution 2: (Stack)**
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
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return root
        ans = []
        stack = [root]
        while stack:
            el = stack.pop()
            ans += [el.val]
            if el.right:
                stack.append(el.right)
            if el.left:
                stack.append(el.left)
            
        return ans
```

**Solution 3: (Morris Traversal, Time:O(N), Space: O(1))**
```
Runtime: 33 ms
Memory: 13.9 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        curr = root
        
        while curr:
            # If there is no left child, go for the right child.
            # Otherwise, find the last node in the left subtree. 
            if not curr.left:
                answer.append(curr.val)
                curr = curr.right
            else:
                last = curr.left
                while last.right and last.right != curr:
                    last = last.right
                    
                # If the last node is not modified, we let 
                # 'curr' be its right child. Otherwise, it means we 
                # have finished visiting the entire left subtree.
                if not last.right:
                    answer.append(curr.val)
                    last.right = curr
                    curr = curr.left
                else:
                    last.right = None
                    curr = curr.right
        
        return answer
```
