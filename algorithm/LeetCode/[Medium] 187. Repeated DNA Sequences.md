187. Repeated DNA Sequences

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

**Example:**
```
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]
```

# Submissions
---
**Solution 1: (Hash Table)**
```
Runtime: 52 ms
Memory Usage: 29.3 MB
```
```python
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        table = {}
        ret = []
        for index, num in enumerate(s):
            pattern = s[index:index+10]            
            if pattern in table:
                ret.append(pattern)
            else:
                table[pattern] = index
        return list(set(ret))
```