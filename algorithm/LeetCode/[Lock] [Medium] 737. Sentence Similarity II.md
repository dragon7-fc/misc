737. Sentence Similarity II

We can represent a sentence as an array of words, for example, the sentence `"I am happy with leetcode"` can be represented as `arr = ["I","am",happy","with","leetcode"]`.

Given two sentences `sentence1` and `sentence2` each represented as a string array and given an array of string pairs `similarPairs` where `similarPairs[i] = [xi, yi]` indicates that the two words `xi` and `yi` are similar.

Return `true` if `sentence1` and `sentence2` are similar, or `false` if they are not similar.

Two sentences are similar if:

* They have **the same length** (i.e., the same number of words)
* `sentence1[i]` and `sentence2[i]` are similar.

Notice that a word is always similar to itself, also notice that the similarity relation is transitive. For example, if the words `a` and `b` are similar, and the words `b` and `c` are similar, then `a` and `c` are similar.

 

**Example 1:**
```
Input: sentence1 = ["great","acting","skills"], sentence2 = ["fine","drama","talent"], similarPairs = [["great","good"],["fine","good"],["drama","acting"],["skills","talent"]]
Output: true
Explanation: The two sentences have the same length and each word i of sentence1 is also similar to the corresponding word in sentence2.
```

**Example 2:**
```
Input: sentence1 = ["I","love","leetcode"], sentence2 = ["I","love","onepiece"], similarPairs = [["manga","onepiece"],["platform","anime"],["leetcode","platform"],["anime","manga"]]
Output: true
Explanation: "leetcode" --> "platform" --> "anime" --> "manga" --> "onepiece".
Since "leetcode is similar to "onepiece" and the first two words are the same, the two sentences are similar.
```

**Example 3:**
```
Input: sentence1 = ["I","love","leetcode"], sentence2 = ["I","love","onepiece"], similarPairs = [["manga","hunterXhunter"],["platform","anime"],["leetcode","platform"],["anime","manga"]]
Output: false
Explanation: "leetcode" is not similar to "onepiece".
```

**Constraints:**

* `1 <= sentence1.length, sentence2.length <= 1000`
* `1 <= sentence1[i].length, sentence2[i].length <= 20`
* `sentence1[i]` and `sentence2[i]` consist of lower-case and upper-case English letters.
* `0 <= similarPairs.length <= 2000`
* `similarPairs[i].length == 2`
* `1 <= xi.length, yi.length <= 20`
* `xi` and `yi` consist of English letters.

# Submissions
---
**Solution 1: (Depth-First Search)**
```
Runtime: 638 ms
Memory Usage: 15.8 MB
```
```python
class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2): return False
        graph = collections.defaultdict(list)
        for w1, w2 in similarPairs:
            graph[w1].append(w2)
            graph[w2].append(w1)

        for w1, w2 in zip(sentence1, sentence2):
            stack, seen = [w1], {w1}
            while stack:
                word = stack.pop()
                if word == w2: break
                for nei in graph[word]:
                    if nei not in seen:
                        seen.add(nei)
                        stack.append(nei)
            else:
                return False
        return True
```

**Solution 2: (Union-Find)**
```
Runtime: 591 ms
Memory Usage: 16 MB
```
```python
class DSU:
    def __init__(self, N):
        self.par = list(range(N))
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    def union(self, x, y):
        self.par[self.find(x)] = self.find(y)

class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2): return False

        index = {}
        count = itertools.count()
        dsu = DSU(2 * len(similarPairs))
        for pair in similarPairs:
            for p in pair:
                if p not in index:
                    index[p] = next(count)
            dsu.union(index[pair[0]], index[pair[1]])

        return all(w1 == w2 or
                   w1 in index and w2 in index and
                   dsu.find(index[w1]) == dsu.find(index[w2])
                   for w1, w2 in zip(sentence1, sentence2))
```
**Solution 3: (DFS, O(n*k*m))**
```
Runtime: 317 ms
Memory: 110.38 MB
```
```c++
class Solution {
    // Returns true if there is a path from source to dest.
    bool dfs(string& source, unordered_set<string>& visit,
             unordered_map<string, unordered_set<string>>& adj, string& dest) {
        visit.insert(source);
        if (source == dest) {
            return true;
        }
        for (auto neighbor : adj[source]) {
            if (!visit.count(neighbor) && dfs(neighbor, visit, adj, dest)) {
                return true;
            }
        }
        return false;
    }
public:
    bool areSentencesSimilarTwo(vector<string>& sentence1, vector<string>& sentence2, vector<vector<string>>& similarPairs) {
        if (sentence1.size() != sentence2.size()) {
            return false;
        }
        // Create the graph using each pair in similarPairs.
        unordered_map<string, unordered_set<string>> adj;
        for (auto& pair : similarPairs) {
            adj[pair[0]].insert(pair[1]);
            adj[pair[1]].insert(pair[0]);
        }
        // The number of nodes in the graph.
        int nodesCount = adj.size();
        for (int i = 0; i < sentence1.size(); i++) {
            if (sentence1[i] == sentence2[i]) {
                continue;
            }
            unordered_set<string> visit;
            if (adj.count(sentence1[i]) && adj.count(sentence2[i]) &&
                dfs(sentence1[i], visit, adj, sentence2[i])) {
                continue;
            }
            return false;
        }
        return true;
    }
};
```

