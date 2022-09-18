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

**Solution 3: (Trie)**
```
Runtime: 1739 ms
Memory Usage: 599.2 MB
```
```c++
struct TrieNode {
    TrieNode *next[26] = {};
    int index = -1;
    vector<int> palindromeIndexes;
};

class Solution {
    TrieNode root; // Suffix trie
    void add(string &s, int i) {
        auto node = &root;
        for (int j = s.size() - 1; j >= 0; --j) {
            if (isPalindrome(s, 0, j)) node->palindromeIndexes.push_back(i); // A[i]'s prefix forms a palindrome
            int c = s[j] - 'a';
            if (!node->next[c]) node->next[c] = new TrieNode();
            node = node->next[c];
        }
        node->index = i;
        node->palindromeIndexes.push_back(i); // A[i]'s prefix is empty string here, which is a palindrome.
    }
    
    bool isPalindrome(string &s, int i, int j) {
        while (i < j && s[i] == s[j]) ++i, --j;
        return i >= j;
    }
public:
    vector<vector<int>> palindromePairs(vector<string>& words) {
        int N = words.size();
        for (int i = 0; i < N; ++i) add(words[i], i);
        vector<vector<int>> ans;
        for (int i = 0; i < N; ++i) {
            auto s = words[i];
            auto node = &root;
            for (int j = 0; j < s.size() && node; ++j) {
                if (node->index != -1 && node->index != i && isPalindrome(s, j, s.size() - 1)) ans.push_back({ i, node->index }); 
                // A[i]'s prefix matches this word and A[i]'s suffix forms a palindrome
                node = node->next[s[j] - 'a'];
            }
            if (!node) continue;
            for (int j : node->palindromeIndexes) { 
                // A[i] is exhausted in the matching above. 
                // If a word whose prefix is palindrome after matching its suffix with A[i], 
                // then this is also a valid pair
                if (i != j) ans.push_back({ i, j });
            }
        }
        return ans;
    }
};
```
