421. Maximum XOR of Two Numbers in an Array

Given a non-empty array of numbers, `a0, a1, a2, … , an-1`, where `0 ≤ ai < 231`.

Find the maximum result of `ai XOR aj`, where `0 ≤ i, j < n`.

Could you do this in O(n) runtime?

**Example:**
```
Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.
```

# Submissions
---
**Solution 1: (Bit Manipulation, Trie)**

The goal is to find 2 numbers in num that will produce the largest XOR, e.g. a number that has the most 1's to the left in its binary representation. We can do this by first building a trie that represents the binary form of the numbers in nums, then, for each num in nums, traverse the trie to find the number that will produce the largest XOR with it.

```
Runtime: 404 ms
Memory Usage: 105.1 MB
```
```python
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        # need to know the largest binary representation
        # bin prepends '0b', ignore
        L = len(bin(max(nums))) - 2

        # preprocess step - left-pad zeros to ensure each number has L bits
        # (x >> i) & 1 produces the bit at position i for number x
        # x's value is moved right by i bits, we & 1 to produce 0 or 1
        # e.g., if L = 5, then 3 = [0, 0, 0, 1, 1], so the steps to get there are:
        # (3 >> 4) & 1 = 0
        # (3 >> 3) & 1 = 0
        # (3 >> 2) & 1 = 0
        # (3 >> 1) & 1 = 1
        # (3 >> 0) & 1 = 1
        nums_bits = [[(x >> i) & 1 for i in reversed(range(L))] for x in nums]
        root = {}
        # build the trie
        for num, bits in zip(nums, nums_bits):
            node = root
            for bit in bits:
                node = node.setdefault(bit, {})
            node["#"] = num

        max_xor = 0
        for num, bits in zip(nums, nums_bits):
            node = root
            # we want to find the node that will produce the largest XOR with num
            for bit in bits:
                # our goal is to find the opposite bit, e.g. bit = 0, we want 1
                # this is our goal because we want as many 1's as possible
                toggled_bit = 1 - bit
                if toggled_bit in node:
                    node = node[toggled_bit]
                else:
                    node = node[bit]
            # we're at a leaf node, now we can do the XOR computation
            max_xor = max(max_xor, node["#"] ^ num)


        return max_xor
```