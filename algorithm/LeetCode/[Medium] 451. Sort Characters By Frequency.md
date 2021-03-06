451. Sort Characters By Frequency

Given a string, sort it in decreasing order based on the frequency of characters.

**Example 1:**
```
Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
```

**Example 2:**
```
Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
```

**Example 3:**
```
Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
```

# Submissions
---
**Solution 1: (Hash Table)**
```
Runtime: 36 ms
Memory Usage: 14.5 MB
```
```python
class Solution:
    def frequencySort(self, s: str) -> str:
        ans = []
        count = collections.Counter(s)
        for el, c in count.most_common():
            ans += [el] * c
            
        return ''.join(ans)
```

**Solution 2: (Heap)**
```
Runtime: 36 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def frequencySort(self, s: str) -> str:
        # count for char
        char2count = collections.Counter(s)
        
        # max heap, by - count
        heap = []
        for char, count in char2count.items():
            heapq.heappush(heap,(-count,char))
            
        # concatenate
        res = ''
        while heap:
            neg_c, char = heapq.heappop(heap)
            res += char*(-neg_c)
            
        return res
```