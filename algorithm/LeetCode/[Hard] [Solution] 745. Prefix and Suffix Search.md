745. Prefix and Suffix Search

Given many words,`words[i]` has weight `i`.

Design a class WordFilter that supports one function, `WordFilter.f(String prefix, String suffix)`. It will return the word with given prefix and suffix with maximum weight. If no word exists, return `-1`.

**Examples:**
```
Input:
WordFilter(["apple"])
WordFilter.f("a", "e") // returns 0
WordFilter.f("b", "") // returns -1
```

**Note:**

* `words` has length in range `[1, 15000]`.
* For each test case, up to `words.length` queries `WordFilter.f` may be made.
* `words[i]` has length in range `[1, 10]`.
* `prefix`, `suffix` have lengths in range `[0, 10]`.
* `words[i]` and `prefix`, `suffix` queries consist of lowercase letters only.

# Solution
---
## Approach #1: Trie + Set Intersection [Time Limit Exceeded]
**Intuition and Algorithm**

We use two tries to separately find all words that match the prefix, plus all words that match the suffix. Then, we try to find the highest weight element in the intersection of these sets.

Of course, these sets could still be large, so we might TLE if we aren't careful.

```python
Trie = lambda: collections.defaultdict(Trie)
WEIGHT = False

class WordFilter(object):
    def __init__(self, words):
        self.trie1 = Trie() #prefix
        self.trie2 = Trie() #suffix
        for weight, word in enumerate(words):
            cur = self.trie1
            self.addw(cur, weight)
            for letter in word:
                cur = cur[letter]
                self.addw(cur, weight)

            cur = self.trie2
            self.addw(cur, weight)
            for letter in word[::-1]:
                cur = cur[letter]
                self.addw(cur, weight)

    def addw(self, node, w):
        if WEIGHT not in node:
            node[WEIGHT] = {w}
        else:
            node[WEIGHT].add(w)

    def f(self, prefix, suffix):
        cur1 = self.trie1
        for letter in prefix:
            if letter not in cur1: return -1
            cur1 = cur1[letter]

        cur2 = self.trie2
        for letter in suffix[::-1]:
            if letter not in cur2: return -1
            cur2 = cur2[letter]

        return max(cur1[WEIGHT] & cur2[WEIGHT])
```

**Complexity Analysis**

* Time Complexity: $O(NK + Q(N+K))$ where $N$ is the number of words, $K$ is the maximum length of a word, and $Q$ is the number of queries. If we use memoization in our solution, we could produce tighter bounds for this complexity, as the complex queries are somewhat disjoint.

* Space Complexity: $O(NK)$, the size of the tries.

## Approach #2: Paired Trie [Accepted]
**Intuition and Algorithm**

Say we are inserting the word apple. We could insert `('a', 'e'), ('p', 'l'), ('p', 'p'), ('l', 'p'), ('e', 'a')` into our trie. Then, if we had equal length queries like `prefix = "ap", suffix = "le"`, we could find the node `trie['a', 'e']['p', 'l']` in our trie. This seems promising.

What about queries that aren't equal? We should just insert them like normal. For example, to capture a case like `prefix = "app", suffix = "e"`, we could create nodes `trie['a', 'e']['p', None]['p', None]`.

After inserting these pairs into our trie, our searches are straightforward.

```python
Trie = lambda: collections.defaultdict(Trie)
WEIGHT = False

class WordFilter(object):
    def __init__(self, words):
        self.trie = Trie()

        for weight, word in enumerate(words):
            cur = self.trie
            cur[WEIGHT] = weight
            for i, x in enumerate(word):
                #Put all prefixes and suffixes
                tmp = cur
                for letter in word[i:]:
                    tmp = tmp[letter, None]
                    tmp[WEIGHT] = weight

                tmp = cur
                for letter in word[:-i or None][::-1]:
                    tmp = tmp[None, letter]
                    tmp[WEIGHT] = weight

                #Advance letters
                cur = cur[x, word[~i]]
                cur[WEIGHT] = weight

    def search(self, prefix, suffix):
        cur = self.trie
        for a, b in map(None, prefix, suffix[::-1]):
            if (a, b) not in cur: return -1
            cur = cur[a, b]
        return cur[WEIGHT]
```

**Complexity Analysis**

* Time Complexity: $O(NK^2 + QK)$ where $N$ is the number of words, $K$ is the maximum length of a word, and $Q$ is the number of queries.

* Space Complexity: $O(NK^2)$, the size of the trie.

## Approach #3: Trie of Suffix Wrapped Words [Accepted]
**Intuition and Algorithm**

Consider the word `'apple'`. For each suffix of the word, we could insert that suffix, followed by `'#'`, followed by the word, all into the trie.

For example, we will insert `'#apple'`, `'e#apple'`, `'le#apple'`, `'ple#apple'`, `'pple#apple'`, `'apple#apple'` into the trie. Then for a query like `prefix = "ap", suffix = "le"`, we can find it by querying our trie for `le#ap`.

```python
Trie = lambda: collections.defaultdict(Trie)
WEIGHT = False

class WordFilter(object):
    def __init__(self, words):
        self.trie = Trie()

        for weight, word in enumerate(words):
            word += '#'
            for i in xrange(len(word)):
                cur = self.trie
                cur[WEIGHT] = weight
                for j in xrange(i, 2 * len(word) - 1):
                    cur = cur[word[j % len(word)]]
                    cur[WEIGHT] = weight

    def f(self, prefix, suffix):
        cur = self.trie
        for letter in suffix + '#' + prefix:
            if letter not in cur:
                return -1
            cur = cur[letter]
        return cur[WEIGHT]
```

**Complexity Analysis**

