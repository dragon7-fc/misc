1268. Search Suggestions System

Given an array of strings `products` and a string `searchWord`. We want to design a system that suggests at most three product names from `products` after each character of `searchWord` is typed. Suggested `products` should have common prefix with the `searchWord`. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return list of lists of the suggested products after each character of `searchWord` is typed. 

 

**Example 1:**
```
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
```

**Example 2:**
```
Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
```

**Example 3:**
```
Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
```

**Example 4:**
```
Input: products = ["havana"], searchWord = "tatiana"
Output: [[],[],[],[],[],[],[]]
```

**Constraints:**

* `1 <= products.length <= 1000`
* `1 <= Σ products[i].length <= 2 * 10^4`
* All characters of `products[i]` are lower-case English letters.
* `1 <= searchWord.length <= 1000`
* All characters of searchWord are lower-case English letters.

# Submissions
---
**Solution 1: (Sort)**
```
Runtime: 100 ms
Memory Usage: 15.3 MB
```
```python
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        result = list() 
        products.sort()
        for i in range(1, len(searchWord)+1):
            products = list(filter(lambda x: x.startswith(searchWord[:i]), products))
            result.append(products[:3])
        return result
```

**Solution 2: (Sorting & Binary Search)**
```
Runtime: 156 ms
Memory Usage: 17 MB
```
```python
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        n = len(products)
        products.sort()  # Sort by increasing lexicographically order of products
        ans = []
        beginSearch = 0
        prefix = ""
        for c in searchWord:
            prefix += c
            beginSearch = insertIndex = bisect_left(products, prefix, beginSearch, n)
            suggestProducts = []
            for i in range(insertIndex, min(insertIndex+3, n)):
                if products[i].startswith(prefix):
                    suggestProducts.append(products[i])
            ans.append(suggestProducts)
        return ans
```

**Solution 3: (Trie)**
```
Runtime: 2652 ms
Memory Usage: 22.4 MB
```
```python
class TrieNode:
    def __init__(self):
        self.word = None
        self.children = [None] * 26

    def addWord(self, word):
        curr = self
        for c in word:
            index = ord(c) - ord('a')
            if curr.children[index] == None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.word = word

    def getWords(self, limit):
        words = []

        def dfs(curr):
            if len(words) == limit: return
            if curr.word != None:
                words.append(curr.word)
            for key in range(26):
                if curr.children[key] != None:
                    dfs(curr.children[key])

        dfs(self)
        return words
    
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = TrieNode()
        for product in products:
            root.addWord(product)

        ans = []
        curr = root
        for c in searchWord:
            key = ord(c) - ord('a')
            if curr != None and curr.children[key] != None:
                curr = curr.children[key]
                ans.append(curr.getWords(3))
            else:
                curr = None
                ans.append([])
        return ans
```

**Solution 4; (Binary Search)**
```
Runtime: 67 ms
Memory Usage: 23.9 MB
```
```c++
class Solution {
public:
    vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) {
        sort(products.begin(), products.end());
        vector<vector<string>> result;
        int start, bsStart = 0, n=products.size();
        string prefix;
        for (char &c : searchWord) {
            prefix += c;

            // Get the starting index of word starting with `prefix`.
            start = lower_bound(products.begin() + bsStart, products.end(), prefix) - products.begin();

            // Add empty vector to result.
            result.push_back({});

            // Add the words with the same prefix to the result.
            // Loop runs until `i` reaches the end of input or 3 times or till the
            // prefix is same for `products[i]` Whichever comes first.
            for (int i = start; i < min(start + 3, n) && !products[i].compare(0, prefix.length(), prefix); i++)
                result.back().push_back(products[i]);

            // Reduce the size of elements to binary search on since we know
            bsStart = start;
        }
        return result;
    }
};
```

**Solution 5: (Trie + DFS)**
```
Runtime: 371 ms
Memory Usage: 76.5 MB
```
```c++
// Custom class Trie with function to get 3 words starting with given prefix
class Trie
{
    // Node definition of a trie
    struct Node {
        bool isWord = false;
        vector<Node *> children{vector<Node *>(26, NULL)};
    } * Root, *curr;

    // Runs a DFS on trie starting with given prefix and adds all the words in the result, limiting result size to 3
    void dfsWithPrefix(Node * curr, string & word, vector<string> & result) {
        if (result.size() == 3)
            return;
        if (curr->isWord)
            result.push_back(word);

        // Run DFS on all possible paths.
        for (char c = 'a'; c <= 'z'; c++)
            if (curr->children[c - 'a']) {
                word += c;
                dfsWithPrefix(curr->children[c - 'a'], word, result);
                word.pop_back();
            }
    }

public:
    Trie() {
        Root = new Node();
    }
    // Inserts the string in trie.
    void insert(string & s) {
        // Points curr to the root of trie.
        curr = Root;
        for (char &c : s) {
            if (!curr->children[c - 'a'])
                curr->children[c - 'a'] = new Node();
            curr = curr->children[c - 'a'];
        }
        // Mark this node as a completed word.
        curr->isWord = true;
    }
    vector<string> getWordsStartingWith(string & prefix) {
        curr = Root;
        vector<string> result;

        // Move curr to the end of prefix in its trie representation.
        for (char &c : prefix) {
            if (!curr->children[c - 'a'])
                return result;
            curr = curr->children[c - 'a'];
        }
        dfsWithPrefix(curr, prefix, result);
        return result;
    }
};

class Solution {
public:
    vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) {
        Trie trie=Trie();
        vector<vector<string>> result;

        // Add all words to trie.
        for(string &w:products)
            trie.insert(w);
        string prefix;
        for (char &c : searchWord) {
            prefix += c;
            result.push_back(trie.getWordsStartingWith(prefix));
        }
        return result;
    }
};
```
