777. Swap Adjacent in LR String

In a string composed of `'L'`, `'R'`, and `'X'` characters, like `"RXXLRXRXL"`, a move consists of either replacing one occurrence of `"XL"` with `"LX"`, or replacing one occurrence of `"RX"` with `"XR"`. Given the starting string `start` and the ending string `end`, return `True` if and only if there exists a sequence of moves to transform one string to the other.

**Example:**
```
Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
Output: True
Explanation:
We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX
```

**Note:**

* `1 <= len(start) = len(end) <= 10000`.
* Both `start` and `end` will only consist of characters in `{'L', 'R', 'X'}`.

# Submissions
---
**Solution 1: (Brainteaser, Two Pointers)**
```
Runtime: 40 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        i, j = 0, 0
        if(start == end): return True
        n = len(start)
        
        while i < n and j < n:
            while i < n - 1 and (start[i] == 'X'): i += 1
            while j < n -1 and (end[j] == 'X'): j += 1
            
            if (start[i] != end[j]): 
                return False
            
            if (start[i] == 'R' and j < i) or (start[i] == 'L' and i < j): 
                return False
            
            i += 1
            j += 1
            
        return True
        
```