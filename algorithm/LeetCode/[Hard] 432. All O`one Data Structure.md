432. All O`one Data Structure

Implement a data structure supporting the following operations:

* `Inc(Key)` - Inserts a new key with value 1. Or increments an existing key by 1. Key is guaranteed to be a **non-empty** string.
* `Dec(Key)` - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1. If the key does not exist, this function does nothing. Key is guaranteed to be a **non-empty** string.
* `GetMaxKey()` - Returns one of the keys with maximal value. If no element exists, return an empty string "".
* `GetMinKey()` - Returns one of the keys with minimal value. If no element exists, return an empty string "".

Challenge: Perform all these in O(1) time complexity.

# Submissions
---
**Solution 1: (Doubly linkedList, Set, Hash Table)**
```
Runtime: 116 ms
Memory Usage: 22.4 MB
```
```python
class Node:
    def __init__(self, val= 0):
        self.val = val
        self.next = None
        self.pre = None
        self.arr = set()
            
class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node()
        self.tail = Node()
        self.head.next, self.tail.pre = self.tail, self.head
        self.d = {}

    def move_forward(self, node, key):
        if node.val+1 != node.next.val:
            newNode = Node(node.val+1)
            newNode.pre, newNode.next = node, node.next
            newNode.pre.next = newNode.next.pre = newNode
        else:
            newNode = node.next
        newNode.arr.add(key)
        return newNode
    
    def pre(self, node, key):
        if node.val-1 != node.pre.val:
            newNode = Node(node.val-1)
            newNode.pre, newNode.next = node.pre, node
            newNode.pre.next = newNode.next.pre = newNode
        else:
            newNode = node.pre
        newNode.arr.add(key)
        return newNode
            
    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key not in self.d:
            node = self.head
        else:
            node = self.d[key]
            node.arr.discard(key)
            
        self.d[key] = self.move_forward(node, key)

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key in self.d:
            node = self.d[key]
            node.arr.discard(key)
            if node.val != 1:
                self.d[key] = self.pre(node, key)
            else:
                del self.d[key]

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        node = self.tail.pre
        while node and len(node.arr) == 0:
            node = node.pre
        
        if not node:
            return ""
        
        val = node.arr.pop()
        node.arr.add(val)
        return val

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        node = self.head.next
        while node and len(node.arr) == 0:
            node = node.next
        if not node:
            return ""
        
        val = node.arr.pop()
        node.arr.add(val)
        return val


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
```

**Solution 2: (Doubly linkedList, Hash Table)**
```
Runtime: 96 ms
Memory Usage: 25.8 MB
```
```c++
class AllOne {
public:
    
    struct Node {
        int freq;
        Node* next;
        Node* prev;
    };
    Node* makeNewNode(int freq){
        Node* node = new Node();
        node->freq = freq;
        node->prev = NULL;
        node->next = NULL;
        return node;
    }
    unordered_map<string,int> MAP;
    unordered_map<int,pair<Node*,unordered_set<string>>> FREQ;
    Node* head = NULL;
    Node* tail = NULL;
    AllOne() {
        
    }
    
    /** Inserts a new key <Key> with value 1. Or increments an existing key by 1. */
    void inc(string key) {
        if(MAP.find(key)==MAP.end()){
            MAP[key] = 1;
            if(FREQ.find(1)!=FREQ.end()){
                FREQ[1].second.insert(key);
            } else {
                Node* node = makeNewNode(1);
                if(head==NULL){
                    head = node;
                    tail = node;
                } else {
                    node->next = head;
                    head->prev = node;
                    head = node;  
                }
                FREQ[1].first = node;
                FREQ[1].second.insert(key);
            }   
        } else {            
            int freq = MAP[key];
            MAP[key]++;
            if(FREQ.find(freq+1)!=FREQ.end()){
                //found freq+1
                FREQ[freq+1].second.insert(key);                
            } else {
                Node* prevNode = FREQ[freq].first;
                Node* newNode = makeNewNode(freq+1);
                if(prevNode->next==NULL){
                    prevNode->next = newNode;
                    newNode->prev = prevNode;
                    tail = newNode;                    
                } else {
                    Node* temp = prevNode->next;
                    prevNode->next = newNode;
                    newNode->prev = prevNode;
                    newNode->next = temp;
                    temp->prev = newNode;                    
                }
                FREQ[freq+1].first = newNode;
                FREQ[freq+1].second.insert(key);
            }
            
            FREQ[freq].second.erase(key);
            if(FREQ[freq].second.size()==0){
                Node* todel = FREQ[freq].first;
                FREQ.erase(freq);
                if(todel->prev==NULL){
                    todel->next->prev = NULL;
                    head = todel->next;
                } else {
                    todel->prev->next = todel->next;
                    todel->next->prev = todel->prev; 
                }
            }
        }
    }
    
    /** Decrements an existing key by 1. If Key's value is 1, remove it from the data structure. */
    void dec(string key) {
        if(MAP.find(key)==MAP.end()) return;
        int freq = MAP[key];
        MAP[key]--;
        if(MAP[key]==0) MAP.erase(key);
        if(freq-1 == 0){
            FREQ[freq].second.erase(key);
            if(FREQ[freq].second.size()==0){
                Node* todel = FREQ[freq].first;
                FREQ.erase(freq);
                if(todel->next==NULL){
                    head = NULL;
                    tail = NULL;
                } else {
                    todel->next->prev = NULL;
                    head = todel->next;
                }
            }
        } else {
            if(FREQ.find(freq-1)!=FREQ.end()){
                //found freq-1
                FREQ[freq-1].second.insert(key);                
            } else {
                Node* nextNode = FREQ[freq].first;
                Node* newNode = makeNewNode(freq-1);
                if(nextNode->prev==NULL){
                    nextNode->prev = newNode;
                    newNode->next = nextNode;
                    head = newNode;                    
                } else {
                    Node* temp = nextNode->prev;
                    nextNode->prev = newNode;
                    newNode->next = nextNode;
                    newNode->prev = temp;
                    temp->next = newNode;                    
                }
                FREQ[freq-1].first = newNode;
                FREQ[freq-1].second.insert(key);
            }
                        
            FREQ[freq].second.erase(key);
            if(FREQ[freq].second.size()==0){
                Node* todel = FREQ[freq].first;
                FREQ.erase(freq);
                if(todel->next==NULL){
                    todel->prev->next = NULL;
                    tail = todel->prev;
                } else {
                    todel->prev->next = todel->next;
                    todel->next->prev = todel->prev; 
                }
            }  
        }
    }
    
    /** Returns one of the keys with maximal value. */
    string getMaxKey() {
        if(tail==NULL) return "";
        return (*FREQ[tail->freq].second.begin());
    }
    
    /** Returns one of the keys with Minimal value. */
    string getMinKey() {
        if(head==NULL) return "";
        return (*FREQ[head->freq].second.begin());
    }
};

/**
 * Your AllOne object will be instantiated and called as such:
 * AllOne* obj = new AllOne();
 * obj->inc(key);
 * obj->dec(key);
 * string param_3 = obj->getMaxKey();
 * string param_4 = obj->getMinKey();
 */
```


