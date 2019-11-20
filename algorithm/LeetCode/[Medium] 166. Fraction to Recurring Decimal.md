166. Fraction to Recurring Decimal

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

**Example 1:**
```
Input: numerator = 1, denominator = 2
Output: "0.5"
```

**Example 2:**
```
Input: numerator = 2, denominator = 1
Output: "2"
```

**Example 3:**
```
Input: numerator = 2, denominator = 3
Output: "0.(6)"
```

# Submissions
---
**Solution 1:**
```
Runtime: 24 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        res = ''
        
        # sign
        if numerator*denominator < 0:
            res+='-'
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        # before point
        res += str(numerator//denominator)
        carrier = numerator%denominator
        
        # after point
        if carrier > 0:
            res+='.'
        memo = {}
        while carrier > 0:
            if carrier in memo:
                index = memo[carrier]
                res = res[:index] + '('+res[index:] +')'
                return res
            else:
                memo[carrier] = len(res)
                res += str((carrier*10)//denominator)
                carrier = ((carrier*10)%denominator)
                
        return res
```