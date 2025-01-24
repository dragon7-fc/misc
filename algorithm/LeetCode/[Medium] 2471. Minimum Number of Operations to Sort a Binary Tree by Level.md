2471. Minimum Number of Operations to Sort a Binary Tree by Level

You are given the `root` of a binary tree with unique values.

In one operation, you can choose any two nodes at the same level and swap their values.

Return the minimum number of operations needed to make the values at each level sorted in a **strictly increasing order**.

The **level** of a node is the number of edges along the path between it and the root node.

 

**Example 1:**

![2471_image-20220918174006-2.png](img/2471_image-20220918174006-2.png)
```
Input: root = [1,4,3,7,6,8,5,null,null,null,null,9,null,10]
Output: 3
Explanation:
- Swap 4 and 3. The 2nd level becomes [3,4].
- Swap 7 and 5. The 3rd level becomes [5,6,8,7].
- Swap 8 and 7. The 3rd level becomes [5,6,7,8].
We used 3 operations so return 3.
It can be proven that 3 is the minimum number of operations needed.
```

**Example 2:**

![2471_image-20220918174026-3.png](img/2471_image-20220918174026-3.png)
```
Input: root = [1,3,2,7,6,5,4]
Output: 3
Explanation:
- Swap 3 and 2. The 2nd level becomes [2,3].
- Swap 7 and 4. The 3rd level becomes [4,6,5,7].
- Swap 6 and 5. The 3rd level becomes [4,5,6,7].
We used 3 operations so return 3.
It can be proven that 3 is the minimum number of operations needed.
```

**Example 3:**

![2471_image-20220918174052-4.png](img/2471_image-20220918174052-4.png)
```
Input: root = [1,2,3,4,5,6]
Output: 0
Explanation: Each level is already sorted in increasing order so return 0.
```

**Constraints:**

* The number of nodes in the tree is in the range `[1, 10^5]`.
* `1 <= Node.val <= 10^5`
* All the values of the tree are **unique**.

# Submissions
---
**Solution 1: (BFS)**
```
Runtime: 1743 ms
Memory: 54.3 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        count = 0
        nodes = [root]
        
        def perm(nodes):
            c = 0
            nn = [n.val for n in nodes]
            ns = {v : j for j,v in enumerate(nn)}
            
            for i,v in enumerate(sorted(nn)):
                j = ns[v]
                w = nn[i]
                if nn[i] != nn[j]:
                    c += 1
                    nn[i], nn[j] = nn[j], nn[i]
                    ns[v], ns[w] = i, j
            return c
            
        
        while True:
            if not nodes: break
            while nodes:
                count += perm(nodes)
                next_nodes = []
                for n in nodes:
                    if n.left  : next_nodes.append(n.left)
                    if n.right : next_nodes.append(n.right)
                nodes = next_nodes
        return count
```

**Solution 2: (BFS, hash table)**
```
Runtime: 125 ms
Memory: 187.94 MB
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
    int minimumOperations(TreeNode* root) {
        int i, j, sz, ans = 0;
        queue<TreeNode*> q;
        vector<int> dp, dp2;
        unordered_map<int,int> m;
        q.push(root);
        while (q.size()) {
            sz = q.size();
            for (i = 0; i < sz; i ++) {
                auto node = q.front();
                q.pop();
                dp.push_back(node->val);
                m[node->val] = i;
                if (node->left) {
                    q.push(node->left);
                }
                if (node->right) {
                    q.push(node->right);
                }
            }
            dp2 = dp;
            sort(dp2.begin(), dp2.end());
            for (i = 0; i < sz; i ++) {
                if (dp[i] != dp2[i]) {
                    j = m[dp2[i]];
                    m[dp[i]] = j;
                    swap(dp[i], dp[j]);
                    ans += 1;
                }
            }
            dp.clear();
            m.clear();
        }
        return ans;
    }
};
```

**Solution 3: (BFS, greedy)**
```
Runtime: 21 ms
Memory: 165.97 MB
```
case 1:
    3 2 1
    ^ 
    1 2 3

case 2:
    3 1 2
    ^
    2 1 3
    1 2 3

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
    int minimumOperations(TreeNode* root) {
        int i, sz, ans = 0;
        queue<TreeNode*> q;
        vector<pair<int,int>> dp;
        q.push(root);
        while (q.size()) {
            sz = q.size();
            for (i = 0; i < sz; i ++) {
                auto node = q.front();
                q.pop();
                dp.push_back({node->val, i});
                if (node->left) {
                    q.push(node->left);
                }
                if (node->right) {
                    q.push(node->right);
                }
            }
            sort(dp.begin(), dp.end());
            for (i = 0; i < sz; i ++) {
                // case 1, 2
                while (dp[i].second != i) {
                    swap(dp[i], dp[dp[i].second]);
                    ans += 1;
                }
            }
            dp.clear();
        }
        return ans;
    }
};```