**Solution 3: (Using Doubly Linked List)**
```
Runtime: 97 ms
Memory: 61.49 MB
```
```c++
class Node {
public:
    int freq;
    Node* prev;
    Node* next;
    unordered_set<string> keys;

    Node(int freq) : freq(freq), prev(nullptr), next(nullptr) {}
};

class AllOne {
    Node* head;                        // Dummy head
    Node* tail;                        // Dummy tail
    unordered_map<string, Node*> map;  // Mapping from key to its node
    void removeNode(Node* node) {
        Node* prevNode = node->prev;
        Node* nextNode = node->next;

        prevNode->next = nextNode;  // Link previous node to next node
        nextNode->prev = prevNode;  // Link next node to previous node
     }
public:
    // Initialize your data structure here.
    AllOne() {
        head = new Node(0);  // Create dummy head
        tail = new Node(0);  // Create dummy tail
        head->next = tail;   // Link dummy head to dummy tail
        tail->prev = head;   // Link dummy tail to dummy head
    }
    
    // Inserts a new key <Key> with value 1. Or increments an existing key by 1.
    void inc(string key) {
        if (map.find(key) != map.end()) {
            Node* node = map[key];
            int freq = node->freq;
            node->keys.erase(key);  // Remove key from current node

            Node* nextNode = node->next;
            if (nextNode == tail || nextNode->freq != freq + 1) {
                // Create a new node if next node does not exist or freq is not
                // freq + 1
                Node* newNode = new Node(freq + 1);
                newNode->keys.insert(key);
                newNode->prev = node;
                newNode->next = nextNode;
                node->next = newNode;
                nextNode->prev = newNode;
                map[key] = newNode;
            } else {
                // Increment the existing next node
                nextNode->keys.insert(key);
                map[key] = nextNode;
            }

            // Remove the current node if it has no keys left
            if (node->keys.empty()) {
                removeNode(node);
            }
        } else {  // Key does not exist
            Node* firstNode = head->next;
            if (firstNode == tail || firstNode->freq > 1) {
                // Create a new node
                Node* newNode = new Node(1);
                newNode->keys.insert(key);
                newNode->prev = head;
                newNode->next = firstNode;
                head->next = newNode;
                firstNode->prev = newNode;
                map[key] = newNode;
            } else {
                firstNode->keys.insert(key);
                map[key] = firstNode;
            }
        }
    }
    
    // Decrements an existing key by 1. If Key's value is 1, remove it from the
    // data structure.
    void dec(string key) {
        if (map.find(key) == map.end()) {
            return;  // Key does not exist
        }

        Node* node = map[key];
        node->keys.erase(key);
        int freq = node->freq;

        if (freq == 1) {
            // Remove the key from the map if freq is 1
            map.erase(key);
        } else {
            Node* prevNode = node->prev;
            if (prevNode == head || prevNode->freq != freq - 1) {
                // Create a new node if the previous node does not exist or freq
                // is not freq - 1
                Node* newNode = new Node(freq - 1);
                newNode->keys.insert(key);
                newNode->prev = prevNode;
                newNode->next = node;
                prevNode->next = newNode;
                node->prev = newNode;
                map[key] = newNode;
            } else {
                // Decrement the existing previous node
                prevNode->keys.insert(key);
                map[key] = prevNode;
            }
        }

        // Remove the node if it has no keys left
        if (node->keys.empty()) {
            removeNode(node);
        }
    }
    
    // Returns one of the keys with maximal value.
    string getMaxKey() {
        if (tail->prev == head) {
            return "";  // No keys exist
        }
        return *(tail->prev->keys.begin());  // Return one of the keys from the
                                             // tail's previous node
    }
    
    // Returns one of the keys with minimal value.
    string getMinKey() {
         if (head->next == tail) {
            return "";  // No keys exist
        }
        return *(
            head->next->keys
                .begin());  // Return one of the keys from the head's next node
    }
};

/**
 * Your AllOne object will be instantiated and called as such:
 * AllOne* obj = new AllOne();
 * obj->inc(key);
 * obj->dec(key);
 * string param_3 = obj->getMaxKey();
 * string param_4 = obj->getMinKey();
 */
```

