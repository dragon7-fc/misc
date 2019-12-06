383. Ransom Note

Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

**Note:**

You may assume that both strings contain only lowercase letters.
```
canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
```

# Submissions
---
**Solution 1:**
```
Runtime: 48 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomCounter = collections.Counter(ransomNote)
        magazineCounter = collections.Counter(magazine)
        magazineCounter.subtract(ransomCounter)
        return all([counts >=  0 for counts in magazineCounter.values()])
```