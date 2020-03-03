519. Random Flip Matrix

You are given the number of rows `n_rows` and number of columns `n_cols` of a 2D binary matrix where all values are initially 0. Write a function `flip` which chooses a 0 value uniformly at random, changes it to 1, and then returns the position `[row.id, col.id]` of that value. Also, write a function `reset` which sets all values back to 0. **Try to minimize the number of calls to system's Math.random()** and optimize the time and space complexity.

**Note:**

* `1 <= n_rows, n_cols <= 10000`
* `0 <= row.id < n_rows and 0 <= col.id < n_cols`
* flip will not be called when the matrix has no `0` values left.
* the total number of calls to flip and reset will not exceed `1000`.

**Example 1:**
```
Input: 
["Solution","flip","flip","flip","flip"]
[[2,3],[],[],[],[]]
Output: [null,[0,1],[1,2],[1,0],[1,1]]
```

**Example 2:**
```
Input: 
["Solution","flip","flip","reset","flip"]
[[1,2],[],[],[],[]]
Output: [null,[0,0],[0,1],null,[0,0]]
```

**Explanation of Input Syntax:**

The input is two lists: the subroutines called and their arguments. Solution's constructor has two arguments, n_rows and n_cols. flip and reset have no arguments. Arguments are always wrapped with a list, even if there aren't any.

# Submissions
---
**Solution 1: ()**

It is like a shuffle problem.  
First, any cell can be converted to a number in `[0, n_rows * n_cols)`, so we only need to generate the random number in that range without repetition.  
Second, recall the random shuffle algo, every time, we generate a number i in `[0, total)` and exchange the number at index i and total - 1, then total -= 1.  
However, if we use array to implement it, it will be MLE. So we can use map, the only difference is that if i is not in that map, we should return i. (self.d.get(i, i))

```
Runtime: 52 ms
Memory Usage: 13.1 MB
```
```python
class Solution:

    def __init__(self, n_rows: int, n_cols: int):
        self.total = n_rows * n_cols
        self.d = {}
        self.r, self.c = n_rows, n_cols
        
    def flip(self) -> List[int]:
        i = random.randint(0, self.total - 1)
        self.total -= 1
        res = self.d.get(i, i)
        # exchange the numbers at index self.total and m
        self.d[i], self.d[self.total] = self.d.get(self.total, self.total), res
        return (res // self.c, res % self.c)
    
    def reset(self) -> None:
        self.total = self.r * self.c


# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()
```