460. LFU Cache

Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: `get` and `put`.

* `get(key)` - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
* `put(key, value)` - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least **recently** used key would be evicted.

Note that the number of times an item is used is the number of calls to the `get` and `put` functions for that item since it was inserted. This number is set to zero when the item is removed.

 

**Follow up:**

* Could you do both operations in **O(1)** time complexity?

 

**Example:**
```
LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
```

# Submissions
---
**Solution 1: (OrderedDict, Hash Table)**
```
Runtime: 332 ms
Memory Usage: 23.3 MB
```
```python
class Node:

	def __init__(self, key, val, freq):
		self.key = key
		self.val = val
		self.freq = freq
        
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mapping = {}
        self.freq_mapping = collections.defaultdict(collections.OrderedDict)
        self.min_freq = None

    def get(self, key: int) -> int:
        if key not in self.mapping:
            return -1

        node = self.mapping[key]
        self.freq_mapping[node.freq].pop(key)

        if not self.freq_mapping[node.freq]:
            self.freq_mapping.pop(node.freq)

        node.freq += 1
        self.freq_mapping[node.freq][key] = node

        if not self.freq_mapping[self.min_freq]:
            self.min_freq += 1

        return node.val

    def put(self, key: int, value: int) -> None:
        if not self.capacity:
            return 

        if key in self.mapping:
            self.mapping[key].val = value
            self.get(key)
            return 
        else:
            if len(self.mapping) == self.capacity:
                k, n = self.freq_mapping[self.min_freq].popitem(last=False)
                self.mapping.pop(k)

            new_node = Node(key, value, 1)
            self.mapping[key] = new_node
            self.freq_mapping[1][key] = new_node
            self.min_freq = 1
            return


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```

**Solution 2: (Doubly LinkedList)**
```
Runtime: 340 ms
Memory Usage: 23.8 MB
```
```python
class Node:
    
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None
        
class DoubleLinkList:
    
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.size = 0
        
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def add(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node
        self.size += 1
    
    def remove(self, node = None):
        if self.size == 0:
            return
        
        if not node:
            node = self.head.next
            
        prev = node.prev
        prev.next = node.next
        node.next.prev = prev
        self.size -= 1
        return node
        
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mapping = {}
        self.freq_mapping = collections.defaultdict(DoubleLinkList)
        self.min_freq = None
        
    def get(self, key: int) -> int:
        if key not in self.mapping:
            return -1
        
        node = self.mapping[key]
        self.freq_mapping[node.freq].remove(node)
        
        if self.freq_mapping[node.freq].size == 0:
            self.freq_mapping.pop(node.freq)
        
        node.freq += 1
        self.freq_mapping[node.freq].add(node)
        
        if self.freq_mapping[self.min_freq].size == 0:
            self.min_freq += 1
        
        return node.val

    def put(self, key: int, value: int) -> None:
        if not self.capacity:
            return 
        
        if key in self.mapping:
            self.mapping[key].val = value
            self.get(key)
            return 
        else:
            if len(self.mapping) == self.capacity:
                remove_node = self.freq_mapping[self.min_freq].remove()
                self.mapping.pop(remove_node.key)
            
            new_node = Node(key, value)
            self.mapping[key] = new_node
            self.freq_mapping[1].add(new_node)
            self.min_freq = 1
            return


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```

**Solution 3: (Hash Table)**
```
Runtime: 268 ms
Memory Usage: 45.3 MB
```
```c++
class LFUCache {
private:
    int cap;
    int size;
    unordered_map<int, list<vector<int>>::iterator> um;
    map<int, list<vector<int>>> freq;

public:
    LFUCache(int capacity) {
        cap = capacity;
        size = 0;
    }
    
    int get(int key) {
        if(um.find(key) == um.end())
            return -1;
        int value = (*(um[key]))[1], f = (*(um[key]))[2];
        freq[f].erase(um[key]);
        if(freq[f].empty())
            freq.erase(f);
        f++;
        freq[f].push_front(vector<int>({key, value, f}));
        um[key] = freq[f].begin();
        return value;
    }
    
    void put(int key, int value) {
        if(cap == 0)
            return;
        if(um.find(key) != um.end()){
            (*(um[key]))[1] = value;
            get(key);
        }
        else if(size < cap){
            size++;
            freq[1].push_front(vector<int>({key, value, 1}));
            um[key] = freq[1].begin();
        }
        else{
            int x = (freq.begin()->second.back())[0];
            freq.begin()->second.pop_back();
            if(freq.begin()->second.empty())
                freq.erase(freq.begin()->first);
            um.erase(x);
            freq[1].push_front(vector<int>({key, value, 1}));
            um[key] = freq[1].begin();
        }
    }
};

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache* obj = new LFUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
```