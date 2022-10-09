653. Two Sum IV - Input is a BST

Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

**Example 1:**
```
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
```

**Example 2:**
```
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
```

# Solution
---
## Approach #1 Using HashSet[Accepted]
The simplest solution will be to traverse over the whole tree and consider every possible pair of nodes to determine if they can form the required sum $k$. But, we can improve the process if we look at a little catch here.

If the sum of two elements $x + y$ equals $k$, and we already know that $x$ exists in the given tree, we only need to check if an element $y$ exists in the given tree, such that $y = k - x$. Based on this simple catch, we can traverse the tree in both the directions(left child and right child) at every step. We keep a track of the elements which have been found so far during the tree traversal, by putting them into a setset.

For every current node with a value of pp, we check if $k-p$ already exists in the array. If so, we can conclude that the sum $k$ can be formed by using the two elements from the given tree. Otherwise, we put this value $p$ into the $set$.

If even after the whole tree's traversal, no such element $p$ can be found, the sum $k$ can't be formed by using any two elements.

```java
public class Solution {
    public boolean findTarget(TreeNode root, int k) {
        Set < Integer > set = new HashSet();
        return find(root, k, set);
    }
    public boolean find(TreeNode root, int k, Set < Integer > set) {
        if (root == null)
            return false;
        if (set.contains(k - root.val))
            return true;
        set.add(root.val);
        return find(root.left, k, set) || find(root.right, k, set);
    }
}
```

**Complexity Analysis**

* Time complexity : $O(n)$. The entire tree is traversed only once in the worst case. Here, $n$ refers to the number of nodes in the given tree.

* Space complexity : $O(n)$. The size of the $set$ can grow upto $n$ in the worst case.

## Approach #2 Using BFS and HashSet [Accepted]
**Algorithm**

In this approach, the idea of using the $set$ is the same as in the last approach. But, we can carry on the traversal in a Breadth First Search manner, which is a very common traversal method used in Trees. The way BFS is used can be summarized as given below. We start by putting the root node into a $queue$. We also maintain a $set$ similar to the last approach. Then, at every step, we do as follows:

1. Remove an element, $p$, from the front of the $queue$.

1. Check if the element $k-p$ already exists in the setset. If so, return `True`.

1. Otherwise, add this element, $p$ to the setset. Further, add the right and the left child nodes of the current node to the back of the $queue$.

1. Continue steps 1. to 3. till the $queue$ becomes empty.

1. Return `false` if the $queue$ becomes empty.

By following this process, we traverse the tree on a level by level basis.

```java
public class Solution {
    public boolean findTarget(TreeNode root, int k) {
        Set < Integer > set = new HashSet();
        Queue < TreeNode > queue = new LinkedList();
        queue.add(root);
        while (!queue.isEmpty()) {
            if (queue.peek() != null) {
                TreeNode node = queue.remove();
                if (set.contains(k - node.val))
                    return true;
                set.add(node.val);
                queue.add(node.right);
                queue.add(node.left);
            } else
                queue.remove();
        }
        return false;
    }
}
```

**Complexity Analysis**

* Time complexity : $O(n)$. We need to traverse over the whole tree once in the worst case. Here, $n$ refers to the number of nodes in the given tree.

* Space complexity : $O(n)$. The size of the $set$ can grow atmost upto $n$.

## Approach #3 Using BST [Accepted]
**Algorithm**

In this approach, we make use of the fact that the given tree is a Binary Search Tree. Now, we know that the inorder traversal of a BST gives the nodes in ascending order. Thus, we do the inorder traversal of the given tree and put the results in a $list$ which contains the nodes sorted in ascending order.

Once this is done, we make use of two pointers $l$ and $r$ pointing to the beginning and the end of the sorted $list$. Then, we do as follows:

1. Check if the sum of the elements pointed by $l$ and $r$ is equal to the required sum $k$. If so, return a `True` immediately.

1. Otherwise, if the sum of the current two elements is lesser than the required sum $k$, update $l$ to point to the next element. This is done, because, we need to increase the sum of the current elements, which can only be done by increasing the smaller number.

1. Otherwise, if the sum of the current two elements is larger than the required sum $k$, update $r$ to point to the previous element. This is done, because, we need to decrease the sum of the current elements, which can only be done by reducing the larger number.

1. Continue steps 1. to 3. till the left pointer $l$ crosses the right pointer $r$.

1. If the two pointers cross each other, return a `False` value.

Note that we need not increase the larger number or reduce the smaller number in any case. This happens because, in case, a number larger than the current $list[r]$ is needed to form the required sum $k$, the right pointer could not have been reduced in the first place. The similar argument holds true for not reducing the smaller number as well.

```java
public class Solution {
    public boolean findTarget(TreeNode root, int k) {
        List < Integer > list = new ArrayList();
        inorder(root, list);
        int l = 0, r = list.size() - 1;
        while (l < r) {
            int sum = list.get(l) + list.get(r);
            if (sum == k)
                return true;
            if (sum < k)
                l++;
            else
                r--;
        }
        return false;
    }
    public void inorder(TreeNode root, List < Integer > list) {
        if (root == null)
            return;
        inorder(root.left, list);
        list.add(root.val);
        inorder(root.right, list);
    }
}
```

**Complexity Analysis**

* Time complexity : $O(n)$. We need to traverse over the whole tree once to do the inorder traversal. Here, $n$ refers to the number of nodes in the given tree.

* Space complexity : $O(n)$. The sorted $list$ will contain $n$ elements.

# Submissions
---
**Solution 1: (BFS)**
```
Runtime: 68 ms
Memory Usage: 14.8 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        s = set()
        
        level = root and [root]
        while level:
            next_level = []
            for node in level:
                if (k - node.val) in s:
                    return True
                else:
                    s.add(node.val)
                next_level += [c for c in [node.left, node.right] if c]
            level = next_level
        return False
```

**Solution 2: (DFS)**
```
Runtime: 76 ms
Memory Usage: 18.2 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        s = set()
        
        def dfs(node):
            if not node:
                return False
            if k-node.val in s:
                return True
            s.add(node.val)
            if dfs(node.left):
                return True
            if dfs(node.right):
                return True
            return False
        
        return dfs(root)
```

**Solution 2: (DFS)**
```
Runtime: 40 ms
Memory: 38.8 MB
```
```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    unordered_set<int> s;
public:
    bool findTarget(TreeNode* root, int k) {
        if (!root) return false;
        if (s.count(k-root->val)) 
            return true;
        s.insert(root->val);
        if (findTarget(root->left, k))
            return true;
        if (findTarget(root->right, k))
            return true;
        return false;
    }
};
```
