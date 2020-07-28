498. Diagonal Traverse

Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

 

**Example:**
```
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Explanation:
```
![498_diagonal_traverse.png](img/498_diagonal_traverse.png)

**Note:**

* The total number of elements of the given matrix will not exceed `10,000`.

# Submissions
---
**Solution 1: (Array)**
```
Runtime: 312 ms
Memory Usage: 16.6 MB
```
```python
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        R, C = len(matrix), len(matrix[0])
        ans = [[] for _ in range(R+C-1)]
        for r in range(R):
            for c in range(C):
                if not (r+c)%2:
                    ans[r+c].insert(0, matrix[r][c])
                else:
                    ans[r+c].append(matrix[r][c])
                    
        return [_ for diag in ans for _ in diag]
```

**Solution 2 (Array)**
```
Runtime: 176 ms
Memory Usage: 18.4 MB
```
```c++
class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& matrix) {
        int m=matrix.size();
        vector<int>v;
        if(m==0)return v;
        int n=matrix[0].size();
        int i=0,j=0;
        for(int i=0;i<m+n-1;i++)
        {
            if(i&1)
            {
               for(int j=i;j>=0;j--)
               {
                   if(j<n&&i-j<m)
                   v.push_back(matrix[i-j][j]);
               }
            }
            else
            {
            for(int j=i;j>=0;j--)
                {
                    if(j<m&&(i-j)<n)
                       v.push_back(matrix[j][i-j]);
                }
            }
        }
        
        return v;
    }
};
```