**Solution 4: (Counter, sorted map)**
```
Runtime: 80 ms, Beats 56.85%
Memory: 94.24 MB, Beats 40.74%
```
```c++
class AllOne {
    unordered_map<string, int> cnt;
    map<int,unordered_set<string>> dp;
public:
    // Initialize your data structure here.
    AllOne() {
        
    }
    
    // Inserts a new key <Key> with value 1. Or increments an existing key by 1.
    void inc(string key) {
        int a = cnt[key];
        if (a != 0) {
            dp[a].erase(key);
            if (dp[a].size() == 0) {
                dp.erase(a);
            }
        }
        cnt[key] = a+1;
        dp[a+1].insert(key);
    }

    // Decrements an existing key by 1. If Key's value is 1, remove it from the
    // data structure.
    void dec(string key) {
        int a = cnt[key];
        if (a > 1) {
            dp[a].erase(key);
            if (dp[a].size() == 0) {
                dp.erase(a);
            }
            cnt[key] = a-1;
            dp[a-1].insert(key);
        } else {
            cnt.erase(key);
            dp[a].erase(key);
            if (dp[a].size() == 0) {
                dp.erase(a);
            }
        }
    }
    
    // Returns one of the keys with maximal value.
    string getMaxKey() {
        if (dp.size() == 0) {
            return "";
        }
        return *dp.rbegin()->second.begin();
    }
    
    // Returns one of the keys with minimal value.
    string getMinKey() {
        if (dp.size() == 0) {
            return "";
        }
        return *dp.begin()->second.begin();
    }
};

/**
 * Your AllOne object will be instantiated and called as such:
 * AllOne* obj = new AllOne();
 * obj->inc(key);
 * obj->dec(key);
 * string param_3 = obj->getMaxKey();
 * string param_4 = obj->getMinKey();
 */
```

**Solution 5: (Counter, sorted set)**
```
Runtime: 103 ms, Beats 20.83%
Memory: 86.25 MB, Beats 79.54%
```
```c++
class AllOne {
    unordered_map<string, int> cnt;
    set<pair<int,string>> dp;
public:
    // Initialize your data structure here.
    AllOne() {
        
    }
    
    // Inserts a new key <Key> with value 1. Or increments an existing key by 1.
    void inc(string key) {
        int a = cnt[key];
        if (a) {
            dp.erase({a, key});
        }
        cnt[key] = a+1;
        dp.insert({a+1, key});
    }

    // Decrements an existing key by 1. If Key's value is 1, remove it from the
    // data structure.
    void dec(string key) {
        int a = cnt[key];
        dp.erase({a, key});
        if (a != 1) {
            cnt[key] = a-1;
            dp.insert({a-1, key});
        } else {
            cnt.erase(key);
        }
    }
    
    // Returns one of the keys with maximal value.
    string getMaxKey() {
        if (dp.size() == 0) {
            return "";
        }
        return dp.rbegin()->second;
    }
    
    // Returns one of the keys with minimal value.
    string getMinKey() {
        if (dp.size() == 0) {
            return "";
        }
        return dp.begin()->second;
    }
};

/**
 * Your AllOne object will be instantiated and called as such:
 * AllOne* obj = new AllOne();
 * obj->inc(key);
 * obj->dec(key);
 * string param_3 = obj->getMaxKey();
 * string param_4 = obj->getMinKey();
 */
```
