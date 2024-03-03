1120. Maximum Average Subtree

Given the `root` of a binary tree, find the maximum average value of any subtree of that tree.

(A subtree of a tree is any node of that tree plus all its descendants. The average value of a tree is the sum of its values, divided by the number of nodes.)

 

**Example 1:**

![1120_1308_example_1.png](img/1120_1308_example_1.png)
```
Input: [5,6,1]
Output: 6.00000
Explanation: 
For the node with value = 5 we have an average of (5 + 6 + 1) / 3 = 4.
For the node with value = 6 we have an average of 6 / 1 = 6.
For the node with value = 1 we have an average of 1 / 1 = 1.
So the answer is 6 which is the maximum.
```

**Note:**

* The number of nodes in the tree is between `1` and `5000`.
* Each node will have a value between `0` and `100000`.
* Answers will be accepted as correct if they are within `10^-5` of the correct answer.

# Submissions
---
**Solution 1: (Postorder)**
```
Runtime: 64 ms
Memory Usage: 16.9 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        max_avg = 0
        
        def helper(node):
            nonlocal max_avg
            if not node:
                return 0, 0
            leftt, leftc = helper(node.left)
            rightt, rightc = helper(node.right)
            avg = (leftt+rightt+node.val)/(leftc+rightc+1)
            max_avg = max(max_avg, avg)
            return (leftt+rightt+node.val), (leftc+rightc+1)
        
        helper(root)
        
        return max_avg
```

**Solution 2: (Postorder Traversal)**
```
Runtime: 20 ms
Memory Usage: 22 MB
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
    struct State {
        // count of nodes in the subtree
        int nodeCount;

        // sum of values in the subtree
        int valueSum;

        // max average found in the subtree
        double maxAverage;
    };

    State maxAverage(TreeNode* root) {
        if (!root) return {0, 0, 0};

        // postorder traversal, solve for both child nodes first.
        State left = maxAverage(root->left);
        State right = maxAverage(root->right);

        // now find nodeCount, valueSum and maxAverage for current node `root`
        int nodeCount = left.nodeCount + right.nodeCount + 1;
        int sum = left.valueSum + right.valueSum + root->val;
        double maxAverage = max(
                (1.0 * (sum)) / nodeCount, // average for current node
                max(right.maxAverage, left.maxAverage) // max average from child nodes
        );

        return {nodeCount, sum, maxAverage};
    }
public:
    double maximumAverageSubtree(TreeNode* root) {
        return maxAverage(root).maxAverage;
    }
```
