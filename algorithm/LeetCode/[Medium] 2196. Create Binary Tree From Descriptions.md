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

**Solution 1: (Hash Table)**
```
Runtime: 1320 ms
Memory Usage: 277.7 MB
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
        unordered_map<int, TreeNode*> getNode;                          //to check if node alredy exist
        unordered_map<int, bool> isChild;                               //to check if node has parent or not
        for(auto &v: descriptions){
            if(getNode.count(v[0])==0){
                TreeNode* par = new TreeNode(v[0]);
                getNode[v[0]] = par;
            }
            if(getNode.count(v[1])==0){
                TreeNode* child = new TreeNode(v[1]);
                getNode[v[1]] = child;
            }
            if(v[2]==1) getNode[v[0]]->left = getNode[v[1]];               //left-child
            else getNode[v[0]]->right = getNode[v[1]];                     //right-child
            isChild[v[1]] = true;
        }
        TreeNode* ans = NULL;
        for(auto &v: descriptions){
            if(isChild[v[0]] != true){                  //if node has no parent then this is root node
                ans = getNode[v[0]]; 
                break;
            }
        }
        return ans;
    }
};
```