**Solution 4: (Union Find, O((n+k)*m))**
```
Runtime: 396 ms
Memory: 76.38 MB
```
```c++
class UnionFind {
private:
    map<string, string> parent;
    map<string, int> rank;

public:
    void addWord(string x) {
        if (!parent.count(x)) {
            parent[x] = x;
            rank[x] = 0;
        }
    }

    bool isWordPresent(string x) {
        if (parent.count(x)) {
            return true;
        }
        return false;
    }

    string find(string x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    void unionSet(string x, string y) {
        string xset = find(x), yset = find(y);
        if (xset == yset) {
            return;
        } else if (rank[xset] < rank[yset]) {
            parent[xset] = yset;
        } else if (rank[xset] > rank[yset]) {
            parent[yset] = xset;
        } else {
            parent[yset] = xset;
            rank[xset]++;
        }
    }
};

class Solution {
public:
    bool areSentencesSimilarTwo(vector<string>& sentence1, vector<string>& sentence2, vector<vector<string>>& similarPairs) {
        if (sentence1.size() != sentence2.size()) {
            return false;
        }

        UnionFind dsu;
        for (auto& pair : similarPairs) {
            // Create the graph using the hashed values of the similarPairs.
            dsu.addWord(pair[0]);
            dsu.addWord(pair[1]);
            dsu.unionSet(pair[0], pair[1]);
        }

        for (int i = 0; i < sentence1.size(); i++) {
            if (sentence1[i] == sentence2[i]) {
                continue;
            }
            if (dsu.isWordPresent(sentence1[i]) && dsu.isWordPresent(sentence2[i]) &&
                dsu.find(sentence1[i]) == dsu.find(sentence2[i])) {
                continue;
            }
            return false;
        }
        return true;
    }
};
```

**Solution 5: (Union Find)**
```
Runtime: 79 ms, Beats 67.33%
Memory: 70.34 MB, Beats 65.35%
```
```c++
class Solution {
    unordered_map<string, string> p;
    unordered_map<string, int> r;
    void add(string &x) {
        if (!p.count(x)) {
            p[x] = x;
            r[x] = 0;
        }
    }
    string find(string &x) {
        if (p[x] != x) {
            p[x] = find(p[x]);
        }
        return p[x];
    }
    void uni(string &x, string &y) {
        string &&xr = find(x), &&yr = find(y);
        if (xr == yr) {
            return;
        } else if (r[xr] < r[yr]) {
            p[xr] = yr;
        } else if (r[xr] > r[yr]) {
            p[yr] = xr;
        } else {
            p[yr] = xr;
            r[xr] += 1;
        }
    }
public:
    bool areSentencesSimilarTwo(vector<string>& sentence1, vector<string>& sentence2, vector<vector<string>>& similarPairs) {
        if (sentence1.size() != sentence2.size()) {
            return false;
        }
        for (auto &pair: similarPairs) {
            // Create the graph using the hashed values of the similarPairs.
            add(pair[0]);
            add(pair[1]);
            uni(pair[0], pair[1]);
        }

        for (int i = 0; i < sentence1.size(); i++) {
            if (sentence1[i] == sentence2[i]) {
                continue;
            }
            if (p.count(sentence1[i]) && p.count(sentence2[i]) &&
                find(sentence1[i]) == find(sentence2[i])) {
                continue;
            }
            return false;
        }
        return true;
    }
};
```
