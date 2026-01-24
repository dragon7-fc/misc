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

**Constraints:**

* `1 <= capacity <= 10^4`
* `0 <= key <= 10^5`
* `0 <= value <= 10^9`
* At most `2 * 10^5` calls will be made to `get` and `put`.

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
Runtime: 449 ms
Memory: 190 MB
```
```c++
class LFUCache {
    unordered_map<int, list<vector<int>>::iterator> m;
    map<int, list<vector<int>>> freq;
    int cap;
    int size;
public:
    LFUCache(int capacity) {
        cap = capacity;
        size = 0;
    }
    
    int get(int key) {
        if (!m.count(key)) {
            return -1;
        }
        int value = (*(m[key]))[1], f = (*(m[key]))[2];
        freq[f].erase(m[key]);
        if (freq[f].empty()) {
            freq.erase(f);
        }
        f += 1;
        freq[f].push_front({key, value, f});
        m[key] = freq[f].begin();
        return value;
    }
    
    void put(int key, int value) {
        if (m.count(key)) {
            (*(m[key]))[1] = value;
            get(key);
        } else if (size < cap) {
            freq[1].push_front({key, value, 1});
            m[key] = freq[1].begin();
            size += 1;
        } else {
            int d_key = freq.begin()->second.back()[0];
            freq.begin()->second.pop_back();
            if (freq.begin()->second.empty()) {
                freq.erase(freq.begin());
            }
            m.erase(d_key);
            freq[1].push_front({key, value, 1});
            m[key] = freq[1].begin();
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

**Solution 4: (OrderedDict, Hash Table)**
```
Runtime: 806 ms
Memory: 79 MB
```
```python
class Node:
    def __init__(self, key, val, freq):
        self.key = key
        self.val = val
        self.freq = freq

class LFUCache:

    def __init__(self, capacity: int):
        self.node = {}
        self.freq = collections.defaultdict(collections.OrderedDict)
        self.cap = capacity
        self.min_freq = 0

    def get(self, key: int) -> int:
        if not key in self.node:
            return -1
        cur = self.node[key]
        del self.freq[cur.freq][key]
        if not self.freq[cur.freq]:
            del self.freq[cur.freq]
        cur.freq += 1
        self.freq[cur.freq][key] = cur
        if not self.freq[self.min_freq]:
            self.min_freq += 1
        return cur.val

    def put(self, key: int, value: int) -> None:
        if not self.cap:
            return
        if key in self.node:
            self.node[key].val = value
            self.get(key)
        else:
            if len(self.node) == self.cap:
                k, n = self.freq[self.min_freq].popitem(last=False)
                del self.node[k]
            new_node = Node(key, value, 1)
            self.node[key] = new_node
            self.freq[1][key] = new_node
            self.min_freq = 1
        

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```

**Solution 5: (Maintaining 2 HashMaps)**
```
Runtime: 420 ms
Memory: 180.2 MB
```
```c++
class LFUCache {
    // key: frequency, value: list of original key-value pairs that have the same frequency.
    unordered_map<int, list<pair<int, int>>> frequencies;
    // key: original key, value: pair of frequency and the iterator corresponding key in the
    // frequencies map's list.
    unordered_map<int, pair<int, list<pair<int, int>>::iterator>> cache;
    int capacity;
    int minf;

    void insert(int key, int frequency, int value) {
        frequencies[frequency].push_back({key, value});
        cache[key] = {frequency, --frequencies[frequency].end()};
    }
public:
    LFUCache(int capacity) : capacity(capacity), minf(0) {}
    
    int get(int key) {
        const auto it = cache.find(key);
        if (it == cache.end()) {
            return -1;
        }
        const int f = it->second.first;
        const auto iter = it->second.second;
        const pair<int, int> kv = *iter;
        frequencies[f].erase(iter);
        if (frequencies[f].empty()){
            frequencies.erase(f);

            if(minf == f) {
                ++minf;
            }
        }
        
        insert(key, f + 1, kv.second);
        return kv.second;
    }
    
    void put(int key, int value) {
        if (capacity <= 0) {
            return;
        }
        const auto it = cache.find(key);
        if (it != cache.end()) {
            it->second.second->second = value;
            get(key);
            return;
        }
        if (capacity == cache.size()) {
            cache.erase(frequencies[minf].front().first);
            frequencies[minf].pop_front();

            if(frequencies[minf].empty()) {
                frequencies.erase(minf);
            }
        }

        minf = 1;
        insert(key, 1, value);
    }
};

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache* obj = new LFUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
```

**Solution 6: (Hash Table, 2 Hash Table)**

LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
m:   (1,1)  // k,f
       |
cnt:   v
1:   (1,1) // f: (key, value)

lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
m:   (1,1) (2,1)  // k,f
       |     |
cnt:   v     v
1:   (1,1) (2,2) // f: (key, value)
lfu.get(1);      // return 1
                 // cache=[1,2], cnt(2)=1, cnt(1)=2
m:   (1,2) (2,1) // k,f
       |     |
cnt:   |     v
1:   (1|1)x(2,2) // f: (key, value)
       v
2:   (1,1)
lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
m:   (1,2) (2,1)x (3,1) // k,f
       |     |      |
cnt:   |     v      v
1:     |   (2,2)x (3,3) // f: (key, value)
       v
2:   (1,1)
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,1], cnt(3)=2, cnt(1)=2
m:   (1,2) (3,2) // k,f
       |     |
cnt:   |     |
1:     |   (3|3)x// f: (key, value)
       v     v
2:   (1,1) (3,3)
lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
   (4,1)         // cache=[4,3], cnt(4)=1, cnt(3)=2
m:   |1,2)x(3,2) // k,f
     | |     |
cnt: v |     |
1: (4,4)     |   // f: (key, value)
       v     v
2:   (1,1)x(3,3)
lfu.get(1);      // return -1 (not found)
m:  (4,1)  (3,2) // k,f
      |      |
cnt:  v      |
1:  (4,4)    |   // f: (key, value)
             v
2:         (3,3)
lfu.get(3);      // return 3
                 // cache=[3,4], cnt(4)=1, cnt(3)=3
m:  (4,1)  (3,3) // k,f
      |      |
cnt:  v      |
1:  (4,4)    |   // f: (key, value)
             |
2:         (3v3)x
3:         (3,3)
lfu.get(4);      // return 4
                 // cache=[4,3], cnt(4)=2, cnt(3)=3
m:  (4,2)  (3,3) // k,f
      |      |
cnt:  |      |
1:  (4|4)x   |   // f: (key, value)
      v      |
2:  (4,4)    v
3:         (3,3)

```
Runtime: 113 ms, Beats 66.14%
Memory: 187.73 MB, Beats 70.90%
```
```c++
class LFUCache {
    int n, mn = 0;
    unordered_map<int,list<pair<int,int>>> cnt;
    // f -> list{k, v}
    unordered_map<int,pair<int,list<pair<int,int>>::iterator>> m;
    // k -> f, list{k, v}->
public:
    LFUCache(int capacity) {
        n = capacity;
    }
    
    int get(int key) {
        if (!m.count(key)) {
            return -1;
        }
        auto [f, it] = m[key];
        auto [_, v] = *it;
        cnt[f].erase(it);
        if (cnt[f].size() == 0) {
            cnt.erase(f);
            if (mn == f) {
                mn += 1;
            }
        }
        f += 1;
        cnt[f].push_front({key, v});
        m[key] = {f, cnt[f].begin()};
        return v;
    }
    
    void put(int key, int value) {
        if (m.count(key)) {
            m[key].second->second = value;
            get(key);
        } else {
            if (m.size() == n) {
                auto [k, _] = cnt[mn].back();
                cnt[mn].pop_back();
                if (cnt[mn].size() == 0) {
                    cnt.erase(mn);
                }
                m.erase(k);
            }
            mn = 1;
            cnt[mn].push_front({key, value});
            m[key] = {mn, cnt[mn].begin()};
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
