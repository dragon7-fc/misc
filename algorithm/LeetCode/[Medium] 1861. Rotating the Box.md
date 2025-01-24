1861. Rotating the Box

You are given an `m x n` matrix of characters box representing a side-view of a box. Each cell of the box is one of the following:

* A stone `'#'`
* A stationary obstacle `'*'`
* Empty `'.'`

The box is rotated **90 degrees clockwise**, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the `box`. Gravity **does not** affect the obstacles' positions, and the inertia from the `box`'s rotation **does not** affect the stones' horizontal positions.

It is **guaranteed** that each stone in **box** rests on an obstacle, another stone, or the bottom of the box.

Return an `n x m` matrix representing the box after the rotation described above.

 

**Example 1:**


```
Input: box = [["#",".","#"]]
Output: [["."],
         ["#"],
         ["#"]]
```

**Example 2:**


```
Input: box = [["#",".","*","."],
              ["#","#","*","."]]
Output: [["#","."],
         ["#","#"],
         ["*","*"],
         [".","."]]
```

**Example 3:**


```
Input: box = [["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]]
Output: [[".","#","#"],
         [".","#","#"],
         ["#","#","*"],
         ["#","*","."],
         ["#",".","*"],
         ["#",".","."]]
```

**Constraints:**

* `m == box.length`
* `n == box[i].length`
* `1 <= m, n <= 500`
* `box[i][j]` is either `'#'`, `'*'`, or `'.'`.

# Submissions
---
**Solution 1: (Array, Shift stones then rotate)**
```
Runtime: 2352 ms
Memory Usage: 23.5 MB
```
```python
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for row in box:
            move_position = len(row) - 1             # initialize with the last position in row
            for j in range(len(row) - 1, -1, -1):    # iterate from the end of the row
                if row[j] == "*":                    # we cannot move stones behind obstacles,
                    move_position = j - 1            # so update move position to the first before obstacle
                elif row[j] == "#":                  # if stone, move it to the "move_position"
                    row[move_position], row[j] = row[j], row[move_position]
                    move_position -= 1

        return zip(*box[::-1])                       # rotate array
```

**Solution 2:(Array, rotate then shift, 2 step)**
```
Runtime: 185 ms
Memory: 56.39 MB
```
```c++
class Solution {
public:
    vector<vector<char>> rotateTheBox(vector<vector<char>>& box) {
        int m = box.size(), n = box[0].size(), i, j, k;
        vector<vector<char>> ans(n, vector<char>(m));
        for (i = 0; i < m; i ++) {
            for (j = 0; j < n; j ++) {
                ans[j][m-1-i] = box[i][j];
            }
        }
        for (i = 0; i < m; i ++) {
            k = n-1;
            for (j = n-1; j >= 0; j --) {
                if (ans[j][i] == '*') {
                    k = j-1;
                } else if (ans[j][i] == '#') {
                    swap(ans[k--][i], ans[j][i]);
                }
            }
        }
        return ans;
    }
};
```


**Solution 3:(Array, rotate and shift, 1 step)**
```
Runtime: 187 ms
Memory: 56.25 MB
```
```c++
class Solution {
public:
    vector<vector<char>> rotateTheBox(vector<vector<char>>& box) {
        int m = box.size(), n = box[0].size(), i, j, k;
        vector<vector<char>> ans(n, vector<char>(m, '.'));
        for (i = 0; i < m; i ++) {
            k = n-1;
            for (j = n-1; j >= 0; j --) {
                if (box[i][j] == '*') {
                    ans[j][m-1-i] = '*';
                    k = j-1;
                } else if (box[i][j] == '#') {
                    ans[k--][m-1-i] = '#';
                }
            }
        }
        return ans;
    }
};
```
