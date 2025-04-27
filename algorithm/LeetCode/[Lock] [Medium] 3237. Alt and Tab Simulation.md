3237. Alt and Tab Simulation

There are n windows open numbered from `1` to `n`, we want to simulate using alt + tab to navigate between the windows.

You are given an array `windows` which contains the initial order of the windows (the first element is at the top and the last one is at the bottom).

You are also given an array `queries` where for each query, the window `queries[i]` is brought to the top.

Return the final state of the array `windows`.

 

**Example 1:**
```
Input: windows = [1,2,3], queries = [3,3,2]

Output: [2,3,1]

Explanation:

Here is the window array after each query:

Initial order: [1,2,3]
After the first query: [3,1,2]
After the second query: [3,1,2]
After the last query: [2,3,1]
```

**Example 2:**
```
Input: windows = [1,4,2,3], queries = [4,1,3]

Output: [3,1,4,2]

Explanation:

Here is the window array after each query:

Initial order: [1,4,2,3]
After the first query: [4,1,2,3]
After the second query: [1,4,2,3]
After the last query: [3,1,4,2]
```

**Constraints:**

* `1 <= n == windows.length <= 10^5`
* `windows` is a permutation of `[1, n]`.
* `1 <= queries.length <= 10^5`
* `1 <= queries[i] <= n`

# Submissions
---
**Solution 1: (Greedy)**

    windows = [1,4,2,3], queries = [4,1,3]
                 ^                      ^
               4 1 2 3
                 ^
               1 4 2 3
                     ^
               3 1 4 2

```
Runtime: 10 ms, Beats 71.43%
Memory: 213.63 MB, Beats 42.86%
```
```c++
class Solution {
public:
    vector<int> simulationResult(vector<int>& windows, vector<int>& queries) {
        int m = windows.size(), n = queries.size(), i;
        vector<int> visited(m+1), ans;
        for (i = n-1; i >= 0; i --) {
            if (!visited[queries[i]]) {
                visited[queries[i]] = 1;
                ans.push_back(queries[i]);
            }
        }
        for (i = 0; i < m; i ++) {
            if (!visited[windows[i]]) {
                ans.push_back(windows[i]);
            }
        }
        return ans;
    }
};
```
