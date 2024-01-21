380. Insert Delete GetRandom O(1)

Design a data structure that supports all following operations in average **O(1)** time.

1. `insert(val)`: Inserts an item val to the set if not already present.
1. `remove(val)`: Removes an item val from the set if present.
1. `getRandom`: Returns a random element from current set of elements. Each element must have the **same probability** of being returned.

**Example:**
```
// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();
```

# Submissions
---
**Solution 1: (Hash Table, Array)**
```
Runtime: 1020 ms
Memory: 60 MB
```
```python
class RandomizedSet:

    def __init__(self):
        self.indices = {}
        self.a = []


    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        self.a += [val]
        self.indices[val] = len(self.a)-1
        return True


    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        i = self.indices[val]
        self.indices[self.a[-1]] = i
        self.a[i] = self.a[-1]
        self.indices.pop(val)
        self.a.pop()
        
        return True

    def getRandom(self) -> int:
        return self.a[random.randrange(len(self.a))]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
```

**Solution 2: (Hash Table, Array)**
```
Runtime: 178 ms
Memory: 97.34 MB
```
```c++
class RandomizedSet {
    vector<int> dp;
    unordered_map<int, int> m;
public:
    RandomizedSet() {
        
    }
    
    bool insert(int val) {
        if (m.count(val)) {
            return false;
        }
        m[val] = dp.size();
        dp.push_back(val);
        return true;
    }
    
    bool remove(int val) {
        if (!m.count(val)) {
            return false;
        }
        int i = m[val];
        dp[i] = dp.back();
        m[dp.back()] = i;
        m.erase(val);
        dp.pop_back();
        return true;
    }
    
    int getRandom() {
        return dp[rand()%dp.size()];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */
```
