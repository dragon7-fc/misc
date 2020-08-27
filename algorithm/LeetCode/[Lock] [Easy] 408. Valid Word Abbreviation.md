408. Valid Word Abbreviation

Given a **non-empty** string `s` and an abbreviation `abbr`, return whether the string matches with the given abbreviation.

A string such as `"word"` contains only the following valid abbreviations:
```
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
```
Notice that only the above abbreviations are valid abbreviations of the string `"word"`. Any other string is not a valid abbreviation of `"word"`.

**Note:**

Assume `s` contains only lowercase letters and abbr contains only lowercase letters and digits.

**Example 1:**
```
Given s = "internationalization", abbr = "i12iz4n":

Return true.
```

**Example 2:**
```
Given s = "apple", abbr = "a2e":

Return false.
```

# Submissions
---
**Solution 1: (Two Pointers)**
```
Runtime: 28 ms
Memory Usage: 13.7 MB
```
```python
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        M, N = len(word), len(abbr)
        i, j = 0, 0
        while i < M and j < N:
            if abbr[j].isdigit() and abbr[j] != '0':
                k = j+1
                while k < N and abbr[k].isdigit():
                    k += 1
                shift = int(abbr[j:k])
                i += shift
                if i >= M+1:
                    return False
                j = k
            elif word[i] == abbr[j]:
                i += 1
                j += 1
            else:
                return False
        if i < M or j < N:
            return False
        return True
        
```