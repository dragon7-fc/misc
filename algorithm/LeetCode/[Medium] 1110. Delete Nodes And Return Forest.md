1110. Delete Nodes And Return Forest

Given the `root` of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in `to_delete`, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest.  You may return the result in any order.

 

**Example 1:**


```
Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
```

**Constraints:**

1. The number of nodes in the given tree is at most `1000`.
1. Each node has `a` distinct value between `1` and `1000`.
1. `to_delete.length <= 1000`
1. `to_delete` contains distinct values between `1` and `1000`.

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 56 ms
Memory Usage: 12.9 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        del_set = set(to_delete) 
        def dfs(root,res,del_set):
            if not root:
                return None
            root.left = dfs(root.left,res,del_set)
            root.right = dfs(root.right,res,del_set)
            # process root
            if root.val not in del_set:
                return root
            else:
                if root.left: res.append(root.left)
                if root.right: res.append(root.right)
                return None
            
        res = []
        root = dfs(root,res,del_set)
        if root:
            res.append(root)
        return res
```

**Solution 2: (Recursion (Postorder Traversal))**
```
Runtime: 11 ms
Memory: 27.45 MB
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
    TreeNode* processNode(TreeNode* node, unordered_set<int>& toDeleteSet,
                          vector<TreeNode*>& forest) {
        if (!node) {
            return nullptr;
        }

        node->left = processNode(node->left, toDeleteSet, forest);
        node->right = processNode(node->right, toDeleteSet, forest);

        // Node Evaluation: Check if the current node needs to be deleted
        if (toDeleteSet.find(node->val) != toDeleteSet.end()) {
            // If the node has left or right children, add them to the forest
            if (node->left) {
                forest.push_back(node->left);
            }
            if (node->right) {
                forest.push_back(node->right);
            }
            // Delete the current node and return null to its parent
            delete node;
            return nullptr;
        }

        return node;
    }
public:
    vector<TreeNode*> delNodes(TreeNode* root, vector<int>& to_delete) {
        unordered_set<int> toDeleteSet(to_delete.begin(), to_delete.end());
        vector<TreeNode*> forest;

        root = processNode(root, toDeleteSet, forest);

        // If the root is not deleted, add it to the forest
        if (root) {
            forest.push_back(root);
        }

        return forest;
    }
};
```

**Solution 3: (BFS Forest Formation)**
```
Runtime: 12 ms
Memory: 27.41 MB
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
    vector<TreeNode*> delNodes(TreeNode* root, vector<int>& to_delete) {
        if (!root) {
            return {};
        }

        unordered_set<int> toDeleteSet(to_delete.begin(), to_delete.end());
        vector<TreeNode*> forest;

        queue<TreeNode*> nodesQueue;
        nodesQueue.push(root);

        while (!nodesQueue.empty()) {
            TreeNode* currentNode = nodesQueue.front();
            nodesQueue.pop();

            if (currentNode->left) {
                nodesQueue.push(currentNode->left);
                // Disconnect the left child if it needs to be deleted
                if (toDeleteSet.find(currentNode->left->val) !=
                    toDeleteSet.end()) {
                    currentNode->left = nullptr;
                }
            }

            if (currentNode->right) {
                nodesQueue.push(currentNode->right);
                // Disconnect the right child if it needs to be deleted
                if (toDeleteSet.find(currentNode->right->val) !=
                    toDeleteSet.end()) {
                    currentNode->right = nullptr;
                }
            }

            // If the current node needs to be deleted, add its non-null
            // children to the forest
            if (toDeleteSet.find(currentNode->val) != toDeleteSet.end()) {
                if (currentNode->left) {
                    forest.push_back(currentNode->left);
                }
                if (currentNode->right) {
                    forest.push_back(currentNode->right);
                }
            }
        }

        // Ensure the root is added to the forest if it is not to be deleted
        if (toDeleteSet.find(root->val) == toDeleteSet.end()) {
            forest.push_back(root);
        }

        return forest;
    }
};
```
