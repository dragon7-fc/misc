536. Construct Binary Tree from String

You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.

**Example:**
```
Input: "4(2(3)(1))(6(5))"
Output: return the tree root node representing the following tree:

       4
     /   \
    2     6
   / \   / 
  3   1 5   
```

**Note:**

* There will only be `'('`, `')'`, `'-'` and `'0' ~ '9'` in the input string.
* An empty tree is represented by `""` instead of `"()"`.

# Submissions
---
**Solution 1: (Stack)**
```
Runtime: 116 ms
Memory Usage: 14.4 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> TreeNode:
        N = len(s)
        i = 0
        st, val = [[]],  ''
        while i < N:
            if s[i] == '(':
                if val:
                    st[-1] += [TreeNode(int(val))]
                    val = ''
                st += [[]]
            elif s[i] == ')':
                if val:
                    st[-1] += [TreeNode(int(val))]
                    val = ''
                if st[-2][-1].left == None:
                    st[-2][-1].left = st[-1].pop(0)
                elif st[-2][-1].right == None:
                    st[-2][-1].right = st[-1].pop(0)
                if not st[-1]:
                    st.pop()
            else:
                val += s[i]
            i += 1
        if val:
            st[-1] += [TreeNode(int(val))]
        return st[0][0] if st[0] else None
```

**Solution 2: (DFS)**
```
Runtime: 108 ms
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
    def str2tree(self, s: str) -> TreeNode:
        N = len(s)
        if not s:
            return None
        
        def dfs(i):
            if i == N:
                return None,i
            val = ''
            left_node = None
            right_node = None
            while i < N:
                if s[i] == "-" or s[i].isdigit():
                    val += s[i]
                    i += 1
                elif s[i] == '(':
                    if not left_node:
                        left_node,j = dfs(i+1)
                    else:
                        right_node,j = dfs(i+1)
                    i = j+1
                else:
                    return TreeNode(int(val), left_node, right_node),i
            root = TreeNode(int(val), left_node, right_node)
            return root, i
      
        return dfs(0)[0]
        
```