1054. Distant Barcodes

In a warehouse, there is a row of `barcodes`, where the `i`-th barcode is `barcodes[i]`.

Rearrange the `barcodes` so that no two adjacent barcodes are equal.  You may return any answer, and it is guaranteed an answer exists.

 

**Example 1:**
```
Input: [1,1,1,2,2,2]
Output: [2,1,2,1,2,1]
```

**Example 2:**
```
Input: [1,1,1,1,2,2,3,3]
Output: [1,3,1,3,2,1,2,1]
``` 

**Note:**

* `1 <= barcodes.length <= 10000`
* `1 <= barcodes[i] <= 10000`
 
# Submissions
---
**Solution 1: (Sort)**
```
Runtime: 520 ms
Memory Usage: 15.1 MB
```
```python
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        N = len(barcodes)
        count = collections.Counter(barcodes)
        barcodes.sort(key=lambda x: (count[x], x))
        barcodes[1::2], barcodes[::2] = barcodes[:N//2], barcodes[N//2:]
        
        return barcodes
```

**Solution 2: (Sort)**
```
Runtime: 456 ms
Memory Usage: 15 MB
```
```python
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        N = len(barcodes)
        ans = [0]*N
        i = 0
        for k,v in collections.Counter(barcodes).most_common():
            for _ in range(v):
                ans[i] = k
                i += 2
                if i >= N:
                    i = 1
                    
        return ans
```