474. Ones and Zeroes

In the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.

For now, suppose you are a dominator of **m** 0s and **n** 1s respectively. On the other hand, there is an array with strings consisting of only 0s and 1s.

Now your task is to find the maximum number of strings that you can form with given **m** `0s` and **n** `1s`. Each `0` and `1` can be used at most **once**.

**Note:**

* The given numbers of 0s and 1s will both not exceed 100
* The size of given string array won't exceed 600.
 

**Example 1:**
```
Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
Output: 4

Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are “10,”0001”,”1”,”0”
```

**Example 2:**
```
Input: Array = {"10", "0", "1"}, m = 1, n = 1
Output: 2

Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".
```

# Submissions
---
**Solution 1: (DP Bottom-Up)**
```
Runtime: 2864 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            zeros, ones = s.count("0"), s.count("1")
            for i in range(m, zeros-1, -1):
                for j in range(n , ones-1, -1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i - zeros][j - ones])
        return dp[-1][-1]
```

**Solution 2: (DP Top-Town)**
```
Runtime: 2100 ms
Memory Usage: 264.5 MB
```
```python
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        N = len(strs)
        
        @functools.lru_cache(None)
        def dp(index, m_zeroes, n_ones):
            if index >= N:
                return 0
            else:
                s = strs[index]
                ones, zeroes = s.count('1'), s.count('0')
                if m_zeroes - zeroes >= 0 and n_ones - ones >= 0:
                    return max(1 + dp(index + 1, m_zeroes - zeroes, n_ones - ones), dp(index + 1, m_zeroes, n_ones))
                else:
                    return dp(index + 1, m_zeroes, n_ones)
        
        return dp(0, m, n)
```