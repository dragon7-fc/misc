472. Concatenated Words

Given a list of words (**without duplicates**), please write a program that returns all concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

**Example:**
```
Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
 "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
```

**Note:**

* The number of elements of the given array will not exceed `10,000`
* The length sum of elements in the given array will not exceed `600,000`.
* All the input string will only include lower case letters.
* The returned elements order does not matter.

# Submissions
---
**Solution 1: (Set, DFS)**
```
Runtime: 344 ms
Memory Usage: 29.2 MB
```
```python
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        s = set(words)
        ans = []
        
        def dfs(w, cnt):
            if not w:
                if cnt <= 1:
                    return False
                else:
                    return True
            elif w in s and cnt >= 1:
                return True
            for i in range(1, len(w)):
                if w[:i] in s and dfs(w[i:], cnt+1):
                    return True
            return False
            
        for word in words:
            if dfs(word, 0):
                ans.append(word)
        
        return ans
```

**Solution 2: (Trie, DFS)**
```
Runtime: 904 ms
Memory Usage: 37.4 MB
```
```python
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            t = trie
            for c in word:
                t = t.setdefault(c, {})
            t['#'] = {}
        ans = []

        def dfs(w, cnt):
            if not w:
                if cnt <= 1:
                    return False
                else:
                    return True
            t = trie
            for i, c in enumerate(w):
                if c in t:
                    t = t[c]
                    if '#' in t:
                        if dfs(w[i+1:], cnt+1):
                            return True
                else:
                    break
            return False      

        for word in words:
            if dfs(word, 0):
                ans.append(word)
            
        return ans
```