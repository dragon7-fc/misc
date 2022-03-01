378. Kth Smallest Element in a Sorted Matrix

Given a n x n `matrix` where each of the rows and columns are sorted in ascending order, find the `k`th smallest element in the matrix.

Note that it is the `k`th smallest element in the sorted order, not the kth distinct element.

**Example:**
```
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
```

**Note:**

* You may assume `k` is always valid, `1 ≤ k ≤ n^2`.

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
