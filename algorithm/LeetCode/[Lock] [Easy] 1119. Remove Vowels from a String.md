1119. Remove Vowels from a String

Given a string `S`, remove the vowels `'a'`, `'e'`, `'i'`, `'o'`, and `'u'` from it, and return the new string.

 

**Example 1:**
```
Input: "leetcodeisacommunityforcoders"
Output: "ltcdscmmntyfrcdrs"
```

**Example 2:**
```
Input: "aeiou"
Output: ""
```

**Note:**

* `S` consists of lowercase English letters only.
* `1 <= S.length <= 1000`

# Submissions
---
**Solution 1: (String)**
```
Runtime: 44 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def removeVowels(self, S: str) -> str:
        return ''.join([c for c in S if c not in 'aeiou'])
```