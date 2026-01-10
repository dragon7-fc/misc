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

**Solution 2: (DP Bottom-Up)**

Use dynamic programming to keep track of `lo` and `hi` boundary of given max `h`eight at given point.

```
Runtime: 204 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0 #edge case 
        M, N = len(matrix), len(matrix[0])
        h, lo, hi = [0]*N, [0]*N, [N]*N
        ans = 0
        for i in range(M):
            left, right = 0, N
            for j in range(N):
                if matrix[i][j] == "1": #forward
                    h[j] += 1
                    lo[j] = max(lo[j], left)
                else: 
                    h[j] = lo[j] = 0
                    left = j+1
                    
                if matrix[i][~j] == "1": #backward
                    hi[~j] = min(hi[~j], right)
                else: 
                    hi[~j] = N
                    right = N - j - 1
            ans = max(ans, max((x-y)*z for x, y, z in zip(hi, lo, h)))
            
        return ans
```

**Solution 3: (DP Bottom-Up)**
```
Runtime: 20 ms
Memory Usage: 7.6 MB
```
```c
int maximalRectangle(char** matrix, int matrixSize, int* matrixColSize){
    if(matrixSize == 0 || *matrixColSize == 0)
        return 0;
    int height[*matrixColSize], left[*matrixColSize], right[*matrixColSize], result = 0;
    for(int i = 0; i < *matrixColSize; i++)
    {
        height[i] = 0;
        left[i] = 0;
        right[i] = *matrixColSize;
    }
    
    for(int i = 0; i< matrixSize; i++)
    {
        int curL = 0, curR = *matrixColSize;
        for(int j = 0; j < *matrixColSize; j++)
            if(matrix[i][j] == '1')
            {
                height[j]++;
                left[j] = left[j] > curL ? left[j] : curL;
            }
            else
            {
                height[j] = 0;
                left[j] = 0;
                curL = j + 1;
            }
        for(int j = *matrixColSize - 1; j >= 0; j--)
            if(matrix[i][j] == '1')
                right[j] = right[j] < curR ? right[j] : curR;
            else
            {
                right[j] = *matrixColSize;
                curR = j;
            }
        for(int j = 0; j < *matrixColSize; j++)
            result = result > (right[j] - left[j]) * height[j] ? result : (right[j] - left[j]) * height[j];
    }        
    return result;  
}
```

**Solution 4: (Stack, mono inc stack, area cover by current stack stop element)**


stk  
              x    ^
            xxx /  v
          /     
        /
            <-->  

            ["1",  "0",   "1",  "0",  "0"],
dp            1     0      1     0     0
stk  -1,-1  -1,-1 -1,-1 -1,-1 -1,-1  -1,-1
             1,0   1,0x
                   0,1   0,1   0,1x
                         1,2   1,2x
                               0,3     0,3x
                                       0,4
ans                 1           1
            ["1",   "0",   "1",  "1",  "1"],
dp            2      0      2     1     1
stk  -1,-1 -1,-1  -1,-1 -1,-1   -1,-1 -1,-1
            2,0    2,0x  0,1     0,1   0,1
                   0,1   2,2    2,2x
                                1,3    1,3x
                                       1,4
ans                 2            2     3
            ["1",  "1",  "1",  "1",  "1"],
dp            3     1     3     2     2
stk  -1,-1 -1,-1 -1,-1 -1,-1 -1,-1 -1,-1 -1,-1
            3,0   3,0x
                  1,1   1,1   1,1   1,1   1,1
                        3,2   3,2x
                              2,3   2,3x
                                    2,4   2,4x
                                          0,5
ans                                  4     6

            ["1","0","0","1","0"]

```
Runtime: 0 ms, Beats 100.00%
Memory: 17.42 MB, Beats 89.33%
```
```c++
class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        int m = matrix.size(), n = matrix[0].size(), i, j, ans = 0;
        vector<int> dp(n+1);
        stack<array<int,2>> stk;  // element, j
        stk.push({-1, -1});
        for (i = 0; i < m; i ++) {
            for (j = 0; j <= n; j ++) {
                if (j == n || matrix[i][j] == '0') {
                    dp[j] = 0;
                } else {
                    dp[j] += 1;
                }
            }
            for (j = 0; j <= n; j ++) {
                while (stk.size() > 1 && stk.top()[0] >= dp[j]) {
                    auto [a, _] = stk.top();
                    stk.pop();
                    ans = max(ans, a * (j - stk.top()[1] - 1));
                }
                stk.push({dp[j], j});
            }
            stk.pop();
        }
        return ans;
    }
};
```

**Solution 5: (Prefix Sum, left right)**

                0   1   2   3   4
    matrix = [["1","0","1","0","0"],
height          1       1
left            0       2
right           1       3        
cur             1       1
              ["1","0","1","1","1"],
height          2       2   1   1
left            0       2   2   2
right           1       3   5   5
cur             2       2   3   3 
              ["1","1","1","1","1"],
height          3   1   3   2   2
left            0   0   2   2   2
right           1   5   3   5   5
cur             3   5   3   6   6
                            ^   ^
              ["1","0","0","1","0"]]
height          4           3
left            0           3
right           1           4    
cur             4           3

```
Runtime: 2 ms, Beats 87.21%
Memory: 16.17 MB, Beats 97.94%
```
```c++
class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        if (matrix.empty()) return 0;
        int m = matrix.size();
        int n = matrix[0].size();
        vector<int> left(n), right(n), height(n);
        fill(right.begin(), right.end(), n);
        int maxarea = 0;
        for (int i = 0; i < m; i++) {
            int cur_left = 0, cur_right = n;
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == '1')
                    height[j]++;
                else
                    height[j] = 0;
            }
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == '1')
                    left[j] = max(left[j], cur_left);
                else {
                    left[j] = 0;
                    cur_left = j + 1;
                }
            }
            for (int j = n - 1; j >= 0; j--) {
                if (matrix[i][j] == '1')
                    right[j] = min(right[j], cur_right);
                else {
                    right[j] = n;
                    cur_right = j;
                }
            }
            for (int j = 0; j < n; j++) {
                maxarea = max(maxarea, (right[j] - left[j]) * height[j]);
            }
        }
        return maxarea;
    }
};
```

**Solution 6: (DP Bottom-Up)**
```
Runtime: 7 ms, Beats 58.75%
Memory: 16.26 MB, Beats 96.92%
```
```c++
class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        int m = matrix.size(), n = matrix[0].size(), i, j, j0, left = 0, ans = 0;
        vector<int> dp(n);
        for (j = 0; j < n; j ++) {
            if (matrix[0][j] == '1') {
                dp[j] = 1;
                left += 1;
                ans = max(ans, left);
            } else {
                left = 0;
            }
        }
        for (i = 1; i < m; i ++) {
            for (j = 0; j < n; j ++) {
                if (matrix[i][j] == '1') {
                    dp[j] += 1;
                    ans = max(ans, dp[j]);
                    left = dp[j];
                    for (j0 = j - 1; j0 >= 0; j0 --) {
                        left = min(left, dp[j0]);
                        if (left == 0) {
                            break;
                        }
                        ans = max(ans, left * (j - j0 + 1));
                    }
                } else {
                    dp[j] = 0;
                }
            }
        }
        return ans;
    }
};
```
