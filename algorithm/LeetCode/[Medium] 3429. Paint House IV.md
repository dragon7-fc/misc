3429. Paint House IV

You are given an even integer `n` representing the number of houses arranged in a straight line, and a 2D array `cost` of size `n x 3`, where `cost[i][j]` represents the cost of painting house `i` with color `j + 1`.

The houses will look beautiful if they satisfy the following conditions:

* No two adjacent houses are painted the same color.
* Houses **equidistant** from the ends of the row are not painted the same color. For example, if `n = 6`, houses at positions `(0, 5)`, `(1, 4)`, and `(2, 3)` are considered equidistant.

Return the **minimum** cost to paint the houses such that they look **beautiful**.

 

**Example 1:**
```
Input: n = 4, cost = [[3,5,7],[6,2,9],[4,8,1],[7,3,5]]

Output: 9

Explanation:

The optimal painting sequence is [1, 2, 3, 2] with corresponding costs [3, 2, 1, 3]. This satisfies the following conditions:

No adjacent houses have the same color.
Houses at positions 0 and 3 (equidistant from the ends) are not painted the same color (1 != 2).
Houses at positions 1 and 2 (equidistant from the ends) are not painted the same color (2 != 3).
The minimum cost to paint the houses so that they look beautiful is 3 + 2 + 1 + 3 = 9.
```

**Example 2:**
```
Input: n = 6, cost = [[2,4,6],[5,3,8],[7,1,9],[4,6,2],[3,5,7],[8,2,4]]

Output: 18

Explanation:

The optimal painting sequence is [1, 3, 2, 3, 1, 2] with corresponding costs [2, 8, 1, 2, 3, 2]. This satisfies the following conditions:

No adjacent houses have the same color.
Houses at positions 0 and 5 (equidistant from the ends) are not painted the same color (1 != 2).
Houses at positions 1 and 4 (equidistant from the ends) are not painted the same color (3 != 1).
Houses at positions 2 and 3 (equidistant from the ends) are not painted the same color (2 != 3).
The minimum cost to paint the houses so that they look beautiful is 2 + 8 + 1 + 2 + 3 + 2 = 18.
```
 

**Constraints:**

* `2 <= n <= 10^5`
* `n` is even.
* `cost.length == n`
* `cost[i].length == 3`
* `0 <= cost[i][j] <= 10^5`

# Submissions
---
**Solution 1: (DP Top-Down)**
```
Runtime: 485 ms
Memory: 375.62 MB
```
```c++
class Solution {
    long long f(int i, int left, int right, int n, vector<vector<int>>& cost, vector<vector<vector<long long>>>& dp) {
        
        if(i >= n/2) return 0;
        if(dp[i][left][right]!=-1) return dp[i][left][right];

        long long t = LONG_MAX;
        for(int col1=0; col1<3; col1++) {
            if(col1 != left) {
                for(int col2=0; col2<3; col2++){
                    if((col2 != right) && (col2 != col1)) {
                        long long q = cost[i][col1] + cost[n-1-i][col2] + f(i+1, col1, col2, n, cost, dp);
                        t = min(t, q);
                    }
                }
            }
        }
        return dp[i][left][right] = t;
    }
public:
    long long minCost(int n, vector<vector<int>>& cost) {
        vector<vector<vector<long long>>> dp(n, vector<vector<long long>>(4, vector<long long>(4, -1)));
        return f(0, 3, 3, n, cost, dp);
    }
};
```

**Solution 2: (DP Bottom-Up)**
```
Runtime: 249 ms
Memory: 257.76 MB
```
```c++
class Solution {
public:
    long long minCost(int n, vector<vector<int>>& cost) {
        vector<vector<vector<long long>>> dp(n/2, vector<vector<long long>> (3, vector<long long>(3, LONG_MAX)));
        for (int i=0;i<3;i++){
            for (int j=0;j<3;j++){
                if (i!=j) {
                    dp[0][i][j] = cost[0][i] + cost.back()[j];
                }
            }
        }
        for (int i=1;i<n/2;i++){
            for (int j=0;j<3;j++){
                for (int k=0;k<3;k++){
                    if (j!=k){
                        for (int l=0;l<3;l++){
                            for(int m=0;m<3;m++){
                                if (l==j || m==k || dp[i-1][l][m]==LONG_MAX) continue;
                                dp[i][j][k] = min(dp[i][j][k], cost[i][j]+cost[n-i-1][k]+dp[i-1][l][m]);
                            }
                        }
                    }
                }
            }
        }
        long long ans = LONG_MAX;
        for (int i=0;i<3;i++){
            for (int j=0;j<3;j++){
                ans = min(ans, dp.back()[i][j]);
            }
        }
        return ans;
    }
};
```
