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