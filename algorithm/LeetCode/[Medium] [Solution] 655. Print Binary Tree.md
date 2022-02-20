655. Print Binary Tree

Print a binary tree in an m*n 2D string array following these rules:

1. The row number `m` should be equal to the height of the given binary tree.
1. The column number `n` should always be an odd number.
1. The root node's value (in string format) should be put in the exactly middle of the first row it can be put. The column and the row where the root node belongs will separate the rest space into two parts (**left-bottom part and right-bottom part**). You should print the left subtree in the left-bottom part and print the right subtree in the right-bottom part. The left-bottom part and the right-bottom part should have the same size. Even if one subtree is none while the other is not, you don't need to print anything for the none subtree but still need to leave the space as large as that for the other subtree. However, if two subtrees are none, then you don't need to leave space for both of them.
1. Each unused space should contain an empty string "".
1. Print the subtrees following the same rules.

**Example 1:**
```
Input:
     1
    /
   2
Output:
[["", "1", ""],
 ["2", "", ""]]
```

**Example 2:**
```
Input:
     1
    / \
   2   3
    \
     4
Output:
[["", "", "", "1", "", "", ""],
 ["", "2", "", "", "", "3", ""],
 ["", "", "4", "", "", "", ""]]
```

**Example 3:**
```
Input:
      1
     / \
    2   5
   / 
  3 
 / 
4 
Output:

[["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
 ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
 ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
 ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
Note: The height of binary tree is in the range of [1, 10].
```

# Solution
---
## Approach #1 Recursive Solution[Accepted]
We start by initializing a $res$ array with the dimensions being $height$x$2^{height} - 1$. Here, $height$ refers to the number of levels in the given tree. In order to fill this $res$ array with the required elements, initially, we fill the complete array with "" . After this we make use of a recursive function `fill(res, root, i, l, r)` which fills the $res$ array such that the current element has to be filled in $i^{th}$ row, and the column being the middle of the indices $l$ and $r$, where $l$ and $r$ refer to the left and the right boundaries of the columns in which the current element can be filled.

In every recursive call, we do as follows:

1. If we've reached the end of the tree, i.e. if root==null, return.

1. Determine the column in which the current element(rootroot) needs to be filled, which is the middle of $l$ and $r$, given by say, $j$. The row number is same as $i$. Put the current element at $res[i][j]$.

1. Make the recursive call for the left child of the $root$ using fill(res, root.left, i + 1, l, (l + r) / 2).

1. Make the recursive call for the right child of the $root$ using `fill(res, root.right, i + 1, (l + r + 1) / 2, r)`.

Note, that in the last two recursive calls, we update the row number(level of the tree). This ensures that the child nodes fit into the correct row. We also update the column boundaries appropriately based on the $l$ and $r$ values.

Further, to determine the $height$ also, we make use of recursive funtion `getHeight(root)`, which returns the height of the tree starting from the $root$ node. We traverse into all the branches possible in the tree recursively and find the depth of the longest branch.

At the end, we convert the $res$ array into the required list format, before returning the results.

```python
public class Solution {
    public List<List<String>> printTree(TreeNode root) {
        int height = getHeight(root);
        String[][] res = new String[height][(1 << height) - 1];
        for(String[] arr:res)
            Arrays.fill(arr,"");
        List<List<String>> ans = new ArrayList<>();
        fill(res, root, 0, 0, res[0].length);
        for(String[] arr:res)
            ans.add(Arrays.asList(arr));
        return ans;
    }
    public void fill(String[][] res, TreeNode root, int i, int l, int r) {
        if (root == null)
            return;
        res[i][(l + r) / 2] = "" + root.val;
        fill(res, root.left, i + 1, l, (l + r) / 2);
        fill(res, root.right, i + 1, (l + r + 1) / 2, r);
    }
    public int getHeight(TreeNode root) {
        if (root == null)
            return 0;
        return 1 + Math.max(getHeight(root.left), getHeight(root.right));
    }
}
```

**Complexity Analysis**

* Time complexity : $O(h*2^h)$. We need to fill the $res$ array of size $h$x$2^h - 1$. Here, $h$ refers to the height of the given tree.

* Space complexity : $O(h*2^h)$. $res$ array of size $h$x$2^h - 1$ is used.

# Submissions
---
**Solution 1:**
```
Runtime: 20 ms
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
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def getHeight(node):
            if not node:
                return 0
            return 1 + max(getHeight(node.left), getHeight(node.right))
        
        def fill(res, node, row, l, r):
            if not node:
                return
            res[row][(l + r) // 2] = str(node.val)
            fill(res, node.left, row+1, l, (l + r) // 2)
            fill(res, node.right, row+1, (l + r + 1) // 2, r)
        
        height = getHeight(root)
        ans = [["" for _ in range((1 << height) - 1)] for _ in range(height)]
        fill(ans, root, 0, 0, len(ans[0]))
        return ans
        
```

**Solution 2: (BFS)**
```
Runtime: 0 ms
Memory Usage: 8.4 MB
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
    int height(TreeNode* node)
    {
        if(node == NULL)
            return -1;
        int lh = height(node->left);
        int rh = height(node->right);
        
        return 1 + max(lh, rh);
    }
public:
    vector<vector<string>> printTree(TreeNode* root) {
        int ht = height(root);
        int m = ht + 1;
        int n = pow(2, ht+1) - 1;
        vector<vector<string>> ans(m, vector<string>(n, ""));
        
        //             node,       row, col
        queue<pair<TreeNode*, pair<int, int>>> que;
        que.push({root, {0, (int)((n-1)/2)}});
                
        while(!que.empty())
        {
            pair<TreeNode*, pair<int, int>> curr = que.front();
            que.pop();
            TreeNode* node = curr.first;
            int row = curr.second.first;
            int col = curr.second.second;
            
            ans[row][col] = to_string(node->val);
            
            if(node->left != NULL)
            {
                que.push({node->left, {row+1, col - pow(2, ht-row-1)}});
            }
            if(node->right != NULL)
            {
                que.push({node->right, {row+1, col + pow(2, ht-row-1)}});
            }
        }
        return ans;
    }
};
```
