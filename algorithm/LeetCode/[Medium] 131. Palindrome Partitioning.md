131. Palindrome Partitioning

Given a string `s`, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of `s`.

**Example:**
```
Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
```

**Solution 1: (Backtracking)**
```
Runtime: 80 ms
Memory Usage: 13 MB
```
```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:    
        def backtrack(s, candidate):
            if not s: res.append(candidate[:]); return
            for i in range(1, len(s)+1):
                #equal to s[:i] == s[:i][::-1]
                if s[:i] == s[i-1::-1]:
                    candidate.append(s[:i])
                    backtrack(s[i:], candidate)
                    candidate.pop()
        res = []
        backtrack(s, [])
        
        return res
```