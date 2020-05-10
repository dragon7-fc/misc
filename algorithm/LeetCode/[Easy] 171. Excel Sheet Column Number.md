171. Excel Sheet Column Number

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:
```
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
```

**Example 1:**
```
Input: "A"
Output: 1
```

**Example 2:**
```
Input: "AB"
Output: 28
```

**Example 3:**
```
Input: "ZY"
Output: 701
```

# Submissions
---
**Solution 1: (Math)**
```
Runtime: 28 ms
Memory Usage: 12.6 MB
```
```python
class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        base = ord('A') - 1
        return sum((ord(v)-base)*26**i for i,v in enumerate(s[::-1]))
```