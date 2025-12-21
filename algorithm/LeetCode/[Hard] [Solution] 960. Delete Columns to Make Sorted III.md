960. Delete Columns to Make Sorted III

We are given an array `A` of `N` lowercase letter strings, all of the same length.

Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.

For example, if we have an array `A = ["babca","bbazb"]` and deletion indices `{0, 1, 4}`, then the final array after deletions is `["bc","az"]`.

Suppose we chose a set of deletion indices `D` such that after deletions, the final array has every element (row) in lexicographic order.

For clarity, `A[0]` is in lexicographic order (ie. `A[0][0] <= A[0][1] <= ... <= A[0][A[0].length - 1]`), `A[1]` is in lexicographic order (ie. `A[1][0] <= A[1][1] <= ... <= A[1][A[1].length - 1]`), and so on.

Return the minimum possible value of `D.length`.

 

**Example 1:**
```
Input: ["babca","bbazb"]
Output: 3
Explanation: After deleting columns 0, 1, and 4, the final array is A = ["bc", "az"].
Both these rows are individually in lexicographic order (ie. A[0][0] <= A[0][1] and A[1][0] <= A[1][1]).
Note that A[0] > A[1] - the array A isn't necessarily in lexicographic order.
```

**Example 2:**
```
Input: ["edcba"]
Output: 4
Explanation: If we delete less than 4 columns, the only row won't be lexicographically sorted.
```

**Example 3:**
```
Input: ["ghi","def","abc"]
Output: 0
Explanation: All rows are already lexicographically sorted.
```

**Note:**

* `1 <= A.length <= 100`
* `1 <= A[i].length <= 100`

# Submissions
---
## Approach 1: Dynamic Programming
**Intuition and Algorithm**

This is a tricky problem that is hard to build an intuition about.

First, lets try to find the number of columns to keep, instead of the number to delete. At the end, we can subtract to find the desired answer.

Now, let's say we must keep the first column `C`. The next column `D` we keep must have all rows lexicographically sorted (ie. `C[i] <= D[i]`), and we can say that we have deleted all columns between `C` and `D`.

Now, we can use dynamic programming to solve the problem in this manner. Let `dp[k]` be the number of columns that are kept in answering the question for input `[row[k:] for row in A]`. The above gives a simple recursion for `dp[k]`.

```python
class Solution(object):
    def minDeletionSize(self, A):
        W = len(A[0])
        dp = [1] * W
        for i in xrange(W-2, -1, -1):
            for j in xrange(i+1, W):
                if all(row[i] <= row[j] for row in A):
                    dp[i] = max(dp[i], 1 + dp[j])

        return W - max(dp)
```

**Complexity Analysis**

* Time Complexity: $O(N * W^2)$, where $N$ is the length of `A`, and $W$ is the length of each word in `A`.

* Space Complexity: $O(W)$.

# Submissions
---
**Solution 1: (Dynamic Programming Bottom-Up)**
```
Runtime: 216 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        W = len(A[0])
        dp = [1] * W  # Longest Increasing Subsequence
        for i in range(W-2, -1, -1):
            for j in range(i+1, W):
                if all(row[i] <= row[j] for row in A):
                    dp[i] = max(dp[i], 1 + dp[j])

        return W - max(dp)
```

**Solution 2: (DP Bottom-Up)**
```
Runtime: 200 ms
Memory Usage: 13.7 MB
```
```python
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        N = len(A[0])
        dp = [1] * N
        for j in range(1, N):
            for i in range(j):
                if all(a[i] <= a[j] for a in A):
                    dp[j] = max(dp[j], dp[i] + 1)
        return N - max(dp)
```

**Solution 3: (DP Top-Down)**
```
Runtime: 380 ms
Memory Usage: 24.5 MB
```
```python
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        M, N = len(A), len(A[0])
        if M == 0: return 0
        ans = float('inf')
        
        @functools.lru_cache(None)
        def dp(lastPickedindex, currentIndex):
            if currentIndex >= N: 
                return 0
            res = dp(lastPickedindex, currentIndex+1) + 1
            if all(A[i][lastPickedindex] <= A[i][currentIndex] for i in range(M)):
                res = min(res, dp(currentIndex, currentIndex+1)) 
            return res
        
        for i in range(N):
            ans = min(ans , dp(i, i+1) + i)
        return ans
```

**Solution 4: (DP Top-Down)**
```
Runtime: 480 ms
Memory Usage: 20.6 MB
```
```python
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        M, N = len(A), len(A[0])
        if M == 0: return 0

        @functools.lru_cache(None)
        def dp(previndex, curpos):
            if curpos == N:
                return 0
            taken = float('inf')
            if previndex < 0 or all(A[i][previndex] <= A[i][curpos] for i in range(M)):
                taken = dp(curpos, curpos + 1)
            nottaken = dp(previndex, curpos + 1) + 1
            return min(taken, nottaken)

        return dp(-1, 0)
```

**Solution 5: (DP Bottom-Up, LIS)**

    x x     x
      x x   x
    x   x   x
    x   x x
    b a b c a
    b b a z b
dp  1 1 1 2 2

```
Runtime: 7 ms, Beats 33.85%
Memory: 13.51 MB, Beats 34.36%
```
```c++
class Solution {
public:
    int minDeletionSize(vector<string>& strs) {
        int n = strs[0].length(), i, j;
        vector<int> dp(n, 1);
        for (j = 1; j < n; j ++) {
            for (i = 0; i < j; i ++) {
                if (all_of(strs.begin(), strs.end(), [&](auto &s){return s[i] <= s[j];})) {
                    dp[j] = max(dp[j], dp[i] + 1);
                }
            }
        }
        return n - *max_element(dp.begin(), dp.end());
    }
};
```
