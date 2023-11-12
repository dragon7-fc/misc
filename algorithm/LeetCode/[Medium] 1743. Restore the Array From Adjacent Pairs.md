1743. Restore the Array From Adjacent Pairs

There is an integer array `nums` that consists of n unique elements, but you have forgotten it. However, you do remember every pair of adjacent elements in `nums`.

You are given a 2D integer array `adjacentPairs` of size `n - 1` where each `adjacentPairs[i] = [ui, vi]` indicates that the elements `ui` and `vi` are adjacent in `nums`.

It is guaranteed that every adjacent pair of elements `nums[i]` and `nums[i+1]` will exist in `adjacentPairs`, either as `[nums[i], nums[i+1]]` or `[nums[i+1], nums[i]]`. The pairs can appear in any order.

Return the original array `nums`. If there are multiple solutions, return any of them.

 

**Example 1:**
```
Input: adjacentPairs = [[2,1],[3,4],[3,2]]
Output: [1,2,3,4]
Explanation: This array has all its adjacent pairs in adjacentPairs.
Notice that adjacentPairs[i] may not be in left-to-right order.
```

**Example 2:**
```
Input: adjacentPairs = [[4,-2],[1,4],[-3,1]]
Output: [-2,4,1,-3]
Explanation: There can be negative numbers.
Another solution is [-3,1,4,-2], which would also be accepted.
```

**Example 3:**
```
Input: adjacentPairs = [[100000,-100000]]
Output: [100000,-100000]
```

**Constraints:**

* `nums.length == n`
* `adjacentPairs.length == n - 1`
* `adjacentPairs[i].length == 2`
* `2 <= n <= 105`
* `-105 <= nums[i], ui, vi <= 105`
* There exists some `nums` that has `adjacentPairs` as its pairs.

# Submissions
---
**Solution 1: (Graph)**
```
Runtime: 1112 ms
Memory Usage: 63.1 MB
```
```python
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj, ans, n = defaultdict(list), [], len(adjacentPairs) + 1
        for a, b in adjacentPairs:
            adj[a] += [b]
            adj[b] += [a]
        prev = cur = -math.inf
        for k, v in adj.items():
            if len(v) == 1:
                cur = k
                break
        ans += [cur]   
        while len(ans) < n:
            for v in adj.pop(cur):
                if v != prev:
                    ans += [v]
                    prev = cur
                    cur = v
                    break
        return ans
```

**Solution 2: (DFS)**
```
Runtime: 298 ms
Memory: 141.1 MB
```
```c++
class Solution {
    unordered_map<int, vector<int>> graph;
    void dfs(int node, int prev, vector<int>& ans) {
        ans.push_back(node);
        for (int neighbor : graph[node]) {
            if (neighbor != prev) {
                dfs(neighbor, node, ans);
            }
        }
    }
public:
    vector<int> restoreArray(vector<vector<int>>& adjacentPairs) {
        for (auto& edge : adjacentPairs) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }
        
        int root = 0;
        for (auto& pair : graph) {
            if (pair.second.size() == 1) {
                root = pair.first;
                break;
            }
        }
        
        vector<int> ans;
        dfs(root, INT_MAX, ans);
        return ans;
    }
};
```

**Solution 3: (Iterative, Follow the Path)**
```
Runtime: 290 ms
Memory: 105.7 MB
```
```c++
class Solution {
public:
    vector<int> restoreArray(vector<vector<int>>& adjacentPairs) {
        unordered_map<int, vector<int>> graph;

        for (auto& edge : adjacentPairs) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }
        
        int root = 0;
        for (auto& pair : graph) {
            if (pair.second.size() == 1) {
                root = pair.first;
                break;
            }
        }
        
        int curr = root;
        vector<int> ans = {root};
        int prev = INT_MAX;
        
        while (ans.size() < graph.size()) {
            for (int neighbor : graph[curr]) {
                if (neighbor != prev) {
                    ans.push_back(neighbor);
                    prev = curr;
                    curr = neighbor;
                    break;
                }
            }
        }

        return ans;
    }
};
```
