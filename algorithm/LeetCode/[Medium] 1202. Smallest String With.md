1202. Smallest String With

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
**Solution 1:**
```
Runtime: 852 ms
Memory Usage: 76 MB
```
```python
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        dic = self.create_graph(pairs)
        self.graph = collections.defaultdict(list)
        self.dfs_wrapper(len(s), dic)
        ans = [''] * len(s)
        visited = set()
        for i in range(len(s)):
            if i in self.graph and i not in visited:
                index_lst = self.graph[i]
                element_lst = [s[j] for j in index_lst]
                index_lst.sort()
                element_lst.sort(reverse=True)
                for index in index_lst:
                    visited.add(index)
                    ans[index] = element_lst.pop()
        return ''.join(ans)


    def create_graph(self, pairs):
        dic = collections.defaultdict(list)
        for p in pairs:
            dic[p[0]].append(p[1])
            dic[p[1]].append(p[0])
        return dic

    def dfs_wrapper(self, n, dic):
        visited = set()
        for i in range(n):
            if i not in visited:
                lst = []
                res = self.dfs(i, visited, dic, lst)
                self.graph[i] = res

    def dfs(self, index, visited, dic, lst):
        visited.add(index)
        lst.append(index)
        for post in dic[index]:
            if post not in visited:
                self.dfs(post, visited, dic, lst)
        return lst
```