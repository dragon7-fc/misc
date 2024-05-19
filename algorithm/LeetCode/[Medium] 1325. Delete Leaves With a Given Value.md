1325. Delete Leaves With a Given Value

Given a binary tree `root` and an integer `target`, delete all the leaf nodes with value `target`.

Note that once you delete a leaf node with value target, if it's parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you can't).

 

**Example 1:**

![1325_sample_1_1684.png](img/1325_sample_1_1684.png)
```
Input: root = [1,2,3,2,null,2,4], target = 2
Output: [1,null,3,null,4]
Explanation: Leaf nodes in green with value (target = 2) are removed (Picture in left). 
After removing, new nodes become leaf nodes with value (target = 2) (Picture in center).
```

**Example 2:**

![1325_sample_2_1684.png](img/1325_sample_2_1684.png)
```
Input: root = [1,3,3,3,2], target = 3
Output: [1,3,null,null,2]
```

**Example 3:**

![1325_sample_3_1684.png](img/1325_sample_3_1684.png)
```
Input: root = [1,2,null,2,null,2], target = 2
Output: [1]
Explanation: Leaf nodes in green with value (target = 2) are removed at each step.
```

**Example 4:**
```
Input: root = [1,1,1], target = 1
Output: []
```

**Example 5:**
```
Input: root = [1,2,3], target = 1
Output: [1,2,3]
```

**Constraints:**

* `1 <= target <= 1000`
* Each tree has at most `3000` nodes.
* Each node's value is between `[1, 1000]`.

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 48 ms
Memory Usage: 13.2 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        def dfs(node):
            if not node:
                return
            node.left, node.right = dfs(node.left), dfs(node.right)
            if node.val == target and node.left == node.right:
                return None
            return node
        return dfs(root)
```

**Solution 2: (Iterative (PostOrder Traversal))**
```
Runtime: 14 ms
Memory: 21.29 MB
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
    TreeNode* removeLeafNodes(TreeNode* root, int target) {
        stack<TreeNode*> stack;
        TreeNode* currentNode = root, *lastRightNode = nullptr;

        while (!stack.empty() || currentNode != nullptr) {
            // Push left nodes to the stack until reaching the leftmost node.
            while (currentNode != nullptr) {
                stack.push(currentNode);
                currentNode = currentNode->left;
            }

            // Access the top node on the stack without removing it.
            // This node is the current candidate for processing.
            currentNode = stack.top();

            // Check if the current node has an unexplored right subtree.
            // If so, shift to the right subtree unless it's the subtree we just visited.
            if (currentNode->right != lastRightNode && currentNode->right) {
                currentNode = currentNode->right;
                continue; // Continue in the while loop to push this new subtree's leftmost nodes.
            }

            // Remove the node from the stack, since we're about to process it.
            stack.pop();

            // If the node has no right subtree or the right subtree has already been visited,
            // then check if it is a leaf node with the target value.
            if (currentNode->right == nullptr && currentNode->left == nullptr && currentNode->val == target) {
                // If the stack is empty after popping, it means the root was a target leaf node.
                if (stack.empty()) {
                    return nullptr; // The tree becomes empty as the root itself is removed.
                }
                
                // Identify the parent of the current node.
                TreeNode* parent = stack.top();

                // Disconnect the current node from its parent.
                if (parent->left == currentNode) {
                    parent->left = nullptr; // If current node is a left child, set the left pointer to null.
                } else {
                    parent->right = nullptr; // If current node  is a right child, set the right pointer to null.
                }
            }

            // Mark this node as visited by setting 'lastRightNode' to 'currentNode' before moving to the next iteration.
            lastRightNode = currentNode;
            // Reset 'currentNode' to null to ensure the next node from the stack is processed.
            currentNode = nullptr;
        }
        return root; // Return the modified tree.
    }
};
```

**Solution 3: (DFS)**
```
Runtime: 10 ms
Memory: 21.22 MB
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
    TreeNode* removeLeafNodes(TreeNode* root, int target) {
        if (!root) {
            return nullptr;
        }
        root->left = removeLeafNodes(root->left, target);
        root->right = removeLeafNodes(root->right, target);
        if (!root->left && !root->right && root->val == target) {
            return nullptr;
        }
        return root;
    }
};
```
