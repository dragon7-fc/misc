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

**Solution 2: (List, Hash Table)**
```
Runtime: 384 ms
Memory Usage: 41.9 MB
```
```c++
class LRUCache {
public:
    list<int>  lru_key;
    //LRU map with integer key and value
    unordered_map<int, int> lru;
    int capacity;
    
    LRUCache(int capacity) {
        this->capacity = capacity;
        lru.clear();
    }
    
    int get(int key) {
        if(lru.count(key)>0)
        {
            lru_key.remove(key);
            lru_key.push_front(key);
            return lru[key];
        }
        else
            return -1;
    }
    
    void put(int key, int value) {
        if(lru.count(key)>0)
        {
            lru[key] = value;
            lru_key.remove(key);
            lru_key.push_front(key);
        }
        else if(lru.size()>=capacity)
        {   
            lru.erase(lru_key.back());
            lru_key.pop_back();
            
            lru.insert({key,value});
            lru_key.push_front(key);
        }
        else
        {
            lru.insert({key,value});
            lru_key.push_front(key);
        }  
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
```