1201. Ugly Number III

Write a program to find the `n`-th ugly number.

Ugly numbers are positive integers which are divisible by `a` **or** `b` **or** `c`.

 

**Example 1:**
```
Input: n = 3, a = 2, b = 3, c = 5
Output: 4
Explanation: The ugly numbers are 2, 3, 4, 5, 6, 8, 9, 10... The 3rd is 4.
```

**Example 2:**
```
Input: n = 4, a = 2, b = 3, c = 4
Output: 6
Explanation: The ugly numbers are 2, 3, 4, 6, 8, 9, 10, 12... The 4th is 6.
```

**Example 3:**
```
Input: n = 5, a = 2, b = 11, c = 13
Output: 10
Explanation: The ugly numbers are 2, 4, 6, 8, 10, 11, 12, 13... The 5th is 10.
```

**Example 4:**
```
Input: n = 1000000000, a = 2, b = 217983653, c = 336916467
Output: 1999999984
```

**Constraints:**

* `1 <= n, a, b, c <= 10^9`
* `1 <= a * b * c <= 10^18`
* It's guaranteed that the result will be in range `[1, 2 * 10^9]`

# Submissions
---
**Solution 1:**

For every integer `A`, `F(A) = (total number of positive integers <= A which are divisible by a or b or c.)`.
`F(A) = A/a + A/b + A/c - A/lcm(a, c) - A/lcm(a, b) - A/lcm(a, c) + A/lcm(a, b, c)`(lcm = least common multiple)
Find the least integer A that satisfies the condition `F(A) == n`.

```
Runtime: 24 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def lcm(x, y):
            return x * y // math.gcd(x, y)
        
        def count_ugly(n, a, b, c, ab, bc, ca, abc):
            answer = n // a + n // b + n // c
            answer -= n // ab + n // bc + n // ca
            answer += n // abc
            return answer
        
        ab, bc, ca = lcm(a, b), lcm(b, c), lcm(c, a)
        abc = lcm(ab, c)
        
        lo, hi = 1, 2 * 10 ** 9
        while lo < hi:
            mi = lo + (hi - lo) // 2
            if count_ugly(mi, a, b, c, ab, bc, ca, abc) < n:
                lo = mi + 1
            else:
                hi = mi
        return lo
```