889. Construct Binary Tree from Preorder and Postorder Traversal

Return any binary tree that matches the given preorder and postorder traversals.

Values in the traversals `pre` and `post` are distinct positive integers.

 

**Example 1:**
```
Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]
```

**Note:**

* `1 <= pre.length == post.length <= 30`
* `pre[]` and `post[]` are both permutations of `1, 2, ..., pre.length`.
* It is guaranteed an answer exists. If there exists multiple answers, you can return any of them.

# Solution
---
## Approach 1: Recursion
**Intuition**

A preorder traversal is:

(root node) (preorder of left branch) (preorder of right branch)`
While a postorder traversal is:

`(postorder of left branch) (postorder of right branch) (root node)`
For example, if the final binary tree is `[1, 2, 3, 4, 5, 6, 7]` (serialized), then the preorder traversal is `[1] + [2, 4, 5] + [3, 6, 7]`, while the postorder traversal is `[4, 5, 2] + [6, 7, 3] + [1]`.

If we knew how many nodes the left branch had, we could partition these arrays as such, and use recursion to generate each branch of the tree.

**Algorithm**

Let's say the left branch has $L$ nodes. We know the head node of that left branch is `pre[1]`, but it also occurs last in the postorder representation of the left branch. So `pre[1] = post[L-1]` (because of uniqueness of the node values.) Hence, `L = post.indexOf(pre[1]) + 1`.

Now in our recursion step, the left branch is represnted by `pre[1 : L+1]` and `post[0 : L]`, while the right branch is represented by `pre[L+1 : N] and post[L : N-1]`.

```python
class Solution(object):
    def constructFromPrePost(self, pre, post):
        if not pre: return None
        root = TreeNode(pre[0])
        if len(pre) == 1: return root

        L = post.index(pre[1]) + 1
        root.left = self.constructFromPrePost(pre[1:L+1], post[:L])
        root.right = self.constructFromPrePost(pre[L+1:], post[L:-1])
        return root
```

**Complexity Analysis**

* Time Complexity: $O(N^2)$, where $N$ is the number of nodes.

* Space Complexity: $O(N^2)$.

## pproach 2: Recursion (Space Saving Variant)
**Explanation**

We present a variation of Approach 1 that uses indexes to refer to the subarrays of pre and post, instead of passing copies of those subarrays. Here, `(i0, i1, N)` refers to `pre[i0:i0+N], post[i1:i1+N]`.

```python
class Solution(object):
    def constructFromPrePost(self, pre, post):
        def make(i0, i1, N):
            if N == 0: return None
            root = TreeNode(pre[i0])
            if N == 1: return root

            for L in xrange(N):
                if post[i1 + L - 1] == pre[i0 + 1]:
                    break

            root.left = make(i0 + 1, i1, L)
            root.right = make(i0 + L + 1, i1 + L, N - 1 - L)
            return root

        return make(0, 0, len(pre))
```

**Complexity Analysis**

* Time Complexity: $O(N^2)$, where $N$ is the number of nodes.

* Space Complexity: $O(N)$, the space used by the answer.

# Submissions
---
**Solution: (Recursion)**
```
Runtime: 52 ms
Memory Usage: 12.8 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre: return None
        root = TreeNode(pre[0])
        if len(pre) == 1: return root

        L = post.index(pre[1]) + 1
        root.left = self.constructFromPrePost(pre[1:L+1], post[:L])
        root.right = self.constructFromPrePost(pre[L+1:], post[L:-1])
        return root
