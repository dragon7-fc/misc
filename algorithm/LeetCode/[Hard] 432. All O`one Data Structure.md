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