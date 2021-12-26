705. Design HashSet

Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

* `add(value)`: Insert a value into the HashSet. 
* `contains(value)` : Return whether the value exists in the HashSet or not.
* `remove(value)`: Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

**Example:**
```
MyHashSet hashSet = new MyHashSet();
hashSet.add(1);         
hashSet.add(2);         
hashSet.contains(1);    // returns true
hashSet.contains(3);    // returns false (not found)
hashSet.add(2);          
hashSet.contains(2);    // returns true
hashSet.remove(2);          
hashSet.contains(2);    // returns false (already removed)
```

**Note:**

* All values will be in the range of `[0, 1000000]`.
* The number of operations will be in the range of `[1, 10000]`.
* Please do not use the built-in HashSet library.

# Submissions
---
**Solution 1: (Array)**
```
Runtime: 300 ms
Memory Usage: 41.2 MB
```
```python
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hs = [0]*1000001
        

    def add(self, key: int) -> None:
        self.hs[key] = 1

    def remove(self, key: int) -> None:
        self.hs[key] = 0

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self.hs[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
```

**Solution 2: (Array)**
```
Runtime: 180 ms
Memory Usage: 162.3 MB
```
```c++
class MyHashSet {
public:
    /** Initialize your data structure here. */
    vector<int> hs;
    MyHashSet() {
        hs.resize(1000000,0);
    }
    
    void add(int key) {
        hs[key]=1;
    }
    
    void remove(int key) {
        hs[key]=0;
    }
    
    /** Returns true if this set contains the specified element */
    bool contains(int key) {
        return hs[key];
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */
```

**Solution 3: (Array)**
```
Runtime: 72 ms
Memory Usage: 30.2 MB
```
```c



typedef struct {
    bool el[1000001];
} MyHashSet;


MyHashSet* myHashSetCreate() {
    MyHashSet *rst = calloc(1, sizeof(MyHashSet));
    return rst;
}

void myHashSetAdd(MyHashSet* obj, int key) {
    obj->el[key] = 1;
}

void myHashSetRemove(MyHashSet* obj, int key) {
    obj->el[key] = 0;
}

bool myHashSetContains(MyHashSet* obj, int key) {
    return obj->el[key];
}

void myHashSetFree(MyHashSet* obj) {
    free(obj);
}

/**
 * Your MyHashSet struct will be instantiated and called as such:
 * MyHashSet* obj = myHashSetCreate();
 * myHashSetAdd(obj, key);
 
 * myHashSetRemove(obj, key);
 
 * bool param_3 = myHashSetContains(obj, key);
 
 * myHashSetFree(obj);
*/
```

**Solution 4: (Linked List)**
```
Runtime: 92 ms
Memory Usage: 27.7 MB
```
```c
#define SIZE 500

typedef struct Node Node;
struct Node {
    int key;
	Node *next;
};

typedef struct {
    Node **table;
} MyHashSet;


MyHashSet* myHashSetCreate() {
    MyHashSet *obj = (MyHashSet*)malloc(sizeof(MyHashSet));
	obj -> table = (Node**)calloc(SIZE, sizeof(Node*));
    for(int i = 0; i < SIZE; i++){
        obj -> table[i] = calloc(1, sizeof(Node));
        obj -> table[i] -> key = -1;
    }
    return obj;
}

void myHashSetAdd(MyHashSet* obj, int key) {
    Node *nextNode = (Node*)malloc(sizeof(Node));
    nextNode->key = 0;
    nextNode->next = NULL;
    
    // add new key
    if(obj->table[key%SIZE]->key == -1){
        obj->table[key%SIZE]->key = key;
        obj->table[key%SIZE]->next = nextNode;
    }
    else{
        Node *curr = obj -> table[key%SIZE];
        while(curr->next != NULL){
            if(curr->key == key)
                return;

            curr = curr->next;
        }
        // add new key with the same key%SIZE (i.e. 1, 1001, 2001, 3001, ....)
        curr->key = key;
        curr->next = nextNode;
    }
}

void myHashSetRemove(MyHashSet* obj, int key) {
    Node *curr = obj->table[key%SIZE];
	Node *pre;
    
	if (curr && curr->key == key) {
		obj->table[key%SIZE] = curr->next;
        return;
	}
    while (curr) {
        // remove key with the same key%SIZE (i.e. 1, 1001, 2001, 3001, ....)
	    if(curr->key != key){
            pre = curr;
            curr = curr->next;
        }
        else{ // curr->key == key
            pre->next = curr->next;
            free(curr);
            return;
        }
	}
}

bool myHashSetContains(MyHashSet* obj, int key) {
    Node *curr = obj->table[key%SIZE];
	while (curr) {
		if (curr->key == key)
			return true;
        
		curr = curr->next;
	}
	return false;
}

void myHashSetFree(MyHashSet* obj) {
    for (int i = 0; i < SIZE; i++) {
	    free(obj->table[i]);
	}
    free(obj->table);
	free(obj);
}

/**
 * Your MyHashSet struct will be instantiated and called as such:
 * MyHashSet* obj = myHashSetCreate();
 * myHashSetAdd(obj, key);
 
 * myHashSetRemove(obj, key);
 
 * bool param_3 = myHashSetContains(obj, key);
 
 * myHashSetFree(obj);
*/
```
