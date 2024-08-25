145. Binary Tree Postorder Traversal

Given a binary tree, return the postorder traversal of its nodes' values.

**Example:**
```
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
```

**Follow up:** Recursive solution is trivial, could you do it iteratively?

# Submissions
---
**Solution 1: (Stack)**
```
Runtime: 24 ms
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
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        postorder, stack = [], [(root, False)]
        while stack:
            (node, visited) = stack.pop()
            if node:
                if visited:
                    postorder.append(node.val)
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return postorder
```

**Solution 2: (DFS)**
```
Runtime: 5 ms
Memory: 11.78 MB
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
    vector<int> postorderTraversal(TreeNode* root) {
        if (!root) {
            return {};
        }
        vector<int> left = postorderTraversal(root->left), right = postorderTraversal(root->right), rst;
        rst.insert(rst.end(), left.begin(), left.end());
        rst.insert(rst.end(), right.begin(), right.end());
        rst.push_back(root->val);
        return rst;
    }
};
```

**Solution 3: (Single Stack Postorder Traversal (Iterative))**
```
Runtime: 4 ms
Memory: 9.98 MB
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
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> result;

        // If the root is null, return an empty list
        if (root == nullptr) {
            return result;
        }

        // To keep track of the previously processed node
        TreeNode* previousNode = nullptr;
        // Stack to manage the traversal
        stack<TreeNode*> traversalStack;

        // Process nodes until both the root is null and the stack is empty
        while (root != nullptr || !traversalStack.empty()) {
            // Traverse to the leftmost node
            if (root != nullptr) {
                traversalStack.push(root);
                root = root->left;
            } else {
                // Peek at the top node of the stack
                root = traversalStack.top();

                // If there is no right child or the right child was already
                // processed
                if (root->right == nullptr || root->right == previousNode) {
                    result.push_back(root->val);
                    traversalStack.pop();
                    previousNode = root;
                    root = nullptr;  // Ensure we don’t traverse again from this
                                     // node
                } else {
                    // Move to the right child
                    root = root->right;
                }
            }
        }

        return result;
    }
};
```

**Solution 4: (Morris Traversal (No stack))**
```
Runtime: 0 ms
Memory: 10.06 MB
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
    void reverseSubtreeLinks(TreeNode* startNode, TreeNode* endNode) {
        if (startNode == endNode) {
            return;  // If the start and end nodes are the same, no need to
                     // reverse
        }

        TreeNode* prev = NULL;
        TreeNode* current = startNode;
        TreeNode* next = NULL;

        // Reverse the direction of the pointers in the subtree
        while (current != endNode) {
            next = current->right;
            current->right = prev;
            prev = current;
            current = next;
        }

        // Reverse the last node
        current->right = prev;
    }
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> result;

        // If the root is null, return an empty list
        if (root == NULL) {
            return result;
        }

        // Create a dummy node to simplify edge cases
        TreeNode dummy = -1;
        TreeNode* dummyNode = &dummy;
        TreeNode* predecessor = NULL;
        dummyNode->left = root;
        root = dummyNode;

        // Traverse the tree
        while (root != NULL) {
            // If the current node has a left child
            if (root->left != NULL) {
                predecessor = root->left;

                // Find the rightmost node in the left subtree or the thread
                // back to the current node
                while (predecessor->right != NULL &&
                       predecessor->right != root) {
                    predecessor = predecessor->right;
                }

                // Create a thread if it doesn't exist
                if (predecessor->right == NULL) {
                    predecessor->right = root;
                    root = root->left;
                } else {
                    // Process the nodes in the left subtree
                    TreeNode* node = predecessor;
                    reverseSubtreeLinks(root->left, predecessor);

                    // Add nodes from right to left
                    while (node != root->left) {
                        result.push_back(node->val);
                        node = node->right;
                    }

                    result.push_back(node->val);  // Add root.left's value
                    reverseSubtreeLinks(predecessor, root->left);
                    predecessor->right = NULL;
                    root = root->right;
                }
            } else {
                // Move to the right child if there's no left child
                root = root->right;
            }
        }

        return result;
    }
};
```
