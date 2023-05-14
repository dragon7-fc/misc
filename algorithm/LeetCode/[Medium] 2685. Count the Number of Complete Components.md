2685. Count the Number of Complete Components

You are given an integer `n`. There is an **undirected** graph with `n` vertices, numbered from `0` to `n - 1`. You are given a 2D integer array `edges` where `edges[i] = [ai, bi]` denotes that there exists an **undirected edge** connecting vertices `ai` and `bi`.

Return the number of **complete connected components** of the graph.

A **connected component** is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.

A connected component is said to be **complete** if there exists an edge between every pair of its vertices.

 

**Example 1:**

![2685_screenshot-from-2023-04-11-23-31-23.png](img/2685_screenshot-from-2023-04-11-23-31-23.png)
```
Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]
Output: 3
Explanation: From the picture above, one can see that all of the components of this graph are complete.
```

**Example 2:**

![2685_screenshot-from-2023-04-11-23-32-00.png](img/2685_screenshot-from-2023-04-11-23-32-00.png)
```
Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
Output: 1
Explanation: The component containing vertices 0, 1, and 2 is complete since there is an edge between every pair of two vertices. On the other hand, the component containing vertices 3, 4, and 5 is not complete since there is no edge between vertices 4 and 5. Thus, the number of complete components in this graph is 1.
```

**Constraints:**

* `1 <= n <= 50`
* `0 <= edges.length <= n * (n - 1) / 2`
* `edges[i].length == 2`
* `0 <= ai, bi <= n - 1`
* `ai != bi`
* There are no repeated edges.

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 863 ms
Memory: 18.2 MB
```
```python
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        g = collections.defaultdict(list)
        for u, v in edges:
            g[u] += [v]
            g[v] += [u]
        seen = [0]*n
        seen_edge = [[0]*n for _ in range(n)]
        
        def dfs(v):
            vs = es = 0
            if seen[v] == 0:
                vs += 1
                seen[v] = 1
            for nv in g[v]:
                if seen_edge[v][nv] == 0:
                    seen_edge[v][nv] = 1
                    seen_edge[nv][v] = 1
                    es += 1
                    nvs, nes = dfs(nv)
                    vs += nvs
                    es += nes
            return [vs, es] 
            
        ans = 0
        for i in range(n):
            if seen[i] == 0:
                vs, es = dfs(i)
                if es == vs*(vs-1)//2:
                    ans += 1
        return ans
```

**Solution 2: (Union-Find)**
```
Runtime: 228 ms
Memory: 112 MB
```
```c++
class DSU {
private:
    vector<int> p, rank, count;
public:
    DSU(int n) {
        p.resize(n), rank.resize(n), count.resize(n, 1);
        for (int i = 0; i < n; ++i) p[i] = i;
    }
    int find(int x) {
        if (x != p[x]) p[x] = find(p[x]);
        return p[x];
    }
    void union_set(int x, int y) {
        int xx = find(x), yy = find(y);
        if (xx == yy) return;
        count[xx] = count[yy] = count[xx] + count[yy];
        if (rank[xx] < rank[yy]) p[xx] = yy;
        else p[yy] = xx;
        if (rank[xx] == rank[yy]) ++rank[xx];
    }
    int sizeOfGroupThatXIsAPartOf(int x) {
        return count[find(x)];
    }
};

class Solution {
public:
    int countCompleteComponents(int n, vector<vector<int>>& edges) {
        DSU uf(n);
        set<int> groups;
        vector<int> counter(n, 0);
        for (auto& e : edges) {
            uf.union_set(e[0], e[1]);
            ++counter[e[0]], ++counter[e[1]];
        }
        
        for (int i = 0; i < n; ++i)
            groups.insert(uf.find(i));

        for (int i = 0; i < n; ++i) {
            int f = uf.find(i);
            if (!groups.count(f)) continue;
            if (uf.sizeOfGroupThatXIsAPartOf(i) != counter[i] + 1) 
                groups.erase(f);
        }
        return groups.size();
    }
};
```
