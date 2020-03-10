381. Insert Delete GetRandom O(1) - Duplicates allowed

Design a data structure that supports all following operations in average **O(1)** time.

**Note: Duplicate elements are allowed.**
1. `insert(val)`: Inserts an item val to the collection.
1. `remove(val)`: Removes an item val from the collection if present.
1. `getRandom`: Returns a random element from current collection of elements. The probability of each element being returned is **linearly related** to the number of same value the collection contains.

**Example:**
```
// Init an empty collection.
RandomizedCollection collection = new RandomizedCollection();

// Inserts 1 to the collection. Returns true as the collection did not contain 1.
collection.insert(1);

// Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
collection.insert(1);

// Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
collection.insert(2);

// getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
collection.getRandom();

// Removes 1 from the collection, returns true. Collection now contains [1,2].
collection.remove(1);

// getRandom should return 1 and 2 both equally likely.
collection.getRandom();
```

# Solution
---
**Intuition**

We must support three operations with duplicates:

1. insert
1. remove
1. getRandom

To getRandom in $O(1)$ and have it scale linearly with the number of copies of a value. The simplest solution is to store all values in a list. Once all values are stored, all we have to do is pick a random index.

We don't care about the order of our elements, so insert can be done in $O(1)$ using a dynamic array (`ArrayList` in Java or `list` in Python).

The issue we run into is how to go about an O(1) remove. Generally we learn that removing an element from an array takes a place in $O(N)$, unless it is the last element in which case it is $O(1)$.

The key here is that we don't care about order. For the purposes of this problem, if we want to remove the element at the ith index, we can simply swap the ith element and the last element, and perform an $O(1)$ pop (technically we don't have to swap, we just have to copy the last element into index i because it's popped anyway).

With this in mind, the most difficult part of the problem becomes finding the index of the element we have to remove. All we have to do is have an accompanying data structure that maps the element values to their index.

## Approach 1: ArrayList + HashMap
**Algorithm**

We will keep a list to store all our elements. In order to make finding the index of elements we want to remove $O(1)$, we will use a HashMap or dictionary to map values to all indices that have those values. To make this work each value will be mapped to a set of indices. The tricky part is properly updating the HashMap as we modify the list.

* `insert`: Append the element to the list and add the index to `HashMap[element]`.
* `remove`: This is the tricky part. We find the index of the element using the `HashMap`. We use the trick discussed in the intuition to remove the element from the list in $O(1)$. Since the last element in the list gets moved around, we have to update its value in the `HashMap`. We also have to get rid of the index of the element we removed from the `HashMap`.
* `getRandom`: Sample a random element from the list.

```python
from collections import defaultdict
from random import choice

class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lst = []
        self.idx = defaultdict(set)


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.idx[val].add(len(self.lst))
        self.lst.append(val)
        return len(self.idx[val]) == 1


    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if not self.idx[val]: return False
        remove, last = self.idx[val].pop(), self.lst[-1]
        self.lst[remove] = last
        self.idx[last].add(remove)
        self.idx[last].discard(len(self.lst) - 1)

        self.lst.pop()
        return True


    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return choice(self.lst)
```

**Complexity Analysis**

* Time complexity : $O(N)$, with $N$ being the number of operations. All of our operations are $O(1)$, giving $N * O(1) = O(N)$.

* Space complexity : $O(N)$, with $N$ being the number of operations. The worst case scenario is if we get $N$ add operations, in which case our `ArrayList` and our `HashMap` grow to size $N$.

# Submissions
---
**Solution: (ArrayList + HashMap)**
```
Runtime: 100 ms
Memory Usage: 18.2 MB
```
```python
class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lst = []
        self.idx = collections.defaultdict(set)

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.idx[val].add(len(self.lst))
        self.lst.append(val)
        return len(self.idx[val]) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if not self.idx[val]: return False
        remove, last = self.idx[val].pop(), self.lst[-1]
        self.lst[remove] = last
        self.idx[last].add(remove)
        self.idx[last].discard(len(self.lst) - 1)

        self.lst.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.lst)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
```