1858. Longest Word With All Prefixes

Given an array of strings `words`, find the **longest** string in `words` such that **every prefix** of it is also in `words`.

    * For example, let `words = ["a", "app", "ap"]`. The string `"app"` has prefixes `"ap"` and `"a"`, all of which are in `words`.

Return the string described above. If there is more than one string with the same length, return the **lexicographically smallest** one, and if no string exists, return `""`.

 

**Example 1:**
```
Input: words = ["k","ki","kir","kira", "kiran"]
Output: "kiran"
Explanation: "kiran" has prefixes "kira", "kir", "ki", and "k", and all of them appear in words.
```

**Example 2:**
```
Input: words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation: Both "apple" and "apply" have all their prefixes in words.
However, "apple" is lexicographically smaller, so we return that.
```

**Example 3:**
```
Input: words = ["abc", "bc", "ab", "qwe"]
Output: ""
```

**Constraints:**

* `1 <= words.length <= 105`
* `1 <= words[i].length <= 10^5`
* `1 <= sum(words[i].length) <= 10^5`

# Submissions
---
**Solution 1: (Trie)**
```
Runtime: 1169 ms
Memory Usage: 56.2 MB
```
```python
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end = False
    
    def addWord(self, word):
        root = self
        for ch in word:
            root = root.children.setdefault(ch, TrieNode())
        root.end = True
        
class Solution:
    def longestWord(self, words: List[str]) -> str:
        self.root = TrieNode()
        for word in words:
            self.root.addWord(word)
        res = ""
        for word in words:
            if self.allPrefixExist(word, self.root):
                if len(word) > len(res):
                    res = word
                elif len(word) == len(res):
                    res = min(word, res)
        return res
        
    def allPrefixExist(self, word, node):        
        for ch in word:
            node = node.children[ch]
            if not node.end:
                return False
        return True
```
