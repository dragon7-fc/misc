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

**Solution 3: (Heap)**
```
Runtime: 544 ms
Memory Usage: 14.9 MB
```
```python
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        count = collections.Counter(barcodes)
        hq = []
        ans = []
        for bc, c in count.items():
            heapq.heappush(hq, (-c, bc))
        while len(hq) >= 2:
            c1, bc1 = heapq.heappop(hq)
            c2, bc2 = heapq.heappop(hq)
            ans.extend([bc1, bc2])
            if c1 + 1: heapq.heappush(hq, (c1 + 1, bc1))
            if c2 + 1: heapq.heappush(hq, (c2 + 1, bc2))
        
        return ans if not hq else ans + [hq[0][1]]

```