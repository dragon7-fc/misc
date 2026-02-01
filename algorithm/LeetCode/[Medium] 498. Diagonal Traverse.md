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
**Solution 1: (Diagonal Iteration and Reversal)**
```
Runtime: 192 ms
Memory Usage: 16.7 MB
```
```python
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        # Check for empty matrices
        if not matrix or not matrix[0]:
            return []
        
        # Variables to track the size of the matrix
        N, M = len(matrix), len(matrix[0])
        
        # The two arrays as explained in the algorithm
        result, intermediate = [], []
        
        # We have to go over all the elements in the first
        # row and the last column to cover all possible diagonals
        for d in range(N + M - 1):
            
            # Clear the intermediate array everytime we start
            # to process another diagonal
            intermediate.clear()
            
            # We need to figure out the "head" of this diagonal
            # The elements in the first row and the last column
            # are the respective heads.
            r, c = 0 if d < M else d - M + 1, d if d < M else M - 1
            
            # Iterate until one of the indices goes out of scope
            # Take note of the index math to go down the diagonal
            while r < N and c > -1:
                intermediate.append(matrix[r][c])
                r += 1
                c -= 1
            
            # Reverse even numbered diagonals. The
            # article says we have to reverse odd 
            # numbered articles but here, the numbering
            # is starting from 0 :P
            if d % 2 == 0:
                result.extend(intermediate[::-1])
            else:
                result.extend(intermediate)
        return result   
```

**Solution 2: (Simulation)**
```
Runtime: 200 ms
Memory Usage: 16.8 MB
```
```python
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        # Check for an empty matrix
        if not matrix or not matrix[0]:
            return []
        
        # The dimensions of the matrix
        N, M = len(matrix), len(matrix[0])
        
        # Incides that will help us progress through 
        # the matrix, one element at a time.
        row, column = 0, 0
        
        # As explained in the article, this is the variable
        # that helps us keep track of what direction we are
        # processing the current diaonal
        direction = 1
        
        # Final result array that will contain all the elements
        # of the matrix
        result = []
        
        # The uber while loop which will help us iterate over all
        # the elements in the array.
        while row < N and column < M:
            
            # First and foremost, add the current element to 
            # the result matrix. 
            result.append(matrix[row][column])
            
            # Move along in the current diagonal depending upon
            # the current direction.[i, j] -> [i - 1, j + 1] if 
            # going up and [i, j] -> [i + 1][j - 1] if going down.
            new_row = row + (-1 if direction == 1 else 1)
            new_column = column + (1 if direction == 1 else -1)
            
            # Checking if the next element in the diagonal is within the
            # bounds of the matrix or not. If it's not within the bounds,
            # we have to find the next head. 
            if new_row < 0 or new_row == N or new_column < 0 or new_column == M:
                
                # If the current diagonal was going in the upwards
                # direction.
                if direction:
                    
                    # For an upwards going diagonal having [i, j] as its tail
                    # If [i, j + 1] is within bounds, then it becomes
                    # the next head. Otherwise, the element directly below
                    # i.e. the element [i + 1, j] becomes the next head
                    row += (column == M - 1)
                    column += (column < M - 1)
                else:
                    
                    # For a downwards going diagonal having [i, j] as its tail
                    # if [i + 1, j] is within bounds, then it becomes
                    # the next head. Otherwise, the element directly below
                    # i.e. the element [i, j + 1] becomes the next head
                    column += (row == N - 1)
                    row += (row < N - 1)
                    
                # Flip the direction
                direction = 1 - direction        
            else:
                row = new_row
                column = new_column
                        
        return result
```

**Solution 3: (Array)**
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

**Solution 3: (Simulation)**

    1  2  3
    4  5  6
    7  8  7

case 1:
     ^  
    / 
    nr = r - 1
    nc = c + 1
case 2:
     /
    v
    nr = r + 1
    nc = c - 1

````
Runtime: 0 ms, Beats 100.00%
Memory: 22.67 MB, Beats 81.55%
```
```c++
class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& mat) {
        int m = mat.size(), n = mat[0].size(), i = 0, j = 0, ni, nj, k = 0, d = -1;
        vector<int> ans;
        i = 0;
        j = 0;
        while (k < m*n) {
            ans.push_back(mat[i][j]);
            ni = i + d;
            nj = j + d*(-1);
            if (ni < 0 || nj < 0 || ni == m || nj == n) {
                d *= -1;
                if (ni < 0) {
                    ni = 0;
                }
                if (nj == n) {
                    ni = i + 1;
                    nj = n-1;
                }
                if (nj < 0) {
                    nj = 0;
                }
                if (ni == m) {
                    ni = m-1;
                    nj = j + 1;
                }
            }
            i = ni;
            j = nj;
            k += 1;
        }
        return ans;
    }
};
```