```

**Solution 1: (Hash Table, DFS)**
```
Runtime: 8 ms
Memory Usage: 25.7 MB
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
    TreeNode* constructFromPrePost(vector<int>& preorder, vector<int>& postorder) {
        int n = preorder.size();
        
        unordered_map<int,int> mp;
        for(int i=0;i<n;i++) mp[postorder[i]] = i;
        
        return solve(preorder,0,n-1,postorder,0,n-1,mp);
    }
    
    TreeNode* solve(vector<int> &preorder,int pre_start,int pre_end,vector<int> &postorder,int post_start,int post_end,unordered_map<int,int> &mp){
        if(pre_start > pre_end or post_start > post_end) return NULL;
        
        int root_val = preorder[pre_start];
        TreeNode* root = new TreeNode(root_val);
        
        if(pre_start+1 <= pre_end){
            int pos = mp[preorder[pre_start+1]];
            int num_left = pos - post_start + 1;
            root->left = solve(preorder,pre_start+1,pre_start+num_left,postorder,post_start,pos,mp);
            root->right = solve(preorder,pre_start+1+num_left,pre_end,postorder,pos+1,post_end-1,mp);
        }
        
        return root;
    }
};
```

**Solution 2: (Optimized Recursion)**

    preorder = [1,2,4,5,3,6,7],     MLR
                    ^^^   ^^^        ^^
    postorder = [4,5,2,6,7,3,1]     LRM
                 ^^^   ^^^          ^^

         1
      2
   4    5


```
Runtime: 0 ms, Beats 100.00%
Memory: 28.20 MB, Beats 76.14%
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
     // Helper function to recursively build the tree
    TreeNode* constructTree(int& preIndex, int& postIndex,
                            vector<int>& preorder, vector<int>& postorder) {
        // Create a new node with the value at the current preorder index
        TreeNode* root = new TreeNode(preorder[preIndex]);
        preIndex++;  // Mark this node as created

        // Recursively construct the left subtree if the root is not the last of
        // its subtree
        if (root->val != postorder[postIndex]) {
            root->left =
                constructTree(preIndex, postIndex, preorder, postorder);
        }

        // Recursively construct the right subtree if the root is still not the
        // last of its subtree
        if (root->val != postorder[postIndex]) {
            root->right =
                constructTree(preIndex, postIndex, preorder, postorder);
        }

        // Mark this node and its subtree as fully processed
        postIndex++;

        return root;
    }
public:
    TreeNode* constructFromPrePost(vector<int>& preorder, vector<int>& postorder) {
        int preIndex = 0;
        int postIndex = 0;
        return constructTree(preIndex, postIndex, preorder, postorder);
    }
};
```

**Solution 3: (DFS, DP)**

    preorder = [1,2,4,5,3,6,7],
                          ^

    postorder = [4,5,2,6,7,3,1]
    visited     [x x x x x x x]
i=0
                             ^
                [           ]
i=1
                     ^
                [   ]
i=2
                 ^
               []
i=3
                  ^
                 []
i=4
                          ^
                      [  ]       
*/

```
Runtime: 0 ms, Beats 100.00%
Memory: 28.22 MB, Beats 56.32%
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
    TreeNode *dfs(int &i, int j, vector<int> &visited, vector<int> &m, vector<int> &preorder, vector<int> &postorder) {
        TreeNode *node = new TreeNode(preorder[i]);
        visited[j] = true;
        if (j == 0 || visited[j-1]) {
            return node;
        }
        if (i+1 < preorder.size() && m[preorder[i+1]] < j) {
            i += 1;
            node->left = dfs(i, m[preorder[i]], visited, m, preorder, postorder);
        }
        if (i+1 < preorder.size() && m[preorder[i+1]] < j) {
            i += 1;
            node->right = dfs(i, m[preorder[i]], visited, m, preorder, postorder);
        }
        return node;
    }
public:
    TreeNode* constructFromPrePost(vector<int>& preorder, vector<int>& postorder) {
        int n = preorder.size(), i = 0, j;
        vector<int> visited(n);
        vector<int> m(n+1);
        for (j = 0; j < n; j ++) {
            m[postorder[j]] = j;
        }
        return dfs(i, m[preorder[i]], visited, m, preorder, postorder);
    }
};
```

**Solution 4: (DFS, left and right)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 28.38 MB, Beats 45.37%
```
```c++
]/**
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
    TreeNode *dfs(int &i, int j, int left, int right, vector<int> &m, vector<int> &preorder, vector<int> &postorder) {
        TreeNode *node = new TreeNode(preorder[i]);
        if (left == right) {
            return node;
        }
        if (i+1 < preorder.size() && m[preorder[i+1]] >= left && m[preorder[i+1]] < j) {
            i += 1;
            node->left = dfs(i, m[preorder[i]], left, m[preorder[i]], m, preorder, postorder);
        }
        if (i+1 < preorder.size() && m[preorder[i+1]] < right) {
            i += 1;
            node->right = dfs(i, m[preorder[i]], m[preorder[i-1]]+1, right-1, m, preorder, postorder);
        }
        return node;
    }
public:
    TreeNode* constructFromPrePost(vector<int>& preorder, vector<int>& postorder) {
        int n = preorder.size(), i = 0, j;
        vector<int> m(n+1);
        for (j = 0; j < n; j ++) {
            m[postorder[j]] = j;
        }
        return dfs(i, m[preorder[i]], 0, m[preorder[i]], m, preorder, postorder);
    }
};
```
