205. Isomorphic Strings

Given two strings **s** and **t**, determine if they are isomorphic.

Two strings are isomorphic if the characters in **s** can be replaced to get **t**.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

**Example 1:**
```
Input: s = "egg", t = "add"
Output: true
```

**Example 2:**
```
Input: s = "foo", t = "bar"
Output: false
```

**Example 3:**
```
Input: s = "paper", t = "title"
Output: true
```

**Note:**

* You may assume both **s** and **t** have the same length.

# Submissions
---
**Solution 1:**
```
Runtime: 32 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        for i in range(len(s)):
            if not d.get(s[i], None):
                if t[i] in d.values():
                    return False
                d[s[i]] = t[i]
            else:
                if d[s[i]] != t[i]:
                    return False
        return True
```