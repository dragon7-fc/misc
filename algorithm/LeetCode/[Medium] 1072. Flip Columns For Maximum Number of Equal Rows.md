1072. Flip Columns For Maximum Number of Equal Rows

Given a `matrix` consisting of 0s and 1s, we may choose any number of columns in the matrix and flip every cell in that column.  Flipping a cell changes the value of that cell from 0 to 1 or from 1 to 0.

Return the maximum number of rows that have all values equal after some number of flips.

 

**Example 1:**
```
Input: [[0,1],[1,1]]
Output: 1
Explanation: After flipping no values, 1 row has all values equal.
```

**Example 2:**
```
Input: [[0,1],[1,0]]
Output: 2
Explanation: After flipping values in the first column, both rows have equal values.
```

**Example 3:**
```
Input: [[0,0,0],[0,0,1],[1,1,0]]
Output: 2
Explanation: After flipping values in the first two columns, the last two rows have equal values.
``` 

**Note:**

* `1 <= matrix.length <= 300`
* `1 <= matrix[i].length <= 300`
* All `matrix[i].length`'s are equal
* `matrix[i][j]` is `0 `or `1`

# Submissions
---
**Solution 1:**

For every row there are two valid moves, either to make the row all zeros and make the row all ones. So we

* For every row find out what sequence of toggles would give us all zeros or all ones
* Add these sequences to a map keeping track of how many times each one occurs
* Whatever sequence is the most common is the answer

```
Runtime: 1744 ms
Memory Usage: 14.6 MB
```
```python
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        switchCount = collections.defaultdict(int)
        for row in matrix:
            oneList = []
            zeroList = []
            
            # for each row get indexes of zeros and ones,
            # this will be possible index flips we can make
            for i in range(len(row)):
                if row[i] == 1:
                    oneList.append(i)
                else:
                    zeroList.append(i)
            
            #count each set of index flips
            oneTuple = tuple(oneList)
            zeroTuple = tuple(zeroList)
            
            switchCount[oneTuple] += 1
            switchCount[zeroTuple] += 1
                
            
        # the flip sequence the was the most common is the answer
        ans = 0
        for val in switchCount.values():
            if val > ans:
                ans = val
                
        return ans 
```