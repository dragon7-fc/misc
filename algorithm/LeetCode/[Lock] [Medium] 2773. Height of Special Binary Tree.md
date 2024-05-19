2773. Height of Special Binary Tree

You are given a `root`, which is the root of a special binary tree with n nodes. The nodes of the special binary tree are numbered from `1` to `n`. Suppose the tree has `k` leaves in the following order: `b_1 < b_2 < ... < b_k`.

The leaves of this tree have a special property! That is, for every leaf `b_i`, the following conditions hold:

* The right child of `b_i` is `b_i + 1` if `i < k`, and `b_1` otherwise.
* The left child of `b_i` is `b_i - 1` if `i > 1`, and `b_k` otherwise.

Return the height of the given tree.

**Note:** The height of a binary tree is the length of the longest path from the root to any other node.

 

**Example 1:**

![2773_1.png](img/2773_1.png)
```
Input: root = [1,2,3,null,null,4,5]
Output: 2
Explanation: The given tree is shown in the following picture. Each leaf's left child is the leaf to its left (shown with the blue edges). Each leaf's right child is the leaf to its right (shown with the red edges). We can see that the graph has a height of 2.
```

**Example 2:**

![2773_2.png](img/2773_2.png)
```
Input: root = [1,2]
Output: 1
Explanation: The given tree is shown in the following picture. There is only one leaf, so it doesn't have any left or right child. We can see that the graph has a height of 1.
```

**Example 3:**

![2773_3.png](img/2773_3.png)
```
Input: root = [1,2,3,null,null,4,null,5,6]
Output: 3
Explanation: The given tree is shown in the following picture. Each leaf's left child is the leaf to its left (shown with the blue edges). Each leaf's right child is the leaf to its right (shown with the red edges). We can see that the graph has a height of 3.
```

 

**Constraints:**

* `n` == number of nodes in the tree
* `2 <= n <= 10^4`
* `1 <= node.val <= n`
* The input is generated such that each `node.val` is unique.

# Submissions
---
**Solution 1: (BFS)**
```
Runtime: 64 ms
Memory: 68.96 MB
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
    int heightOfTree(TreeNode* root) {
        queue<TreeNode *> q;
        TreeNode *cur, *ncur;
        bool visited[10001] = {0};
        q.push(root);
        visited[root->val] = true;
        int ans = 0, sz;
        while (q.size()) {
            sz = q.size();
            for (int i = 0; i < sz; i++) {
                cur = q.front();
                q.pop();
                if (cur->left) {
                    ncur = cur->left;
                    if (ncur->right != cur && !visited[ncur->val]) {
                        q.push(ncur);
                        visited[ncur->val] = true;
                    }
                }
                if (cur->right) {
                    ncur = cur->right;
                    if (ncur->left != cur && !visited[ncur->val]) {
                        q.push(ncur);
                        visited[ncur->val] = true;
                    }
                }
            }
            if (!q.size()) {
                break;
            }
            ans += 1;
        }
        return ans;
    }
};
```

**Solution 2: (DFS)**
```
Runtime: 69 ms
Memory: 65.38 MB
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
    int heightOfTree(TreeNode* root) {
        return root == nullptr || (root->left != nullptr && root->left->right == root) ? 0 :
        1 + max(heightOfTree(root->left), heightOfTree(root->right));
    }
};
```
