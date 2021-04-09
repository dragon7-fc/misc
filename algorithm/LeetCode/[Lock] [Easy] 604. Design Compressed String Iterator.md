604. Design Compressed String Iterator

Design and implement a data structure for a compressed string iterator. The given compressed string will be in the form of each letter followed by a positive integer representing the number of this letter existing in the original uncompressed string.

Implement the StringIterator class:

* `next()` Returns **the next character** if the original string still has uncompressed characters, otherwise returns a **white space**.
* `hasNext()` Returns `true` if there is any letter needs to be uncompressed in the original string, otherwise returns `false`.
 

**Example 1:**
```
Input
["StringIterator", "next", "next", "next", "next", "next", "next", "hasNext", "next", "hasNext"]
[["L1e2t1C1o1d1e1"], [], [], [], [], [], [], [], [], []]
Output
[null, "L", "e", "e", "t", "C", "o", true, "d", true]

Explanation
StringIterator stringIterator = new StringIterator("L1e2t1C1o1d1e1");
stringIterator.next(); // return "L"
stringIterator.next(); // return "e"
stringIterator.next(); // return "e"
stringIterator.next(); // return "t"
stringIterator.next(); // return "C"
stringIterator.next(); // return "o"
stringIterator.hasNext(); // return True
stringIterator.next(); // return "d"
stringIterator.hasNext(); // return True
```

**Constraints:**

* `1 <= compressedString.length <= 1000`
* compressedString consists of lower-case an upper-case English letters and digits.
* The number of a single character repetitions in compressedString is in the range `[1, 10^9]`
* At most `100` calls will be made to next and hasNext.

# Submissions
---
**Solution 1: (String)**
```
Runtime: 48 ms
Memory Usage: 14.4 MB
```
```python
class StringIterator:

    def __init__(self, compressedString: str):
        self.s = []
        for w, d in re.findall(r"([a-zA-Z]+)(\d+)", compressedString):
            self.s += [[w, int(d)]]

    def next(self) -> str:
        if self.s:
            ret = self.s[0][0]
            self.s[0][1] -= 1
            if self.s[0][1] == 0:
                self.s.pop(0)
            return ret
        else:
            return " "

    def hasNext(self) -> bool:
        return self.s


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
```