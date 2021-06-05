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