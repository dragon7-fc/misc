709. To Lower Case

Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

 

**Example 1:**
```
Input: "Hello"
Output: "hello"
```

**Example 2:**
```
Input: "here"
Output: "here"
```

**Example 3:**
```
Input: "LOVELY"
Output: "lovely"
```

# Submissions
---
**Solution 1:**
```
Runtime: 28 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return str.lower()
```