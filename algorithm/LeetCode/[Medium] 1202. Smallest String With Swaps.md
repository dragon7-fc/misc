1202. Smallest String With Swaps

You are given a string `s`, and an array of `pairs` of indices in the string pairs where `pairs[i] = [a, b]` indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given `pairs` **any number of times**.

Return the lexicographically smallest string that `s` can be changed to after using the swaps.

 

**Example 1:**
```
Input: s = "dcab", pairs = [[0,3],[1,2]]
Output: "bacd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[1] and s[2], s = "bacd"
```

**Example 2:**
```
Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
Output: "abcd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[0] and s[2], s = "acbd"
Swap s[1] and s[2], s = "abcd"
```

**Example 3:**
```
Input: s = "cba", pairs = [[0,1],[1,2]]
Output: "abc"
Explaination: 
Swap s[0] and s[1], s = "bca"
Swap s[1] and s[2], s = "bac"
Swap s[0] and s[1], s = "abc"
```

**Constraints:**

* `1 <= s.length <= 10^5`
* `0 <= pairs.length <= 10^5`
* `0 <= pairs[i][0], pairs[i][1] < s.length`
* `s` only contains lower case English letters.

# Submissions
---
**Solution: (Depth-First Search (DFS))**
```
Runtime: 345 ms
Memory Usage: 73.1 MB
```
```c++
class Solution {
    // Maximum number of vertices
    static const int N = 100001;
    vector<int> adj[N];
    bool visited[N];
    
    void DFS(string& s, int vertex, vector<char>& characters, vector<int>& indices) {
        // Add the character and index to the list
        characters.push_back(s[vertex]);
        indices.push_back(vertex);
        
        visited[vertex] = true;
        
        // Traverse the adjacents
        for (int adjacent : adj[vertex]) {
            if (!visited[adjacent]) {
                DFS(s, adjacent, characters, indices);
            }
        }
    }
    
public:
    string smallestStringWithSwaps(string s, vector<vector<int>>& pairs) {
        // Build the adjacency list
        for (vector<int> edge : pairs) {
            int source = edge[0];
            int destination = edge[1];
            
            // Undirected edge
            adj[source].push_back(destination);
            adj[destination].push_back(source);
        }
        
        for (int vertex = 0; vertex < s.size(); vertex++) {
            // If not covered in the DFS yet
            if (!visited[vertex]) {
                vector<char> characters;
                vector<int> indices;
                
                DFS(s, vertex, characters, indices);
                // Sort the list of characters and indices
                sort(characters.begin(), characters.end());
                sort(indices.begin(), indices.end());

                // Store the sorted characters corresponding to the index
                for (int index = 0; index < characters.size(); index++) {
                    s[indices[index]] = characters[index];
                }
            }
        }
        
        return s;
    }
};
```

**Solution: (Disjoint Set Union (DSU))**
```
Runtime: 239 ms
Memory Usage: 57.1 MB
```
```c++
class UnionFind {
private:
    vector<int> root;
    vector<int> rank;
public:
    // Initialize the array root and rank
    // Each vertex is representative of itself with rank 1
    UnionFind(int sz) : root(sz), rank(sz) {
        for (int i = 0; i < sz; i++) {
            root[i] = i;
            rank[i] = 1;
        }
    }
    
    // Get the root of a vertex
    int find(int x) {
        if (x == root[x]) {
            return x;
        }
        return root[x] = find(root[x]);
    }

    // Perform the union of two components
    void unionSet(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            if (rank[rootX] >= rank[rootY]) {
                root[rootY] = rootX;
                rank[rootX] += rank[rootY];
            } else {
                root[rootX] = rootY;
                rank[rootY] += rank[rootX];
            }
        }
    }
};

class Solution {
public:
    string smallestStringWithSwaps(string s, vector<vector<int>>& pairs) {
        UnionFind uf(s.size());
        
        // Iterate over the edges
        for (vector<int> edge : pairs) {
            int source = edge[0];
            int destination = edge[1];
            
            // Perform the union of end points
            uf.unionSet(source, destination);
        }
        
        
        unordered_map<int, vector<int>> rootToComponent;
        // Group the vertices that are in the same component
        for (int vertex = 0; vertex < s.size(); vertex++) {
            int root = uf.find(vertex);
            // Add the vertices corresponding to the component root
            rootToComponent[root].push_back(vertex);
        }
        
        // String to store the answer
        string smallestString(s.length(), ' ');
        // Iterate over each component
        for (auto component : rootToComponent) {
            vector<int> indices = component.second;
            
            // Sort the characters in the group
            vector<char> characters;
            for (int index : indices) {
                characters.push_back(s[index]);
            }
            sort(characters.begin(), characters.end());
            
            // Store the sorted characters
            for (int index = 0; index < indices.size(); index++) {
                smallestString[indices[index]] = characters[index];
            }
        }
        
        return smallestString;
    }
};
```

**Solution 1: (DFS)**

* Search all swapable char and sort them

```
Runtime: 756 ms
Memory Usage: 75.5 MB
```
```python
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def dfs(i):
            visited.add(i)
            char.append(s[i])
            idx.append(i)
            for j in g[i]:
                if j not in visited:
                    dfs(j)

        if not pairs or not pairs[0]:
            return s
        
        S = list(s)
        visited = set()
        g = [[] for _ in range(len(s))]
        for i, j in pairs:
            g[i].append(j)
            g[j].append(i)
            
        for i in range(len(s)):
            if i not in visited:
                char = []
                idx = []
                dfs(i)
                char = sorted(char)
                idx = sorted(idx)
                for k in range(len(idx)):
                    S[idx[k]] = char[k]
        
        return ''.join(S)
```

**Solution 2: (Union Find)**
```
Runtime: 668 ms
Memory Usage: 49.1 MB
```
```python
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        p = list(range(len(s)))
        def find(u):
            if u == p[u]:
                return u
            return find(p[u])
        for u, v in pairs:
            pu = find(u)
            pv = find(v)
            if pu != pv:
                if pu > pv:
                    p[pu] = pv
                else:
                    p[pv] = pu      
        for i in range(len(p)): # need to redirect some child node to the grand parent
            if p[i] != p[p[i]]:
                p[i] = p[p[i]]    
        ans = list(s)
        d = collections.defaultdict(list)
        for i, v in enumerate(p):
            d[v].append(i)           
        for i in d.keys():
            if len(d[i]) <=1:
                continue
            ind = d[i] # find the index that has the same parent i
            s_sub = [s[j] for j in ind]
            s_sub.sort()
            k = 0
            for i in ind:
                ans[i] = s_sub[k]
                k += 1
        return ''.join(ans)
```
