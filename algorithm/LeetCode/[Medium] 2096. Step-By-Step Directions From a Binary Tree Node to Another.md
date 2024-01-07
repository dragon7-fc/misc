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
