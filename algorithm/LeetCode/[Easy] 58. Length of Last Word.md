58. Length of Last Word

Given a string s consists of upper/lower-case alphabets and empty space characters `' '`, return the length of last word in the string.

If the last word does not exist, return `0`.

**Note:** A word is defined as a character sequence consists of non-space characters only.

**Example:**
```
Input: "Hello World"
Output: 5
```

# Submissions
---
**Solution 1: (String)**
```
Runtime: 28 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        if words:
            return len(words[-1])
        else:
            return 0
```