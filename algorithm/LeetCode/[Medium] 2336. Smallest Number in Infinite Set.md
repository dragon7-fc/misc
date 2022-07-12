2336. Smallest Number in Infinite Set

You have a set which contains all positive integers `[1, 2, 3, 4, 5, ...]`.

Implement the `SmallestInfiniteSet` class:

* `SmallestInfiniteSet()` Initializes the **SmallestInfiniteSet** object to contain all positive integers.
* `int popSmallest()` **Removes** and returns the smallest integer contained in the infinite set.
* `void addBack(int num)` **Adds** a positive integer `num` back into the infinite set, if it is **not** already in the infinite set.
 

**Example 1:**
```
Input
["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
[[], [2], [], [], [], [1], [], [], []]
Output
[null, null, 1, 2, 3, null, 1, 4, 5]

Explanation
SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
smallestInfiniteSet.addBack(2);    // 2 is already in the set, so no change is made.
smallestInfiniteSet.popSmallest(); // return 1, since 1 is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 2, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 3, and remove it from the set.
smallestInfiniteSet.addBack(1);    // 1 is added back to the set.
smallestInfiniteSet.popSmallest(); // return 1, since 1 was added back to the set and
                                   // is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 4, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 5, and remove it from the set.
```

**Constraints:**

* `1 <= num <= 1000`
* At most `1000` calls will be made in total to `popSmallest` and `addBack`.

# Submissions
---
**Solution 1: (Set, Heap)**
```
Runtime: 132 ms
Memory Usage: 14.6 MB
```
```python
class SmallestInfiniteSet:

    def __init__(self):
        self.next_num = 1
        self.added_back_heap = []
        self.added_back_set = set()

    def popSmallest(self) -> int:
        if self.added_back_heap:
            smallest = heappop(self.added_back_heap)
            self.added_back_set.remove(smallest)
            return smallest
    
        num_to_return = self.next_num
        self.next_num += 1
        return num_to_return

    def addBack(self, num: int) -> None:
        if num < self.next_num and num not in self.added_back_set:
            self.added_back_set.add(num)
            heappush(self.added_back_heap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
```

**Solution 2: (Set)**
```
Runtime: 197 ms
Memory Usage: 46.3 MB
```
```c++
class SmallestInfiniteSet {
    set<int>st;
public:
    SmallestInfiniteSet() {
        for (int i = 1; i <= 1000; i ++)
            st.insert(i);
    }
    
    int popSmallest() {
        int rst = *(st.begin());
        st.erase(st.begin());
        return rst;
    }
    
    void addBack(int num) {
        st.insert(num);
    }
};

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * SmallestInfiniteSet* obj = new SmallestInfiniteSet();
 * int param_1 = obj->popSmallest();
 * obj->addBack(num);
 */
```
