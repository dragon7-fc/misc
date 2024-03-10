1238. Circular Permutation in Binary Representation

Given 2 integers `n` and `start`. Your task is return any permutation `p` of `(0,1,2.....,2^n -1)` such that :

* `p[0] = start`
* `p[i]` and `p[i+1]` differ by only one bit in their binary representation.
* `p[0]` and `p[2^n -1]` must also differ by only one bit in their binary representation.
 

**Example 1:**
```
Input: n = 2, start = 3
Output: [3,2,0,1]
Explanation: The binary representation of the permutation is (11,10,00,01). 
All the adjacent element differ by one bit. Another valid permutation is [3,1,0,2]
```

**Example 2:**
```
Input: n = 3, start = 2
Output: [2,6,7,5,4,0,1,3]
Explanation: The binary representation of the permutation is (010,110,111,101,100,000,001,011).
```

**Constraints:**

* 1 <= n <= 16
* 0 <= start < 2 ^ n

# Submissions
---
**Solution 1: (gray code)**

Gray code has the property that any two neighboring elements differ by only one bit. So we can map every number from 0 to 2^n - 1 to its Gray code, find the start element, and make the array circularly offset by index.

```
Runtime: 232 ms
Memory Usage: 21.5 MB
```
```python
class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        array = list(map(self.binaryToGray, range(0, 2 ** n)))
        index = array.index(start)

        return array[index: ] + array[: index]

    def binaryToGray(self, n: int) -> int:
        return n ^ (n >> 1)
```
