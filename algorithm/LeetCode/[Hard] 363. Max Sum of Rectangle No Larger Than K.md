363. Max Sum of Rectangle No Larger Than K

Given a non-empty 2D matrix matrix and an integer k, find the max sum of a rectangle in the matrix such that its sum is no larger than k.

**Example:**
```
Input: matrix = [[1,0,1],[0,-2,3]], k = 2
Output: 2 
Explanation: Because the sum of rectangle [[0, 1], [-2, 3]] is 2,
             and 2 is the max number no larger than k (k = 2).
```
**Note:**

* The rectangle inside the `matrix` must have an `area > 0`.
* What if the number of rows is much larger than the number of columns?

# Submissions
---
**Solution 1: (Prefix Sum, Binary Search)**

* For each row, calculate the prefix sum. For each pair of columns, calculate the sum of rows.
* Now this problem is changed to a 1D problem: max subarray sum no more than k.
```
Runtime: 1008 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        def maxSumSubarray(arr):
            sub_s_max = float('-inf')
            s_curr = 0
            prefix_sums = [float('inf')]
            for x in arr:
                bisect.insort(prefix_sums, s_curr)
                s_curr += x
                i = bisect.bisect_left(prefix_sums, s_curr - k)
                sub_s_max = max(sub_s_max, s_curr - prefix_sums[i])
            return sub_s_max
        
        m, n = len(matrix), len(matrix[0])
        for x in range(m):
            for y in range(n - 1):
                matrix[x][y+1] += matrix[x][y]
        res = float('-inf')
        for y1 in range(n):
            for y2 in range(y1, n):
                arr = [matrix[x][y2] - (matrix[x][y1-1] if y1 > 0 else 0) for x in range(m)]
                res = max(res, maxSumSubarray(arr))
        return res
```

**Solution 2: (Brute Force)**
```
Runtime: 317 ms
Memory Usage: 10.4 MB
```
```c++
class Solution {
public:
    int maxSumSubmatrix(vector<vector<int>>& matrix, int k) {
        int max_sum = INT_MIN, m=matrix.size(), n=matrix[0].size(), subarr[m];
        for(int l=0; l<n; l++) {
            memset(subarr,0,sizeof(subarr));
            for(int r=l; r<n; r++) {
                for(int i=0; i<m; i++) subarr[i] += matrix[i][r];
                for(int i=0; i<m; i++) {
                    int sum = 0;
                    for(int j=i; j<m; j++) {
                        sum += subarr[j];
                        if(sum > max_sum && sum <=k) max_sum = sum;
                    }
                }
            }
        }
        return max_sum;
    }
};
```

**Solution 3: (Prefix Sum, Binary Search, O(n^3 log n))**
```
Runtime: 669 ms, Beats 62.53%
Memory: 241.68 MB, Beats 50.63%
```
```c++
class Solution {
public:
    int maxSumSubmatrix(vector<vector<int>>& matrix, int k) {
        int m = matrix.size(), n = matrix[0].size(), i, l, r, ans = INT_MIN;
        for (l = 0; l < n; ++l) {
            vector<int> sums(m);
            for (r = l; r < n; ++r) {
                for (int i = 0; i < m; ++i) 
                    sums[i] += matrix[i][r];
                set<int> st = {0};
                int run_sum = 0;
                for (int sum : sums) {
                    run_sum += sum;
                    auto it = st.lower_bound(run_sum - k);
                    if (it != end(st)) {
                        ans = max(ans, run_sum - *it);
                    }
                    st.insert(run_sum);
                }
            }
        }
        return ans;
    }
};
```
