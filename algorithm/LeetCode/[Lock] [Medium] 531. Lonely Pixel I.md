531. Lonely Pixel I

Given a picture consisting of black and white pixels, find the number of **black** lonely pixels.

The picture is represented by a 2D char array consisting of 'B' and 'W', which means black and white pixels respectively.

A black lonely pixel is character 'B' that located at a specific position where the same row and same column don't have any other black pixels.

**Example:**
```
Input: 
[['W', 'W', 'B'],
 ['W', 'B', 'W'],
 ['B', 'W', 'W']]

Output: 3
Explanation: All the three 'B's are black lonely pixels.
```

**Note:**

* The range of width and height of the input 2D array is `[1,500]`.

# Submissions
---
**Solution 1: (Hash Table)**
```
Runtime: 488 ms
Memory Usage: 15 MB
```
```python
class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        dr, dc = collections.defaultdict(list), collections.defaultdict(list)
        ans = 0
        for r in range(len(picture)):
            for c in range(len(picture[0])):
                if picture[r][c] == 'B':
                    dr[r] += [c]
                    dc[c] += [r]
        for r in dr:
            if len(dr[r]) == 1 and len(dc[dr[r][0]]) == 1:
                ans += 1
        
        return ans
```

**Solution 1: (Array)**
```
Runtime: 484 ms
Memory Usage: 14.8 MB
```
```python
class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        rows = [[] for _ in range(len(picture[0]))]
        row_count = [0] * len(picture)

        for i in range(len(picture)):
            for j, pixel in enumerate(picture[i]):
                if pixel == 'B':
                    rows[j].append(i)
                    row_count[i] += 1

        return sum(len(r) == 1 and row_count[r[0]] == 1 for r in rows)
```