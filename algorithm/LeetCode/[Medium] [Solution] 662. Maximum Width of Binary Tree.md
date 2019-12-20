662. Maximum Width of Binary Tree

Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a **full binary tree**, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the `null` nodes between the end-nodes are also counted into the length calculation.

**Example 1:**
```
Input: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
```

**Example 2:**
```
Input: 

          1
         /  
        3    
       / \       
      5   3     

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).
```

**Example 3:**
```
Input: 

          1
         / \
        3   2 
       /        
      5      

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).
```

**Example 4:**
```
Input: 

          1
         / \
        3   2
       /     \  
      5       9 
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).
```

**Note:** Answer will in the range of 32-bit signed integer.

# Solution
---
## Approach Framework
**Explanation**

As we need to reach every node in the given tree, we will have to traverse the tree, either with a depth-first search, or with a breadth-first search.

The main idea in this question is to give each node a position value. If we go down the left neighbor, then `position -> position * 2`; and if we go down the right neighbor, then `position -> position * 2 + 1`. This makes it so that when we look at the `position` values `L` and `R` of two nodes with the same depth, the width will be `R - L + 1`.

## Approach #1: Breadth-First Search [Accepted]
**Intuition and Algorithm**

Traverse each node in breadth-first order, keeping track of that node's position. For each depth, the first node reached is the left-most, while the last node reached is the right-most.

```java
def widthOfBinaryTree(self, root):
    queue = [(root, 0, 0)]
    cur_depth = left = ans = 0
    for node, depth, pos in queue:
        if node:
            queue.append((node.left, depth+1, pos*2))
            queue.append((node.right, depth+1, pos*2 + 1))
            if cur_depth != depth:
                cur_depth = depth
                left = pos
            ans = max(pos - left + 1, ans)

    return ans
```

**Complexity Analysis**

* Time Complexity: $O(N)$ where $N$ is the number of nodes in the input tree. We traverse every node.

* Space Complexity: $O(N)$, the size of our queue.

## Approach #2: Depth-First Search [Accepted]
**Intuition and Algorithm**

Traverse each node in depth-first order, keeping track of that node's position. For each depth, the position of the first node reached of that depth will be kept in `left[depth]`.

Then, for each node, a candidate width is `pos - left[depth] + 1`. We take the maximum of the candidate answers.

```python
class Solution(object):
    def widthOfBinaryTree(self, root):
        self.ans = 0
        left = {}
        def dfs(node, depth = 0, pos = 0):
            if node:
                left.setdefault(depth, pos)
                self.ans = max(self.ans, pos - left[depth] + 1)
                dfs(node.left, depth + 1, pos * 2)
                dfs(node.right, depth + 1, pos * 2 + 1)

        dfs(root)
        return self.ans
```

**Complexity Analysis**

* Time Complexity: $O(N)$ where $N$ is the number of nodes in the input tree. We traverse every node.

* Space Complexity: $O(N)$, the size of the implicit call stack in our DFS.

# Submissions
---
**Solution:**
```
Runtime: 20 ms
Memory Usage: 14.9 MB
```
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0
        left = {}
        def dfs(node, depth = 0, pos = 0):
            if node:
                left.setdefault(depth, pos)
                self.ans = max(self.ans, pos - left[depth] + 1)
                dfs(node.left, depth + 1, pos * 2)
                dfs(node.right, depth + 1, pos * 2 + 1)

        dfs(root)
        return self.ans
```