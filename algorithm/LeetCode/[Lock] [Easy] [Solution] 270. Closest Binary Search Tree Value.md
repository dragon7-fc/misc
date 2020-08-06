270. Closest Binary Search Tree Value

Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

**Note:**

* Given target value is a floating point.
* You are guaranteed to have only one unique value in the BST that is closest to the target.

**Example:**
```
Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4
```

# Solution
---
## Approach 1: Recursive Inorder + Linear search, O(N) time
**Intuition**

The simplest approach (3 lines in Python) is to build inorder traversal and then find the closest element in a sorted array with built-in function `min`.

![270_dummy.png](img/270_dummy.png)

This approach is simple stupid, and serves to identify the subproblems.

**Algorithm**

Build an inorder traversal array.

Find the closest to target element in that array.

**Implementation**

```python
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        def inorder(r: TreeNode):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
        
        return min(inorder(root), key = lambda x: abs(target - x))
```

**Complexity Analysis**

* Time complexity : $\mathcal{O}(N)$ because to build inorder traversal and then to perform linear search takes linear time.
* Space complexity : $\mathcal{O}(N)$ to keep inorder traversal.

## Approach 2: Iterative Inorder, O(k) time
**Intuition**

Let's optimise Approach 1 in the case when index k of the closest element is much smaller than the tree heigh H.

First, one could merge both steps by traversing the tree and searching the closest value at the same time.

Second, one could stop just after identifying the closest value, there is no need to traverse the whole tree. The closest value is found if the target value is in-between of two inorder array elements `nums[i] <= target < nums[i + 1]`. Then the closest value is one of these elements.

![270_iteration.png](img/270_iteration.png)

**Algorithm**

* Initiate stack as an empty array and predecessor value as a very small number.

* While root is not null:

    * To build an inorder traversal iteratively, go left as far as you can and add all nodes on the way into stack.

    * Pop the last element from stack `root = stack.pop()`.

    * If target is in-between of `pred` and `root.val`, return the closest between these two elements.

    * Set predecessor value to be equal to root.val and go one step right: `root = root.right`.

* We're here because during the loop one couldn't identify the closest value. That means that the closest value is the last value in the inorder traversal, i.e. current predecessor value. Return it.

**Implementation**

```python
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        stack, pred = [], float('-inf')
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            
            if pred <= target and target < root.val:
                return min(pred, root.val, key = lambda x: abs(target - x))
                
            pred = root.val
            root = root.right

        return pred
```

**Complexity Analysis**

* Time complexity : $\mathcal{O}(k)$ in the average case and \mathcal{O}(H + k)O(H+k) in the worst case, where k is an index of closest element. It's known that average case is a balanced tree, in that case stack always contains a few elements, and hence one does 2k2k operations to go to kth element in inorder traversal (k times to push into stack and then k times to pop out of stack). That results in $\mathcal{O}(k)$ time complexity. The worst case is a completely unbalanced tree, then you first push H elements into stack and then pop out k elements, that results in $\mathcal{O}(H + k)$ time complexity.

![270_unbalanced.png](img/270_unbalanced.png)

* Space complexity : up to $\mathcal{O}(H)$ to keep the stack in the case of non-balanced tree.

## Approach 3: Binary Search, O(H) time
**Intuition**

Approach 2 works fine when index k of closest element is much smaller than the tree height H.

Let's now consider another limit and optimise Approach 1 in the case of relatively large k, comparable with N.

Then it makes sense to use a binary search: go left if target is smaller than current root value, and go right otherwise. Choose the closest to target value at each step.

![270_binary.png](img/270_binary.png)

Kudos for this solution go to @stefanpochmann.

**Implementation**

```python
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = root.val
        while root:
            closest = min(root.val, closest, key = lambda x: abs(target - x))
            root = root.left if target < root.val else root.right
        return closest
```

**Complexity Analysis**

* Time complexity : $\mathcal{O}(H)$ since here one goes from root down to a leaf.

* Space complexity : $\mathcal{O}(1)$.

# Submissions
---
**Solution 1: (Recursive Inorder + Linear search, O(N) time)**
```
Runtime: 72 ms
Memory Usage: 15.9 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        def inorder(r: TreeNode):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
        
        return min(inorder(root), key = lambda x: abs(target - x))
```

**Solution 2: (Iterative Inorder, O(k) time)**
```
Runtime: 68 ms
Memory Usage: 15.7 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        stack, pred = [], float('-inf')
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            
            if pred <= target and target < root.val:
                return min(pred, root.val, key = lambda x: abs(target - x))
                
            pred = root.val
            root = root.right

        return pred
```

**Solution 3: (Binary Search, O(H) time)**
```
Runtime: 44 ms
Memory Usage: 15.9 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = root.val
        while root:
            closest = min(root.val, closest, key = lambda x: abs(target - x))
            root = root.left if target < root.val else root.right
        return closest
```