1198. Find Smallest Common Element in All Rows

Given a matrix `mat` where every row is sorted in **increasing** order, return the **smallest common element** in all rows.

If there is no common element, return -1.

 

**Example 1:**
```
Input: mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
Output: 5
```

**Constraints:**

* `1 <= mat.length, mat[i].length <= 500`
* `1 <= mat[i][j] <= 10^4`
* `mat[i]` is sorted in increasing order.

# Submissions
---
**Solution**
```
Runtime: 604 ms
Memory Usage: 39.1 MB
```
```python
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        dic = collections.defaultdict(int)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                dic[mat[i][j]] += 1
        common = [k for k in dic.keys() if dic[k] >= len(mat)]
        if common:
            return min(common)
        else:
            return -1
```
