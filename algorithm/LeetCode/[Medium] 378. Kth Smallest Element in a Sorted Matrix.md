378. Kth Smallest Element in a Sorted Matrix

Given an `n x n` matrix where each of the rows and columns is sorted in ascending order, return the `k`th smallest element in the matrix.

Note that it is the `k`th smallest element in the sorted order, not the `k`th distinct element.

You must find a solution with a memory complexity better than O(n^2).

 

**Example 1:**
```
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
```

**Example 2:**
```
Input: matrix = [[-5]], k = 1
Output: -5
```

**Constraints:**

* `n == matrix.length == matrix[i].length`
* `1 <= n <= 300`
* `-10^9 <= matrix[i][j] <= 10^9`
* All the rows and columns of `matrix` are guaranteed to be sorted in non-decreasing order.
* `1 <= k <= n^2`

**Follow up:**

* Could you solve the problem with a constant memory (i.e., `O(1)` memory complexity)?
* Could you solve the problem in `O(n)` time complexity? The solution may be too advanced for an interview but you may find reading this paper fun.

# Submissions
---
**SOlution 1: (Sort)**
```
Runtime: 168 ms
Memory Usage: 18.9 MB
```
```python
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        array = []
        for row in matrix:
            array += row
            
        return sorted(array)[k-1]
```

**Solution 2: (Heap)**
```
Runtime: 196 ms
Memory Usage: 18.8 MB
```
```python
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        res = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if len(res) < k:
                    heapq.heappush(res, -matrix[i][j]) 
                else:
                    heapq.heappushpop(res, -matrix[i][j])
        return -(res[0])
```

**Solution 3: (Binary Search)**
```
Runtime: 156 ms
Memory Usage: 20.1 MB
```
```python
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])  # For gerneral, matrix doesn't need to be a square

        def countLessOrEqual(x):
            cnt = 0
            c = n - 1  # start with the rightmost column
            for r in range(m):
                while c >= 0 and matrix[r][c] > x: c -= 1  # decrease column until matrix[r][c] <= x
                cnt += (c + 1)
            return cnt

        left, right = matrix[0][0], matrix[-1][-1]
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if countLessOrEqual(mid) >= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
```

**Solution 4: (Heap)**
```
Runtime: 61 ms
Memory Usage: 14.1 MB
```
```c++
class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        priority_queue<int> pq;
        for (int i = 0; i < matrix.size(); i ++) {
            for (int j = 0; j < matrix[0].size(); j ++) {
                if (pq.size() < k)
                    pq.push(matrix[i][j]);
                else if (pq.top() > matrix[i][j]) {
                    pq.push(matrix[i][j]);
                    pq.pop();
                } else
                    break;
            }
        }
        return pq.top();
    }
};
```

**Solution 5: (Binary Serach)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 17.12 MB, Beats 62.99%
```
```c++
class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        int n = matrix.size(), i, left = matrix[0][0], right = matrix[n-1][n-1], mid, ck, ans;
        while (left <= right) {
            mid = left + (right-left)/2;
            ck = 0;
            for (i = 0; i < n; i ++) {
                ck += upper_bound(matrix[i].begin(), matrix[i].end(), mid) - matrix[i].begin();
            }
            if (ck < k) {
                left = mid + 1;
            } else {
                ans = mid;
                right = mid - 1;
            }
        }
        return ans;
    }
};
```
