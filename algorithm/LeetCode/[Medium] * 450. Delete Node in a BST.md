450. Delete Node in a BST

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

* Search for a node to remove.
* If the node is found, delete the node.

Note: Time complexity should be O(height of tree).

**Example:**
```
root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7
```

# Submissions
---
**Solution 1: (Recursion)**
```
Runtime: 80 ms
Memory Usage: 18.1 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def successor(self, root):
        """
        One step right and then always left
        """
        root = root.right
        while root.left:
            root = root.left
        return root.val
    
    def predecessor(self, root):
        """
        One step left and then always right
        """
        root = root.left
        while root.right:
            root = root.right
        return root.val
    
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        
        # delete from the right subtree
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        # delete from the left subtree
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        # delete the current node
        else:
            # the node is a leaf
            if not (root.left or root.right):
                root = None
            # the node is not a leaf and has a right child
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            # the node is not a leaf, has no right child, and has a left child    
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
                        
        return root
```

**Solution 2: (DFS, Post Order)**
```
Runtime: 68 ms
Memory Usage: 16.9 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMin(self, node):
        if node is None:
            return
        while node.left:
            node = node.left
        return node
    
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return
        if root.val == key:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            
            temp = self.findMin(root.right)
            root.val = temp.val
            root.right = self.deleteNode(root.right, temp.val)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root
```

**Solution 3: (DFS, Post Order)**
```
Runtime: 32 ms
Memory Usage: 13.8 MB
```
```c
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int findMax(struct TreeNode *root)
{
	if (root->right == NULL)
		return root->val;
	else
		return findMax(root->right);
}

struct TreeNode* deleteNode(struct TreeNode* root, int key){
    struct TreeNode *temp;

	if (root == NULL)
		return NULL;
	else if (key < root->val)
		root->left = deleteNode(root->left, key);
	else if (key > root->val)
		root->right = deleteNode(root->right, key);
	else
	{
		if (root->left == NULL && root->right == NULL)
		{
			free(root);
			root = NULL;
		}
		else if (root->right == NULL)
		{
			temp = root->left;
			free(root);
			root = temp;
		}
		else if (root->left == NULL)
		{
			temp = root->right;
			free(root);
			root = temp;
		}
		else
		{
			root->val = findMax(root->left);
			root->left = deleteNode(root->left, root->val);
		}
	}

	return root;
}
```

**Solution 4: (DFS, Pre order, Early stop, binary search)**

case 1:
             1
           /
          2x
        /
       3

case 2:
             1
              \
               2x
                \
                 3
case 3:

             5
           /   \
      p> 3x <r  6
        /  \     \
   pn> 2 <  4x     7
        \   v  
       n> 4+

```
Runtime: 0 ms, Beats 100.00%
Memory: 34.24 MB, Beats 62.89%
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
public:
    TreeNode* deleteNode(TreeNode* root, int key) {
        if (!root) {
            return nullptr;
        }
        if (root->val == key) {
            if (!root->left || !root->right) {
                return !root->left ? root->right : root->left;
            }
            TreeNode *node = root->left, *par = root;
            while (node) {
                par = node;
                node = node->right;
            }
            par->right = root->right;
            return root->left;
        } else if (root->val < key) {
            root->right = deleteNode(root->right, key);
        } else {
            root->left = deleteNode(root->left, key);
        }
        return root;
    }
};
```
