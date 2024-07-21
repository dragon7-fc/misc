2196. Create Binary Tree From Descriptions

You are given a 2D integer array `descriptions` where `descriptions[i] = [parenti, childi, isLefti]` indicates that `parenti` is the parent of `childi` in a binary tree of unique values. Furthermore,

* If `isLefti == 1`, then `childi` is the left child of `parenti`.
* If `isLefti == 0`, then `childi` is the right child of `parenti`.

Construct the binary tree described by `descriptions` and return its root.

The test cases will be generated such that the binary tree is **valid**.

 

**Example 1:**

!{2196_example1drawio.png](img/2196_example1drawio.png)
```
Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
Output: [50,20,80,15,17,19]
Explanation: The root node is the node with value 50 since it has no parent.
The resulting binary tree is shown in the diagram.
```

**Example 2:**

![2196_example2drawio.png](img/2196_example2drawio.png)
```
Input: descriptions = [[1,2,1],[2,3,0],[3,4,1]]
Output: [1,2,null,null,3,4]
Explanation: The root node is the node with value 1 since it has no parent.
The resulting binary tree is shown in the diagram.
```

**Constraints:**

* `1 <= descriptions.length <= 104`
* `descriptions[i].length == 3`
* `1 <= parenti, childi <= 10^5`
* `0 <= isLefti <= 1`
* The binary tree described by descriptions is valid.

# Submissions
---
**Solution 1: (Hash Table)**
```
Runtime: 3606 ms
Memory Usage: 31.9 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        children = set()
        m = {}
        for p,c,l in descriptions:
            np = m.setdefault(p, TreeNode(p))
            nc = m.setdefault(c, TreeNode(c))
            if l:
                np.left = nc
            else:
                np.right = nc
            children.add(c)
        root = (m.keys() - children).pop()
        return m[root]
```

**Solution 2: (Convert to Graph with Breadth First Search)**
```
Runtime: 833 ms
Memory: 318.28 MB
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
    TreeNode* createBinaryTree(vector<vector<int>>& descriptions) {
        // Sets to track unique children and parents
        unordered_set<int> children, parents;
        // Map to store parent to children relationships
        unordered_map<int, vector<pair<int, int>>> parentToChildren;

        // Build graph from parent to child, and add nodes to HashSets
        for (auto& d : descriptions) {
            int parent = d[0], child = d[1], isLeft = d[2];
            parents.insert(parent);
            parents.insert(child);
            children.insert(child);
            parentToChildren[parent].emplace_back(child, isLeft);
        }

        // Find the root node by checking which node is in parents but not in
        // children
        for (auto it = parents.begin(); it != parents.end();) {
            if (children.find(*it) != children.end()) {
                it = parents.erase(it);
            } else {
                ++it;
            }
        }
        TreeNode* root = new TreeNode(*parents.begin());

        // Starting from root, use BFS to construct binary tree
        queue<TreeNode*> queue;
        queue.push(root);

        while (!queue.empty()) {
            TreeNode* parent = queue.front();
            queue.pop();
            // Iterate over children of current parent
            for (auto& childInfo : parentToChildren[parent->val]) {
                int childValue = childInfo.first, isLeft = childInfo.second;
                TreeNode* child = new TreeNode(childValue);
                queue.push(child);
                // Attach child node to its parent based on isLeft flag
                if (isLeft == 1) {
                    parent->left = child;
                } else {
                    parent->right = child;
                }
            }
        }

        return root;
    }
};
```

**Solution 3: (Convert to Graph with Depth First Search)**
```
Runtime: 846 ms
Memory: 309.36 MB
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
    TreeNode* dfs(unordered_map<int, vector<pair<int, bool>>>& parentToChildren,
                  int val) {
        // Create new TreeNode for current value
        TreeNode* node = new TreeNode(val);

        // If current node has children, recursively build them
        if (parentToChildren.find(val) != parentToChildren.end()) {
            for (auto& child_info : parentToChildren[val]) {
                int child = child_info.first;
                bool isLeft = child_info.second;

                // Attach child node based on isLeft flag
                if (isLeft) {
                    node->left = dfs(parentToChildren, child);
                } else {
                    node->right = dfs(parentToChildren, child);
                }
            }
        }

        return node;
    }
public:
    TreeNode* createBinaryTree(vector<vector<int>>& descriptions) {
        // Step 1: Organize data
        unordered_map<int, vector<pair<int, bool>>> parentToChildren;
        unordered_set<int> allNodes;
        unordered_set<int> children;

        for (auto& desc : descriptions) {
            int parent = desc[0];
            int child = desc[1];
            bool isLeft = desc[2];

            parentToChildren[parent].push_back({child, isLeft});
            allNodes.insert(parent);
            allNodes.insert(child);
            children.insert(child);
        }

        // Step 2: Find the root
        int rootVal = 0;
        for (int node : allNodes) {
            if (!children.contains(node)) {
                rootVal = node;
                break;
            }
        }

        // Step 3 & 4: Build the tree using DFS
        return dfs(parentToChildren, rootVal);
    }
};
```

**Solution 4: (Constructing Tree From Directly Map and TreeNode Object)**
```
Runtime: 713 ms
Memory: 276.28 MB
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
    TreeNode* createBinaryTree(vector<vector<int>>& descriptions) {
        // Maps values to TreeNode pointers
        unordered_map<int, TreeNode*> nodeMap;
        // Stores values which are children in the descriptions
        unordered_set<int> children;

        // Iterate through descriptions to create nodes and set up tree
        // structure
        for (const auto& description : descriptions) {
            // Extract parent value, child value, and whether it is a
            // left child (1) or right child (0)
            int parentValue = description[0];
            int childValue = description[1];
            bool isLeft = description[2];

            // Create parent and child nodes if not already created
            if (nodeMap.count(parentValue) == 0) {
                nodeMap[parentValue] = new TreeNode(parentValue);
            }
            if (nodeMap.count(childValue) == 0) {
                nodeMap[childValue] = new TreeNode(childValue);
            }

            // Attach child node to parent's left or right branch
            if (isLeft) {
                nodeMap[parentValue]->left = nodeMap[childValue];
            } else {
                nodeMap[parentValue]->right = nodeMap[childValue];
            }

            // Mark child as a child in the set
            children.insert(childValue);
        }

        // Find and return the root node
        for (auto& entry : nodeMap) {
            auto& value = entry.first;
            auto& node = entry.second;
            // Root node found
            if (children.find(value) == children.end()) {
                return node;
            }
        }

        // Should not occur according to problem statement
        return nullptr;
    }
};
```

**Solution 5: (Hash Table)**
```
Runtime: 641 ms
Memory: 256.38 MB
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
    TreeNode* createBinaryTree(vector<vector<int>>& descriptions) {
        unordered_map<int, pair<TreeNode*,bool>> m;
        int p, c, isLeft;
        for (int i = 0; i < descriptions.size(); i ++) {
            p = descriptions[i][0];
            c = descriptions[i][1];
            isLeft = descriptions[i][2];
            if (!m.count(p)) {
                m[p] = {new TreeNode(p), false};
            }
            if (!m.count(c)) {
                m[c] = {new TreeNode(c), false};
            }
            m[c].second = true;
            if (isLeft) {
                m[p].first->left = m[c].first;
            } else {
                m[p].first->right = m[c].first;
            }
        }
        TreeNode *ans;
        for (auto [_, pa]: m) {
            if (!pa.second) {
                ans = pa.first;
                break;
            }
        }
        return ans;
    }
};
```
