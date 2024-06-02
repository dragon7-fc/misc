3078. Match Alphanumerical Pattern in Matrix I

You are given a 2D integer matrix `board` and a 2D character matrix `pattern`. Where `0 <= board[r][c] <= 9` and each element of `pattern` is either a digit or a lowercase English letter.

Your task is to find **asubmatrix** of board that matches `pattern`.

An integer matrix `part` matches `pattern` if we can replace cells containing letters in `pattern` with some digits (each **distinct** letter with a **unique** digit) in such a way that the resulting matrix becomes identical to the integer matrix part. In other words,

* The matrices have identical dimensions.
* If `pattern[r][c]` is a digit, then `part[r][c]` must be the same digit.
* If `pattern[r][c]` is a letter `x`:
    * For every `pattern[i][j] == x`, `part[i][j]` must be the same as `part[r][c].`
    * For every `pattern[i][j] != x`, `part[i][j]` must be different than `part[r][c]`.

Return an array of length `2` containing the row number and column number of the upper-left corner of a submatrix of board which matches pattern. If there is more than one such submatrix, return the coordinates of the submatrix with the lowest row index, and in case there is still a tie, return the coordinates of the submatrix with the lowest column index. If there are no suitable answers, return `[-1, -1]`.

 

**Example 1:**
```
1	2	2
2	2	3
2	3	3
a	b
b	b
Input: board = [[1,2,2],[2,2,3],[2,3,3]], pattern = ["ab","bb"]

Output: [0,0]

Explanation: If we consider this mapping: "a" -> 1 and "b" -> 2; the submatrix with the upper-left corner (0,0) is a match as outlined in the matrix above.

Note that the submatrix with the upper-left corner (1,1) is also a match but since it comes after the other one, we return [0,0].
```

**Example 2:**
```
1	1	2
3	3	4
6	6	6
a	b
6	6
Input: board = [[1,1,2],[3,3,4],[6,6,6]], pattern = ["ab","66"]

Output: [1,1]

Explanation: If we consider this mapping: "a" -> 3 and "b" -> 4; the submatrix with the upper-left corner (1,1) is a match as outlined in the matrix above.

Note that since the corresponding values of "a" and "b" must differ, the submatrix with the upper-left corner (1,0) is not a match. Hence, we return [1,1].
```

**Example 3:**
```
1	2
2	1
x	x
Input: board = [[1,2],[2,1]], pattern = ["xx"]

Output: [-1,-1]

Explanation: Since the values of the matched submatrix must be the same, there is no match. Hence, we return [-1,-1].
```
 

**Constraints:**

`1 <= board.length <= 50`
`1 <= board[i].length <= 50`
`0 <= board[i][j] <= 9`
`1 <= pattern.length <= 50`
`1 <= pattern[i].length <= 50`
`pattern[i][j]` is either a digit represented as a string or a lowercase English letter.

# Submissions
---
**Solution 1: (Brute Force)**
```
Runtime: 95 ms
Memory: 94.86 MB
```
```c++
class Solution {
public:
    vector<int> findPattern(vector<vector<int>>& board, vector<string>& pattern) {
        int r = board.size(), c = board[0].size(), r2 = pattern.size(), c2 = pattern[0].size();
        bool flag;
        int m[26];
        int m2[10];
        for (int i = 0; i <= r-r2; i ++) {
            for (int j = 0; j <= c-c2; j ++) {
                flag = true;
                memset(m, -1, sizeof(m));
                memset(m2, -1, sizeof(m2));
                for (int i2 = 0; i2 < r2; i2 ++) {
                    for (int j2 = 0; j2 < c2; j2 ++) {
                        if ('0' <= pattern[i2][j2] && pattern[i2][j2] <= '9') {
                            if (board[i+i2][j+j2] + '0' != pattern[i2][j2]) {
                                flag = false;
                                break;
                            }
                        } else {
                            if (m[pattern[i2][j2]-'a'] != -1 && m[pattern[i2][j2]-'a'] != board[i+i2][j+j2]
                                || m2[board[i+i2][j+j2]] != -1 && m2[board[i+i2][j+j2]] != pattern[i2][j2]-'a') {
                                flag = false;
                                break;
                            } else {
                                m[pattern[i2][j2]-'a'] = board[i+i2][j+j2];
                                m2[board[i+i2][j+j2]] = pattern[i2][j2]-'a';
                            }
                        }
                    }
                    if (flag == false) {
                        break;
                    }
                }
                if (flag) {
                    return {i, j};
                }
            }
        }
        return {-1, -1};
    }
};
```
