780. Reaching Points

A move consists of taking a point `(x, y)` and transforming it to either `(x, x+y)` or `(x+y, y)`.

Given a starting point `(sx, sy)` and a target point `(tx, ty)`, return `True` if and only if a sequence of moves exists to transform the point `(sx, sy)` to `(tx, ty)`. Otherwise, return `False`.

**Examples:**
```
Input: sx = 1, sy = 1, tx = 3, ty = 5
Output: True
Explanation:
One series of moves that transforms the starting point to the target is:
(1, 1) -> (1, 2)
(1, 2) -> (3, 2)
(3, 2) -> (3, 5)
```

```
Input: sx = 1, sy = 1, tx = 2, ty = 2
Output: False
```

```
Input: sx = 1, sy = 1, tx = 1, ty = 1
Output: True
```

**Note:**

* `sx, sy, tx, ty` will all be integers in the range `[1, 10^9]`.

# Submissions
---
**Solution 1: (BFS, Time Limit Exceeded)**
```python
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        q = collections.deque([(sx, sy)])
        while q:
            x, y = q.pop()
            if x == tx and y == ty:
                return True
            if x > tx or y > ty:
                continue
            for nei in [(x+y, y), (x, x+y)]:
                q.appendleft(nei)
                
        return False
```

**Solution 2: (Math)**
```
Runtime: 32 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if tx == 0 or ty == 0: return (sx, sy) == (tx, ty)
        while not (sx == tx and sy == ty):
            if sx > tx or sy > ty: return False
            elif tx == ty: return ((0, ty) == (sx, sy) or (tx, 0) == (sx, sy))
            
            if ty > tx: 
                if tx == sx: return (ty - sy)%sx == 0
                ty %= tx
            else: 
                if ty == sy: return (tx-sx)%sy == 0
                tx %= ty
                     
        return True
```