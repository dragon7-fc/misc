1134. Armstrong Number

Given an integer `n`, return `true` if and only if it is an Armstrong number.

The k-digit number `n` is an Armstrong number if and only if the `k`th power of each digit sums to `n`.

 

**Example 1:**
```
Input: n = 153
Output: true
Explanation: 153 is a 3-digit number, and 153 = 13 + 53 + 33.
```

**Example 2:**
```
Input: n = 123
Output: false
Explanation: 123 is a 3-digit number, and 123 != 13 + 23 + 33 = 36.
```

**Constraints:**

* `1 <= n <= 108`

# Submissions
---
**Solution 1: (String)**
```
Runtime: 32 ms
Memory Usage: 14.4 MB
```
```python
class Solution:
    def isArmstrong(self, n: int) -> bool:
        return sum([d**len(str(n)) for d in map(int, str(n))]) == n
```