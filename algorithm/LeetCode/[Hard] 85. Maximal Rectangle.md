85. Maximal Rectangle

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

**Example:**
```
Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
```

# Submissions
---
**Solution 1: (Stack)**

Basically, it is same as previous problem which calculate max rectangular area in histogram

One more step we need to do in this problem is  
calculating heights for each rows and call function for finding max area given heights list

If you don't understand previous problem, see link below  
https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/510500/python-using-stack

```
Runtime: 212 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        def calArea(heights):
            stack, max_area = [-1], 0
            for i, h in enumerate(heights + [-1]):
                while stack and stack[-1] >= 0 and h <= heights[stack[-1]]:
                    max_area = max(heights[stack.pop()] * (i - stack[-1] - 1), max_area)
                stack.append(i)
            return max_area
        
        heights = [0] * len(matrix[0])
        ret = 0
        
        for row in matrix:
            for i, v in enumerate(row):
                heights[i] = heights[i]+1 if v == '1' else 0
            maA = calArea(heights)
            ret = max(ret, maA)
            
            
        return ret
```