710. Random Pick with Blacklist

Given a blacklist `B` containing unique integers from `[0, N)`, write a function to return a uniform random integer from `[0, N)` which is **NOT** in `B`.

Optimize it such that it minimizes the call to system’s `Math.random()`.

**Note:**

* `1 <= N <= 1000000000`
* `0 <= B.length < min(100000, N)`
* `[0, N)` does NOT include N. See interval notation.

**Example 1:**
```
Input: 
["Solution","pick","pick","pick"]
[[1,[]],[],[],[]]
Output: [null,0,0,0]
```

**Example 2:**
```
Input: 
["Solution","pick","pick","pick"]
[[2,[]],[],[],[]]
Output: [null,1,1,1]
```

**Example 3:**
```
Input: 
["Solution","pick","pick","pick"]
[[3,[1]],[],[],[]]
Output: [null,0,0,2]
```

**Example 4:**
```
Input: 
["Solution","pick","pick","pick"]
[[4,[2]],[],[],[]]
Output: [null,1,3,1]
```

**Explanation of Input Syntax:**

The input is two lists: the subroutines called and their arguments. Solution's constructor has two arguments, `N` and the blacklist `B`. `pick` has no arguments. Arguments are always wrapped with a list, even if there aren't any.

# Submissions
---
**Solution 1: (Random)**

Remap blacklist to last index
```
Runtime: 412 ms
Memory Usage: 25.2 MB
```
```python
class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        self.N = N
        self.translate_table = {}
        self.blacklist = set(blacklist)
        
        swap_index = N-1
        for b in self.blacklist:
            if b < N-len(self.blacklist):
                while swap_index in self.blacklist:
                    swap_index -= 1
                self.translate_table[b] = swap_index
                swap_index -= 1

    def pick(self) -> int:
        rand_index = random.randint(0, self.N-len(self.blacklist)-1)
        return self.translate_table.get(rand_index, rand_index)

# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()
```