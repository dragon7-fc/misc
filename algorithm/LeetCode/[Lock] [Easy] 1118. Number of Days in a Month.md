1118. Number of Days in a Month

Given a year `Y` and a month `M`, return how many days there are in that month.

 

**Example 1:**
```
Input: Y = 1992, M = 7
Output: 31
```

**Example 2:**
```
Input: Y = 2000, M = 2
Output: 29
```

**Example 3:**
```
Input: Y = 1900, M = 2
Output: 28
```

**Note:**

* `1583 <= Y <= 2100`
* `1 <= M <= 12`

# Submissions
---
**Solution 1: (Data and Time)**
```
Runtime: 28 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def numberOfDays(self, Y: int, M: int) -> int:
        month =(31,28,31,30,31,30,31,31,30,31,30,31)
        if Y%4 ==0 and M ==2:
            if Y%100 == 0 and Y%400 !=0:
                return 28
            else:
                return 29
        else:
            return month[M-1]
```