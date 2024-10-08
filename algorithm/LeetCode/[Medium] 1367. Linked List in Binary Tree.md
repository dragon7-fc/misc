1367. Linked List in Binary Tree

Given a binary tree `root` and a linked list with `head` as the first node. 

Return `True` if all the elements in the linked list starting from the `head` correspond to some downward path connected in the binary tree otherwise return `False`.

In this context downward path means a path that starts at some node and goes downwards.

 

**Example 1:**

![1367_sample_1_1720.png](img/1367_sample_1_1720.png)
```
Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true
Explanation: Nodes in blue form a subpath in the binary Tree.  
```

**Example 2:**

![1367_sample_2_1720.png](img/1367_sample_2_1720.png)
```
Input: head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true
```

**Example 3:**
```
Input: head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: false
Explanation: There is no path in the binary tree that contains all the elements of the linked list from head.
```

**Constraints:**

* `1 <= node.val <= 100` for each node in the linked list and binary tree.
* The given linked list will contain between `1` and `100` nodes.
* The given binary tree will contain between `1` and `2500` nodes.

# Submissions
---
**Solution 1: (DFS)**

Time `O(N * min(L,H))`  
Space `O(H)`  
where `N` = tree size, `H` = tree height, `L` = list length.
```
Runtime: 132 ms
Memory Usage: 15.2 MB
```
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        def dfs(head, root):
            if not head: return True
            if not root: return False
            return root.val == head.val and (dfs(head.next, root.left) or dfs(head.next, root.right))
        if not head: return True
        if not root: return False
        return dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
```

**Solution 2: (DFS)**
```
Runtime: 24 ms
Memory Usage: 13.9 MB
```
```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

bool dfs(struct ListNode *head, struct TreeNode *root) {
    if (!head)
        return true;
    if (!root)
        return false;
    return head->val == root->val 
            && (dfs(head->next, root->left) || dfs(head->next, root->right));
}

bool isSubPath(struct ListNode* head, struct TreeNode* root){
    if (!head)
        return true;
    if (!root)
        return false;
    if (dfs(head, root) 
        || isSubPath(head, root->left) 
        || isSubPath(head, root->right))
        return true;
    return false;
}
```

**Solution 3: (Iterative Approach)**
```
Runtime: 24 ms
Memory: 31.03 MB
```
```c++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
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
    bool isMatch(TreeNode* node, ListNode* list) {
        while (node && list) {
            if (node->val != list->val) return false;
            list = list->next;
            // Continue to the next node in the tree, left or right
            if (list) {
                node = (node->left && isMatch(node->left, list)) ? node->left
                                                                 : node->right;
            }
        }
        return !list;  // Ensure that all nodes in the linked list were matched
    }
public:
    bool isSubPath(ListNode* head, TreeNode* root) {
        if (!root) return false;

        stack<pair<TreeNode*, ListNode*>> stk;
        stk.push({root, head});

        while (!stk.empty()) {
            auto [node, list] = stk.top();
            stk.pop();

            if (!node) continue;

            if (isMatch(node, list)) return true;

            // Push left and right children with the linked list head
            if (node->left) stk.push({node->left, head});
            if (node->right) stk.push({node->right, head});
        }

        return false;
    }
};
```

**Solution 4: (Knuth-Morris-Pratt (KMP) Algorithm)**
```
Runtime: 16 ms
Memory: 30.78 MB
```
```c++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
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
    bool searchInTree(TreeNode* node, int patternIndex,
                      const vector<int>& pattern,
                      const vector<int>& prefixTable) {
        if (!node) return false;

        while (patternIndex && node->val != pattern[patternIndex])
            patternIndex = prefixTable[patternIndex - 1];
        patternIndex += node->val == pattern[patternIndex];

        // Check if the pattern is fully matched
        if (patternIndex == pattern.size()) return true;

        // Recursively search left and right subtrees
        return searchInTree(node->left, patternIndex, pattern, prefixTable) ||
               searchInTree(node->right, patternIndex, pattern, prefixTable);
    }
public:
    bool isSubPath(ListNode* head, TreeNode* root) {
        // Build the pattern and prefix table from the linked list
        vector<int> pattern = {head->val}, prefixTable = {0};
        int patternIndex = 0;
        head = head->next;

        while (head) {
            while (patternIndex && head->val != pattern[patternIndex])
                patternIndex = prefixTable[patternIndex - 1];
            patternIndex += head->val == pattern[patternIndex];
            pattern.push_back(head->val);
            prefixTable.push_back(patternIndex);
            head = head->next;
        }

        // Perform DFS to search for the pattern in the tree
        return searchInTree(root, 0, pattern, prefixTable);
    }
};
```

**Solution 5: (DFS)**
```
Runtime: 19 ms
Memory: 30.66 MB
```
```c++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
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
    bool dfs(ListNode *node, TreeNode *root) {
        if (!node) {
            return true;
        }
        if (!root) {
            return false;
        }
        if (node->val != root->val) {
            return false;
        }
        if (dfs(node->next, root->left) || dfs(node->next, root->right)) {
            return true;
        }
        return false;
    }
public:
    bool isSubPath(ListNode* head, TreeNode* root) {
        if (!root) {
            return false;
        }
        return dfs(head, root) || isSubPath(head, root->left) || isSubPath(head, root->right);
    }
};
```
