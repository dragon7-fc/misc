839. Similar String Groups

Two strings `X` and `Y` are similar if we can swap two letters (in different positions) of `X`, so that it equals `Y`. Also two strings `X` and `Y` are similar if they are equal.

For example, `"tars"` and `"rats"` are similar (swapping at positions `0` and `2`), and `"rats"` and `"arts"` are similar, but `"star"` is not similar to `"tars"`, `"rats"`, or `"arts"`.

Together, these form two connected groups by similarity: `{"tars", "rats", "arts"}` and `{"star"}`.  Notice that `"tars"` and `"arts"` are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

We are given a list `A` of strings.  Every string in `A` is an anagram of every other string in `A`.  How many groups are there?

 

**Example 1:**
```
Input: A = ["tars","rats","arts","star"]
Output: 2
```

**Constraints:**

* `1 <= A.length <= 2000`
* `1 <= A[i].length <= 1000`
* `A.length * A[i].length <= 20000`
* All words in `A` consist of lowercase letters only.
* All words in `A` have the same length and are anagrams of each other.
* The judging time limit has been increased for this question.

# Solution
---
## Approach #1: Piecewise [Accepted]
**Intuition**

Let `W = A[0].length`. It is clear that we can determine in O(W)O(W) time, whether two words from `A` are similar.

One attempt is a standard kind of brute force: for each pair of words, let's draw an edge between these words if they are similar. We can do this in $O(N^2 W)$ time. After, finding the connected components can be done in $O(N^2)$ time naively (each node may have up to $N-1$ edges), (or $O(N)$ with a union-find structure.) The total complexity is $O(N^2 W)$.

Another attempt is to enumerate all neighbors of a word. A word has up to $\binom{W}{2}$ neighbors, and if that neighbor is itself a given word, we know that word and neighbor are connected by an edge. In this way, we can build the graph in $O(N W^3)$ time, and again take $O(N^2)$ or $O(N)$ time to analyze the number of connected components.

One insight is that between these two approaches, we can choose which approach works better. If we have very few words, we want to use the first approach; if we have very short words, we want to use the second approach. We'll piecewise add these two approaches (with complexity $O(N^2 W)$ and $O(N W^3)$, to create an approach with $O(NW\min(N, W^2))$ complexity.

**Algorithm**

We will build some underlying graph with `N` nodes, where nodes `i` and `j` are connected if and only if `A[i]` is similar to `A[j]`, then look at the number of connected components.

There are a few challenges involved in this problem, but each challenge is relatively straightforward.

* Use a helper function `similar(word1, word2)` that is `true` if and only if two given words are similar.

* Enumerate all neighbors of a word, and discover when it is equal to a given word.

* Use either a union-find structure or a depth-first search, to calculate the number of connected components of the underlying graph. We've showcased a union-find structure in this solution, with notes of a depth-first search in the comments.

For more details, see the implementations below.

```python
class DSU:
    def __init__(self, N):
        self.par = range(N)
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    def union(self, x, y):
        self.par[self.find(x)] = self.find(y)

class Solution(object): # (NW) * min(N, W*W) complexity
    def numSimilarGroups(self, A):
        N, W = len(A), len(A[0])

        def similar(word1, word2):
            diff = 0
            for x, y in itertools.izip(word1, word2):
                if x != y:
                    diff += 1
            return diff <= 2

        dsu = DSU(N)

        if N < W*W: # If few words, then check for pairwise similarity: O(N^2 W)
            for (i1, word1), (i2, word2) in \
                    itertools.combinations(enumerate(A), 2):
                if similar(word1, word2):
                    dsu.union(i1, i2)

        else: # If short words, check all neighbors: O(N W^3)
            buckets = collections.defaultdict(set)
            for i, word in enumerate(A):
                L = list(word)
                for j0, j1 in itertools.combinations(xrange(W), 2):
                    L[j0], L[j1] = L[j1], L[j0]
                    buckets["".join(L)].add(i)
                    L[j0], L[j1] = L[j1], L[j0]

            for i1, word in enumerate(A):
                for i2 in buckets[word]:
                    dsu.union(i1, i2)

        return sum(dsu.par[x] == x for x in xrange(N))
```

**Complexity Analysis**

* Time Complexity: $O(NW \min(N, W^2))$, where $N$ is the length of `A`, and $W$ is the length of each given word.

* Space Complexity: $O(NW^3)$. If $N < W^2$, the space complexity is $O(N)$. Otherwise, the space complexity is $O(NW^3)$: for each of $NW^2$ neighbors we store a word of length $W$. (Plus, we store $O(NW^2)$ node indices ("buckets") which is dominated by the $O(NW^3)$ term.) Because $W^2 <= N$ in this case, we could also write the space complexity as $O(N^2 W)$.

