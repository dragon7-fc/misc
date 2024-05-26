2782. Number of Unique Categories

You are given an integer `n` and an object `categoryHandler` of class `CategoryHandler`.

There are `n` elements, numbered from `0` to `n - 1`. Each element has a category, and your task is to find the number of unique categories.

The class `CategoryHandler` contains the following function, which may help you:

* `boolean haveSameCategory(integer a, integer b)`: Returns `true` if `a` and `b` are in the same category and `false` otherwise. Also, if either `a` or `b` is not a valid number (i.e. it's greater than or equal to nor less than 0), it returns `false`.

Return the number of unique categories.

 

**Example 1:**
```
Input: n = 6, categoryHandler = [1,1,2,2,3,3]
Output: 3
Explanation: There are 6 elements in this example. The first two elements belong to category 1, the second two belong to category 2, and the last two elements belong to category 3. So there are 3 unique categories.
```

**Example 2:**
```
Input: n = 5, categoryHandler = [1,2,3,4,5]
Output: 5
Explanation: There are 5 elements in this example. Each element belongs to a unique category. So there are 5 unique categories.
```

**Example 3:**
```
Input: n = 3, categoryHandler = [1,1,1]
Output: 1
Explanation: There are 3 elements in this example. All of them belong to one category. So there is only 1 unique category.
```

**Constraints:**

* `1 <= n <= 100`

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 182 ms
Memory: 112.16 MB
```
```c++
/**
 * Definition for a category handler.
 * class CategoryHandler {
 * public:
 *     CategoryHandler(vector<int> categories);
 *     bool haveSameCategory(int a, int b);
 * };
 */
class Solution {
    void dfs(vector<int> adjList[], vector<bool>& vis, int src) {
        vis[src] = true;
        
        for (int i = 0; i < adjList[src].size(); i++) {
            if (!vis[adjList[src][i]]) {
                dfs(adjList, vis, adjList[src][i]);
            }
        }
    }
public:
    int numberOfCategories(int n, CategoryHandler* categoryHandler) {
        vector<int> adjList[n];
        
        // Iterate over every pair and add an undirected edge if both belong to the same category.
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (categoryHandler->haveSameCategory(i, j)) {
                    adjList[i].push_back(j);
                    adjList[j].push_back(i);
                }
            }
        }
        
        vector<bool> vis(n, false);
        int components = 0;
        // Each DFS means that a new category is being accessed.
        for (int i = 0; i < n; i++) {
            if (!vis[i]) {
                components++;
                dfs(adjList, vis, i);
            }
        }
        
        return components;
    }
};
```

**Solution 2: (Union Find)**
```
Runtime: 106 ms
Memory: 110.42 MB
```
```c++
/**
 * Definition for a category handler.
 * class CategoryHandler {
 * public:
 *     CategoryHandler(vector<int> categories);
 *     bool haveSameCategory(int a, int b);
 * };
 */
class UnionFind {
    vector<int> root;
    vector<int> componentSize;
    // Number of distinct components in the graph.
    int componentsCount;
    
public:
    // Initialize the list root and componentSize
    // Each node is root of itself with size 1.
    UnionFind(int n) {
        componentsCount = n;
        for (int i = 0; i <= n; i++) {
            root.push_back(i);
            componentSize.push_back(1);
        }
    }
    
    // Get the root of a node.
    int findRoot(int x) {
        if (root[x] == x) {
            return x;
        }
        
        // Path compression.
        return root[x] = findRoot(root[x]);
    }
    
    // Perform the union of two components that belongs to node x and node y.
    void performUnion(int x, int y) {       
        x = findRoot(x); y = findRoot(y);
        
        if (x == y) {
            return;
        }
        
        if (componentSize[x] > componentSize[y]) {
            componentSize[x] += componentSize[y];
            root[y] = x;
        } else {
            componentSize[y] += componentSize[x];
            root[x] = y;
        }
        
        componentsCount--;
    }
    
    // Return the number of components.
    int getComponentsCount() {
        return componentsCount;
    }
};
class Solution {
public:
    int numberOfCategories(int n, CategoryHandler* categoryHandler) {
        UnionFind uF(n);
        
        // Iterate over every pair and perform union if both belong to the same category.
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (categoryHandler->haveSameCategory(i, j)) {
                    uF.performUnion(i, j);
                }
            }
        }
        
        return uF.getComponentsCount();
    }
};
```

**Solution 3: (Greedy)**
```
Runtime: 101 ms
Memory: 101.58 MB
```
```c++
/**
 * Definition for a category handler.
 * class CategoryHandler {
 * public:
 *     CategoryHandler(vector<int> categories);
 *     bool haveSameCategory(int a, int b);
 * };
 */
class Solution {
public:
    int numberOfCategories(int n, CategoryHandler* categoryHandler) {
        int components = n;
        
        // Iterate over every pair, and if both belong to the same category,
        //Remove the element from separate components.
        for (int i = 0; i < n; i++) {
            for (int j = i - 1; j >= 0; j--) {
                if (categoryHandler->haveSameCategory(i, j)) {
                    components--;
                    break;
                }
            }
        }
        
        return components;
    }
};
```
