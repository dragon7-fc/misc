706. Design HashMap

Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

* `put(key, value)` : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
* `get(key)`: Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
* `remove(key)` : Remove the mapping for the value key if this map contains the mapping for the key.

**Example:**
```
MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);          
hashMap.put(2, 2);         
hashMap.get(1);            // returns 1
hashMap.get(3);            // returns -1 (not found)
hashMap.put(2, 1);          // update the existing value
hashMap.get(2);            // returns 1 
hashMap.remove(2);          // remove the mapping for 2
hashMap.get(2);            // returns -1 (not found) 
```

**Note:**

* All keys and values will be in the range of `[0, 1000000]`.
* The number of operations will be in the range of `[1, 10000]`.
* Please do not use the built-in HashMap library.

# Submissions
---
**Solution 1: (Array)**
```
Runtime: 1376 ms
Memory Usage: 39.1 MB
```
```python
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = [-1 for _ in range(1000001)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.buckets[key] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        return self.buckets[key]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        self.buckets[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
```

**Solution 2: (Array)**
```
Runtime: 144 ms
Memory Usage: 188 MB
```
```c



typedef struct {
    int el[1000001];
} MyHashMap;


MyHashMap* myHashMapCreate() {
    MyHashMap *rst = malloc(sizeof(MyHashMap));
    for (int i = 0; i < 1000001; i ++) {
        rst->el[i] = -1;
    }
    return rst;
}

void myHashMapPut(MyHashMap* obj, int key, int value) {
    obj->el[key] = value;
}

int myHashMapGet(MyHashMap* obj, int key) {
    return obj->el[key];
}

void myHashMapRemove(MyHashMap* obj, int key) {
    obj->el[key] = -1;
}

void myHashMapFree(MyHashMap* obj) {
    free(obj);
}

/**
 * Your MyHashMap struct will be instantiated and called as such:
 * MyHashMap* obj = myHashMapCreate();
 * myHashMapPut(obj, key, value);
 
 * int param_2 = myHashMapGet(obj, key);
 
 * myHashMapRemove(obj, key);
 
 * myHashMapFree(obj);
*/
```

**Solution 3: (Linked List)**
```
Runtime: 172 ms
Memory Usage: 51.3 MB
```
```c

#define CAPACITY 2048

typedef struct bucket {
    struct bucket *next; // for collision resolve
    uint32_t val;
} bucket;

typedef struct {
    bucket root[CAPACITY];
} MyHashMap;


MyHashMap* myHashMapCreate() {
    MyHashMap *hash_map = (MyHashMap *)malloc(sizeof(MyHashMap));
    bucket *root = hash_map->root;
    for (int i = 0; i < CAPACITY; i++)
    {
        root[i].next = NULL;
        root[i].val = 0xffffffff;
    }
    return hash_map;
}

int hash_function(int key)
{
    return key % CAPACITY;
}

void myHashMapPut(MyHashMap* obj, int key, int value) {
    // basically insert into a linked-list as a head
    bucket *current = obj->root + hash_function(key);
    bucket *prev = NULL;
    int index = key / CAPACITY;
    int i = 0;
    for (; i < index; i++)
    {
        prev = current;
        current = current->next;
        if (current == NULL)
        {
            current = (bucket *)malloc(sizeof(bucket));
            current->next = NULL;
            current->val = 0xffffffff;
            prev->next = current;
        }
    }
    current->val = value;
}

int myHashMapGet(MyHashMap* obj, int key) {
    // find an item and return the copy of the value
    int index = key / CAPACITY;
    bucket *current = obj->root + hash_function(key);
    for (int i = 0; i < index && current != NULL; i++)
    {
        current = current->next;
    }
    if (current)
    {
        return current->val;
    }
    
    return -1;
}

void myHashMapRemove(MyHashMap* obj, int key) {
    int index = key / CAPACITY;
    bucket *current = obj->root + hash_function(key);
    for (int i = 0; i < index && current != NULL; i++)
    {
        current = current->next;
    }
    if (current)
    {
        current->val = 0xffffffff;
    }
}

void myHashMapFree(MyHashMap* obj) {
    for (int i = 0; i < CAPACITY; i++)
    {
        bucket *item = (obj->root + i)->next;
        bucket *next = NULL;
        while (item)
        {
            next = item->next;
            free(item);
            item = next;
        }
    }
    free(obj);
}


/**
 * Your MyHashMap struct will be instantiated and called as such:
 * MyHashMap* obj = myHashMapCreate();
 * myHashMapPut(obj, key, value);
 
 * int param_2 = myHashMapGet(obj, key);
 
 * myHashMapRemove(obj, key);
 
 * myHashMapFree(obj);
*/
```
