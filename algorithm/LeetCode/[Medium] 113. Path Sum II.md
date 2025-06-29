113. Path Sum II

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

**Note:** A leaf is a node with no children.

**Example:**

Given the below binary tree and `sum = 22`,
```
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
```

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 40 ms
Memory Usage: 17.8 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root == None:
            return []
        
        ans = []
        def dfs(node, path_sum, path):
            nonlocal ans
            if not node:
                return False
            if node.val == path_sum and not node.left and not node.right:
                ans += [path]
                return
            else:
                if node.left:
                    dfs(node.left, path_sum-node.val, path + [node.left.val])
                if node.right:
                    dfs(node.right, path_sum-node.val, path + [node.right.val])
            return
        
        dfs(root, sum, [root.val])
        return ans
```

**Solution 2: (DFS)**
```
Runtime: 8 ms
Memory Usage: 10.2 MB
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

void help(struct TreeNode *root, int sum, int ***res, int *buff, int i, int *rSize, int **cSizes)
{
	if (root == NULL)
		return;

	if (sum - root->val == 0 && !root->left && !root->right)
	{
		*cSizes = realloc(*cSizes, sizeof(int) * (*rSize + 1));
		(*cSizes)[*rSize] = i + 1;
		*res = realloc(*res, sizeof(int *) * (*rSize + 1));
		(*res)[*rSize] = malloc(sizeof(int) * (i + 1));
		memcpy((*res)[*rSize], buff, sizeof(int) * (i + 1));
		(*res)[*rSize][i] = root->val;
		(*rSize)++;
		return;
	}

	buff[i] = root->val;
	help(root->left, sum - root->val, res, buff, i + 1, rSize, cSizes);
	help(root->right, sum - root->val, res, buff, i + 1, rSize, cSizes);
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** pathSum(struct TreeNode* root, int targetSum, int* returnSize, int** returnColumnSizes){
    *returnSize = 0;
	int **res = NULL;
	*returnColumnSizes = NULL;
	int *buff = calloc(1001, sizeof(int));

	help(root, targetSum, &res, buff, 0, returnSize, returnColumnSizes);

	return res;
}
```

**Solution 3: (Backtracking)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 21.02 MB, Beats 48.94%
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
    void bt(TreeNode *node, int targetSum, int a, vector<int> &p, vector<vector<int>> &ans) {
        if (!node->left && !node->right) {
            if (a == targetSum) {
                ans.push_back(p);
            }
            return;
        }
        if (node->left) {
            p.push_back(node->left->val);
            bt(node->left, targetSum, a + node->left->val, p, ans);
            p.pop_back();
        }
        if (node->right) {
            p.push_back(node->right->val);
            bt(node->right, targetSum, a + node->right->val, p, ans);
            p.pop_back();
        }
    }
public:
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        if (!root) {
            return {};
        }
        vector<vector<int>> ans;
        vector<int> p;
        p.push_back(root->val);
        bt(root, targetSum, root->val, p, ans);
        return ans;
    }
};
```

**Solution 4: (Backtracking)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 20.98 MB, Beats 68.67%
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
    void bt(TreeNode *node, int targetSum, int a, vector<int> &p, vector<vector<int>> &ans) {
        if (!node) {
            return;
        }
        a += node->val;
        p.push_back(node->val);
        if (!node->left && !node->right) {
            if (a == targetSum) {
                ans.push_back(p);
            }
        }
        bt(node->left, targetSum, a, p, ans);
        bt(node->right, targetSum, a, p, ans);
        p.pop_back();
    }
public:
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<vector<int>> ans;
        vector<int> p;
        bt(root, targetSum, 0, p, ans);
        return ans;
    }
};
```
