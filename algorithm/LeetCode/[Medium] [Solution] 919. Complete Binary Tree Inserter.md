919. Complete Binary Tree Inserter

A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.

Write a data structure `CBTInserter` that is initialized with a complete binary tree and supports the following operations:

* `CBTInserter(TreeNode root)` initializes the data structure on a given tree with head node `root`;
* `CBTInserter.insert(int v)` will insert a `TreeNode` into the tree with value `node.val = v` so that the tree remains complete, and returns the value of the parent of the inserted `TreeNode`;
* `CBTInserter.get_root()` will return the head node of the tree.
 

**Example 1:**
```
Input: inputs = ["CBTInserter","insert","get_root"], inputs = [[[1]],[2],[]]
Output: [null,1,[1,2]]
```

**Example 2:**
```
Input: inputs = ["CBTInserter","insert","insert","get_root"], inputs = [[[1,2,3,4,5,6]],[7],[8],[]]
Output: [null,3,4,[1,2,3,4,5,6,7,8]]
``` 

**Note:**

* The initial given tree is complete and contains between `1` and `1000` nodes.
* `CBTInserter.insert` is called at most `10000` times per test case.
* Every value of a given or inserted node is between `0` and `5000`.

# Solution
---
## Approach 1: Deque
**Intuition**

Consider all the nodes numbered first by level and then left to right. Call this the "number order" of the nodes.

At each insertion step, we want to insert into the node with the lowest number (that still has 0 or 1 children).

By maintaining a `deque` (double ended queue) of these nodes in number order, we can solve the problem. After inserting a node, that node now has the highest number and no children, so it goes at the end of the deque. To get the node with the lowest number, we pop from the beginning of the deque.

**Algorithm**

First, perform a breadth-first search to populate the `deque` with nodes that have 0 or 1 children, in number order.

Now when inserting a node, the parent is the first element of `deque`, and we add this new node to our `deque`.

```python
class CBTInserter(object):
    def __init__(self, root):
        self.deque = collections.deque()
        self.root = root
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if not node.left or not node.right:
                self.deque.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def insert(self, v):
        node = self.deque[0]
        self.deque.append(TreeNode(v))
        if not node.left:
            node.left = self.deque[-1]
        else:
            node.right = self.deque[-1]
            self.deque.popleft()
        return node.val

    def get_root(self):
        return self.root
```

**Complexity Analysis**

* Time Complexity: The preprocessing is $O(N)$, where $N$ is the number of nodes in the tree. Each insertion operation thereafter is $O(1)$.

* Space Complexity: $O(N_{\text{cur}})$ space complexity, when the size of the tree during the current insertion operation is $N_{\text{cur}}$.

# Submissions
---
**Solution:**
```
Runtime: 56 ms
Memory Usage: 13.3 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class CBTInserter:

    def __init__(self, root: TreeNode):
        self.deque = collections.deque()
        self.root = root
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if not node.left or not node.right:
                self.deque.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def insert(self, v: int) -> int:
        node = self.deque[0]
        self.deque.append(TreeNode(v))
        if not node.left:
            node.left = self.deque[-1]
        else:
            node.right = self.deque[-1]
            self.deque.popleft()
        return node.val

    def get_root(self) -> TreeNode:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()
```

**Solution 1: (BFS)**
```
Runtime: 144 ms
Memory Usage: 64.4 MB
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
class CBTInserter {
    TreeNode* node;
public:
    CBTInserter(TreeNode* root) {
        node = root;
    }
    
    int insert(int val) {
        TreeNode* root = node;
        queue<TreeNode*>q;
        if(!root->left and !root->right){
            root->left = new TreeNode(val);
            return root->val;
        }
        q.push(root);
        while(!q.empty()){
            auto temp = q.front();
            q.pop();
            if(temp->left)q.push(temp->left);
            if(temp->right)q.push(temp->right);
            if(!temp->left){
                temp->left = new TreeNode(val);
                return temp->val;
            }
            if(!temp->right){
                temp->right = new TreeNode(val);
                return temp->val;
            }
        }
        return -1;
    }
    
    TreeNode* get_root() {
        return node;
    }
};

/**
 * Your CBTInserter object will be instantiated and called as such:
 * CBTInserter* obj = new CBTInserter(root);
 * int param_1 = obj->insert(val);
 * TreeNode* param_2 = obj->get_root();
 */
```
