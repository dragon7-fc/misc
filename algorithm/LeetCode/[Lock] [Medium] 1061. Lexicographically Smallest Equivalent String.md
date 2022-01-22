1061. Lexicographically Smallest Equivalent String

You are given two strings of the same length `s1` and `s2` and a string `baseStr`.

We say `s1[i]` and `s2[i]` are equivalent characters.

* For example, if `s1 = "abc"` and `s2 = "cde"`, then we have `'a'` == `'c'`, `'b'` == `'d'`, and `'c'` == `'e'`.
Equivalent characters follow the usual rules of any equivalence relation:

* **Reflexivity**: `'a'` == `'a'`.
* **Symmetry**: `'a'` == `'b'` implies `'b'` == `'a'`.
* **Transitivity**: `'a'` == `'b'` and `'b'` == `'c'` implies `'a'` == `'c'`.

For example, given the equivalency information from `s1 = "abc"` and `s2 = "cde"`, `"acd"` and `"aab"` are equivalent strings of `baseStr = "eed"`, and `"aab"` is the lexicographically smallest equivalent string of `baseStr`.

Return the lexicographically smallest equivalent string of `baseStr` by using the equivalency information from `s1` and `s2`.

 

**Example 1:**
```
Input: s1 = "parker", s2 = "morris", baseStr = "parser"
Output: "makkek"
Explanation: Based on the equivalency information in s1 and s2, we can group their characters as [m,p], [a,o], [k,r,s], [e,i].
The characters in each group are equivalent and sorted in lexicographical order.
So the answer is "makkek".
```

**Example 2:**
```
Input: s1 = "hello", s2 = "world", baseStr = "hold"
Output: "hdld"
Explanation: Based on the equivalency information in s1 and s2, we can group their characters as [h,w], [d,e,o], [l,r].
So only the second letter 'o' in baseStr is changed to 'd', the answer is "hdld".
```

**Example 3:**
```
Input: s1 = "leetcode", s2 = "programs", baseStr = "sourcecode"
Output: "aauaaaaada"
Explanation: We group the equivalent characters in s1 and s2 as [a,o,e,r,s,c], [l,p], [g,t] and [d,m], thus all letters in baseStr except 'u' and 'd' are transformed to 'a', the answer is "aauaaaaada".
```

**Constraints:**

* `1 <= s1.length, s2.length, baseStr <= 1000`
* `s1.length == s2.length`
* `s1`, `s2`, and `baseStr` consist of lowercase English letters.

# Submissions
---
**Solution 1: (Union Find)**
```
Runtime: 67 ms
Memory Usage: 14.4 MB
```
```python
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        # Use a rank array to record the height of each vertex, i.e., the "rank" of each vertex.
        # The initial "rank" of each vertex is 1, because each of them is
        # a standalone vertex with no connection to other vertices.
        self.rank = [1] * size
        
    # The find function here is the same as that in the disjoint set with path compression.
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    # The union function with union by rank
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            
    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind(26)
        for i in range(len(s1)):
            uf.union(ord(s1[i])-ord('a'), ord(s2[i])-ord('a'))
        
        res = ""
        
        indexes = defaultdict(list)
        for i in range(len(uf.root)):
            if not indexes[uf.root[i]]:    
                indexes[uf.root[i]].append(i)
            
        for base in baseStr:
            root = uf.find(ord(base)-ord('a'))
            t = indexes[root]
            res += chr(t[0] + ord('a'))
            
        return res
```
