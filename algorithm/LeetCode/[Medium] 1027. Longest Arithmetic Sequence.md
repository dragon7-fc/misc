1027. Longest Arithmetic Sequence

Given an array `A` of integers, return the length of the longest arithmetic subsequence in `A`.

Recall that a subsequence of `A` is a list `A[i_1], A[i_2], ..., A[i_k]` with `0 <= i_1 < i_2 < ... < i_k <= A.length - 1`, and that a sequence `B` is arithmetic if `B[i+1] - B[i]` are all the same value (for `0 <= i < B.length - 1`).

 

**Example 1:**

```
Input: [3,6,9,12]
Output: 4
Explanation: 
The whole array is an arithmetic sequence with steps of length = 3.
```

**Example 2:**

```
Input: [9,4,7,2,10]
Output: 3
Explanation: 
The longest arithmetic subsequence is [4,7,10].
```

**Example 3:**

```
Input: [20,1,15,3,10,5,8]
Output: 4
Explanation: 
The longest arithmetic subsequence is [20,15,10,5].
```

**Note:**

1. `2 <= A.length <= 2000`
1. `0 <= A[i] <= 10000`

# Submissions
---
**Solution 1: (DP Top-Down, Time Limit Exceeded)**
```python
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        N = len(A)
        
        @functools.lru_cache(None)
        def dp(j, d):
            if j == N:
                return 0
            rst = 1
            for k in range(j + 1, N):
                if d == A[k] - A[j]:
                    rst = max(rst, dp(k, d) + 1)
            return rst
        
        max_len = 0
        for i in range(N):
            for j in range(i+1, N):
                max_len = max(max_len, dp(i, A[j] - A[i]))
        return max_len
```

**Solution 1: (DP Bottom-Up)**
```
Runtime: 1124 ms
Memory Usage: 312.4 MB
```
```python
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        for j, a2 in enumerate(A[1:], start=1):
            for i, a1 in enumerate(A[:j]):
                d = a2 - a1
                if (i, d) in dp:
                    dp[j, d] = dp[i, d] + 1
                else:
                    dp[j, d] = 2
        return max(dp.values())
```

**Solution 2: (DP Bottom-Up)**
```
Runtime: 236 ms
Memory Usage: 272.4 MB
```
```c++
class Solution {
public:
    int longestArithSeqLength(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> dp(n, vector<int>(2000,0));//dp[index][diff] equals to the length of arithmetic sequence at index with difference diff.
        int ans = 2;
        for(int j = 1; j < n; j++)
        {
            for(int i = 0; i < j; i++)
            {
                int d = nums[j] - nums[i] + 1000;//to make cd always positive
                dp[j][d] = max(2, dp[i][d] + 1);//since min length of an ap wll always be 2 
                ans = max(ans, dp[j][d]);//storing the max of all length
            }
        }
        return ans;
    }
};
```
