290. Word Pattern

Given a `pattern` and a string `str`, find if `str` follows the same `pattern`.

Here follow means a full match, such that there is a bijection between a letter in `pattern` and a non-empty word in `str`.

**Example 1:**
```
Input: pattern = "abba", str = "dog cat cat dog"
Output: true
```

**Example 2:**
```
Input:pattern = "abba", str = "dog cat cat fish"
Output: false
```

**Example 3:**
```
Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
```

**Example 4:**
```
Input: pattern = "abba", str = "dog dog dog dog"
Output: false
```

**Notes:**

* You may assume pattern contains only lowercase letters, and `str` contains lowercase letters that may be separated by a single space.

# Submissions
---
**Solution 1:**
```
Runtime: 16 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        d = {}
        word = str.split()
        if len(word) != len(pattern): return False
        for i in range(len(pattern)):
            if not d.get(pattern[i], None):
                if word[i] in d.values():
                    return False
                d[pattern[i]] = word[i]
            else:
                if d[pattern[i]] != word[i]:
                    return False
        return True
```