223. Rectangle Area

Find the total area covered by two rectilinear rectangles in a **2D** plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

![223_rectangle_area](img/223_rectangle_area.png)

**Example:**
```
Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45
```

**Note:**

Assume that the total area is never beyond the maximum possible value of int.

# Submissions
---
**Solution 1:**
```
Runtime: 48 ms
Memory Usage: 12.6 MB
```
```python
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        return (C-A)*(D-B)+(G-E)*(H-F)-max(min(G, C) - max(A, E),0)*max(min(D,H) - max(B, F),0)
```