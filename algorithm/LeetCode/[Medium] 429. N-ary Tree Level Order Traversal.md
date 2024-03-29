429. N-ary Tree Level Order Traversal

Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

**Example 1:**

![429_narytreeexample.png](img/429_narytreeexample.png)
```
Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]
```

**Example 2:**

![429_sample_4_964.png](img/429_sample_4_964.png)
```
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
```

**Constraints:**

* The height of the n-ary tree is less than or equal to `1000`
* The total number of nodes is between `[0, 10^4]`

# Submissions
---
**Solution 1: (BFS)**
```
Runtime: 48 ms
Memory Usage: 14.6 MB
```
```
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans = []
        level = root and [root]
        while level:
            ans.append([node.val for node in level])
            level = [c for node in level for c in node.children if c]
        return ans
```

**Solution 2: (BFS)**
```
Runtime: 24 ms
Memory Usage: 11.7 MB
```
```c++
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    vector<vector<int>> levelOrder(Node* root) {
        if (!root) return {};
        queue<Node*> q;
        vector<vector<int>> ans;
        Node *cur;
        vector<int> level;
        q.push(root);
        while (!q.empty()) {
            int sz = q.size();
            level.erase(level.begin(), level.end());
            for (int i = 0; i < sz; i ++) {
                cur = q.front();
                q.pop();
                level.push_back(cur->val);
                for (auto &c: cur->children){
                    if (c)
                        q.push(c);
                }
            }
            ans.push_back(level);
        }
        return ans;
    }
};
```
