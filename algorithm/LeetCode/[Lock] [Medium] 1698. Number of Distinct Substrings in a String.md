1698. Number of Distinct Substrings in a String

Given a string `s`, return the number of **distinct** substrings of `s`.

A **substring** of a string is obtained by deleting any number of characters (possibly zero) from the front of the string and any number (possibly zero) from the back of the string.

 

**Example 1:**
```
Input: s = "aabbaba"
Output: 21
Explanation: The set of distinct strings is ["a","b","aa","bb","ab","ba","aab","abb","bab","bba","aba","aabb","abba","bbab","baba","aabba","abbab","bbaba","aabbab","abbaba","aabbaba"]
```

**Example 2:**
```
Input: s = "abcdefg"
Output: 28
```

**Constraints:**

* `1 <= s.length <= 500`
* `s` consists of lowercase English letters.

# Submissions
---
**Solution 1: (combinations)**
```
Runtime: 1456 ms
Memory Usage: 57.9 MB
```
```python
class Solution:
    def countDistinct(self, s: str) -> int:
        res=list(combinations(range(len(s) + 1), r = 2))
        subs=set()
        for r in res:
            subs.add(s[r[0]:r[1]])
        return(len(subs))
```
