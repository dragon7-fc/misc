1362. Closest Divisors

Given an integer `num`, find the closest two integers in absolute difference whose product equals `num + 1` or `num + 2`.

Return the two integers in any order.

 

**Example 1:**
```
Input: num = 8
Output: [3,3]
Explanation: For num + 1 = 9, the closest divisors are 3 & 3, for num + 2 = 10, the closest divisors are 2 & 5, hence 3 & 3 is chosen.
```

**Example 2:**
```
Input: num = 123
Output: [5,25]
```

**Example 3:**
```
Input: num = 999
Output: [40,25]
```

# Submissions
---
**Solution 1: (Math)**
```
Runtime: 336 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        res = [1, num + 1]
        for a in range(1, int((num+2)**0.5) + 1):
            if (num + 2) % a == 0:
                res = [a, (num + 2) // a]
            if (num + 1) % a == 0:
                res = [a, (num + 1) // a]
        return res
```