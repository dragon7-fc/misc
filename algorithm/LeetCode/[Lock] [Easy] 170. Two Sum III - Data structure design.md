170. Two Sum III - Data structure design

Design a data structure that accepts a stream of integers and checks if it has a pair of integers that sum up to a particular value.

Implement the `TwoSum` class:

* `TwoSum()` Initializes the `TwoSum` object, with an empty array initially.
* `void add(int number)` Adds `number` to the data structure.
* `boolean find(int value)` Returns `true` if there exists any pair of numbers whose sum is equal to value, otherwise, it returns `false`.
 

**Example 1:**
```
Input
["TwoSum", "add", "add", "add", "find", "find"]
[[], [1], [3], [5], [4], [7]]
Output
[null, null, null, null, true, false]

Explanation
TwoSum twoSum = new TwoSum();
twoSum.add(1);   // [] --> [1]
twoSum.add(3);   // [1] --> [1,3]
twoSum.add(5);   // [1,3] --> [1,3,5]
twoSum.find(4);  // 1 + 3 = 4, return true
twoSum.find(7);  // No two integers sum up to 7, return false
```

**Constraints:**

* `-105 <= number <= 105`
* `-231 <= value <= 231 - 1`
* At most `5 * 104` calls will be made to `add` and `find`.

# Submissions
---
**Solution 1: (HashTable, search key)**
```
Runtime: 352 ms
Memory Usage: 20.7 MB
```
```python
class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num_counts = collections.defaultdict(int)
        
    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.num_counts[number] += 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for num in self.num_counts.keys():
            comple = value - num
            if num != comple:
                if comple in self.num_counts:
                    return True
            elif self.num_counts[num] > 1:
                return True
        
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
```