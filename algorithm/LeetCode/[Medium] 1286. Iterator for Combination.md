1286. Iterator for Combination

Design an Iterator class, which has:

* A constructor that takes a string `characters` of sorted distinct lowercase English letters and a number `combinationLength` as arguments.
* A function `next()` that returns the next combination of length `combinationLength` in lexicographical order.
* A function `hasNext()` that returns `True` if and only if there exists a next combination.
 

**Example:**
```
CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.

iterator.next(); // returns "ab"
iterator.hasNext(); // returns true
iterator.next(); // returns "ac"
iterator.hasNext(); // returns true
iterator.next(); // returns "bc"
iterator.hasNext(); // returns false
```

**Constraints:**

* `1 <= combinationLength <= characters.length <= 15`
* There will be at most `10^4` function calls per test.
* It's guaranteed that all calls of the function next are valid.

# Submissions
---
**Solution 1:**
```
Runtime: 44 ms
Memory Usage: 14.6 MB
```
```python
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.it = itertools.combinations(characters, combinationLength)
        self.last = characters[-combinationLength:]
        self.hasNext = lambda: True

    def next(self) -> str:
        res = ''.join(list(next(self.it)))
        self.hasNext = lambda: res != self.last
        return res

    def hasNext(self) -> bool:
        return self.hasNext
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
```