528. Random Pick with Weight

Given an array w of positive integers, where `w[i]` describes the weight of index `i`, write a function `pickIndex` which randomly picks an index in proportion to its weight.

**Note:**

* `1 <= w.length <= 10000`
* `1 <= w[i] <= 10^5`
* `pickIndex` will be called at most `10000` times.

**Example 1:**
```
Input: 
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]
```

**Example 2:**
```
Input: 
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]
```

**Explanation of Input Syntax:**

The input is two lists: the subroutines called and their arguments. `Solution`'s constructor has one argument, the array `w`. `pickIndex` has no arguments. Arguments are always wrapped with a list, even if there aren't any.

# Submissions
---
**Solution 1: (Random)**

* Sum all left weights for each index.
* Then generate a random value between 0 and len(w) to see in which section it falls.
* To do that, we can perform a binarysearch.

```
Runtime: 236 ms
Memory Usage: 17.4 MB
```
```python
class Solution:

    def __init__(self, w: List[int]):
        for i in range(1, len(w)):
            w[i] += w[i-1]
        self.w = w  # prefix sum

    def pickIndex(self) -> int:
        ranint = random.randint(1, self.w[-1])
        return bisect.bisect_left(self.w, ranint)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
```