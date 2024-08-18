3256. Maximum Value Sum by Placing Three Rooks I

You are given a `m x n` 2D array board representing a chessboard, where `board[i][j]` represents the **value** of the cell `(i, j)`.

Rooks in the **same** row or column attack each other. You need to place three rooks on the chessboard such that the rooks **do not attack** each other.

Return the **maximum** sum of the cell values on which the rooks are placed.

 

**Example 1:**
```
Input: board = [[-3,1,1,1],[-3,1,-3,1],[-3,2,1,1]]

Output: 4

Explanation:
```
![3256_rooks2.png](img/3256_rooks2.png)
```
We can place the rooks in the cells (0, 2), (1, 3), and (2, 1) for a sum of 1 + 1 + 2 = 4.
```

**Example 2:**
```
Input: board = [[1,2,3],[4,5,6],[7,8,9]]

Output: 15

Explanation:

We can place the rooks in the cells (0, 0), (1, 1), and (2, 2) for a sum of 1 + 5 + 9 = 15.
```

**Example 3:**
```
Input: board = [[1,1,1],[1,1,1],[1,1,1]]

Output: 3

Explanation:

We can place the rooks in the cells (0, 2), (1, 1), and (2, 0) for a sum of 1 + 1 + 1 = 3.
```
 

**Constraints:**

* `3 <= m == board.length <= 100`
* `3 <= n == board[i].length <= 100`
* `-109 <= board[i][j] <= 10^9`

# Submissions
---
**Solution 1: (Brute Force)**

__Intuition__

Store the largest 3 values for each row.
Select any 3 rows and brute force all combinations.

__Complexity__

Time complexity: O((N∗3)^3)
Space complexity: O(N^2)

```
class Solution {
public:
    long long maximumValueSum(vector<vector<int>>& board) {
        int m = board.size(), n = board[0].size();
        vector<vector<pair<int, int>>> dp(m);
        for (int i = 0; i < m; i ++){
            for (int j = 0; j < n; j ++){
                dp[i].push_back({board[i][j], j});
            }
            sort(dp[i].rbegin(), dp[i].rend());
            while(dp[i].size() > 3) dp[i].pop_back();
        }
        long long ans = -3e9;
        for (int i1 = 0; i1 < m; i1 ++){
            for (int j1 = 0; j1 < 3; j1 ++){
                int val1 = dp[i1][j1].first;
                int col1 = dp[i1][j1].second;
                for (int i2 = i1 + 1; i2 < m; i2 ++){
                    for (int j2 = 0; j2 < 3; j2 ++){
                        int val2 = dp[i2][j2].first;
                        int col2 = dp[i2][j2].second;
                        for (int i3 = i2 + 1; i3 < m; i3 ++){
                            for (int j3 = 0; j3 < 3; j3 ++){
                                int val3 = dp[i3][j3].first;
                                int col3 = dp[i3][j3].second;
                                if (col1 != col2 && col2 != col3 && col1 != col3){
                                    long long sum = (long long)val1 + (long long)val2 + (long long)val3;
                                    ans = max(ans, sum);
                                }
                            }
                        } 
                    }
                }  
            }
        }
        return ans;
    }
};
```
