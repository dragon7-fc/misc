1014. Best Sightseeing Pair

Given an array `A` of positive integers, `A[i]` represents the value of the `i`-th sightseeing spot, and two sightseeing spots `i` and `j` have distance `j - i` between them.

The score of a pair `(i < j)` of sightseeing spots is `(A[i] + A[j] + i - j)` : the sum of the values of the sightseeing spots, minus the distance between them.

Return the maximum score of a pair of sightseeing spots.

 

**Example 1:**
```
Input: [8,1,5,2,6]
Output: 11
Explanation: i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11
``` 

**Note:**

1. `2 <= A.length <= 50000`
1. `1 <= A[i] <= 1000`

# Submissions
---
**Solution 1: (Greedy)**

* We can change `A[i] + A[j] + i - j` to `(A[i] + i ) + (A[j] - j)`
* For each index, we only need to track the max `A[i] + i` before it.

class Solution:
```
Runtime: 536 ms
Memory Usage: 19.4 MB
```
```python
class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        f_add = -sys.maxsize
        res = 0
        for i,n in enumerate(A):
            res = max(res, n - i + f_add)
            if i + n >= f_add:
                f_add = i + n            
        return res
```

**Solution 2: (Greedy, Math)**

A[i] + A[j] + i - j
-> A[i] + i - (j - A[j])
   ^^^^^^^^
     pre

```
Runtime: 0 ms
Memory: 45.60 MB
```
```c++
class Solution {
public:
    int maxScoreSightseeingPair(vector<int>& values) {
        int n = values.size(), j, pre = values[0], ans = INT_MIN;
        for (j = 1; j < n; j ++) {
            ans = max(ans, pre - (j-values[j]));
            pre = max(pre, j+values[j]);
        }
        return ans;
    }
};
```

**Solution 3: (Two Pointers)**

A[i] + A[j] + i - j
->  (A[i] + (i-j)) + A[j]
    ^^^^^^^^^^^^^^
         pre

```
Runtime: 0 ms
Memory: 45.40 MB
```
```c++
class Solution {
public:
    int maxScoreSightseeingPair(vector<int>& values) {
        int n = values.size(), i, pre = values[0], ans = INT_MIN;
        for (i = 1; i < n; i ++) {
            pre -= 1;
            ans = max(ans, pre + values[i]);
            pre = max(pre, values[i]);
        }
        return ans;
    }
};
```
