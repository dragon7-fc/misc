2096. Step-By-Step Directions From a Binary Tree Node to Another

You are given the `root` of a **binary tree** with `n` nodes. Each node is uniquely assigned a value from `1` to `n`. You are also given an integer `startValue` representing the value of the start node `s`, and a different integer `destValue` representing the value of the destination node `t`.

Find the shortest path starting from node `s` and ending at node `t`. Generate step-by-step directions of such path as a string consisting of only the uppercase letters `'L'`, `'R'`, and `'U'`. Each letter indicates a specific direction:

* `'L'` means to go from a node to its **left child** node.
* `'R'` means to go from a node to its **right child** node.
* `'U'` means to go from a node to its **parent** node.

Return the step-by-step directions of the **shortest path** from node `s` to node `t`.

 

**Example 1:**

![2096_eg1.png](img/2096_eg1.png)
```
Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
Output: "UURL"
Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.
```

**Example 2:**

![2096_eg2.png](img/2096_eg2.png)
```
Input: root = [2,1], startValue = 2, destValue = 1
Output: "L"
Explanation: The shortest path is: 2 → 1.
```

**Constraints:**

* The number of nodes in the tree is `n`.
* `2 <= n <= 10^5`
* `1 <= Node.val <= n`
* All the values in the tree are **unique**.
* `1 <= startValue, destValue <= n`
* `startValue != destValue`

# Submissions
---
**Solution 1: (DFS + BFS)**
```
Runtime: 5665 ms
Memory: 173.7 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        g = collections.defaultdict(list)

        def dfs(node, p):
            if p:
                g[node.val] += [['U', p.val]]
            if node.left:
                g[node.val] += [["L", node.left.val]]
                dfs(node.left, node)
            if node.right:
                g[node.val] += [["R", node.right.val]]
                dfs(node.right, node)

        dfs(root, None)
        q = collections.deque([[startValue, ""]])
        seen = set([startValue])
        while q:
            v, path = q.popleft()
            if v == destValue:
                return path
            for d, nv in g[v]:
                if not nv in seen:
                    seen.add(nv)
                    q += [[nv, path+d]]
```

**Solution 2: (3 Steps)**

1. Build directions for both start and destination from the root.
	* Say we get "LLRRL" and "LRR".
1. Remove common prefix path.
	* We remove "L", and now start direction is "LRRL", and destination - "RR"
1. Replace all steps in the start direction to "U" and add destination direction.
	* The result is "UUUU" + "RR".
```
Runtime: 168 ms
Memory: 113.5 MB
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
    bool find(TreeNode* n, int val, string &path) {
        if (n->val == val)
            return true;
        if (n->left && find(n->left, val, path))
            path.push_back('L');
        else if (n->right && find(n->right, val, path))
            path.push_back('R');
        return !path.empty();
    }
public:
    string getDirections(TreeNode* root, int startValue, int destValue) {
        string s_p, d_p;
        find(root, startValue, s_p);
        find(root, destValue, d_p);
        while (!s_p.empty() && !d_p.empty() && s_p.back() == d_p.back()) {
            s_p.pop_back();
            d_p.pop_back();
        }
        return string(s_p.size(), 'U') + string(rbegin(d_p), rend(d_p));
    }
};
```

**Solution 3: (DFS + BFS)**
```
Runtime: 1256 ms
Memory: 612.06 MB
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
    void dfs(TreeNode* node, TreeNode *p, TreeNode **s, int startValue, unordered_map<TreeNode*, vector<pair<TreeNode*,char>>> &g) {
        if (!node) {
            return;
        }
        if (node->val == startValue) {
            *s = node;
        }
        if(p) {
            g[node].push_back({p, 'U'});
        }
        if (node->left) {
            g[node].push_back({node->left, 'L'});
            dfs(node->left, node, s, startValue, g);
        }
        if (node->right) {
            g[node].push_back({node->right, 'R'});
            dfs(node->right, node, s, startValue, g);
        }
    }
public:
    string getDirections(TreeNode* root, int startValue, int destValue) {
        unordered_map<TreeNode*, vector<pair<TreeNode*,char>>> g;
        unordered_map<TreeNode*, pair<TreeNode*, char>> visited;
        TreeNode *s, node;
        dfs(root, nullptr, &s, startValue, g);
        queue<TreeNode*> q;
        q.push(s);
        visited[s] = {nullptr, ' '};
        string ans;
        while (q.size()) {
            auto node = q.front();
            q.pop();
            if (node->val == destValue) {
                while (node != s) {
                    ans += visited[node].second;
                    node = visited[node].first;
                }
                reverse(ans.begin(), ans.end());
                return ans;
            }
            for (auto [nnode, d]: g[node]) {
                if (!visited.count(nnode)) {
                    visited[nnode] = {node, d};
                    q.push({nnode});
                }
            }
        }
        return "";
    }
};
```