* Time Complexity: $O(NK^2 + QK)$ where $N$ is the number of words, $K$ is the maximum length of a word, and $Q$ is the number of queries.

* Space Complexity: $O(NK^2)$, the size of the trie.

# Submissions
---
**Solution 1: (Trie of Suffix Wrapped Words)**
```
Runtime: 948 ms
Memory Usage: 59.4 MB
```
```python
Trie = lambda: collections.defaultdict(Trie)
WEIGHT = False

class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()

        for weight, word in enumerate(words):
            word += '#'
            for i in range(len(word)):
                cur = self.trie
                cur[WEIGHT] = weight
                for j in range(i, 2 * len(word) - 1):
                    cur = cur[word[j % len(word)]]
                    cur[WEIGHT] = weight
            
    def f(self, prefix: str, suffix: str) -> int:
        cur = self.trie
        for letter in suffix + '#' + prefix:
            if letter not in cur:
                return -1
            cur = cur[letter]
        return cur[WEIGHT]


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
```

**Solution 2: (Trie of Suffix Wrapped Words)**
```
Runtime: 668 ms
Memory Usage: 200.3 MB
```
```c++
class TrieNode{
public :
    
    vector<TrieNode*>children;
    int index;
    
    TrieNode(){
        children = vector<TrieNode*>(27, NULL);
        index = -1;
    }
    // create destructor to avoid any memory leak
    ~TrieNode(){
        for (int i = 0; i < 26; i++) {
            if (children[i]) {
                delete children[i];
            }
        }
    }
};

// Class to do the basic operations like insert, searching etc.
class Trie{
public:
    
    TrieNode* root;
    Trie(){
        root = new TrieNode();
    }

    void insert(string &s, int idx)
    {        
        TrieNode* cur = root;
        for(int i=0;i<s.size();i++)
        {
            if(cur->children[s[i]-'a'] == NULL)
                cur->children[s[i]-'a'] = new TrieNode();
            
            cur = cur->children[s[i]-'a'];
            cur->index = idx;
        }
    }
    
    int search(string &word)
    {
        TrieNode* cur = root;
        for(int i = 0; i < word.size(); i++){
            cur = cur->children[word[i] - 'a'];
            if(!cur) 
                return -1;
        }
        return cur->index;
    }
};

class WordFilter {
    Trie *trie = new Trie();
public:
    WordFilter(vector<string>& words) {
        int idx = 0;
        string s = "";
        
        for(auto &word : words) 
        {
            s = "{" + word;
            trie->insert(s, idx);
            
            for(int i=word.size()-1; i>=0; i--) 
            {
                s = word[i] + s;
                trie->insert(s, idx);
            }
            idx++;
        }
    }
    
    int f(string prefix, string suffix) {
        string match = suffix + "{" + prefix;
        int ansIdx = trie->search(match);
        return ansIdx;
    }
};

/**
 * Your WordFilter object will be instantiated and called as such:
 * WordFilter* obj = new WordFilter(words);
 * int param_1 = obj->f(prefix,suffix);
 */
```

**Solution 3: (Hash Table)**
```
Runtime: 612 ms
Memory Usage: 137.4 MB
```
```
class WordFilter {
    unordered_map<string,int> data;
public:
    WordFilter(vector<string>& words) {
        for (int k = 0; k < words.size(); ++k) {
            string const& word = words[k];
            int const n = word.size();
            for (int i = 1; i <= n; ++i) {
                string key = word.substr(0, i);
                key += '.';
                for (int j = 1; j <= n; ++j) {
                    key.resize(i+1);
                    key.append(word, n-j, j);
                    data[key] = k;
                }
            }
        }
    }
    
    int f(string prefix, string suffix) {
        prefix += '.';
        prefix += suffix;
        return data.count(prefix) ? data[prefix] : -1;
    }
};

/**
 * Your WordFilter object will be instantiated and called as such:
 * WordFilter* obj = new WordFilter(words);
 * int param_1 = obj->f(prefix,suffix);
 */
```

**Solution 4: (Trie)**

"apple"
build:  "apple{apple", "pple{apple", "ple{apple", "le{apple", "e{apple", "{apple"
search:                                                        ^^^

```
Runtime: 383 ms, Beats 55.38%
Memory: 566.82 MB, Beats 19.22%
```
```c++
class WordFilter {
    struct TrieNode {
        TrieNode *child[27] = {nullptr};
        int idx = -1;
    };
    TrieNode *root;
    void build(vector<string> &words, int i) {
        TrieNode *node;
        int n = words[i].length(), j, k;
        string s;
        for (j = 0; j < n; j ++) {
            node = root;
            s = words[i].substr(j) + "{" + words[i];
            for (k = 0; k < s.length(); k ++) {
                if (!node->child[s[k] - 'a']) {
                    node->child[s[k] - 'a'] = new TrieNode();
                }
                node = node->child[s[k] - 'a'];
                node->idx = i;  
            }  
        }
    }
    int search(string &s) {
        TrieNode *node = root;
        for (int i = 0; i < s.size(); i ++) {
            if (!node->child[s[i] - 'a']) {
                return -1;
            }
            node = node->child[s[i] - 'a'];
        }
        return node->idx;
    }
public:
    WordFilter(vector<string>& words) {
        int n = words.size(), i;
        root = new TrieNode();
        for (i = 0; i < n; i++) {
            build(words, i);
        }
    }
    
    int f(string pref, string suff) {
        string s = suff + "{" + pref;
        return search(s);
    }
};

/**
 * Your WordFilter object will be instantiated and called as such:
 * WordFilter* obj = new WordFilter(words);
 * int param_1 = obj->f(pref,suff);
 */
```
