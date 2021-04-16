267. Palindrome Permutation II

Given a string `s`, return all the palindromic permutations (without duplicates) of it.

You may return the answer in **any order**. If `s` has no palindromic permutation, return an empty list.

 

**Example 1:**
```
Input: s = "aabb"
Output: ["abba","baab"]
```

**Example 2:**
```
Input: s = "abc"
Output: []
```

**Constraints:**

* `1 <= s.length <= 16`
* `s` consists of only lowercase English letters.

# Submissions
---
**Solution 1: (Backtracking)**
```
Runtime: 148 ms
Memory Usage: 23.6 MB
```
```python
class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        counter = Counter(s)
        
        # could extract as a separate method
        mid = [k for k,v in counter.items() if v % 2]
        
        if len(mid) > 1:
            return []
        
        mid = mid[0] if len(mid) > 0 else ""
        
        # half the string
        half = [k * (v//2) for k,v in counter.items()]
        half = "".join(half)
        
        res = set()
        def dfs(input_str, permutation):
            if len(input_str) == len(permutation):
                res.add(permutation + mid + permutation[::-1])
                return
            
            for i in range(len(input_str)):
                # pruning.  
                if visited[i] or (i > 0 and input_str[i] == input_str[i-1] and not visited[i-1]):
                    continue
                    
                visited[i] = True
                dfs(input_str, permutation+input_str[i])
                visited[i] = False
            
        visited = [False] * len(half)
        dfs(half, "")
        return res
```