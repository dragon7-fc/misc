987. Vertical Order Traversal of a Binary Tree

Given a binary tree, return the vertical order traversal of its nodes values.

For each node at position `(X, Y)`, its left and right children respectively will be at positions `(X-1, Y-1)` and `(X+1, Y-1)`.

Running a vertical line from `X = -infinity` to `X = +infinity`, whenever the vertical line touches some nodes, we report the values of the nodes in order from top to bottom (decreasing `Y` coordinates).

If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.

Return an list of non-empty reports in order of `X` coordinate.  Every report will have a list of values of nodes.

 

**Example 1:**


```
Input: [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation: 
Without loss of generality, we can assume the root node is at position (0, 0):
Then, the node with value 9 occurs at position (-1, -1);
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
The node with value 20 occurs at position (1, -1);
The node with value 7 occurs at position (2, -2).
```

**Example 2:**


```
Input: [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation: 
The node with value 5 and the node with value 6 have the same position according to the given scheme.
However, in the report "[1,5,6]", the node value of 5 comes first since 5 is smaller than 6.
```

**Note:**

1. The tree will have between `1` and `1000` nodes.
1. Each node's value will be between `0` and `1000`.

# Solution
---
## Approach 1: Store Locations
**Intuition**

It's evident that there are two steps in a straightforward solution: first, find the location of every node, then report their locations.

**Algorithm**

To find the location of every node, we can use a depth-first search. During the search, we will maintain the location `(x, y)` of the node. As we move from parent to child, the location changes to `(x-1, y+1)` or `(x+1, y+1)` depending on if it is a left child or right child. [We use `y+1` to make our sorting by decreasing `y` easier.]

To report the locations, we sort them by `x` coordinate, then `y` coordinate, so that they are in the correct order to be added to our answer.

Please see the inline comments for more details.

```python
class Solution(object):
    def verticalTraversal(self, root):
        seen = collections.defaultdict(
                  lambda: collections.defaultdict(list))

        def dfs(node, x=0, y=0):
            if node:
                seen[x][y].append(node)
                dfs(node.left, x-1, y+1)
                dfs(node.right, x+1, y+1)

        dfs(root)
        ans = []

        for x in sorted(seen):
            report = []
            for y in sorted(seen[x]):
                report.extend(sorted(node.val for node in seen[x][y]))
            ans.append(report)

        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N \log N)$, where $N$ is the number of nodes in the given tree.

* Space Complexity: $O(N)$.

# Submissions
---
**Solution 1: (Store Locations)**
```
Runtime: 28 ms
Memory Usage: 12.9 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        seen = collections.defaultdict(
                  lambda: collections.defaultdict(list))

        def dfs(node, x=0, y=0):
            if node:
                seen[x][y].append(node)
                dfs(node.left, x-1, y+1)
                dfs(node.right, x+1, y+1)

        dfs(root)
        ans = []

        for x in sorted(seen):
            report = []
            for y in sorted(seen[x]):
                report.extend(sorted(node.val for node in seen[x][y]))
            ans.append(report)

        return ans
```

**Solution 2: (DFS)**
```
Runtime: 4 ms
Memory Usage: 14.7 MB
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
    void dfs(map<pair<int, int>, set<int>>& map, TreeNode* root, int x, int y, int& maxValue, int& minValue) {
        if (root == NULL) {
            return;
        }
        map[{x, y}].insert(root->val);
        maxValue = max(maxValue, x);
        minValue = min(minValue, x);
        dfs(map, root->left, x - 1, y + 1, maxValue, minValue);
        dfs(map, root->right, x + 1, y + 1, maxValue, minValue);
    }
    vector<vector<int>> verticalTraversal(TreeNode* root) {
        if (root == NULL) {
            return {};
        }
        
        map<pair<int, int>, set<int>> map;
        int maxValue = INT_MIN;
        int minValue = INT_MAX;
        dfs(map, root, 0, 0, maxValue, minValue);
        vector<vector<int>> result(maxValue - minValue + 1);
        for (const auto& pair : map) {
            int index = pair.first.first - minValue;
            result[index].insert(result[index].end(), pair.second.begin(), pair.second.end());
        }
        return result;
    }
};
```

**Solution 3: (DFS)**
```
Runtime: 0 ms
Memory Usage: 12.9 MB
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
typedef struct
{
    int val;
    int row;
    int col;
} Entry_t;

Entry_t** addNode(struct TreeNode* node, int row, int col, Entry_t** table, int* tableSize)
{
    table = realloc(table, (++(*tableSize)) * sizeof(Entry_t*));
    table[(*tableSize)-1] = malloc(sizeof(Entry_t));
    table[(*tableSize)-1]->val = node->val;
    table[(*tableSize)-1]->row = row;
    table[(*tableSize)-1]->col = col;
    
    // printf("%d, %d, %d\n", *tableSize, table[(*tableSize)-1]->val, table[(*tableSize)-1]->height);
    
    // printf("table = %d\n", table);
    return table;
}

Entry_t** getVerticalTraversal(struct TreeNode* root, int row, int col, Entry_t** table, int* tableSize)
{
    if (root == NULL) return table;
    table = addNode(root, row, col, table, tableSize);
    table = getVerticalTraversal(root->left, row+1, col-1, table, tableSize);
    table = getVerticalTraversal(root->right, row+1, col+1, table, tableSize);
    
    // printf("table = %d\n", table);
    return table;
}

