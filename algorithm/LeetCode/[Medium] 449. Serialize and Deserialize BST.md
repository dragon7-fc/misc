449. Serialize and Deserialize BST

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a **binary search tree** can be serialized to a string and this string can be deserialized to the original tree structure.

**The encoded string should be as compact as possible.**

**Note:** Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

# Submissions
---
**Solution 1:**
```
Runtime: 56 ms
Memory Usage: 17.4 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        res = []
        def dfs(node):
            nonlocal res
            if not node:
                res += ['null']
                return 
            res += [str(node.val)]
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        res = ','.join(res)
        return res

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        q = collections.deque(data.split(','))
        def dfs(data_list):
            if data_list[0] == 'null':
                data_list.popleft()
                return None
            node = TreeNode(int(data_list[0]))
            data_list.popleft()
            node.left = dfs(data_list)
            node.right = dfs(data_list)
            return node
            
        root = dfs(q)    
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
```