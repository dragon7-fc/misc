272. Closest Binary Search Tree Value II

Given the `root` of a binary search tree, a `target` value, and an integer `k`, return the `k` values in the BST that are closest to the `target`. You may return the answer in any order.

You are guaranteed to have only one unique set of k values in the BST that are closest to the `target`.

 

**Example 1:**

![272_closest1-1-tree.jpg](img/272_closest1-1-tree.jpg)
```
Input: root = [4,2,5,1,3], target = 3.714286, k = 2
Output: [4,3]
```

**Example 2:**
```
Input: root = [1], target = 0.000000, k = 1
Output: [1]
```

**Constraints:**

* The number of nodes in the tree is `n`.
* `1 <= k <= n <= 10^4`.
* `0 <= Node.val <= 10^9`
* `-10^9 <= target <= 10^9`
 

**Follow up:** Assume that the BST is balanced. Could you solve it in less than `O(n)` runtime (where n = total nodes)?

# Submissions
---
**Solution 1: (Binary Search)**

    root = [ 4, 2, 5, 1, 3], target = 3.714286, k = 2

dp           1  2  3  4  5
             l  m     r
                   lm r
                   lrx

```
Runtime: 8 ms
Memory: 21.8 MB
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
    void dfs(TreeNode *node, vector<int> &dp) {
        if (!node) {
            return;
        }
        dfs(node->left, dp);
        dp.push_back(node->val);
        dfs(node->right, dp);
    }
public:
    vector<int> closestKValues(TreeNode* root, double target, int k) {
        vector<int> dp;
        dfs(root, dp);
        int left = 0, right = dp.size()-k, mid;
        while (left < right) {
            mid = left + (right-left)/2;
            if (abs(target - dp[mid+k]) < abs(target - dp[mid])) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return vector<int>(dp.begin()+left, dp.begin()+left+k);
    }
};
```

**Solution 2: (Binary Search)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 22.35 MB, Beats 48.98%
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
    void dfs(TreeNode *node, vector<int> &dp) {
        if (!node) {
            return;
        }
        dfs(node->left, dp);
        dp.push_back(node->val);
        dfs(node->right, dp);
    }
public:
    vector<int> closestKValues(TreeNode* root, double target, int k) {
        vector<int> dp;
        dfs(root, dp);
        int left = 0, right = dp.size() - k, mid, st;
        while (left <= right) {
            mid = left + (right-left)/2;
            if (mid + k < dp.size() && abs(target - dp[mid + k]) < abs(target - dp[mid])) {
                left = mid + 1;
            } else {
                st = mid;
                right = mid - 1;
            }
        }
        return vector<int>(dp.begin() + st, dp.begin() + st + k);
    }
};
```
