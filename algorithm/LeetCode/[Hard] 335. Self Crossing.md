335. Self Crossing

You are given an array x of n positive numbers. You start at point `(0,0)` and moves `x[0]` metres to the north, then `x[1]` metres to the west, `x[2]` metres to the south, `x[3]` metres to the east and so on. In other words, after each move your direction changes counter-clockwise.

Write a one-pass algorithm with `O(1)` extra space to determine, if your path crosses itself, or not.

 

**Example 1:**
```
┌───┐
│   │
└───┼──>
    │

Input: [2,1,1,2]
Output: true
```

**Example 2:**
```
┌──────┐
│      │
│
│
└────────────>

Input: [1,2,3,4]
Output: false
```

**Example 3:**
```
┌───┐
│   │
└───┼>

Input: [1,1,1,1]
Output: true
```

# Submissions
---
**Solution 1: (Math)**
```
Runtime: 28 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def isSelfCrossing(self, x: List[int]) -> bool:
        
              Case 1                  Case 2                  Case 3               
                1                       1                       1                  
       +----------------+      +----------------+      +----------------+          
       |                |      |                |      |                |          
       |                |      |                |      |                |          
     2 |                | 0  2 |                | 0  2 |                | 0        
       |                |      |                |      |                |    5     
       +--------------->|      |                |      |                | <----+   
                3       |      |                ^ 4    |                |      | 4 
                               |                |      |                       |   
                               +----------------+      +-----------------------+   
                                        3                       3 
        
        if not x  or len(x) <= 3:
            return False
        n = len(x)
        for i in range(3, n):
            
            # case 1: X(0) >= X(2), X(3) >= X(1)           
            if x[i-3] >= x[i-1] and x[i] >= x[i-2]:
                return True
            
            # case 2: X(1) == X(3), X(0) + X(4) >= X(2)
            if i >= 4 and x[i-3] == x[i-1] and (x[i-4] + x[i] >= x[i-2]):
                return True
            
            # case 3: X(3) >= X(1), X(2) >= X(4), X(0) + X(4) >= X(2), X(1) + X(5) >= X(3)
            if i >= 5 and x[i-2] >= x[i-4] and x[i-3] >= x[i-1] and (x[i-5] + x[i-1] >= x[i-3]) and (x[i-4] + x[i] >= x[i-2]):
                return True
            
        return False
```