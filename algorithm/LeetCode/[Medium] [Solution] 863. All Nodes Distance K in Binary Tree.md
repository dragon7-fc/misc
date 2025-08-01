863. All Nodes Distance K in Binary Tree

We are given a binary tree (with root node `root`), a `target` node, and an integer value `K`.

Return a list of the values of all nodes that have a distance `K` from the `target` node.  The answer can be returned in any order.

 

**Example 1:**
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.
```
![863_sketch0.png](img/863_sketch0.png)
```
Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.
```

**Note:**

* The given tree is non-empty.
* Each node in the tree has unique values `0 <= node.val <= 500`.
* The `target` node is a node in the tree.
* `0 <= K <= 1000`.

# Solution
---
## Approach 1: Annotate Parent
**Intuition**

If we know the parent of every node `x`, we know all nodes that are distance `1` from `x`. We can then perform a breadth first search from the `target` node to find the answer.

**Algorithm**

We first do a depth first search where we annotate every node with information about it's parent.

After, we do a breadth first search to find all nodes a distance `K` from the `target`.

```python
class Solution(object):
    def distanceK(self, root, target, K):
        def dfs(node, par = None):
            if node:
                node.par = par
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)

        queue = collections.deque([(target, 0)])
        seen = {target}
        while queue:
            if queue[0][1] == K:
                return [node.val for node, d in queue]
            node, d = queue.popleft()
            for nei in (node.left, node.right, node.par):
                if nei and nei not in seen:
                    seen.add(nei)
                    queue.append((nei, d+1))

        return []
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the number of nodes in the given tree.

* Space Complexity: $O(N)$.

## Approach 2: Percolate Distance
**Intuition**

From `root`, say the `target` node is at depth `3` in the left branch. It means that any nodes that are distance `K - 3` in the right branch should be added to the answer.

**Algorithm**

Traverse every node with a depth first search `dfs`. We'll add all nodes `x` to the answer such that node is the node on the path from `x` to `target` that is closest to the `root`.

To help us, `dfs(node)` will return the distance from node to the `target`. Then, there are 4 cases:

1. If `node == target`, then we should add nodes that are distance `K` in the subtree rooted at `target`.

1. If `target` is in the left branch of `node`, say at distance `L+1`, then we should look for nodes that are distance `K - L - 1` in the right branch.

1. If `target` is in the right branch of `node`, the algorithm proceeds similarly.

1. If `target` isn't in either branch of `node`, then we stop.

In the above algorithm, we make use of the auxillary function `subtree_add(node, dist)` which adds the nodes in the subtree rooted at `node` that are distance `K - dist` from the given `node`.

