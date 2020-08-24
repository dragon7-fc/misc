1055. Shortest Way to Form String

From any string, we can form a subsequence of that string by deleting some number of characters (possibly no deletions).

Given two strings `source` and `target`, return the minimum number of subsequences of `source` such that their concatenation equals target. If the task is impossible, return `-1`.

 

**Example 1:**
```
Input: source = "abc", target = "abcbc"
Output: 2
Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".
```

**Example 2:**
```
Input: source = "abc", target = "acdbc"
Output: -1
Explanation: The target string cannot be constructed from the subsequences of source string due to the character "d" in target string.
```

**Example 3:**
```
Input: source = "xyz", target = "xzyxz"
Output: 3
Explanation: The target string can be constructed as follows "xz" + "y" + "xz".
```

**Constraints:**

* Both the `source` and `target` strings consist of only lowercase English letters from `"a"-"z"`.
* The lengths of `source` and `target` string are between `1` and `1000`.

# Submissions
---
**Solution 1: (Greedy)**
```
Runtime: 32 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        i, j = 0, 0
        count = 1
        while j < len(target):
            i = source.find(target[j], i)
            if i == -1:
                i = source.find(target[j])
                if i == -1:
                    return -1
                count += 1
            i += 1
            j += 1
        return count
```

**Solution 2: (Greedy. Binary Search, Hash Table)**
```
Runtime: 32 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        h = collections.defaultdict(list)
        for i, ch in enumerate(source):
            h[ch].append(i)        
        i, j = -1, 0
        count = 1
        while j < len(target):
            if target[j] not in h:
                return -1
            idx = bisect.bisect(h[target[j]], i) 
            if idx == len(h[target[j]]):
                i = -1
                count += 1
                continue
            i = h[target[j]][idx]
            j += 1
        return count
```