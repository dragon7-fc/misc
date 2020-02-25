336. Palindrome Pairs

Given a list of **unique** words, find all pairs of **distinct** indices `(i, j)` in the given list, so that the concatenation of the two words, i.e. `words[i] + words[j]` is a palindrome.

**Example 1:**
```
Input: ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]] 
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
```

**Example 2:**
```
Input: ["bat","tab","cat"]
Output: [[0,1],[1,0]] 
Explanation: The palindromes are ["battab","tabbat"]
```

# Submissions
---
**Solution 1: (Hash Table)**
```
Runtime: 512 ms
Memory Usage: 14.2 MB
```
```python
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        dicts = {}
        for i, word in enumerate(words):
            dicts[word[::-1]] = i
        
        def isPalindrome(s):
            return s == s[::-1]
        
        res = set()
        for i, word in enumerate(words):
            for j in range(len(word) + 1):  # to cover the case of empty string 
                left = word[:j]
                right = word[j:]
                # case 1: e.g. ["abcd","dcba"], ["lls","s"], ["sssll","lls"]
                if isPalindrome(left) and (right in dicts) and (i!=dicts[right]):
                    res.add((dicts[right], i))
                # case 2: E.G. ["a", ""]
                if isPalindrome(right) and (left in dicts) and (i!=dicts[left]):
                    res.add((i, dicts[left]))
        return res
```

**Solution 2: (Trie, DFS)**

Build trie from reverse word order and search in forward order.
```
Runtime: 512 ms
Memory Usage: 16.7 MB
```
```python
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        if not words:
            return []
        n = len(words)
        if n == 1:
            return []
        
        res = []
        
        def isPalindrome(w: str) -> bool:
            return w == w [::-1]
            
        
        # "" can combine with any palindromic word to form palidrome-pair
        if "" in words:
            j = words.index("")
            for i, word in enumerate(words):
                if i != j and isPalindrome(word):
                    res.extend([[i, j], [j, i]])
            
        # build trie of reversed words
        trie = {}
        for i, word in enumerate(words):
            if word == "":
                continue
            rev_word = word[::-1]
            t = trie
            for letter in rev_word:
                t = t.setdefault(letter, {})
            t['#'] = i
        
        def trie_scan(trienode, word, cur_word_index):
            for letter in trienode:
                if letter == '#':
                    if cur_word_index != trienode['#'] and isPalindrome(word):
                        res.append([cur_word_index, trienode['#']])
                else:    
                    trie_scan(trienode[letter], word + letter, cur_word_index)
        
        # search    
        for i, word in enumerate(words):
            if word == "":
                continue
            scanned_len = 0
            node = trie
            for letter in word:
                # if a trie-word ended here, check if the rest of this word is palindromic
                if '#' in node and i != node['#'] and isPalindrome(word[scanned_len:]):
                    res.append([i, node['#']])
                    
                node = node.get(letter, False)
                # if this letter is not found in trie-node, this word can't form palidromic-pair 
                if not node:
                    break
                scanned_len += 1
            
            if scanned_len == len(word):
                # check if any of the rest of the trie-words are palindromic
                trie_scan(node, "", i)
            
            else: # check if the rest of this word is palindromic
                if node and i != node['#'] and isPalindrome(word[scanned_len+1:]):
                    res.append([i, node['#']])
                
        return res

```