int cmp(const void* a, const void* b)
{
    /*
    a, b -> Entry_t*, hence a, b are Entry_t**
    */
    const Entry_t* e1 = *(const Entry_t**)a;
    const Entry_t* e2 = *(const Entry_t**)b;
    
    if (e1->col == e2->col)
    {
        if (e1->row == e2->row)
        {
            return e1->val - e2->val;
        }
        return e1->row - e2->row;
    }
    
    return e1->col - e2->col;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** verticalTraversal(struct TreeNode* root, int* returnSize, int** returnColumnSizes){
    /*
    table -> [Entry_t*, Entry_t*, ...]
    
    Input: root = [3,9,20,null,null,15,7]
    Output: [[9],[3,15],[20],[7]]
    */
    Entry_t** table = NULL;
    int tableSize = 0;
    
    table = getVerticalTraversal(root, 0, 0, table, &tableSize);
       
    qsort(table, tableSize, sizeof(Entry_t*), cmp);
    
    // printf("tableSize = %d\n", tableSize);
    // for (int i = 0; i < tableSize; i++)
    // {
    //     printf("%d, %d\n", table[i]->val, table[i]->height);
    // }
       
    int** ans = NULL;
    *returnSize = 0;
    *returnColumnSizes = NULL;
    
    for (int i = 0; i < tableSize; i++)
    {
        if (i == 0 || table[i]->col != table[i-1]->col)
        {
            (*returnSize)++;
            ans = realloc(ans, (*returnSize) * sizeof(int*));
            *returnColumnSizes = realloc(*returnColumnSizes, (*returnSize) * sizeof(int));
            (*returnColumnSizes)[(*returnSize)-1] = 1;
            ans[(*returnSize)-1] = malloc(sizeof(int));
            ans[(*returnSize)-1][0] = table[i]->val;
            // printf("Here in 1\n");
        }
        else
        {
            (*returnColumnSizes)[(*returnSize)-1]++;
            ans[(*returnSize)-1] = realloc(ans[(*returnSize)-1], (*returnColumnSizes)[(*returnSize)-1] * sizeof(int));
            ans[(*returnSize)-1][(*returnColumnSizes)[(*returnSize)-1]-1] = table[i]->val;
            // printf("Here in 2\n");
        }
    }
    
    return ans;
}
```

**Solution 4: (DFS)**
```
Runtime: 13 ms
Memory Usage: 14.6 MB
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
    void dfs(map<pair<int, int>, multiset<int>>& map, TreeNode* root, int x, int y, int& maxValue, int& minValue) {
        if (root == NULL) {
            return;
        }
        map[{x, y}].insert(root->val);
        maxValue = max(maxValue, x);
        minValue = min(minValue, x);
        dfs(map, root->left, x - 1, y + 1, maxValue, minValue);
        dfs(map, root->right, x + 1, y + 1, maxValue, minValue);
    }

public:
    vector<vector<int>> verticalTraversal(TreeNode* root) {
        if (root == NULL) {
            return {};
        }
        
        map<pair<int, int>, multiset<int>> map;
        int maxValue = INT_MIN;
        int minValue = INT_MAX;
        dfs(map, root, 0, 0, maxValue, minValue);
        vector<vector<int>> result(maxValue - minValue + 1);
        for (const auto& pair : map) {
            int index = pair.first.first - minValue;
            result[index].insert(result[index].end(), pair.second.begin(), pair.second.end());
        }
        return result;

    }
};
```

**Solution 5: (DFS, sorted map)**
```
Runtime: 3 ms, Beats 41.58%
Memory: 17.26 MB, Beats 5.03%
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
    map<int, map<int, multiset<int>>> m;
    void dfs(TreeNode *node, int r, int c) {
        if (!node) {
            return;
        }
        m[c][r].insert(node->val);
        dfs(node->left, r+1, c-1);
        dfs(node->right, r+1, c+1);
    }
public:
    vector<vector<int>> verticalTraversal(TreeNode* root) {
        vector<vector<int>> ans;
        dfs(root, 0, 0);
        for (auto [_, cm]: m) {
            ans.push_back({});
            for (auto [r, rs]: cm) {
                for (auto a: rs) {
                    ans.back().push_back(a);
                }
            }
        }
        return ans;
    }
};
```

**Solution 6: (DFS, sorted map)**
```
Runtime: 4 ms, Beats 22.49%
Memory: 16.40 MB, Beats 30.52%
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
    map<pair<int,int>,  multiset<int>> m;
    void dfs(TreeNode *node, int r, int c) {
        if (!node) {
            return;
        }
        m[{c, r}].insert(node->val);
        dfs(node->left, r+1, c-1);
        dfs(node->right, r+1, c+1);
    }
public:
    vector<vector<int>> verticalTraversal(TreeNode* root) {
        vector<vector<int>> ans;
        dfs(root, 0, 0);
        auto it = m.begin();
        while (it != m.end()) {
            ans.push_back({});
            auto cit = it;
            while (cit != m.end() && cit->first.first == it->first.first) {
                for (auto a: cit->second) {
                    ans.back().push_back(a);
                }
                cit++;
            }
            it = cit;
        }
        return ans;
    }
};
```
