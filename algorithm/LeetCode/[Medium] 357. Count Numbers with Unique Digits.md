357. Count Numbers with Unique Digits

Given a **non-negative** integer n, count all numbers with unique digits, x, where 0 ≤ x < 10^n.

**Example:**
```
Input: 2
Output: 91 
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, 
             excluding 11,22,33,44,55,66,77,88,99
```

# Submissions
---
**Solution 1: (Backtracking)**
```
Runtime: 4608 ms
Memory Usage: 12.6 MB
```
```python
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        def backtracking(num):
            nonlocal res, used
            for i in range(len(digits)):
                if num*10 + digits[i] < limit:
                    if num == 0 and i == 0 or used[i]:
                        continue 
                    res += 1
                    num = num*10 + digits[i]
                    used[i] = True
                    backtracking(num)
                    used[i] = False
                    num //= 10  
        res = 1
        digits = list(range(10))
        used = [False]*10
        limit = 10 ** n
        backtracking(0)
        
        return res
```

**Solution 2: (Math, DP Bottom-Up)**
```
Runtime: 36 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0: return 1
        if n == 1: return 10
        res = 10      # res initially stores number 1,2,...,9 and 10^n
        choices = 9   # number of choices for the leading digit (which is 1,2,...,9)
        for i in range(1, n):
            choices = choices * (10 - i)    # number of choices remaining for the ith digit after fixing the digits preceding it and the last digit
                                            # e.g. for i = 2, fixing the first and last digit leaves 8 choices for the second digit
            res += choices
        return res
```

**Solution 3: (DFS)**
```
Runtime: 28 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0: return 1
        if n == 1: return 10
        ans = 10      # res initially stores number 1,2,...,9 and 10^n

        def dfs(i):
            nonlocal ans
            if i == 0:
                return 9
            rst = dfs(i-1) * (10-i)
            ans += rst
            return rst
            
        dfs(n-1)
        return ans
```

**Solution 4: (DP Top-Down, Digit DP)**
```
Runtime: 32 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        
        @lru_cache(None)
        def dp(n):
            if n == 1:
                return 10
            elif n == 0:
                return 1
            num = 9
            res = 9
            for _ in range(n - 1):
                res *= num
                num -= 1
            return res + dp(n - 1)
        
        return dp(min(n, 10))
```