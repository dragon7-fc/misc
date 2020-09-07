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
**Solution 1: (Two Hash Maps)**
```
Runtime: 32 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        map_char = {}
        map_word = {}
        
        words = str.split(' ')
        if len(words) != len(pattern):
            return False
        
        for c, w in zip(pattern, words):
            if c not in map_char:
                if w in map_word:
                    return False
                else:
                    map_char[c] = w
                    map_word[w] = c
            else:
                if map_char[c] != w:
                    return False
        return True
```

**Solution 2: (Single Index Hash Map)**
```
Runtime: 32 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        map_index = {}
        words = str.split()
        
        if len(pattern) != len(words):
            return False
        
        for i in range(len(words)):
            c = pattern[i]
            w = words[i]

            char_key = 'char_{}'.format(c)
            char_word = 'word_{}'.format(w)
            
            if char_key not in map_index:
                map_index[char_key] = i
            
            if char_word not in map_index:
                map_index[char_word] = i 
            
            if map_index[char_key] != map_index[char_word]:
                return False
        
        return True
```

**Solution 3: (Hash Table)**
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