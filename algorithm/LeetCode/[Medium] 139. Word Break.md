139. Word Break

Given a **non-empty** string `s` and a dictionary `wordDict` containing a list of **non-empty** words, determine if `s` can be segmented into a space-separated sequence of one or more dictionary words.

**Note:**

* The same word in the dictionary may be reused multiple times in the segmentation.
* You may assume the dictionary does not contain duplicate words.

**Example 1:**
```
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
```

**Example 2:**
```
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
```

**Example 3:**
```
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
```
# Submissions
---
**Solution 1: (DP Bottom-Up)**
```
Runtime: 40 ms
Memory Usage: 13 MB
```
```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        dp = [False] * N    
        for i in range(N):
            for w in wordDict:
                w_size = len(w)
                if w == s[i - w_size + 1:i + 1] and (dp[i - w_size] or i - w_size == -1):
                    dp[i] = True
        return dp[-1]
```

**Solution 2: (DP Top-Down)**
```
Runtime: 32 ms
Memory Usage: 13.3 MB
```
```python
import functools
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        
        @functools.lru_cache(None)
        def dfs(i):
            if i == N:
                return True
            rst = False
            for w in wordDict:
                w_size = len(w)
                if i + w_size <= N and s[i:i + w_size] == w:
                    rst = rst | dfs(i + w_size)
            return rst
        
        return dfs(0)
        

```