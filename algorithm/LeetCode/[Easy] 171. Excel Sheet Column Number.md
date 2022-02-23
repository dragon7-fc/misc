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
**Solution 1: (Right to Left)**
```
Runtime: 36 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        
        # Decimal 65 in ASCII corresponds to char 'A'
        alpha_map = {chr(i + 65): i + 1 for i in range(26)}

        n = len(s)
        for i in range(n):
            cur_char = s[n - 1 - i]
            result += (alpha_map[cur_char] * (26 ** i))
        return result
```

**Solution 2: (Left to Right)**
```
Runtime: 28 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        
        result = 0
        n = len(s)
        for i in range(n):
            result = result * 26
            result += (ord(s[i]) - ord('A') + 1)
        return result
```

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

**Solution 2: (Math)**
```
Runtime: 4 ms
Memory Usage: 5.9 MB
```
```c++
class Solution {
public:
    int titleToNumber(string columnTitle) {
        int ans = 0;
        for (auto &c: columnTitle) {
            ans *= 26;
            ans += (c-'A')+1;
        }
        return ans;
    }
};
```
