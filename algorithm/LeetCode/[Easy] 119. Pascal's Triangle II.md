119. Pascal's Triangle II

Given a non-negative index k where k ≤ 33, return the $k^{th}$ index row of the Pascal's triangle.

Note that the row index starts from 0.

![PascalTriangleAnimated2](img/119_PascalTriangleAnimated2.gif)

In Pascal's triangle, each number is the sum of the two numbers directly above it.

**Example:**
```
Input: 3
Output: [1,3,3,1]
```

**Follow up:**

Could you optimize your algorithm to use only O(k) extra space?

# Submissions
---
**Solution 1: (DP)**
```
Runtime: 32 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev_row = []
        
        for row_number in range(rowIndex+1):
            row = [None for _ in range(row_number+1)]
            row[0], row[-1] = 1,1
            for column_number in range(1,len(row)-1):
                row[column_number] = prev_row[column_number-1] + prev_row[column_number]
            prev_row = row
        return prev_row
```
