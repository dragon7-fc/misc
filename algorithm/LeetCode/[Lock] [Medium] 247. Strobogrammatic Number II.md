247. Strobogrammatic Number II

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

**Example:**
```
Input:  n = 2
Output: ["11","69","88","96"]
```

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 176 ms
Memory Usage: 21.5 MB
```
```python
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        one = {
            '0': '0',
            '1': '1',
            '8': '8'
        }
        two = {
            '6': '9',
            '9': '6'
        }
        ans = []
        
        def dfs(i, p):
            if i == n//2:
                if n%2:
                    for k in one:
                        p[i] = one[k]
                        ans.append(''.join(p))
                else:
                    ans.append(''.join(p))
                return
            for k in one:
                if i == 0 and k == '0':
                    continue
                p[i] = k
                p[n-1-i] = one[k]
                dfs(i+1, p)
            for k in two:
                p[i] = k
                p[n-1-i] = two[k]
                dfs(i+1, p)
            
        
        dfs(0, [' ']*n)
        return ans
```