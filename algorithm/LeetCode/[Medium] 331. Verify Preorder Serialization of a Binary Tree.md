331. Verify Preorder Serialization of a Binary Tree

One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as `#`.

     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #
For example, the above binary tree can be serialized to the string `"9,3,4,#,#,1,#,#,2,#,6,#,#"`, where `#` represents a null node.

Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer or a character `'#'` representing null pointer.

You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3".

**Example 1:**
```
Input: "9,3,4,#,#,1,#,#,2,#,6,#,#"
Output: true
```

**Example 2:**
```
Input: "1,#"
Output: false
```

**Example 3:**
```
Input: "9,#,#,1"
Output: false
```

# Submissions
---
**Solution 1: (Greedy)**
```
Runtime: 52 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        nodes = preorder.split(",")
        nul_nodes = 1
        for node in nodes:
            if node == "#":
                nul_nodes -=1
            else:
                nul_nodes += 1
                if nul_nodes == 1:
                    return False
        return nul_nodes == 0
```

**Solution 2: (Stack)**

Similar to Problem 297: Serialize and Deserialize Binary Tree, but here we do not really need to reconstruct our tree, and using stack is enough. The trick is to add elements one by one and when we see `num, #, #`, we replace it with `#`. If we get just one `#` in the end, return `True`, else: `False`. Let us look at the example `9,3,4,#,#,1,#,#,2,#,6,#,#`. Let us go through steps:

* We add elements until we have `9, 3, 4, #, #`. It means now that `4` is leaf, so let us remove it: we have `9, 3, #`.
* Add elements, so we have `9, 3, #, 1, #, #`, We have leaf `1`, remove it: `9, 3, #, #`. Now, we have `3` as leaf as well: remove it: `9, #`.
* Add elements `9, #, 2, #, 6, #, #` -> `9, #, 2, #, #` -> `9, #, #` -> `#`.

```
Runtime: 77 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = []
        for elem in preorder.split(","):
            stack.append(elem)
            while len(stack) > 2 and stack[-2:] == ["#"]*2 and stack[-3] != "#":
                stack.pop(-3)
                stack.pop(-2)
            
        return stack == ["#"]
```
