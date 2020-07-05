1504. Count Submatrices With All Ones

Given a `rows` * `columns` matrix `mat` of ones and zeros, return how many **submatrices** have all ones.

 

**Example 1:**
```
Input: mat = [[1,0,1],
              [1,1,0],
              [1,1,0]]
Output: 13
Explanation:
There are 6 rectangles of side 1x1.
There are 2 rectangles of side 1x2.
There are 3 rectangles of side 2x1.
There is 1 rectangle of side 2x2. 
There is 1 rectangle of side 3x1.
Total number of rectangles = 6 + 2 + 3 + 1 + 1 = 13.
```

**Example 2:**
```
Input: mat = [[0,1,1,0],
              [0,1,1,1],
              [1,1,1,0]]
Output: 24
Explanation:
There are 8 rectangles of side 1x1.
There are 5 rectangles of side 1x2.
There are 2 rectangles of side 1x3. 
There are 4 rectangles of side 2x1.
There are 2 rectangles of side 2x2. 
There are 2 rectangles of side 3x1. 
There is 1 rectangle of side 3x2. 
Total number of rectangles = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24.
```

**Example 3:**
```
Input: mat = [[1,1,1,1,1,1]]
Output: 21
```

**Example 4:**
```
Input: mat = [[1,0,1],[0,1,0],[1,0,1]]
Output: 5
```

**Constraints:**

* `1 <= rows <= 150`
* `1 <= columns <= 150`
* `0 <= mat[i][j] <= 1`

# Submissions
---
**Solution 1: (Brute Force)**
```
Runtime: 640 ms
Memory Usage: 14.2 MB
```
```python
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        if not mat: return 0
        rows = len(mat)
        cols = len(mat[0])
        n = 0
        for top in range(rows):
            for left in range(cols):
                bottom = rows
                for right in range(left, cols):
                    scan = top
                    while scan < bottom and mat[scan][right]: scan += 1
                    bottom = scan
                    n += bottom - top
                    if bottom == top: break
        return n
```

**Solution 2: (DP Bottom-Up)**

dp[m][n]: is the number of left ones starting from (m,n)
->we first pre-calculate dp[m][n]
->we then spend O(n)*O(m^2) of time to find the maximum number of rectangles we can make with the bottom-right corner being mat[i][j]
->each row of an rectangle should be the same length (so the minimum number of the left ones on a straight line is the number of rectangle that can be made with that line height)

```
Runtime: 88 ms
Memory Usage: 13.6 MB
```
```c++
class Solution {
public:
    int numSubmat(vector<vector<int>>& mat) {
        int result=0;
        int m=mat.size(),n=mat[0].size();
        int dp[m][n];
        memset(dp,0,sizeof(dp));
        for(int i=0;i<m;i++) //calculate dp[m][n]
        {
            for(int j=0;j<n;j++)
            {
                if(j==0)
                {
                    dp[i][j]=mat[i][j]; 
                }
                else
                {
                    if(mat[i][j]==0)
                    {
                        dp[i][j]=0;//no consecutive left zeroes starting from mat[i][j]
                    }
                    else
                    {
                        dp[i][j]=dp[i][j-1]+1;//count consecutive left zeroes
                    }
                }
            }
        }
        for(int j=0;j<n;j++) //from left to right
        {
            for(int i=0;i<m;i++) //from top to bottom
            {
                int minimum=dp[i][j];
                for(int k=i;k>-1;k--) //from i to top (count the number of rectangles that can be made)
                {
                    minimum=min(minimum,dp[k][j]);//the number of rectangles that can be made with the right edge extended from mat[i][j] to mat[k][j]
                    if(minimum==0)
                    {
                        break;
                    }
                    result+=minimum;
                }
            }
        }
        return result;
    }
};
```