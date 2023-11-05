501. Find Mode in Binary Search Tree

Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

* The left subtree of a node contains only nodes with keys **less than or equal to** the node's key.
* The right subtree of a node contains only nodes with keys **greater than or equal to** the node's key.
* Both the left and right subtrees must also be binary search trees.
 

For example:
Given BST `[1,null,2,2]`,
```
   1
    \
     2
    /
   2
```

return [2].

**Note:** If a tree has more than one mode, you can return them in any order.

**Follow up:** Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).

# Submissions
---
**Solution 1:**
```
Runtime: 52 ms
Memory Usage: 16.8 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        def dfs(node, count):
            if not node:
                return []
            
            count[node.val] += 1
            dfs(node.left, count)
            dfs(node.right, count)
            return
        
        counter = collections.defaultdict(int)
        dfs(root, counter)
        most_freq = max(counter.values()) if counter else -1
        ans = []
        for k in counter.keys():
            if counter[k] == most_freq:
                ans += [k]
        return ans
```

**Solution 2: (DFS)**
```
Runtime: 15 ms
Memory: 25.6 MB
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
    void dfs(TreeNode* node, unordered_map<int, int>& counter) {
        if (node == nullptr) {
            return;
        }

        counter[node->val]++;
        dfs(node->left, counter);
        dfs(node->right, counter);
    }
public:
    vector<int> findMode(TreeNode* root) {
        unordered_map<int, int> counter;
        dfs(root, counter);
        int maxFreq = 0;

        for (auto& [key, val] : counter) {
            maxFreq = max(maxFreq, val);
        }
        
        vector<int> ans;
        for (auto& [key, val] : counter) {
            if (val == maxFreq) {
                ans.push_back(key);
            } 
        }
        
        return ans;
    }
};
```

**Solution 3: (Iterative DFS)**
```
Runtime: 22 ms
Memory: 25.6 MB
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
    vector<int> findMode(TreeNode* root) {
        unordered_map<int, int> counter;
        vector<TreeNode*> stack;
        stack.push_back(root);
        
        while (!stack.empty()) {
            TreeNode* node = stack.back();
            stack.pop_back();

            counter[node->val]++;
            if (node->left != nullptr) {
                stack.push_back(node->left);
            }
            if (node->right != nullptr) {
                stack.push_back(node->right);
            }
        }
        
        int maxFreq = 0;

        for (auto& [key, val] : counter) {
            maxFreq = max(maxFreq, val);
        }
        
        vector<int> ans;
        for (auto& [key, val] : counter) {
            if (val == maxFreq) {
                ans.push_back(key);
            } 
        }
        
        return ans;
    }
};
```

**Solution 4: (DFS, No Hash-Map)**
```
Runtime: 8 ms
Memory: 24.5 MB
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
    void dfs(TreeNode* node, vector<int>& values) {
        if (node == nullptr) {
            return;
        }
        
        // Inorder traversal visits nodes in sorted order
        dfs(node->left, values);
        values.push_back(node->val);
        dfs(node->right, values);
    }
public:
    vector<int> findMode(TreeNode* root) {
        vector<int> values;
        dfs(root, values);
        
        int maxStreak = 0;
        int currStreak = 0;
        int currNum = 0;
        vector<int> ans;
        
        for (int num : values) {
            if (num == currNum) {
                currStreak++;
            } else {
                currStreak = 1;
                currNum = num;
            }
            
            if (currStreak > maxStreak) {
                ans = {};
                maxStreak = currStreak;
            }
            
            if (currStreak == maxStreak) {
                ans.push_back(num);
            }
        }
        
        return ans;
    }
};
```

**Solution 5: (BFS)**
```
Runtime: 19 ms
Memory: 25.9 MB
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
    vector<int> findMode(TreeNode* root) {
        unordered_map<int, int> counter;
        queue<TreeNode*> queue;
        queue.push(root);
        
        while (!queue.empty()) {
            TreeNode* node = queue.front();
            queue.pop();

            counter[node->val]++;
            if (node->left != nullptr) {
                queue.push(node->left);
            }
            if (node->right != nullptr) {
                queue.push(node->right);
            }
        }
        
        int maxFreq = 0;
        for (auto& [key, val] : counter) {
            maxFreq = max(maxFreq, val);
        }
        
        vector<int> ans;
        for (auto& [key, val] : counter) {
            if (val == maxFreq) {
                ans.push_back(key);
            } 
        }
        
        return ans;
    }
};
```

**Solution 6: (True Constant Space: Morris Traversal)**
```
Runtime: 12 ms
Memory: 12.7 MB
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
    vector<int> findMode(TreeNode* root) {
        vector<int> ans;
        int maxStreak = 0;
        int currStreak = 0;
        int currNum = 0;
        
        TreeNode* curr = root;
        while (curr != nullptr) {
            if (curr->left != nullptr) {
                // Find the friend
                TreeNode* friendNode = curr->left;
                while (friendNode->right != nullptr) {
                    friendNode = friendNode->right;
                }
                
                friendNode->right = curr;
                
                // Delete the edge after using it
                TreeNode* left = curr->left;
                curr->left = nullptr;
                curr = left;
            } else {
                // Handle the current node
                int num = curr->val;
                if (num == currNum) {
                    currStreak++;
                } else {
                    currStreak = 1;
                    currNum = num;
                }

                if (currStreak > maxStreak) {
                    ans = {};
                    maxStreak = currStreak;
                }

                if (currStreak == maxStreak) {
                    ans.push_back(num);
                }
                
                curr = curr->right;
            }
        }
        
        return ans;
    }
};

```
