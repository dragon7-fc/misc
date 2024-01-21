508. Most Frequent Subtree Sum

Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

**Examples 1**
```
Input:

  5
 /  \
2   -3
return [2, -3, 4], since all the values happen only once, return all of them in any order.
Examples 2
Input:

  5
 /  \
2   -5
return [2], since 2 happens twice, however -5 only occur once.
```

**Note:** You may assume the sum of values in any subtree is in the range of 32-bit signed integer.

# Submissions
---
**Solution 1: (Hash Table):**
```
Runtime: 48 ms
Memory Usage: 16.1 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        subtree_sum = []
        def dfs(node):
            nonlocal subtree_sum
            if not node:
                return 0
            res = node.val
            res += dfs(node.left)
            res += dfs(node.right)
            subtree_sum += [res]
            return res
        dfs(root)
        counter = collections.Counter(subtree_sum)
        most_freq = counter.most_common(1)[0][1] if counter else -1
        ans = []
        for k in counter:
            if counter[k] == most_freq:
                ans += [k]
        return ans
```

**Solution 2: (Hash Table):**
```
Runtime: 24 ms
Memory Usage: 24.5 MB
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
    unordered_map<int,int> mp;
    int helper(TreeNode *root){
        if(!root){
            return 0;
        }
        int l=helper(root->left);
        int r=helper(root->right);
        mp[l+r+root->val]++;
        return l+r+root->val;
    }
public:
    vector<int> findFrequentTreeSum(TreeNode* root) {
        helper(root);
        int mx=INT_MIN;
        for(auto &it: mp) mx=max(mx,it.second);
        vector<int> ans;
        for(auto &it: mp){
            if(it.second==mx)
                ans.push_back(it.first);
        }
        return ans;
    }
};
```
