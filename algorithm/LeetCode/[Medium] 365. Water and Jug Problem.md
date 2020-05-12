365. Water and Jug Problem

You are given two jugs with capacities `x` and `y` litres. There is an infinite amount of water supply available. You need to determine whether it is possible to measure exactly `z` litres using these two jugs.

If `z` liters of water is measurable, you must have `z` liters of water contained within one or both buckets by the end.

Operations allowed:

* Fill any of the jugs completely with water.
* Empty any of the jugs.
* Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.

**Example 1:** (From the famous "Die Hard" example)
```
Input: x = 3, y = 5, z = 4
Output: True
```

**Example 2:**
```
Input: x = 2, y = 6, z = 5
Output: False
```

# Submissions
---
**Solution 1: (Math)**

I see a lot of solutions using gcd, but no one explains why it works. So I do some research and find out that the problem is just like a implementation of a math theory named "Bezout's Lemma". I copy the definition below, and you can find the proof of it on google if you are interested in it.

**Bezout's Lemma states that if x and y are nonzero integers and g = gcd(x,y), then there exist integers a and b such that ax+by=g. In other words, there exists a linear combination of x and y equal to g.**

**Furthermore, g is the smallest positive integer that can be expressed in this form, i.e. g = min{ax+by | a, b in Z, ax+by > 0}.**

```
Runtime: 24 ms
Memory Usage: 12.6 MB
```
```python
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        def gcd(a,b):
            if a%b == 0:
                return b
            else :
                return gcd(b,a%b)
        
        if z == 0:
            return True
        if x+y<z:
            return  False
        return z % gcd(x, y) == 0        
```

**Solution 2: (Math)**
```
Runtime: 28 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if z == 0:
            return True
        if x+y < z:
            return  False
        return z % math.gcd(x, y) == 0
```