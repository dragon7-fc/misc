1286. Iterator for Combination

Design an Iterator class, which has:

* A constructor that takes a string `characters` of **sorted distinct** lowercase English letters and a number `combinationLength` as arguments.
* A function `next()` that returns the next combination of length `combinationLength` in **lexicographical order**.
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
**Solution 1: (itertools)**
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

**Solution 2: (Backtracking)**
```
Runtime: 56 ms
Memory Usage: 15 MB
```
```python
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.c = characters
        self.n = combinationLength
        self.i = 0
        self.ans = []
        self.permute(0, '')

    def permute(self, index, path):
        if len(path) == self.n:
            self.ans.append(path)
            return
        else:
            for i in range(index, len(self.c)):
                self.permute(i + 1, path + self.c[i])
                
    def next(self) -> str:
        ans = self.ans[self.i]
        self.i += 1
        return ans

    def hasNext(self) -> bool:
        return self.i < len(self.ans)


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
```

**Solution 3: (Backtracking)**
```
Runtime: 60 ms
Memory Usage: 15.9 MB
```
```python
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combinations = []
        n, k = len(characters), combinationLength

        def backtrack(first = 0, curr = []):
                # if the combination is done
                if len(curr) == k:  
                    self.combinations.append(''.join(curr[:]))
                    # speed up by non-constructing combinations 
                    # with more than k elements
                    return 
                for i in range(first, n):
                    # add i into the current combination
                    curr.append(characters[i])
                    # use next integers to complete the combination
                    backtrack(i + 1, curr)
                    # backtrack
                    curr.pop()

        backtrack()
        self.combinations.reverse()
                
    def next(self) -> str:
        return self.combinations.pop()

    def hasNext(self) -> bool:
        return self.combinations


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
```

**Solution 4: (Bitmasking: Precomputation)**
```
Runtime: 76 ms
Memory Usage: 16 MB
```
```python
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combinations = []
        n, k = len(characters), combinationLength

        # generate bitmasks from 0..00 to 1..11  
        for bitmask in range(1 << n):
            # use bitmasks with k 1-bits
            if bin(bitmask).count('1') == k:
                # convert bitmask into combination
                # 111 --> "abc", 000 --> ""
                # 110 --> "ab", 101 --> "ac", 011 --> "bc"
                curr = [characters[j] for j in range(n) if bitmask & (1 << n - j - 1)]
                self.combinations.append(''.join(curr))
                
    def next(self) -> str:
        return self.combinations.pop()

    def hasNext(self) -> bool:
        return self.combinations


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
```

**Solution 5: (Bitmasking: Next Combination)**
```
Runtime: 68 ms
Memory Usage: 15.6 MB
```
```python
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.n = n = len(characters)
        self.k = k = combinationLength
        self.chars = characters

        # generate first bitmask 1(k)0(n - k)
        self.b = (1 << n) - (1 << n - k)
                
    def next(self) -> str:
        # convert bitmasks into combinations
        # 111 --> "abc", 000 --> ""
        # 110 --> "ab", 101 --> "ac", 011 --> "bc"
        curr = [self.chars[j] for j in range(self.n) if self.b & (1 << self.n - j - 1)]
        
        # generate next bitmask
        self.b -= 1
        while self.b > 0 and bin(self.b).count('1') != self.k:
            self.b -= 1
        
        return ''.join(curr)

    def hasNext(self) -> bool:
        return self.b > 0


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
```

**Solution 6: (Algorithm L by D. E. Knuth: Lexicographic Combinations: Precomputation)**
```
Runtime: 60 ms
Memory Usage: 16 MB
```
```python
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combinations = []
        n, k = len(characters), combinationLength
        
        # init the first combination
        nums = list(range(k)) + [n]
        
        j = 0
        while j < k:
            # add current combination
            curr = [characters[n - 1 - nums[i]] for i in range(k - 1, -1, -1)]
            self.combinations.append(''.join(curr))
            
            # Generate next combination.
            # Find the first j such that nums[j] + 1 != nums[j + 1].
            # Increase nums[j] by one.
            j = 0
            while j < k and nums[j + 1] == nums[j] + 1:
                nums[j] = j
                j += 1
            nums[j] += 1
                
    def next(self) -> str:
        return self.combinations.pop()

    def hasNext(self) -> bool:
        return self.combinations


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
```

**Solution 7: (Algorithm L by D. E. Knuth: Lexicographic Combinations: Next Combination)**
```
Runtime: 48 ms
Memory Usage: 15.7 MB
```
```python
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.n = len(characters)
        self.k = k = combinationLength
        self.chars = characters
        
        # init the first combination
        self.nums = list(range(k))
        self.has_next = True
                
    def next(self) -> str:
        nums = self.nums
        n, k = self.n, self.k
        curr = [self.chars[j] for j in nums]
        
        # Generate next combination.
        # Find the first j such that nums[j] != n - k + j.
        # Increase nums[j] by one.
        j = k - 1
        while j >= 0 and nums[j] == n - k + j:
            j -= 1 
        nums[j] += 1
        
        if j >= 0:
            for i in range(j + 1, k):
                nums[i] = nums[j] + i - j
        else:
            self.has_next = False
        
        return ''.join(curr)

    def hasNext(self) -> bool:
        return self.has_next

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
```