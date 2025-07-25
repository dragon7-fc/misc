337. House Robber III

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

**Example 1:**
```
Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
```

**Example 2:**
```
Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \ 
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
```

# Submissions
---
**Solution 1: (Recursion)**
```
Runtime: 44 ms
Memory Usage: 16 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def helper(node):
            # return [rob this node, not rob this node]
            if not node:
                return (0, 0)
            left = helper(node.left)
            right = helper(node.right)
            # if we rob this node, we cannot rob its children
            rob = node.val + left[1] + right[1]
            # else we could choose to either rob its children or not
            not_rob = max(left) + max(right)
            return [rob, not_rob]

        return max(helper(root))
```

**Solution 2: (Recursion with Memoization)**
```
Runtime: 60 ms
Memory Usage: 17 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        rob_saved = {}
        not_rob_saved = {}

        def helper(node, parent_robbed):
            if not node:
                return 0

            if parent_robbed:
                if node in rob_saved:
                    return rob_saved[node]
                result = helper(node.left, False) + helper(node.right, False)
                rob_saved[node] = result
                return result
            else:
                if node in not_rob_saved:
                    return not_rob_saved[node]
                rob = node.val + helper(node.left, True) + helper(node.right, True)
                not_rob = helper(node.left, False) + helper(node.right, False)
                result = max(rob, not_rob)
                not_rob_saved[node] = result
                return result

        return helper(root, False)
```

**Solution 3: (Dynamic Programming)**
```
Runtime: 64 ms
Memory Usage: 18.1 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
            
        # reform tree into array-based tree
        tree = []
        graph = {-1: []}
        index = -1
        q = [(root, -1)]
        while q:
            node, parent_index = q.pop(0)
            if node:
                index += 1
                tree.append(node.val)
                graph[index] = []
                graph[parent_index].append(index)
                q.append((node.left, index))
                q.append((node.right, index))

        # represent the maximum start by node i with robbing i
        dp_rob = [0] * (index+1)

        # represent the maximum start by node i without robbing i
        dp_not_rob = [0] * (index+1)

        for i in reversed(range(index+1)):
            if not graph[i]:  # if is leaf
                dp_rob[i] = tree[i]
                dp_not_rob[i] = 0
            else:
                dp_rob[i] = tree[i] + sum(dp_not_rob[child]
                                          for child in graph[i])
                dp_not_rob[i] = sum(max(dp_rob[child], dp_not_rob[child])
                                    for child in graph[i])

        return max(dp_rob[0], dp_not_rob[0])
```

**Solution 4: (Recursion)**
```
Runtime: 8 ms
Memory Usage: 8.4 MB
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

typedef struct {
    int robMoney;
    int notRobMoney;
} Money;

Money robMoney(struct TreeNode* root) {
    if (root == NULL) {
        Money money = {0};
        return money;
    }

    Money moneyFromLeft = robMoney(root->left);
    Money moneyFromRight = robMoney(root->right);
    Money money;
    money.robMoney = root->val + moneyFromLeft.notRobMoney + moneyFromRight.notRobMoney;
    money.notRobMoney = (moneyFromLeft.robMoney > moneyFromLeft.notRobMoney ?
    moneyFromLeft.robMoney : moneyFromLeft.notRobMoney)
    +
    (moneyFromRight.robMoney > moneyFromRight.notRobMoney ?
    moneyFromRight.robMoney : moneyFromRight.notRobMoney);
    
    return money;
}

int rob(struct TreeNode* root){
    Money money = robMoney(root);
    return money.robMoney > money.notRobMoney ? money.robMoney : money.notRobMoney;
}
```

**Solution 5: (DP Bottom Up)**

                    3 (8,9)
                /        \
              4  (4,4)    5 (5,1)
           /    \        /
         1       3     1
        (1,0)   (3,0)  (1,0)

```
Runtime: 0 ms, Beats 100.00%
Memory: 22.58 MB, Beats 64.05%
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
    pair<int,int> dfs(TreeNode *node) {
        if (!node) {
            return {0, 0};
        }
        if (!node->left && !node->right) {
            return {node->val, 0};
        }
        auto [al, bl] = dfs(node->left);
        auto [ar, br] = dfs(node->right);
        return {node->val + bl + br, max(al, bl) + max(ar, br)};
    }
public:
    int rob(TreeNode* root) {
        auto [a, b] = dfs(root);
        return max(a, b);
    }
};
```
