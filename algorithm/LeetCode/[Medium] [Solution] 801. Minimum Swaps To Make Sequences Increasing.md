801. Minimum Swaps To Make Sequences Increasing

We have two integer sequences `A` and `B` of the same non-zero length.

We are allowed to swap elements `A[i]` and `B[i]`.  Note that both elements are in the same index position in their respective sequences.

At the end of some number of swaps, `A` and `B` are both strictly increasing.  (A sequence is strictly increasing if and only if `A[0] < A[1] < A[2] < ... < A[A.length - 1]`.)

Given `A` and `B`, return the minimum number of swaps to make both sequences strictly increasing.  It is guaranteed that the given input always makes it possible.

**Example:**

```
Input: A = [1,3,5,4], B = [1,2,3,7]
Output: 1
Explanation: 
Swap A[3] and B[3].  Then the sequences are:
A = [1, 3, 5, 7] and B = [1, 2, 3, 4]
which are both strictly increasing.
```

**Note:**

* `A`, `B` are arrays with the same length, and that length will be in the range `[1, 1000]`.
* `A[i]`, `B[i]` are integer values in the range `[0, 2000]`.

# Solution
---
## Approach #1: Dynamic Programming [Accepted]
**Intuition**

The cost of making both sequences increasing up to the first `i` columns can be expressed in terms of the cost of making both sequences increasing up to the first `i-1` columns. This is because the only thing that matters to the `i`th column is whether the previous column was swapped or not. This makes dynamic programming an ideal choice.

Let's remember `n1` (natural1), the cost of making the first `i-1` columns increasing and not swapping the `i-1`th column; and `s1` (swapped1), the cost of making the first `i-1` columns increasing and swapping the `i-1`th column.

Now we want candidates `n2` (and `s2`), the costs of making the first `i` columns increasing if we do not swap (or swap, respectively) the `i`th column.

**Algorithm**

For convenience, say `a1 = A[i-1], b1 = B[i-1] and a2 = A[i], b2 = B[i]`.

Now, if `a1 < a2` and `b1 < b2`, then it is allowed to have both of these columns natural (unswapped), or both of these columns swapped. This possibility leads to `n2 = min(n2, n1)` and `s2 = min(s2, s1 + 1)`.

Another, (not exclusive) possibility is that `a1 < b2` and `b1 < a2`. This means that it is allowed to have exactly one of these columns swapped. This possibility leads to `n2 = min(n2, s1)` or `s2 = min(s2, n1 + 1)`.

Note that it is important to use two if statements separately, because both of the above possibilities might be possible.

At the end, the optimal solution must leave the last column either natural or swapped, so we take the minimum number of swaps between the two possibilities.

```python
class Solution(object):
    def minSwap(self, A, B):
        n1, s1 = 0, 1
        for i in xrange(1, len(A)):
            n2 = s2 = float("inf")
            if A[i-1] < A[i] and B[i-1] < B[i]:
                n2 = min(n2, n1)
                s2 = min(s2, s1 + 1)
            if A[i-1] < B[i] and B[i-1] < A[i]:
                n2 = min(n2, s1)
                s2 = min(s2, n1 + 1)

            n1, s1 = n2, s2

        return min(n1, s1)
```

**Complexity Analysis**

* Time Complexity: $O(N)$.

* Space Complexity: $O(1)$.

# Submissions
---
**Solution: (Dynamic Programming Bottom-Up)**
```
Runtime: 96 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        n1, s1 = 0, 1
        for i in range(1, len(A)):
            n2 = s2 = float("inf")
            if A[i-1] < A[i] and B[i-1] < B[i]:
                n2 = min(n2, n1)
                s2 = min(s2, s1 + 1)
            if A[i-1] < B[i] and B[i-1] < A[i]:
                n2 = min(n2, s1)
                s2 = min(s2, n1 + 1)

            n1, s1 = n2, s2

        return min(n1, s1)
```

**Solution 1: (DP Top-Down)**
```
Runtime: 156 ms
Memory Usage: 17.5 MB
```
```python
class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        N = len(A)
    
        @functools.lru_cache(None)
        def dfs(i, prev_a, prev_b, swap):
            if i == N:
                return 0
            make_swap = no_swap = float('inf')
            if B[i] > prev_a and A[i] > prev_b:     # make_swap
                make_swap = 1 + dfs(i+1, B[i], A[i], True)
            if A[i] > prev_a and B[i] > prev_b:     # no swap
                no_swap = dfs(i+1, A[i], B[i], False)
            return min(make_swap, no_swap)
        
        return dfs(0, -1, -1, False)
```

**Solution 3: (DP Bottom-Up)**

                   v
    nums1 = [1,3,5,4],
                   7 
    nums2 = [1,2,3,7]
                   4
            {1,1,0}
            {1,1,1}
              {3,2,0}
              {2,3,1}
                {5,3,0}
                {3,5,1}
                   {4,7,1}
                   {7,4,1}

             v
    nums1 = [0,3,5,8,9],
             2
    nums2 = [2,1,4,6,9]
             0
            {0,2,0}
            {2,0.1}
              {3,1,1}
              {1,3,1}
                {5,4,1}
                {4,5,2}
                  {8,6,1}
                  {6,8,2}
                    {9,9,1}
                    {9,9,2}

```
Runtime: 11 ms, Beats 76.87%
Memory: 94.07 MB, Beats 96.97%
```
```c++
class Solution {
public:
    int minSwap(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size(), i, ans = 0;
        vector<array<int,3>> pre(2), dp(2);
        pre = {{nums1[0], nums2[0], 0}, {nums2[0], nums1[0], 1}};
        for (i = 1; i < n; i ++) {
            dp[0] = {nums1[i], nums2[i], INT_MAX};
            dp[1] = {nums2[i], nums1[i], INT_MAX};
            if (dp[0][0] > pre[0][0] && dp[0][1] > pre[0][1]) {
                dp[0][2] = min(dp[0][2], pre[0][2]);
            }
            if (dp[0][0] > pre[1][0] && dp[0][1] > pre[1][1]) {
                dp[0][2] = min(dp[0][2], pre[1][2]);
            }
            if (dp[1][0] > pre[0][0] && dp[1][1] > pre[0][1]) {
                dp[1][2] = min(dp[1][2], pre[0][2] + 1);
            }
            if (dp[1][0] > pre[1][0] && dp[1][1] > pre[1][1]) {
                dp[1][2] = min(dp[1][2], pre[1][2] + 1);
            }
            pre = dp;
        }
        return min(pre[0][2], pre[1][2]);
    }
};
```