```python
class Solution(object):
    def distanceK(self, root, target, K):
        ans = []

        # Return distance from node to target if exists, else -1
        # Vertex distance: the # of vertices on the path from node to target
        def dfs(node):
            if not node:
                return -1
            elif node is target:
                subtree_add(node, 0)
                return 1
            else:
                L, R = dfs(node.left), dfs(node.right)
                if L != -1:
                    if L == K: ans.append(node.val)
                    subtree_add(node.right, L + 1)
                    return L + 1
                elif R != -1:
                    if R == K: ans.append(node.val)
                    subtree_add(node.left, R + 1)
                    return R + 1
                else:
                    return -1

        # Add all nodes 'K - dist' from the node to answer.
        def subtree_add(node, dist):
            if not node:
                return
            elif dist == K:
                ans.append(node.val)
            else:
                subtree_add(node.left, dist + 1)
                subtree_add(node.right, dist + 1)

        dfs(root)
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the number of nodes in the given tree.

* Space Complexity: $O(N)$.

# Submissions
---
**Solution 1: (DFS, BFS)**
```
Runtime: 32 ms
Memory Usage: 13.1 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        graph = collections.defaultdict(list)
        def dfs(node):
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                dfs(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                dfs(node.right)
        
        dfs(root)
        level = [target.val]
        ans = []
        visited = set(level)
        while level and K > 0:
            level = [nei for node in level for nei in graph[node] if nei not in visited]
            visited = visited | set(level)
            K -= 1
        return level if K == 0 else []
```

**Solution 2: (BFS)**
```
Runtime: 8 ms
Memory Usage: 12.6 MB
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

void helper_DeepSearch(struct TreeNode* root, struct TreeNode* target, int K, int* returnSize, int** result)
{
    if((root==NULL) || (K<0))
        return;
    
    if(K==0)
    {
        (*result) = (int*)realloc(*result,(*returnSize+1)*sizeof(int));
        (*result)[(*returnSize)++] = root->val;
    }
    else
    {
        helper_DeepSearch(root->left,target,K-1,returnSize,result);
        helper_DeepSearch(root->right,target,K-1,returnSize,result);
    }
}

int helper(struct TreeNode* root, struct TreeNode* target, int K, int* returnSize, int** result)
{
    int left, right;
    
    if(root==NULL)
        return 0;
    
    if(root==target)
    {
        helper_DeepSearch(root->left,target,K-1,returnSize,result);
        helper_DeepSearch(root->right,target,K-1,returnSize,result);
        return 1;
    }
    
    left = helper(root->left,target,K,returnSize,result);
    if(left > 0)
    {
        if(left==K)
        {
            (*result) = (int*)realloc(*result,(*returnSize+1)*sizeof(int));
            (*result)[(*returnSize)++] = root->val;
        }
        helper_DeepSearch(root->right,target,K-left-1,returnSize,result);
        return left + 1;
    }
    
    right = helper(root->right,target,K,returnSize,result);
    if(right > 0)
    {
        if(right==K)
        {
            (*result) = (int*)realloc(*result,(*returnSize+1)*sizeof(int));
            (*result)[(*returnSize)++] = root->val;
        }
        helper_DeepSearch(root->left,target,K-right-1,returnSize,result);
        return right + 1;
    }
    
    return 0;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* distanceK(struct TreeNode* root, struct TreeNode* target, int k, int* returnSize) {
    int* result = NULL;
    
    if((root==NULL) || (target==NULL))
    {
        *returnSize = 0;
        return NULL;
    }
    
    if(k==0)
    {
        *returnSize = 1;
        result = (int*)malloc(1*sizeof(int));
        result[0] = target->val;
        return result;
    }
    
    helper(root,target,k,returnSize,&result);
    
    return result;
}
```

**Solution 3: (DFS)**
```
Runtime: 11 ms
Memory Usage: 13.6 MB
```
```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
    unordered_map<int, vector<int>> graph;
    unordered_set<int> visit;
    vector<int> ans;
public:
    vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
        traverse(root);
        dfs(target->val, k);
        return ans;
    }
    void traverse(TreeNode* root){//converting bst into an undirected graph
        if(root==NULL)
            return;
        if(root->left){
            graph[root->val].push_back(root->left->val);
            graph[root->left->val].push_back(root->val);
            traverse(root->left);
        }
        if(root->right){
            graph[root->val].push_back(root->right->val);
            graph[root->right->val].push_back(root->val);
            traverse(root->right);
        }       
    }
    void dfs(int target, int k){//checking all the nodes at a distance k from the target node and putting them in ans vector
        if(visit.find(target)!=visit.end())
            return;        
        visit.insert(target);        
        if(k==0)
            ans.push_back(target);      
        for(auto it:graph[target])
            dfs(it, k-1);
    }
};
```

**Solution 4: (BFS)**
```
Runtime: 3 ms, Beats 81.76%
Memory: 16.25 MB, Beats 11.61%
```
```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
    unordered_map<TreeNode*,TreeNode*> par;
    void dfs(TreeNode *node, TreeNode *p) {
        if (!node) {
            return;
        }
        if (p) {
            par[node] = p;
        }
        dfs(node->left, node);
        dfs(node->right, node);
    }
public:
    vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
        if (k == 0) {
            return {target->val};
        }
        int sz, i;
        dfs(root, nullptr);
        queue<TreeNode*> q;
        vector<int> ans;
        unordered_set<TreeNode*> visited;
        q.push(target);
        visited.insert(target);
        while (q.size() && k) {
            sz = q.size();
            ans.clear();
            for (i = 0; i < sz; i ++) {
                auto node = q.front();
                q.pop();
                if (node->left && !visited.count(node->left)) {
                    q.push(node->left);
                    visited.insert(node->left);
                    ans.push_back(node->left->val);
                }
                if (node->right && !visited.count(node->right)) {
                    q.push(node->right);
                    visited.insert(node->right);
                    ans.push_back(node->right->val);
                }
                if (par[node] && !visited.count(par[node])) {
                    q.push(par[node]);
                    visited.insert(par[node]);
                    ans.push_back(par[node]->val);
                }
            }
            k -= 1;
        }
        if (k == 0) {
            return ans;
        }
        return {};
    }
};

```
