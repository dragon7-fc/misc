2166. Design Bitset

A Bitset is a data structure that compactly stores bits.

Implement the Bitset class:

* `Bitset(int size)` Initializes the Bitset with `size` bits, all of which are `0`.
* `void fix(int idx)` Updates the value of the bit at the index idx to `1`. If the value was already `1`, no change occurs.
* `void unfix(int idx)` Updates the value of the bit at the index idx to `0`. If the value was already `0`, no change occurs.
* `void flip()` Flips the values of each bit in the Bitset. In other words, all bits with value `0` will now have value `1` and vice versa.
* `boolean all()` Checks if the value of **each** bit in the Bitset is `1`. Returns `true` if it satisfies the condition, `false` otherwise.
* `boolean one()` Checks if there is **at least one** bit in the Bitset with value `1`. Returns `true` if it satisfies the condition, `false` otherwise.
* `int count()` Returns the **total number** of bits in the Bitset which have value `1`.
* `String toString()` Returns the current composition of the Bitset. Note that in the resultant string, the character at the `i`th index should coincide with the value at the `i`th bit of the Bitset.
 

**Example 1:**
```
Input
["Bitset", "fix", "fix", "flip", "all", "unfix", "flip", "one", "unfix", "count", "toString"]
[[5], [3], [1], [], [], [0], [], [], [0], [], []]
Output
[null, null, null, null, false, null, null, true, null, 2, "01010"]

Explanation
Bitset bs = new Bitset(5); // bitset = "00000".
bs.fix(3);     // the value at idx = 3 is updated to 1, so bitset = "00010".
bs.fix(1);     // the value at idx = 1 is updated to 1, so bitset = "01010". 
bs.flip();     // the value of each bit is flipped, so bitset = "10101". 
bs.all();      // return False, as not all values of the bitset are 1.
bs.unfix(0);   // the value at idx = 0 is updated to 0, so bitset = "00101".
bs.flip();     // the value of each bit is flipped, so bitset = "11010". 
bs.one();      // return True, as there is at least 1 index with value 1.
bs.unfix(0);   // the value at idx = 0 is updated to 0, so bitset = "01010".
bs.count();    // return 2, as there are 2 bits with value 1.
bs.toString(); // return "01010", which is the composition of bitset.
```

**Constraints:**

* `1 <= size <= 10^5`
* `0 <= idx <= size - 1`
* At most `10^5` calls will be made **in total** to `fix`, `unfix`, `flip`, `all`, `one`, `count`, and `toString`.
* At least one call will be made to `all`, `one`, `count`, or `toString`.
* At most `5` calls will be made to `toString`.

# Submissions
---
**Solution 1: (Keep status)**
```
Runtime: 752 ms
Memory Usage: 45.6 MB
```
```python
class Bitset:

    def __init__(self, size: int):
        self.l = [0] * size
        self.ones = 0
        self.flipp = False

    def fix(self, idx: int) -> None:
        if self.flipp:
            if self.l[idx] == 1: self.ones += 1
            self.l[idx] = 0
        else:
            if self.l[idx] == 0: self.ones += 1
            self.l[idx] = 1

    def unfix(self, idx: int) -> None:
        if self.flipp:
            if self.l[idx] == 0: self.ones -= 1
            self.l[idx] = 1
        else: 
            if self.l[idx] == 1: self.ones -= 1
            self.l[idx] = 0

    def flip(self) -> None:
        self.flipp = not self.flipp
        self.ones = len(self.l) - self.ones

    def all(self) -> bool:
        return self.ones == len(self.l)
    
    def one(self) -> bool:
        return self.ones > 0

    def count(self) -> int:
        return self.ones

    def toString(self) -> str:
        return ''.join([str(0 if i else 1) for i in self.l]) if self.flipp else ''.join([str(i) for i in self.l])


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()
```

**Solution 2: (Keep status)**
```
Runtime: 748 ms
Memory Usage: 196 MB
```
```c++
class Bitset {
public:
    string s, flipp;
    int ones = 0, siz = 0;
    
    Bitset(int size) {
        s = string(size, '0'); flipp = string(size, '1');
        siz = size;
    }
    
    void fix(int idx) {
        if(s[idx] == '0') ones++;  
        s[idx] = '1'; flipp[idx] = '0'; 
    }
    
    void unfix(int idx) {
        if(s[idx] == '1') ones--;
        s[idx] = '0'; flipp[idx] = '1';
    }
    
    void flip() {
        ones = siz - ones;
        s.swap(flipp);
    }
    
    bool all() {
        return ones == siz; 
    }
    
    bool one() {
        return ones;
    }
    
    int count() {
        return ones;
    }
    
    string toString() {
        return s;
    }
};

/**
 * Your Bitset object will be instantiated and called as such:
 * Bitset* obj = new Bitset(size);
 * obj->fix(idx);
 * obj->unfix(idx);
 * obj->flip();
 * bool param_4 = obj->all();
 * bool param_5 = obj->one();
 * int param_6 = obj->count();
 * string param_7 = obj->toString();
 */
```
