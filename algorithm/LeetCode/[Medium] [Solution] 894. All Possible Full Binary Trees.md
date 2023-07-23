894. All Possible Full Binary Trees

A full binary tree is a binary tree where each node has exactly `0` or `2` children.

Return a list of all possible full binary trees with `N` nodes.  Each element of the answer is the root node of one possible tree.

Each `node` of each tree in the answer must have `node.val = 0`.

You may return the final list of trees in any order.

 

**Example 1:**
```
Input: 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
Explanation:
```
 

**Note:**

* `1 <= N <= 20`

# Solution
---
## Approach 1: Recursion
**Intuition and Algorithm**

Let $\text{FBT}(N)$ be the list of all possible full binary trees with $N$ nodes.

Every full binary tree $T$ with 3 or more nodes, has 2 children at its root. Each of those children left and right are themselves full binary trees.

Thus, for $N \geq 3$, we can formulate the recursion: $\text{FBT}(N) =$ [All trees with left child from $\text{FBT}(x)$ and right child from $\text{FBT}(N-1-x)$, for all $x$].

Also, by a simple counting argument, there are no full binary trees with a positive, even number of nodes.

Finally, we should cache previous results of the function $\text{FBT}$ so that we don't have to recalculate them in our recursion.

```python
class Solution(object):
    memo = {0: [], 1: [TreeNode(0)]}

    def allPossibleFBT(self, N):
        if N not in Solution.memo:
            ans = []
            for x in xrange(N):
                y = N - 1 - x
                for left in self.allPossibleFBT(x):
                    for right in self.allPossibleFBT(y):
                        bns = TreeNode(0)
                        bns.left = left
                        bns.right = right
                        ans.append(bns)
            Solution.memo[N] = ans

        return Solution.memo[N]
```

**Complexity Analysis**

* Time Complexity: $O(2^N)$. For odd $N$, let $N = 2k + 1$. Then, $\Big| \text{FBT}(N) \Big| = C_k$, the $k$-th catalan number; and $\sum\limits_{k < \frac{N}{2}} C_k$ (the complexity involved in computing intermediate results required) is bounded by $O(2^N)$. However, the proof is beyond the scope of this article.

* Space Complexity: $O(2^N)$.

# Submissions
---
**Solution: (Recursion, DP Top-down, Tree)**
```
Runtime: 140 ms
Memory Usage: 15.3 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    memo = {0: [], 1: [TreeNode(0)]}
    
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N not in Solution.memo:
            ans = []
            for x in range(N):
                y = N - 1 - x
                for left in self.allPossibleFBT(x):
                    for right in self.allPossibleFBT(y):
                        bns = TreeNode(0)
                        bns.left = left
                        bns.right = right
                        ans.append(bns)
            Solution.memo[N] = ans

        return Solution.memo[N]
```

**Solution 1: (Recursion, DP Top-down, Tree)**
```
Runtime: 101 ms
Memory: 27.9 MB
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
    unordered_map<int, vector<TreeNode*>> dp; 
public:
    vector<TreeNode*> allPossibleFBT(int n) {
        vector<TreeNode*> result;
        if (n % 2 == 0) return {};
        if (n == 1) return {new TreeNode(0)};
        if (dp.find(n) != dp.end()) return dp[n];
        for (int i = 1; i < n; i += 2){
            auto lst = allPossibleFBT(i);
            auto rst = allPossibleFBT(n - i - 1);
            for (auto lnode: lst){
                for (auto rnode: rst){
                    result.push_back(new TreeNode(0, lnode, rnode));
                }
            }
        }
        
        return dp[n] = result;
    }
};
```
