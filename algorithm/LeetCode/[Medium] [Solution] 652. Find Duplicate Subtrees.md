652. Find Duplicate Subtrees

Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any **one** of them.

Two trees are duplicate if they have the same structure with same node values.

**Example 1:**
```
        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
```
The following are two duplicate subtrees:
```
      2
     /
    4
```
and
```
    4
```
Therefore, you need to return above trees' root in the form of a list.

# Solution
---
## Approach #1: Depth-First Search [Accepted]
**Intuition**

We can serialize each subtree. For example, the tree
```
   1
  / \
 2   3
    / \
   4   5
```
can be represented as the serialization `1,2,#,#,3,4,#,#,5,#,#`, which is a unique representation of the tree.

**Algorithm**

Perform a depth-first search, where the recursive function returns the serialization of the tree. At each node, record the result in a map, and analyze the map after to determine duplicate subtrees.

```python
class Solution(object):
    def findDuplicateSubtrees(self, root):
        count = collections.Counter()
        ans = []
        def collect(node):
            if not node: return "#"
            serial = "{},{},{}".format(node.val, collect(node.left), collect(node.right))
            count[serial] += 1
            if count[serial] == 2:
                ans.append(node)
            return serial

        collect(root)
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N^2)$, where $N$ is the number of nodes in the tree. We visit each node once, but each creation of serial may take $O(N)$ work.

* Space Complexity: $O(N^2)$, the size of count.

## Approach #2: Unique Identifier [Accepted]
**Intuition**

Suppose we have a unique identifier for subtrees: two subtrees are the same if and only if they have the same id.

Then, for a node with left child id of `x` and right child id of `y`, `(node.val, x, y)` uniquely determines the tree.

**Algorithm**

If we have seen the triple `(node.val, x, y)` before, we can use the identifier we've remembered. Otherwise, we'll create a new one.

```python
class Solution(object):
    def findDuplicateSubtrees(self, root):
        trees = collections.defaultdict()
        trees.default_factory = trees.__len__
        count = collections.Counter()
        ans = []
        def lookup(node):
            if node:
                uid = trees[node.val, lookup(node.left), lookup(node.right)]
                count[uid] += 1
                if count[uid] == 2:
                    ans.append(node)
                return uid

        lookup(root)
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the number of nodes in the tree. We visit each node once.

* Space Complexity: $O(N)$. Every structure we use is using $O(1)$ storage per node.

# Submissions
---
**Solution: (Unique Identifier)**
```
Runtime: 56 ms
Memory Usage: 16.5 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        rees = collections.defaultdict()
        trees.default_factory = trees.__len__
        count = collections.Counter()
        ans = []
        def lookup(node):
            if node:
                uid = trees[node.val, lookup(node.left), lookup(node.right)]
                count[uid] += 1
                if count[uid] == 2:
                    ans.append(node)
                return uid

        lookup(root)
        return ans
```

**Solution 1: (DFS, Hash Table, post-order)**
```
Runtime: 73 ms
Memory Usage: 30.6 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        result = []
        paths = defaultdict(int)

        def get_path(node):
            if not node:
                return "None"
            else:
                path = str(node.val)
            path += '.' + get_path(node.left)
            path += '.' + get_path(node.right)
            paths[path] += 1
            if paths[path] == 2:
                result.append(node)
            return path

        get_path(root)
        return result
```

**Solution 2: (DFS, Hash Table, post-order)**
```
Runtime: 28 ms
Memory: 49.6 MB
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
    string dfs(TreeNode* node, unordered_map<string, int>& cnt, vector<TreeNode*>& ans) {
        if (!node) {
            return ",";
        }
        string rst;
        rst += dfs(node->left, cnt, ans);
        rst += dfs(node->right, cnt, ans);
        rst += to_string(node->val) + ",";
        cnt[rst] += 1;
        if (cnt[rst] == 2) {
            ans.push_back(node);
        }
        return rst;
    }
public:
    vector<TreeNode*> findDuplicateSubtrees(TreeNode* root) {
        unordered_map<string, int> cnt;
        vector<TreeNode*> ans;
        dfs(root, cnt, ans);
        return ans;
    }
};
```
