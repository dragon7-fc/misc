970. Powerful Integers

Given two positive integers `x` and `y`, an integer is powerful if it is equal to `x^i + y^j` for some integers `i >= 0` and `j >= 0`.

Return a list of all powerful integers that have value less than or equal to bound.

You may return the answer in any order.  In your answer, each value should occur at most once.

 

**Example 1:**
```
Input: x = 2, y = 3, bound = 10
Output: [2,3,4,5,7,9,10]
Explanation: 
2 = 2^0 + 3^0
3 = 2^1 + 3^0
4 = 2^0 + 3^1
5 = 2^1 + 3^1
7 = 2^2 + 3^1
9 = 2^3 + 3^0
10 = 2^0 + 3^2
```

**Example 2:**
```
Input: x = 3, y = 5, bound = 15
Output: [2,4,6,8,10,14]
```

**Note:**

1. `1 <= x <= 100`
1. `1 <= y <= 100`
1. `0 <= bound <= 10^6`

# Solution
---
## Approach 1: Brute Force
**Intuition**

If $x^i > \text{bound}$, the sum $x^i + y^j$ can't be less than or equal to the bound. Similarly for $y^j$.

Thus, we only have to check for $0 \leq i, j \leq \log_x(\text{bound}) < 18$.

We can use a HashSet to store all the different values.

```python
class Solution(object): 
    def powerfulIntegers(self, x, y, bound):
        ans = set()
        # 2**18 > bound
        for i in xrange(18):
            for j in xrange(18):
                v = x**i + y**j
                if v <= bound:
                    ans.add(v)
        return list(ans)
```

**Complexity Analysis**

* Time Complexity: $O(\log^2{\text{bound}})$.

* Space Complexity: $O(\log^2{\text{bound}})$.

# Submissions
---
**Solution 1: (Brute Force)**
```
Runtime: 44 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        ans = set()
        # 2**21 > bound
        for i in range(21):
            for j in range(21):
                v = x**i + y**j
                if v <= bound:
                    ans.add(v)
        return list(ans)
```

**Solution 2: (Logartihmic Bounds)**
```
Runtime: 32 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        
        a = bound if x == 1 else int(log(bound, x))
        b = bound if y == 1 else int(log(bound, y))
        
        powerful_integers = set([])
        
        for i in range(a + 1):
            for j in range(b + 1):
                
                value = x**i + y**j
                
                if value <= bound:
                    powerful_integers.add(value)
                    
                if y == 1:
                    break
            
            if x == 1:
                break
                
        return list(powerful_integers)
```