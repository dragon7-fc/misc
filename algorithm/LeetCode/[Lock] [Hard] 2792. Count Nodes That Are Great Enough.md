2792. Count Nodes That Are Great Enough

You are given a `root` to a binary tree and an integer `k`. A node of this tree is called **great enough** if the followings hold:

* Its subtree has at least `k` nodes.
* Its value is **greater** than the value of **at least** `k` nodes in its subtree.

Return the number of nodes in this tree that are great enough.

The node `u` is in the **subtree** of the node `v`, if `u == v` or `v` is an ancestor of `u`.

 

**Example 1:**

![2792_1.png](img/2792_1.png)
```
Input: root = [7,6,5,4,3,2,1], k = 2
Output: 3
Explanation: Number the nodes from 1 to 7.
The values in the subtree of node 1: {1,2,3,4,5,6,7}. Since node.val == 7, there are 6 nodes having a smaller value than its value. So it's great enough.
The values in the subtree of node 2: {3,4,6}. Since node.val == 6, there are 2 nodes having a smaller value than its value. So it's great enough.
The values in the subtree of node 3: {1,2,5}. Since node.val == 5, there are 2 nodes having a smaller value than its value. So it's great enough.
It can be shown that other nodes are not great enough.
See the picture below for a better understanding.
```

**Example 2:**

![2792_2.png](img/2792_2.png)
```
Input: root = [1,2,3], k = 1
Output: 0
Explanation: Number the nodes from 1 to 3.
The values in the subtree of node 1: {1,2,3}. Since node.val == 1, there are no nodes having a smaller value than its value. So it's not great enough.
The values in the subtree of node 2: {2}. Since node.val == 2, there are no nodes having a smaller value than its value. So it's not great enough.
The values in the subtree of node 3: {3}. Since node.val == 3, there are no nodes having a smaller value than its value. So it's not great enough.
See the picture below for a better understanding.
```

**Example 3:**

![2792_3.png](img/2792_3.png)
```
Input: root = [3,2,2], k = 2
Output: 1
Explanation: Number the nodes from 1 to 3.
The values in the subtree of node 1: {2,2,3}. Since node.val == 3, there are 2 nodes having a smaller value than its value. So it's great enough.
The values in the subtree of node 2: {2}. Since node.val == 2, there are no nodes having a smaller value than its value. So it's not great enough.
The values in the subtree of node 3: {2}. Since node.val == 2, there are no nodes having a smaller value than its value. So it's not great enough.
See the picture below for a better understanding.
```

 

**Constraints:**

* The number of nodes in the tree is in the range `[1, 10^4]`.
* `1 <= Node.val <= 10^4`
* `1 <= k <= 10`

# Submissions
---
**Solution 1: (Heap, post order)**
```
Runtime: 602 ms
Memory: 271.9 MB
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
    int node_count;
    priority_queue<int> dfs(TreeNode* root, int k) {
        priority_queue<int> pq, right;
        if (!root) return pq;
        pq = dfs(root->left, k);
        right = dfs(root->right, k);

        while (!right.empty()) {
            pq.push(right.top()); right.pop();
            if (pq.size() > k) pq.pop();
        }

        if (pq.size() == k && root->val > pq.top()) ++node_count;
        pq.push(root->val);
        if (pq.size() > k) pq.pop();
        return pq;
    }
public:
    int countGreatEnoughNodes(TreeNode* root, int k) {
        node_count = 0;
        dfs(root, k);

        return node_count;
    }
};
```
