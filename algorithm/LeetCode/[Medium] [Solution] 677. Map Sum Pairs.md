677. Map Sum Pairs

Implement a MapSum class with `insert`, and `sum` methods.

For the method `insert`, you'll be given a pair of (string, integer). The string represents the key and the integer represents the value. If the key already existed, then the original key-value pair will be overridden to the new one.

For the method `sum`, you'll be given a string representing the prefix, and you need to return the sum of all the pairs' value whose key starts with the prefix.

**Example 1:**
```
Input: insert("apple", 3), Output: Null
Input: sum("ap"), Output: 3
Input: insert("app", 2), Output: Null
Input: sum("ap"), Output: 5
```

# Solution
---
## Approach #1: Brute Force [Accepted]
**Intuition and Algorithm**

For each key in the map, if that key starts with the given prefix, then add it to the answer.

```python
class MapSum(object):
    def __init__(self):
        self.map = {}

    def insert(self, key, val):
        self.map[key] = val

    def sum(self, prefix):
        return sum(val for key, val in self.map.items()
                   if key.startswith(prefix))
```

**Complexity Analysis**

* Time Complexity: Every insert operation is $O(1)$. Every sum operation is $O(N * P)$ where $N$ is the number of items in the map, and $P$ is the length of the input prefix.

* Space Complexity: The space used by map is linear in the size of all input key and val values combined.

## Approach #2: Prefix Hashmap [Accepted]
**Intuition and Algorithm**

We can remember the answer for all possible prefixes in a HashMap score. When we get a new (key, val) pair, we update every prefix of key appropriately: each prefix will be changed by `delta = val - map[key]`, where `map` is the previous associated value of key (zero if undefined.)

```python
class MapSum(object):
    def __init__(self):
        self.map = {}
        self.score = collections.Counter()

    def insert(self, key, val):
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        for i in xrange(len(key) + 1):
            prefix = key[:i]
            self.score[prefix] += delta

    def sum(self, prefix):
        return self.score[prefix]
```

**Complexity Analysis**

* Time Complexity: Every insert operation is $O(K^2)$, where $K$ is the length of the key, as $K$ strings are made of an average length of $K$. Every sum operation is $O(1)$.

* Space Complexity: The space used by map and score is linear in the size of all input key and val values combined.

## Approach #3: Trie [Accepted]
**Intuition and Algorithm**

Since we are dealing with prefixes, a Trie (prefix tree) is a natural data structure to approach this problem. For every node of the trie corresponding to some prefix, we will remember the desired answer (score) and store it at this node. As in Approach #2, this involves modifying each node by `delta = val - map[key]`.

```python
class TrieNode(object):
    __slots__ = 'children', 'score'
    def __init__(self):
        self.children = {}
        self.score = 0

class MapSum(object):
    def __init__(self):
        self.map = {}
        self.root = TrieNode()

    def insert(self, key, val):
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        cur = self.root
        cur.score += delta
        for char in key:
            cur = cur.children.setdefault(char, TrieNode())
            cur.score += delta

    def sum(self, prefix):
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return 0
            cur = cur.children[char]
        return cur.score
```

**Complexity Analysis**

* Time Complexity: Every insert operation is $O(K)$, where $K$ is the length of the key. Every sum operation is $O(K)$.

* Space Complexity: The space used is linear in the size of the total input.

# Submissions
---
**Solution 1: (Brute Force)**
```
Runtime: 28 ms
Memory Usage: 12.9 MB
```
```python
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        self.map[key] = val
        

    def sum(self, prefix: str) -> int:
        return sum(val for key, val in self.map.items()
                   if key.startswith(prefix))


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
```

**Solution 2: (Prefix Hashmap)**
```
Runtime: 32 ms
Memory Usage: 12.8 MB
```
```python
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}
        self.score = collections.Counter()

    def insert(self, key: str, val: int) -> None:
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        for i in range(len(key) + 1):
            prefix = key[:i]
            self.score[prefix] += delta
        

    def sum(self, prefix: str) -> int:
        return self.score[prefix]


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
```

**Solution 3: (Trie)**
```
Runtime: 28 ms
Memory Usage: 12.7 MB
```
```python
class TrieNode(object):
    __slots__ = 'children', 'score'
    def __init__(self):
        self.children = {}
        self.score = 0

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        cur = self.root
        cur.score += delta
        for char in key:
            cur = cur.children.setdefault(char, TrieNode())
            cur.score += delta
        

    def sum(self, prefix: str) -> int:
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return 0
            cur = cur.children[char]
        return cur.score


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
```

**Solution 4: (Hash Table, String)**
```
Runtime: 0 ms
Memory Usage: 7.8 MB
```
```c++
class MapSum {
    unordered_map<string,int>mp;
public:
    MapSum() {
        
    }
    
    void insert(string key, int val) {
        mp[key]=val;
    }
    
    int sum(string prefix) {
        int ans=0;
        for(auto x:mp){
            size_t found = x.first.find(prefix);
           if (found != string::npos && found==0) //if found is 0 then add the value in the sum 
           {
               ans+=x.second;
           }
        }

        return ans;
    }
};

/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum* obj = new MapSum();
 * obj->insert(key,val);
 * int param_2 = obj->sum(prefix);
 */
```

**Solution 5: (trie)**
```
Runtime: 0 ms
Memory Usage: 8.5 MB
```
```c++
class MapSum {
    struct TrieNode{
        unordered_map<char, TrieNode*> edges;
        int val;
        bool isEnd;
        
        TrieNode(){
            edges = {};
            val = 0;
            isEnd = false;
        }
    };
    
    TrieNode* root;
public:
    MapSum() {
        root = new TrieNode();
    }
    
    void insert(string key, int val) {
        TrieNode* cur = root;
        for(char c: key){
            if(cur->edges.find(c) == cur->edges.end())
                cur->edges[c] = new TrieNode();
            cur = cur->edges[c];
        }
        cur->val = val;
        cur->isEnd = true;
    }
    
    int sum(string prefix) {
        TrieNode* cur = root;
        for(char c: prefix){
            if(cur->edges.find(c) == cur->edges.end())
                return 0;
            cur = cur->edges[c];
        }
        int sum = 0;
        queue<TrieNode*> queue;
        queue.push(cur);
        while(!queue.empty()){
            int n = queue.size();
            for(int i = 0; i < n; i++){
                cur = queue.front();
                queue.pop();
                sum += cur ->val;
                for(auto x: cur->edges)
                    queue.push(x.second);
            }
        }
        return sum;
    }
};

/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum* obj = new MapSum();
 * obj->insert(key,val);
 * int param_2 = obj->sum(prefix);
 */
```