# Submissions
---
**Solution 1: (Union Find)**
```
Runtime: 7252 ms
Memory Usage: 15.4 MB
```
```python
class Solution:
    def numSimilarGroups(self, A: List[str]) -> int:
        self.uf = {}
        def union(x, y):
            self.uf[find(y)] = self.uf[find(x)]
        def find(x):
            self.uf.setdefault(x, x)
            if x != self.uf[x]:
                self.uf[x] = find(self.uf[x])
            return self.uf[x]
        #***********trick to get it pass  ***************
        A.sort()
        valid_idx = []
        for i in range(len(A[0])):
            if A[-1][i] == A[0][i]: continue
            else:
                valid_idx += list(range(i, len(A[0])))
                break
        if not valid_idx: return 1
        #*************************************************
        for a, b in itertools.combinations(A, 2):
            dif = 0
            for k in valid_idx:
                if a[k] != b[k]:
                    dif += 1
                if dif > 2: break
            else:
                union(a, b)
        return len({find(a) for a in A})
```

**Solution 2: (DFS)**
```
Runtime: 4332 ms
Memory Usage: 19.8 MB
```
```python
class Solution:
    def numSimilarGroups(self, A: List[str]) -> int:
        def similar(w1, w2):
            return sum(w1[i] != w2[i] for i in range(len(w1))) <= 2
        
        def swap(word, i, j):
            return word[:i] + word[j] + word[i+1:j] + word[i] + word[j+1:]
        
        m, n = len(A[0]), len(A)
        words = set(A)
        visited = set()
        
        def dfs(word):
            visited.add(word)
            if m < n:
                for i in range(m):
                    for j in range(i + 1, m):
                        swapped = swap(word, i, j)
                        if swapped in words and swapped not in visited:
                            dfs(swapped)
            else:
                for word1 in A:
                    if word1 not in visited and similar(word, word1):
                        dfs(word1)

        res = 0
        for word in A:
            if word not in visited:
                dfs(word)
                res += 1
        return res
```

**Solution 3: (DFS)**
```
Runtime: 57 ms
Memory: 10.6 MB
```
```c++
class Solution {
    void dfs(int i, vector<string> &strs, vector<bool> &seen, vector<vector<bool>> &g) {
        seen[i] = true;
        for (int j = 0; j < strs.size(); j ++) {
            if (g[i][j] && !seen[j]) {
                dfs(j, strs, seen, g);
            }
        }
    }
public:
    int numSimilarGroups(vector<string>& strs) {
        int m = strs.size(), n = strs[0].size();
        vector<vector<bool>> g(m, vector<bool>(m));
        int diff;
        for (int i = 0; i < m; i ++) {
            for (int j = i+1; j < m; j ++) {
                diff = 0;
                for (int k = 0; k < n; k ++) {
                    diff += (strs[i][k] != strs[j][k] ? 1 : 0);
                    if (diff > 2) {
                        break;
                    }
                }
                if (diff <= 2) {
                    g[i][j] = true;
                    g[j][i] = true;
                }
            }
        }
        vector<bool> seen(m);
        int ans = 0;
        for (int i = 0; i < m; i ++) {
            if (!seen[i]) {
                dfs(i, strs, seen, g);
                ans += 1;
            }
        }
        return ans;
    }
};
```

**Solution 4: (Union Find)**
```
Runtime: 14 ms, Beats 78.57%
Memory: 14.19 MB, Beats 64.29%
```
```c++
class Solution {
    vector<int> p;
    int find(int x) {
        if (x != p[x]) {
            p[x] = find(p[x]);
        }
        return p[x];
    }
    void uni(int x, int y) {
        int rx = find(x), ry = find(y);
        p[rx] = ry;
    }
public:
    int numSimilarGroups(vector<string>& strs) {
        int m = strs.size(), n = strs[0].size(), i, j, k, diff;
        p.resize(m);
        for (i = 0; i < m; i ++) {
            p[i] = i;
        }
        for (i = 0; i < m; i ++) {
            for (j = i+1; j < m; j ++) {
                diff = 0;
                for (k = 0; k < n; k ++) {
                    diff += (strs[i][k] != strs[j][k] ? 1 : 0);
                    if (diff > 2) {
                        break;
                    }
                }
                if (diff <= 2) {
                    uni(i, j);
                }
            }
        }
        unordered_set<int> st;
        for (i = 0; i < m; i ++) {
            st.insert(find(i));
        }
        return st.size();
    }
};
```
