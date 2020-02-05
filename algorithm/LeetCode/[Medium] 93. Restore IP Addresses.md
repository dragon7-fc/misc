93. Restore IP Addresses

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

**Example:**
```
Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
```

# Submissions
---
**Solution 1: (Backtracking)**
```
Runtime: 32 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        def backtrack(digits, ip):     
            if len(ip) >= 4:
                if len(digits) == 0:
                    ans.append('.'.join(ip))
                return
            for i in range(1, min(len(digits)+1, 4)):
                if int(digits[:i]) > 255 or int(digits[:i]) < 0 or (i > 1 and digits[0] == '0'):
                    continue 
                backtrack(digits[i:], ip + [digits[:i]])
                
        backtrack(s, [])
        return ans
```