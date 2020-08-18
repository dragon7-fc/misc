276. Paint Fence

There is a fence with `n` posts, each post can be painted with one of the `k` colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.

**Note:**

`n` and `k` are non-negative integers.

**Example:**
```
Input: n = 3, k = 2
Output: 6
Explanation: Take c1 as color 1, c2 as color 2. All possible ways are:

            post1  post2  post3      
 -----      -----  -----  -----       
   1         c1     c1     c2 
   2         c1     c2     c1 
   3         c1     c2     c2 
   4         c2     c1     c1  
   5         c2     c1     c2
   6         c2     c2     c1
```

# Submissions
---
**Solution 1: (DP Bottom-Up)**

It's not too hard to figure out the pattern if you play with it.

Suppose k == 3, let's say the 3 colors are a, b, c.

* If n == 1, then the result is a b c.
* If n == 2, then the result is ab ac ba bc ca cb aa bb cc.

* If n > 2, then the result can be derived by appending 2 posts with the same color that is different from the last one to the result of n-2 and appending 1 post with a color that's different from the last one to the result of n-1.

For example, if n == 3, the result is:

abb acc baa bcc caa cbb

and

aba abc aca acb bab bac bca bcb cab cac cba cbc aab aac bba bbc cca ccb

```
Runtime: 28 ms
Memory Usage: 13.6 MB
```
```python
class Solution:
    def numWays(self, n: int, k: int) -> int:
        arr = [0, k, k*k]
        while len(arr) <= n:
            arr.append(arr[-2]*(k-1) + arr[-1]*(k-1))
        return arr[n]
```

**Solution 2: (DP Bottom-Up 1D)**
```
Runtime: 28 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0: return 0
        same, diff = 0, k
        for i in range(1, n):
            same, diff = diff, (same + diff) * (k-1)
        return same + diff
```

**Solution 3: (DP Top-Down)**
```
Runtime: 32 ms
Memory Usage: 13.7 MB
```
```python
class Solution:
    def numWays(self, n: int, k: int) -> int:
        def find(i):
            if i == 0: return 0, k
            
            same, diff = find(i-1)            
            return diff, (same + diff) * (k-1)
        
        if n == 0: return 0
        same, diff = find(n-1)
        return same + diff
```