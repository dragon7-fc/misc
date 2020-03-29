552. Student Attendance Record II

Given a positive integer **n**, return the number of all possible attendance records with length n, which will be regarded as rewardable. The answer may be very large, return it after mod 10^9 + 7.

A student attendance record is a string that only contains the following three characters:

1. '**A**' : Absent.
1. '**L**' : Late.
1. '**P**' : Present.

A record is regarded as rewardable if it doesn't contain **more than one 'A' (absent)** or **more than two continuous 'L' (late)**.

**Example 1:**
```
Input: n = 2
Output: 8 
Explanation:
There are 8 records with length 2 will be regarded as rewardable:
"PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" won't be regarded as rewardable owing to more than one absent times. 
```

**Note:** The value of **n** won't exceed `100,000`.

# Submissions
---
**Solution 1: (DP Top-Down, Memory Limit Exceeded)**
```python
class Solution:
    def checkRecord(self, n: int) -> int:
        
        @functools.lru_cache(None)
        def dp(i, seq):
            if seq.count('A') >= 2 or seq.count('LLL') >= 1: return 0
            if i == n: return 1
            return dp(i+1, seq + 'A') + dp(i+1, seq + 'L') + dp(i+1, seq + 'P')
            
        return dp(0, '')
```

**Solution 2: (DP Top-Town, Time Limit Exceeded)**
```python
class Solution:
    def checkRecord(self, n: int) -> int:
        memo = collections.defaultdict(int)

        def dp(i, seq):
            if memo[i, seq]: return memo[i, seq]
            if seq.count('A') >= 2 or seq.count('LLL') >= 1: return 0
            if i == n: return 1
            rst = dp(i+1, seq + 'A') + dp(i+1, seq + 'L') + dp(i+1, seq + 'P')
            memo[i, seq] = rst
            return rst
            
        return dp(0, '')
```

**Solution 3: (DP Bottom-Up)**
```
Runtime: 804 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = int(1e9 + 7)
        XAXL = 1      # No A no L in the end
        XAL = 0       # No A with one L in the end 
        XALL = 0      # No A with two L in the end 
        AXL = 0       # One A no L in the end
        AL = 0        # One A with one L in the end
        ALL = 0       # One A with two L in the end
        for _ in range(1, n+1):
            N_XAXL = XAXL
            N_XAL = XAL
            N_XALL = XALL
            N_AXL = AXL
            N_AL = AL
            N_ALL = ALL

            ALL = N_AL
            AL = N_AXL
            XAL = N_XAXL
            XALL = N_XAL
            XAXL = (N_XAL + N_XALL + N_XAXL) % MOD;
            AXL = (N_AXL + N_AL + N_ALL + N_XAL + N_XALL + N_XAXL) % MOD;

        return (XAXL + XAL + XALL + AXL + AL + ALL) % MOD
```