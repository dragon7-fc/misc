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
**Solution 1: (String)**
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

**Solution 2: (Greedy)**
```
Runtime: 32 ms
Memory Usage: 14.2 MB
```
```python
class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = ''
        for c in s:
            if c.isalpha() and ord(c) < ord('a'):
                ans += chr(ord('a')+ord(c)-ord('A')) 
            else:
                ans += c
        return ans
```