533. Lonely Pixel II

Given a picture consisting of black and white pixels, and a positive integer `N`, find the number of black pixels located at some specific row **R** and column **C** that align with all the following rules:

1. Row `R` and column `C` both contain exactly `N` black pixels.
1. For all rows that have a black pixel at column `C`, they should be exactly the same as row `R`

The picture is represented by a 2D char array consisting of 'B' and 'W', which means black and white pixels respectively.

**Example:**
```
Input:                                            
[['W', 'B', 'W', 'B', 'B', 'W'],    
 ['W', 'B', 'W', 'B', 'B', 'W'],    
 ['W', 'B', 'W', 'B', 'B', 'W'],    
 ['W', 'W', 'B', 'W', 'B', 'W']] 

N = 3
Output: 6
Explanation: All the bold 'B' are the black pixels we need (all 'B's at column 1 and 3).
        0    1    2    3    4    5         column index                                            
0    [['W', 'B', 'W', 'B', 'B', 'W'],    
1     ['W', 'B', 'W', 'B', 'B', 'W'],    
2     ['W', 'B', 'W', 'B', 'B', 'W'],    
3     ['W', 'W', 'B', 'W', 'B', 'W']]    
row index

Take 'B' at row R = 0 and column C = 1 as an example:
Rule 1, row R = 0 and column C = 1 both have exactly N = 3 black pixels. 
Rule 2, the rows have black pixel at column C = 1 are row 0, row 1 and row 2. They are exactly the same as row R = 0.
```

**Note:**

* The range of width and height of the input 2D array is `[1,200]`.

# Submissions
---
**Solution 1: (Array)**
```
Runtime: 476 ms
Memory Usage: 14.2 MB
```
```python
class Solution:
    def findBlackPixel(self, picture: List[List[str]], N: int) -> int:
        count=0
        for col in zip(*picture):
            if col.count("B") == N:
                if picture[col.index("B")].count("B") == N and picture.count(picture[col.index("B")]) == N: count  += 1
        return count*N
```

**Solution 2: (Array)**
```
Runtime: 160 ms
Memory Usage: 18.3 MB
```
```c++
class Solution {
private:
    bool rowsEqual(const vector<vector<char>>& picture, const vector<int> & indexes) {
        for (int i = 1; i < indexes.size(); ++i) {
            for (int j = 0; j < picture[0].size(); ++j) {
                if (picture[indexes[i]][j] != picture[indexes[0]][j]) {
                    return false;
                }
            }
        }
        return true;
    }
public:
    int findBlackPixel(vector<vector<char>>& picture, int N) {
        const int m = picture.size(), n = picture[0].size();
        
        vector<int> indexes; // max size N
        // scan rows and mark black:
        for (int i = 0; i < m; ++i) {
            indexes.clear();
            for (int j = 0; j < n; ++j) {
                if (picture[i][j] == 'W') {
                    continue;
                }
                if (indexes.size() == N) {
                    indexes.clear();
                    break;
                }
                indexes.push_back(j);
            }
            
            if (indexes.size() == N) {
                for (int j : indexes) {
                    picture[i][j] = 'X';
                }
            }
        }
        
        int ans = 0;
        // scan cols and count:
        for (int j = 0; j < n; ++j) {
            indexes.clear();
            for (int i = 0; i < m; ++i) {
                if (picture[i][j] == 'W') {
                    continue;
                }
                if (indexes.size() == N) {
                    indexes.clear();
                    break;
                }
                indexes.push_back(i);
            }
            
            for (int i : indexes) {
                if (picture[i][j] != 'X') {
                    indexes.clear();
                    break;
                }
            }
                        
            if (indexes.size() == N && rowsEqual(picture, indexes)) {
                ans += N;
            }
        }
        
        return ans;
    }
};
```
