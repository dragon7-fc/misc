146. LRU Cache

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: `get` and `put`.

* `get(key)` - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
* `put(key, value)` - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a **positive** capacity.

**Follow up:**

* Could you do both operations in O(1) time complexity?

**Example:**
```
LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
```

# Submissions
---
**Solution 1: (OrderedDict)**
```
Runtime: 184 ms
Memory Usage: 21.9 MB
```
```python
class LRUCache:

    def __init__(self, capacity: int):
        self.max_capacity = capacity
        self.lru_cache = collections.OrderedDict()

    def get(self, key: int) -> int:
        key = str(key)
        if(key not in self.lru_cache):
            return -1
        value = self.lru_cache[key]
        del self.lru_cache[key]
        self.lru_cache[key] = value
        return value

    def put(self, key: int, value: int) -> None:
        key = str(key)
        if(key not in self.lru_cache):
            if(len(self.lru_cache) < self.max_capacity):
                self.lru_cache[key] = value
            else:
                self.lru_cache.popitem(last=False)
                self.lru_cache[key] = value
        else:
            del self.lru_cache[key]
            self.lru_cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```

**Solution 2: (double Linked List, Hash Table)**
```
Runtime: 538 ms
Memory: 178.7 MB
```
```c++
class LRUCache {
    class Node{
        public: 
            int key;
            int val;
            Node* prev;
            Node* next;

            Node(int key, int val){
                this->key = key;
                this->val = val;
            }
    };

    Node* head = new Node(-1, -1);
    Node* tail = new Node(-1, -1);

    int cap;
    unordered_map<int, Node*> m;

    void addNode(Node* newnode){
        Node* temp = head -> next;

        newnode -> next = temp;
        newnode -> prev = head;

        head -> next = newnode;
        temp -> prev = newnode;
    }

    void deleteNode(Node* delnode){
        Node* prevv = delnode -> prev;
        Node* nextt = delnode -> next;

        prevv -> next = nextt;
        nextt -> prev = prevv;
    }
public:
    LRUCache(int capacity) {
        cap = capacity;
        head -> next = tail;
        tail -> prev = head;
    }
    
    int get(int key) {
        if (m.count(key)) {
            Node* resNode = m[key];
            int ans = resNode -> val;

            m.erase(key);
            deleteNode(resNode);
            addNode(resNode);

            m[key] = head -> next;
            return ans;
        }
        return -1;
    }
    
    void put(int key, int value) {
        if (m.count(key)) {
            Node* curr = m[key];
            m.erase(key);
            deleteNode(curr);
        }
        if (m.size() == cap) {
            m.erase(tail -> prev -> key);
            deleteNode(tail -> prev);
        }
        addNode(new Node(key, value));
        m[key] = head -> next;
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
```

**Solution 3: (List, queue, not deque)**

LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
m:  1
    |
    v   
q: (1,1)

lRUCache.put(2, 2); // cache is {1=1, 2=2}
m:  2     1
    |     |
    v     v 
q: (2,2) (1,1)

lRUCache.get(1);    // return 1
m:  1     2
    |     |
    v     v 
q: (1,1) (2,2)

lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
                x
m:  3     1     2
    |     |     |
    V     v     v 
q: (3,3) (1,1) (2,2)
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
                x 
m:  4     3     1
    |     |     |
    V     V     v 
q: (4,4) (3,3) (1,1)

lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
m:  3     4
    |     |
    V     V 
q: (3,3) (4,4)

lRUCache.get(4);    // return 4
m:  4     3
    |     |
    V     V 
q: (4,4) (3,3)

```
Runtime: 445 ms
Memory: 183.3 MB
```
```c++
class LRUCache {
    list<pair<int,int>> q;  // list(k, v)
    unordered_map<int, list<pair<int,int>>::iterator> m;  // k, list(k, v)->
    int n;
public:
    LRUCache(int capacity) {
        n = capacity;
    }
    
    int get(int key) {
        if (!m.count(key)) {
            return -1;
        }
        auto it = m[key];
        int rst = it->second;
        q.push_front(*it);
        q.erase(it);
        m[key] = q.begin();
        return rst;
    }
    
    void put(int key, int value) {
        if (m.count(key)) {
            q.erase(m[key]);
        } else if (m.size() == n) {
            m.erase(q.back().first);
            q.pop_back();
        }
        q.push_front({key, value});
        m[key] = q.begin();
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
```
