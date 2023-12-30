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
Runtime: 45 ms
Memory: 14 MB
```
```python
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = [i for i in range(26)]
            
        def union(x, y):
            px, py = find(x), find(y)
            if px < py:
                parent[py] = px
            else:
                parent[px] = py
        
        def find(x):
            if parent[x] == x:
                return x
            return find(parent[x])

        for a, b in zip(s1, s2):
            union(ord(a) - ord('a'), ord(b) - ord('a'))
        return ''.join([chr(find(ord(c) - ord('a')) + ord('a')) for c in baseStr])
```

**Solution2: (DFS)**
```
Runtime: 35 ms
Memory: 14.2 MB
```
```python
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        g = collections.defaultdict(list)
        for c1, c2 in zip(list(s1), list(s2)):
            g[c1] += [c2]
            g[c2] += [c1]
        d = {}

        def dfs(c, p):
            p.add(c)
            for nc in g[c]:
                if not nc in p:
                    dfs(nc, p)
            return p

        for c in g:
            if not c in d:
                group = dfs(c, set())
                d.update({x: group for x in group})
        ans = ''
        for c in baseStr:
            ans += min(d[c]) if c in d else c

        return ans
```
