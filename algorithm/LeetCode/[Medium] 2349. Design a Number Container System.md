2349. Design a Number Container System

Design a number container system that can do the following:

* **Insert** or **Replace** a number at the given index in the system.
* **Return** the smallest index for the given number in the system.

Implement the `NumberContainers` class:

* `NumberContainers()` Initializes the number container system.
* `void change(int index, int number)` Fills the container at `index` with the number. If there is already a number at that `index, replace it.
* `int find(int number)` Returns the smallest index for the given `number`, or `-1` if there is no index that is filled by `number` in the system.
 

**Example 1:**
```
Input
["NumberContainers", "find", "change", "change", "change", "change", "find", "change", "find"]
[[], [10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]]
Output
[null, -1, null, null, null, null, 1, null, 2]

Explanation
NumberContainers nc = new NumberContainers();
nc.find(10); // There is no index that is filled with number 10. Therefore, we return -1.
nc.change(2, 10); // Your container at index 2 will be filled with number 10.
nc.change(1, 10); // Your container at index 1 will be filled with number 10.
nc.change(3, 10); // Your container at index 3 will be filled with number 10.
nc.change(5, 10); // Your container at index 5 will be filled with number 10.
nc.find(10); // Number 10 is at the indices 1, 2, 3, and 5. Since the smallest index that is filled with 10 is 1, we return 1.
nc.change(1, 20); // Your container at index 1 will be filled with number 20. Note that index 1 was filled with 10 and then replaced with 20. 
nc.find(10); // Number 10 is at the indices 2, 3, and 5. The smallest index that is filled with 10 is 2. Therefore, we return 2.
```

**Constraints:**

* `1 <= index, number <= 10^9`
* At most 10^5 calls will be made in total to `change` and `find`.

# Submissions
---
**Solution 1: (Hash Table, Heap)**
```
Runtime: 1193 ms
Memory Usage: 59.6 MB
```
```python
class NumberContainers:

    def __init__(self):
        self.numbersByIndex = {}
        self.numberIndexes = defaultdict(set)
        self.numberIndexesHeap = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        if index in self.numbersByIndex:
            if number != self.numbersByIndex[index]:
                self.numberIndexes[self.numbersByIndex[index]].remove(index)
                self.numbersByIndex[index] = number
                self.numberIndexes[number].add(index)
                heappush(self.numberIndexesHeap[number], index)
        else:
            self.numbersByIndex[index] = number
            self.numberIndexes[number].add(index)
            heappush(self.numberIndexesHeap[number], index)

    def find(self, number: int) -> int:
        while self.numberIndexesHeap[number] and self.numberIndexesHeap[number][0] not in self.numberIndexes[number]:
                heappop(self.numberIndexesHeap[number])  # make sure the smallest index in heap is still an index for number
        return self.numberIndexesHeap[number][0] if self.numberIndexesHeap[number] else -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
```

**Solution 2: (Hash Table, set)**
```
Runtime: 106 ms, Beats 74.38%
Memory: 195.80 MB, Beats 61.88%
```
```c++
class NumberContainers {
    unordered_map<int, int> m;  // index -> number, ex: 1 -> 12
    unordered_map<int, set<int>> dp;  // number -> index, ex: 12 -> {x x x ...}
public:
    NumberContainers() {
        
    }
    
    void change(int index, int number) {
        if (m.count(index)) {
            int pre = m[index];
            dp[pre].erase(index);
            if (!dp[pre].size()) {
                dp.erase(pre);
            }
        }
        m[index] = number;
        dp[number].insert(index);
    }
    
    int find(int number) {
        if (dp.count(number)) {
            return *dp[number].begin();
        } else {
            return -1;
        }
    }
};

/**
 * Your NumberContainers object will be instantiated and called as such:
 * NumberContainers* obj = new NumberContainers();
 * obj->change(index,number);
 * int param_2 = obj->find(number);
 */
```

**Solution 3: (Hash Table, heap, lazy update)**
```
Runtime: 88 ms, Beats 93.44%
Memory: 185.95 MB, Beats 84.69%
```
```c++
class NumberContainers {
    unordered_map<int, int> m;  // index -> number, ex: 1 -> 12
    unordered_map<int, priority_queue<int, vector<int>, greater<int>>> dp;  // number -> index, ex: 12 -> {x x x ...}
public:
    NumberContainers() {
        
    }
    
    void change(int index, int number) {
        m[index] = number;
        dp[number].push(index);
    }
    
    int find(int number) {
        while (dp[number].size()) {
            auto i = dp[number].top();
            if (m[i] == number) {
                return i;
            }
            dp[number].pop();
        }
        return -1;
    }
};

/**
 * Your NumberContainers object will be instantiated and called as such:
 * NumberContainers* obj = new NumberContainers();
 * obj->change(index,number);
 * int param_2 = obj->find(number);
 */
```
