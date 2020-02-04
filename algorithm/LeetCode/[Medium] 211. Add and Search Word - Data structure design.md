211. Add and Search Word - Data structure design

Design a data structure that supports the following two operations:

* `void addWord(word)`
* `bool search(word)`

`search(word)` can search a literal word or a regular expression string containing only letters `a-z` or .`. A` `.` means it can represent any one letter.

**Example:**
```
addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
```

**Note:**

* You may assume that all words are consist of lowercase letters `a-z`.

# Submissions
---
**Solution 1: (Trie)**
```
Runtime: 356 ms
Memory Usage: 28.7 MB
```
```python
class Node:
    def __init__(self):
        self.sub = collections.defaultdict(Node)
        self.isend = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur = self.root
        for i in word: cur = cur.sub[i]
        cur.isend = True
        
    def searchnode(self, word: str, st, node) -> bool:
        for i in range(st, len(word)):
            if word[i] == '.':
                for n in node.sub.values():
                    if self.searchnode(word, i+1, n): return True
                return False
            else:
                node = node.sub.get(word[i], None)
                if node is None: return False
        return node and node.isend

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.searchnode(word, 0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
```