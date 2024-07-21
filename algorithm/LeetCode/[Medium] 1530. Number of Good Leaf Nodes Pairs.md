1530. Number of Good Leaf Nodes Pairs

Given the `root` of a binary tree and an integer `distance`. A pair of two different leaf nodes of a binary tree is said to be good if the length of the shortest path between them is less than or equal to `distance`.

Return the number of good leaf node pairs in the tree.

 

**Example 1:**

![1530_e1.jpg](img/1530_e1.jpg)
```
Input: root = [1,2,3,null,4], distance = 3
Output: 1
Explanation: The leaf nodes of the tree are 3 and 4 and the length of the shortest path between them is 3. This is the only good pair.
```

**Example 2:**

![1530_e2.jpg](img/1530_e2.jpg)
```
Input: root = [1,2,3,4,5,6,7], distance = 3
Output: 2
Explanation: The good pairs are [4,5] and [6,7] with shortest path = 2. The pair [4,6] is not good because the length of ther shortest path between them is 4.
```

**Example 3:**
```
Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
Output: 1
Explanation: The only good pair is [2,5].
```

**Example 4:**
```
Input: root = [100], distance = 1
Output: 0
```

**Example 5:**
```
Input: root = [1,1,1], distance = 2
Output: 1
```

**Constraints:**

* The number of nodes in the tree is in the range `[1, 2^10]`.
* Each node's value is between `[1, 100]`.
* `1 <= distance <= 10`

# Submissions
---
**Solution 1: (DFS, Post Order)**
```
Runtime: 360 ms
Memory Usage: 15.3 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        ans = 0
        
        def dfs(node):
            nonlocal ans
            if not node:
                return []
            if not node.left and not node.right:
                return [(0, 1)]
            left = dfs(node.left)
            right = dfs(node.right)
            for ld, ln in left:
                for rd, rn in right:
                    if ld+rd+2 <= distance:
                        ans += ln*rn
            return [(d+1, n) for d, n in left + right]
        
        dfs(root)
        return ans
```

**Solution 2: (DFS, Counter, Post Order)**
```
Runtime: 224 ms
Memory Usage: 15.2 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        ans = 0
        
        def dfs(node):
            nonlocal ans
            if not node:
                return collections.Counter()
            if not node.left and not node.right:
                return collections.Counter([0])
            lcount = dfs(node.left)
            rcount = dfs(node.right)
            for ld, ln in lcount.items():
                for rd, rn in rcount.items():
                    if ld+rd+2 <= distance:
                        ans += ln*rn
            return Counter({d+1: n for d, n in (lcount + rcount).items()})
        
        dfs(root)
        return ans
            
```

**Solution 3: (DFS, Post Order)**
```
Runtime: 132 ms
Memory Usage: 36.8 MB
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
    int ans = 0;
    int countPairs(TreeNode* root, int distance) {
        dfs(root, distance);
        return ans;
    }
    //Idea is it do dfs & return a list of distances of all leaf nodes to the ancestor 
    //and let the ancestor compare the distances of all it's leaf nodes, add them to result
    vector<int> dfs(TreeNode*root, int d){
        vector<int> p = {};
        if(root == nullptr) return p;
        
        auto left = dfs(root->left, d);
        auto right = dfs(root->right, d);
        
        if(left.size() == 0 && right.size() ==0){
            p.push_back(1);
            return p;
        } 
        //Compare distance and add them to answer
        for(int i = 0; i<left.size(); i++){
            for(int j=0; j<right.size(); j++){
                if(left[i]+right[j] <=d ){
                    ans ++;
                }
            }
        }
        //Increase distance by one for all child and send them to parent
        for(int i=0; i<left.size(); i++){
            left[i]++;
            p.push_back(left[i]);
        }
          
         for(int i=0; i<right.size(); i++){
            right[i]++;
            p.push_back(right[i]);
        }
        
        return p;
    }
};
```

**Solution 4: (Graph Conversion + BFS)**
```
Runtime: 264 ms
Memory: 118.63 MB
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
    void traverseTree(TreeNode* currNode, TreeNode* prevNode,
                      unordered_map<TreeNode*, vector<TreeNode*>>& graph,
                      unordered_set<TreeNode*>& leafNodes) {
        if (!currNode) {
            return;
        }
        if (!currNode->left && !currNode->right) {
            leafNodes.insert(currNode);
        }
        if (prevNode) {
            graph[prevNode].push_back(currNode);
            graph[currNode].push_back(prevNode);
        }
        traverseTree(currNode->left, currNode, graph, leafNodes);
        traverseTree(currNode->right, currNode, graph, leafNodes);
    }
public:
    int countPairs(TreeNode* root, int distance) {
        unordered_map<TreeNode*, vector<TreeNode*>> graph;
        unordered_set<TreeNode*> leafNodes;

        traverseTree(root, nullptr, graph, leafNodes);

        int ans = 0;

        for (auto leaf : leafNodes) {
            queue<TreeNode*> bfsQueue;
            unordered_set<TreeNode*> seen;
            bfsQueue.push(leaf);
            seen.insert(leaf);

            // Go through all nodes that are within the given distance of
            // the current leaf node
            for (int i = 0; i <= distance; i++) {
                int size = bfsQueue.size();
                for (int j = 0; j < size; j++) {
                    TreeNode* currNode = bfsQueue.front();
                    bfsQueue.pop();
                    if (leafNodes.count(currNode) && currNode != leaf) {
                        ans++;
                    }
                    if (graph.count(currNode)) {
                        for (auto neighbor : graph[currNode]) {
                            if (!seen.count(neighbor)) {
                                bfsQueue.push(neighbor);
                                seen.insert(neighbor);
                            }
                        }
                    }
                }
            }
        }
        return ans / 2;
    }
};
```

**Solution 5: (Post-Order Traversal)**
```
Runtime: 41 ms
Memory: 35.31 MB
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
     vector<int> postOrder(TreeNode* currentNode, int distance) {
        if (!currentNode)
            return vector<int>(12);
        else if (!currentNode->left && !currentNode->right) {
            vector<int> current(12);
            // Leaf node's distance from itself is 0
            current[0] = 1;
            return current;
        }

        // Leaf node count for a given distance i
        vector<int> left = postOrder(currentNode->left, distance);
        vector<int> right = postOrder(currentNode->right, distance);

        vector<int> current(12);

        // Combine the counts from the left and right subtree and shift by
        // +1 distance
        for (int i = 0; i < 10; i++) {
            current[i + 1] = left[i] + right[i];
        }

        // Initialize to total number of good leaf nodes pairs from left and
        // right subtrees.
        current[11] += left[11] + right[11];

        // Iterate through possible leaf node distance pairs
        for (int d1 = 0; d1 <= distance; d1++) {
            for (int d2 = 0; d2 <= distance; d2++) {
                if (2 + d1 + d2 <= distance) {
                    // If the total path distance is less than the given
                    // distance limit, then add to the total number of good
                    // pairs.
                    current[11] += left[d1] * right[d2];
                }
            }
        }

        return current;
    }
public:
    int countPairs(TreeNode* root, int distance) {
        return postOrder(root, distance)[11];
    }
};
```
