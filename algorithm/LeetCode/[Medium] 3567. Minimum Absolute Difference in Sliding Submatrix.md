3567. Minimum Absolute Difference in Sliding Submatrix

You are given an `m x n` integer matrix `grid` and an integer `k`.

For every contiguous `k x k` submatrix of grid, compute the **minimum absolute difference** between any two **distinct** values within that submatrix.

Return a 2D array ans of size `(m - k + 1) x (n - k + 1)`, where `ans[i][j]` is the minimum absolute difference in the submatrix whose top-left corner is `(i, j)` in `grid`.

**Note**: If all elements in the submatrix have the same value, the answer will be 0.

A submatrix `(x1, y1, x2, y2)` is a matrix that is formed by choosing all cells `matrix[x][y]` where `x1 <= x <= x2` and `y1 <= y <= y2`.
 

**Example 1:**
```
Input: grid = [[1,8],[3,-2]], k = 2

Output: [[2]]

Explanation:

There is only one possible k x k submatrix: [[1, 8], [3, -2]].
Distinct values in the submatrix are [1, 8, 3, -2].
The minimum absolute difference in the submatrix is |1 - 3| = 2. Thus, the answer is [[2]].
```

**Example 2:**
```
Input: grid = [[3,-1]], k = 1

Output: [[0,0]]

Explanation:

Both k x k submatrix has only one distinct element.
Thus, the answer is [[0, 0]].
```

**Example 3:**
```
Input: grid = [[1,-2,3],[2,3,5]], k = 2

Output: [[1,2]]

Explanation:

There are two possible k × k submatrix:
Starting at (0, 0): [[1, -2], [2, 3]].
Distinct values in the submatrix are [1, -2, 2, 3].
The minimum absolute difference in the submatrix is |1 - 2| = 1.
Starting at (0, 1): [[-2, 3], [3, 5]].
Distinct values in the submatrix are [-2, 3, 5].
The minimum absolute difference in the submatrix is |3 - 5| = 2.
Thus, the answer is [[1, 2]].
```

**Constraints:**

* `1 <= m == grid.length <= 30`
* `1 <= n == grid[i].length <= 30`
* `-10^5 <= grid[i][j] <= 10^5`
* `1 <= k <= min(m, n)`

# Submissions
---
**Solution 1: (Brute Force, Sort)**
```
Runtime: 27 ms, Beats 22.22%
Memory: 35.96 MB, Beats 22.22%
```
```c++
class Solution {
    int get_min(map<int,int> &cnt) {
        if (cnt.size() <= 1) {
            return 0;
        }
        int rst = INT_MAX;
        for (auto it = cnt.begin(); next(it) != cnt.end(); it++) {
            rst = min(rst, next(it)->first - it->first);
        }
        return rst;
    }
public:
    vector<vector<int>> minAbsDiff(vector<vector<int>>& grid, int k) {
        int m = grid.size(), n = grid[0].size(), i, j, i2, j2;
        map<int,int> cnt;
        vector<vector<int>> ans(m-k+1, vector<int>(n-k+1));
        for (i = 0; i <= m-k; i ++) {
            cnt.clear();
            for (j = 0; j < n; j ++) {
                for (i2 = i; i2 < i+k; i2 ++) {
                    cnt[grid[i2][j]] += 1;
                    if (j >= k) {
                        cnt[grid[i2][j-k]] -= 1;
                        if (cnt[grid[i2][j-k]] == 0) {
                            cnt.erase(grid[i2][j-k]);
                        }
                    }
                }
                if (j >= k-1) {
                    ans[i][j-k+1] = get_min(cnt);
                }
            }
        }
        return ans;
    }
};
```

**Solution 2: (Brute Force, Sort)**
```
Runtime: 4 ms, Beats 100.00%
Memory: 31.69 MB, Beats 88.89%
```
```c++
class Solution {
public:
    vector<vector<int>> minAbsDiff(vector<vector<int>>& grid, int k) {
        int m=grid.size();
        int n=grid[0].size();
        int rows=m-k+1;
        int cols=n-k+1;
        vector<vector<int>>ans(rows,vector<int>(cols,0));
        for(int i=0;i<rows;i++){
            for(int j=0;j<cols;j++){
                vector<int>vals(k*k);
                int ind=0;
                for(int x=i;x<i+k;x++){
                    for(int y=j;y<j+k;y++){
                        vals[ind++]=grid[x][y];
                    }
                }
                sort(vals.begin(),vals.end());
                vector<int>uniq;
                uniq.reserve(k*k);
                uniq.push_back(vals[0]);
                for(int t=1;t<vals.size();t++){
                    if(vals[t]!=vals[t-1]){
                        uniq.push_back(vals[t]);
                    }
                }
                if(uniq.size()<=1){
                    ans[i][j]=0; 
                    continue;
                }
                int mini=INT_MAX;
                for(int t=1;t<uniq.size();t++){
                    int dif=uniq[t]-uniq[t-1];
                    if(dif<mini){
                        mini=dif;
                    }
                    if(mini==0) break;
                }
                ans[i][j]=mini;
            }
        }
        return ans;
    }
};
```
