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
**Solution 1:**
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