168. Excel Sheet Column Title

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:
```
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
```

**Example 1:**
```
Input: 1
Output: "A"
```

**Example 2:**
```
Input: 28
Output: "AB"
```

**Example 3:**
```
Input: 701
Output: "ZY"
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
    def convertToTitle(self, n: int) -> str:
        ans = []
        while n > 0:
            n, r = divmod(n-1, 26)
            ans.insert(0, chr(ord('A')+r))
        return ''.join(ans)
```