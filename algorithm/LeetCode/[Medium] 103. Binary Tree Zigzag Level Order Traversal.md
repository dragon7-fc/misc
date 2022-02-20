103. Binary Tree Zigzag Level Order Traversal

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree `[3,9,20,null,null,15,7]`,
```
    3
   / \
  9  20
    /  \
   15   7
```
return its zigzag level order traversal as:
```
[
  [3],
  [20,9],
  [15,7]
]
```

# Submissions
---
**Solution 1: (BFS)**
```
Runtime: 36 ms
Memory Usage: 14.1 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        level = root and [root]
        ans = []
        forward = True
        while level:
            if forward:
                ans.append([node.val for node in level])
            else:
                ans.append([node.val for node in level[::-1]])
            level = [c for node in level for c in [node.left, node.right] if c]
            forward = not forward
        
        return ans
```

**Solution 2: (BFS)**
```
Runtime: 0 ms
Memory Usage: 12.4 MB
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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
if (!root) return {};
        std::queue<TreeNode*> q;
        q.push(root);
        int level = 0;
        std::vector<vector<int>> res;
        while(!q.empty()){
            int sz = q.size(); 
            std::vector<int> curr(sz);
            for(int i = 0; i < sz; i++){
                TreeNode* temp = q.front();
                q.pop();
                if(level == 0){
                    curr[i] = temp->val;
                }else{
                    curr[sz - i - 1] = temp->val;
                }
                if(temp->left){
                    q.push(temp->left);
                }
                if(temp->right){
                    q.push(temp->right);
                }
            }
            level = level == 0 ? 1 : 0;
            res.push_back(curr);
        }
        return res;
    }
};
```

**Solution 3: (DFS)**
```
Runtime: 8 ms
Memory Usage: 12.4 MB
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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        if (!root) return {};
        
        int l2r = 1;
        vector<vector<int>>res;
        stack<TreeNode*> current, next;
        
        current.push(root);
        
        TreeNode *temp;
        vector<int> v;
        
        while(!current.empty()) {
            temp = current.top();
            current.pop();
            if(temp) {
                v.push_back(temp->val);
                if(l2r) {
                    if(temp->left)   next.push(temp->left);
                    if(temp->right)  next.push(temp->right);
                }
                else {
                    if(temp->right)  next.push(temp->right);
                    if(temp->left)   next.push(temp->left);
                }
            }
            if(current.empty())
            {
                l2r = 1 - l2r;
                res.push_back(v);
                swap(current, next);
                v.clear();
            }
        }
       
        return res;
    }
};
```

**Solution 4: (BFS)**
```
Runtime: 6 ms
Memory Usage: 6.5 MB
```
```c
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct Pair {
    struct TreeNode* node;
    int level;
};

struct Queue {
    struct Pair data[3000];
    int size;
    int i;
    int j;
};

void qpush(struct Queue* q, struct Pair p) {
    q->size ++;
    q->data[q->j] = p;
    q->j=(q->j+1)%3000;
}

struct Pair qpop(struct Queue* q) {
    struct Pair r;
    q->size--;
    r = q->data[q->i];
    q->i=(q->i+1)%3000;
    return r;
}

int qempty(struct Queue* q) {
    return q->size==0;
}

struct Result {
    int** r;
    int* cols;
    int size;
    int cap;
    
    int* cur;
    int cur_size;
    int cur_cap;
};

void flush(struct Result* r) {
    if (r->cur == NULL) {
        return;
    }
    if (r->size >= r->cap) {
        r->cap = (r->cap+1)*2;
        r->r = realloc(r->r, r->cap*sizeof(int*));
        r->cols = realloc(r->cols, r->cap*sizeof(int));
    }
    r->r[r->size] = r->cur;
    r->cols[r->size] = r->cur_size;
    r->size++;
    r->cur = NULL;
    r->cur_size = r->cur_cap = 0;
}

void add(struct Result* r, int x) {
    if (r->cur_size >= r->cur_cap) {
        r->cur_cap = (r->cur_cap+1)*2;
        r->cur = realloc(r->cur, r->cur_cap*sizeof(int));
    }
    r->cur[r->cur_size++] = x;
}

void reverse(int* data, int size) {
    int i;
    for (i = 0; i < size/2; i++) {
        int t = data[i]; data[i] = data[size-i-1]; data[size-i-1] = t;
    }
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** zigzagLevelOrder(struct TreeNode* root, int* returnSize, int** returnColumnSizes){
    struct Queue q;
    struct Result r;
    int level = 0, i;
    struct Pair c = {root, level};
    memset(&q, 0, sizeof(q));
    memset(&r, 0, sizeof(r));
    if (root) {
        qpush(&q, c);
    }
    while (!qempty(&q)) {
        struct Pair cur = qpop(&q);
        if (cur.level != level) {
            flush(&r);
        }
        add(&r, cur.node->val);
        if (cur.node->left) {
            struct Pair n = {cur.node->left, cur.level+1};
            qpush(&q, n);
        }
        if (cur.node->right) {
            struct Pair n = {cur.node->right, cur.level+1};
            qpush(&q, n);
        }
        level = cur.level;
    }
    flush(&r);
    
    *returnColumnSizes = r.cols;
    *returnSize = r.size;
    for (i = 1; i < r.size; i += 2) {
        reverse(r.r[i], r.cols[i]);
    }
    return r.r;
}
```