**Solution 4: (DFS + BFS)**
```
Runtime: 517 ms
Memory: 283.79 MB
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
    string backtrackPath(
        TreeNode* node,
        unordered_map<TreeNode*, pair<TreeNode*, string>> pathTracker) {
        string path;
        // Construct the path
        while (pathTracker.count(node)) {
            // Add the directions in reverse order and
            // move on to the previous node
            path += pathTracker[node].second;
            node = pathTracker[node].first;
        }
        reverse(path.begin(), path.end());
        return path;
    }

    void populateParentMap(TreeNode* node,
                           unordered_map<int, TreeNode*>& parentMap) {
        if (node == nullptr) return;

        // Add children to the map and recurse further
        if (node->left != nullptr) {
            parentMap[node->left->val] = node;
            populateParentMap(node->left, parentMap);
        }

        if (node->right != nullptr) {
            parentMap[node->right->val] = node;
            populateParentMap(node->right, parentMap);
        }
    }

    TreeNode* findStartNode(TreeNode* node, int startValue) {
        if (node == nullptr) return nullptr;

        if (node->val == startValue) return node;

        TreeNode* leftResult = findStartNode(node->left, startValue);

        // If left subtree returns a node, it must be StartNode. Return it
        // Otherwise, return whatever is returned by right subtree.
        if (leftResult != nullptr) return leftResult;
        return findStartNode(node->right, startValue);
    }
public:
    string getDirections(TreeNode* root, int startValue, int destValue) {
        unordered_map<int, TreeNode*> parentMap;

        // Find the start node and populate parent map
        TreeNode* startNode = findStartNode(root, startValue);
        populateParentMap(root, parentMap);

        // Perform BFS to find the path
        queue<TreeNode*> q;
        q.push(startNode);
        unordered_set<TreeNode*> visitedNodes;
        // Key: next node, Value: <current node, direction>
        unordered_map<TreeNode*, pair<TreeNode*, string>> pathTracker;
        visitedNodes.insert(startNode);

        while (!q.empty()) {
            TreeNode* currentNode = q.front();
            q.pop();

            // If destination is reached, return the path
            if (currentNode->val == destValue) {
                return backtrackPath(currentNode, pathTracker);
            }

            // Check and add parent node
            if (parentMap.find(currentNode->val) != parentMap.end()) {
                TreeNode* parentNode = parentMap[currentNode->val];
                if (visitedNodes.find(parentNode) == visitedNodes.end()) {
                    q.push(parentNode);
                    pathTracker[parentNode] = {currentNode, "U"};
                    visitedNodes.insert(parentNode);
                }
            }

            // Check and add left child
            if (currentNode->left != nullptr &&
                visitedNodes.find(currentNode->left) == visitedNodes.end()) {
                q.push(currentNode->left);
                pathTracker[currentNode->left] = {currentNode, "L"};
                visitedNodes.insert(currentNode->left);
            }

            // Check and add right child
            if (currentNode->right != nullptr &&
                visitedNodes.find(currentNode->right) == visitedNodes.end()) {
                q.push(currentNode->right);
                pathTracker[currentNode->right] = {currentNode, "R"};
                visitedNodes.insert(currentNode->right);
            }
        }

        // This line should never be reached if the tree is valid
        return "";
    }
};
```

**Solution 5: (LCA + DFS)**
```
Runtime: 158 ms
Memory: 118.66 MB
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
    TreeNode* findLowestCommonAncestor(TreeNode* node, int value1, int value2) {
        if (node == nullptr) return nullptr;

        if (node->val == value1 || node->val == value2) return node;

        TreeNode* leftLCA =
            findLowestCommonAncestor(node->left, value1, value2);
        TreeNode* rightLCA =
            findLowestCommonAncestor(node->right, value1, value2);

        if (leftLCA == nullptr)
            return rightLCA;
        else if (rightLCA == nullptr)
            return leftLCA;
        else
            return node;  // Both values found, this is the LCA
    }

    bool findPath(TreeNode* node, int targetValue, string& path) {
        if (node == nullptr) return false;

        if (node->val == targetValue) return true;

        // Try left subtree
        path.push_back('L');
        if (findPath(node->left, targetValue, path)) {
            return true;
        }
        path.pop_back();  // Remove last character

        // Try right subtree
        path.push_back('R');
        if (findPath(node->right, targetValue, path)) {
            return true;
        }
        path.pop_back();  // Remove last character

        return false;
    }
public:
    string getDirections(TreeNode* root, int startValue, int destValue) {
        // Find the Lowest Common Ancestor (LCA) of start and destination nodes
        TreeNode* lowestCommonAncestor =
            findLowestCommonAncestor(root, startValue, destValue);

        string pathToStart;
        string pathToDest;

        // Find paths from LCA to start and destination nodes
        findPath(lowestCommonAncestor, startValue, pathToStart);
        findPath(lowestCommonAncestor, destValue, pathToDest);

        string directions;

        // Add "U" for each step to go up from start to LCA
        directions.append(pathToStart.length(), 'U');

        // Append the path from LCA to destination
        directions.append(pathToDest);

        return directions;
    }
};
```

**Solution 6: (LCA + DFS (Optimized))**
```
Runtime: 164 ms
Memory: 119.62 MB
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
    bool findPath(TreeNode* node, int target, string& path) {
        if (node == nullptr) {
            return false;
        }

        if (node->val == target) {
            return true;
        }

        // Try left subtree
        path += "L";
        if (findPath(node->left, target, path)) {
            return true;
        }
        path.pop_back();  // Remove last character

        // Try right subtree
        path += "R";
        if (findPath(node->right, target, path)) {
            return true;
        }
        path.pop_back();  // Remove last character

        return false;
    }
public:
    string getDirections(TreeNode* root, int startValue, int destValue) {
        string startPath, destPath;

        // Find paths from root to start and destination nodes
        findPath(root, startValue, startPath);
        findPath(root, destValue, destPath);

        string directions;
        int commonPathLength = 0;

        // Find the length of the common path
        while (commonPathLength < startPath.length() &&
               commonPathLength < destPath.length() &&
               startPath[commonPathLength] == destPath[commonPathLength]) {
            commonPathLength++;
        }

        // Add "U" for each step to go up from start to common ancestor
        for (int i = 0; i < startPath.length() - commonPathLength; i++) {
            directions += "U";
        }

        // Add directions from common ancestor to destination
        for (int i = commonPathLength; i < destPath.length(); i++) {
            directions += destPath[i];
        }

        return directions;
    }
};
```
