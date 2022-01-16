1804. Implement Trie II (Prefix Tree)

A trie (pronounced as "try") or **prefix tree** is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

* `Trie()` Initializes the trie object.
* `void insert(String word)` Inserts the string `word` into the trie.
* `int countWordsEqualTo(String word)` Returns the number of instances of the string `word` in the trie.
* `int countWordsStartingWith(String prefix)` Returns the number of strings in the trie that have the string `prefix` as a prefix.
* `void erase(String word)` Erases the string `word` from the trie.
 

**Example 1:**
```
Input
["Trie", "insert", "insert", "countWordsEqualTo", "countWordsStartingWith", "erase", "countWordsEqualTo", "countWordsStartingWith", "erase", "countWordsStartingWith"]
[[], ["apple"], ["apple"], ["apple"], ["app"], ["apple"], ["apple"], ["app"], ["apple"], ["app"]]
Output
[null, null, null, 2, 2, null, 1, 1, null, 0]

Explanation
Trie trie = new Trie();
trie.insert("apple");               // Inserts "apple".
trie.insert("apple");               // Inserts another "apple".
trie.countWordsEqualTo("apple");    // There are two instances of "apple" so return 2.
trie.countWordsStartingWith("app"); // "app" is a prefix of "apple" so return 2.
trie.erase("apple");                // Erases one "apple".
trie.countWordsEqualTo("apple");    // Now there is only one instance of "apple" so return 1.
trie.countWordsStartingWith("app"); // return 1
trie.erase("apple");                // Erases "apple". Now the trie is empty.
trie.countWordsStartingWith("app"); // return 0
```

**Constraints:**

* `1 <= word.length, prefix.length <= 2000`
* `word` and `prefix` consist only of lowercase English letters.
* At most `3 * 10^4` calls in total will be made to `insert`, `countWordsEqualTo`, `countWordsStartingWith`, and `erase`.
* It is guaranteed that for any function call to `erase`, the string word will exist in the trie.

# Submissions
---
**Solution 1: (Trie)**
```
Runtime: 584 ms
Memory Usage: 26.5 MB
```
```python
class Trie:

    def __init__(self):
        self.trie = {}
        self.end = 'end' # symbol of ending of word
        self.count = 'count' # symbol of ending of prefix

    def insert(self, word: str) -> None:
        node = self.trie
        for c in word:
            if c not in node:
                node[c] = {}
                node[c][self.count] = 0
            
            node[c][self.count] += 1 # increase count of prefixes
            node = node[c]
        
        if self.end not in node:
            node[self.end] = 0
        
        node[self.end] += 1 # increase count of word

    def countWordsEqualTo(self, word: str) -> int:
        node = self.trie
        for c in word:
            if c not in node:
                return 0 # no such word
            
            node = node[c]
        
        if self.end not in node:
            return 0 # word may be valid prefix, but such word is absent
        
        return node[self.end] # return count of such words

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self.trie
        for c in prefix:
            if c not in node:
                return 0 # no such prefix
            
            node = node[c]
        
        return node[self.count] # return count of such prefixes
        

    def erase(self, word: str) -> None:
        node = self.trie
        for c in word:
            node[c][self.count] -= 1 # decrease count of prefixes
            node = node[c]
        
        node[self.end] -= 1 # decrease count of words


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)
```

**Solution 2: (Trie)**
```
Runtime: 351 ms
Memory Usage: 66.7 MB
```
```c++
class TrieNode {
public:
    int countWords;                // number of words that end here
    int countStarts;                // number of words that pass through this node
    TrieNode* children[26] = {NULL};      // children nodes
    TrieNode(){
        countWords = 0;
        countStarts = 0;
    }
};

class Trie {
public:
    TrieNode* root;
    Trie() {
        root = new TrieNode();
    }
    
    void insert(string word) {
        TrieNode* temp = root;
        int n = word.size();
        for(int i = 0; i < n; i++){
		// if this character is not present in trie, we add it
            if(temp->children[word[i]-'a'] == NULL){
                temp->children[word[i]-'a'] = new TrieNode();
            }
            temp = temp->children[word[i]-'a'];
			// increment the count of words starting with/passing through this character
            temp->countStarts++;
        }
		// increment word counter for the last character
        temp->countWords++;
    }
    
    int countWordsEqualTo(string word) {
        TrieNode* temp = root;
        int n = word.size();
		// base case
        if(n == 0){
            return 0;
        }
        for(int i = 0; i < n; i++){
		    // if this character is not present in trie, there are no matching words possible
            if(temp->children[word[i]-'a'] == NULL){
                return 0;
            } else {
			// move to the next character
               temp = temp->children[word[i]-'a'];
            }
        }
		// return the count of words ending with the last character
        return temp->countWords;
    }
    
    int countWordsStartingWith(string prefix) {
        TrieNode* temp = root;
        
        int n = prefix.size();
        if(n == 0){
            return 0;
        }
        for(int i = 0; i < n; i++){
		// if this character is not present, there are no matching words possible.
		// NOTE: Because of ERASE operation, we might have nodes which are no longer
		// present in any word's path, so we have to check countStarts
            if(temp->children[prefix[i]-'a'] == NULL || 
               temp->children[prefix[i]-'a']->countStarts == 0){
                return 0;
            } else {
               temp = temp->children[prefix[i]-'a'];
            }
        }
		// return the count of words passing through the last character
        return temp->countStarts;
 
    }
    
    void erase(string word) {
        TrieNode* temp = root;
        int n = word.size();
        for(int i = 0; i < n; i++){
		    // decrement the counter for words which pass through this node
            temp->children[word[i]-'a']->countStarts--;
            temp = temp->children[word[i]-'a'];
        }
		// decrement the word counter for the last character
        temp->countWords--;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * int param_2 = obj->countWordsEqualTo(word);
 * int param_3 = obj->countWordsStartingWith(prefix);
 * obj->erase(word);
 */
```
