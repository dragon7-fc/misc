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
**Solution 1: (Random)**

nspired by @akaenki and Durstenfeld version Fisher–Yates shuffle  
The baisc idea: flatten matrix to 1-d array; each time we filp a element, swap it with end of current array tail, and decrease the array size by 1; Therefore, we won't touch fliped elements and keep the flip uniformly  
Note: elements in the valid range of index array are untouched indexes; and each element is not related to indexes of index array
```
example: [[0, 0], [0, 0]]
step 1: flatten it to 1-d index array [0, 1, 2, 3|]; remain = 4
step 2: remain = 3; get a random index, say index = 0; 0 did not swap with other index; update swap[0] = 3 (current tail);
        index array [3, 1, 2,| 0] (index before | means untouched, afterwards means flipped); return [0 // 2, 0 % 2]
        the original matrix will be [[1, 0], [0, 0]]
step 3: remain = 2; get a random index, say index = 0 as before; 0 swapped with 3, thus actual index = 3; update swap[0] = 2 (current tail), which means swap elemnets of index 0 with element of index 2
        index array [2, 1,| 3, 0] (index before | means untouched, afterwards means flipped); return [3 // 2, 3 % 2]
        the original matrix will be [[1, 0], [0, 1]]
step 4: remain = 1; get a random index, say index = 0 as before; 0 swapped with 2, thus actual index = 2; update swap[0] = 1 (current tail), which means swap elemnets of index 0 with element of index 1
        index array [1,| 2, 3, 0] (index before | means untouched, afterwards means flipped); return [2 // 2, 2 % 2]
        the original matrix will be [[1, 0], [1, 1]]
step 5: remain = 0; get a random index, say index = 0 as before; 0 swapped with 1, thus actual index = 1; update swap[0] = 0 (current tail), which means swap elemnets of index 0 with element of index 0
        index array [|1, 2, 3, 0] (index before | means untouched, afterwards means flipped); return [1 // 2, 1 % 2]
        the original matrix will be [[1, 1], [1, 1]]
```

```
Runtime: 60 ms
Memory Usage: 13 MB
```
```python
class Solution:

    def __init__(self, n_rows: int, n_cols: int):
        self.rows, self.cols = n_rows, n_cols
        self.remain = self.rows*self.cols  # the number of remaining 0
        self.swap = {}  # {original index : new index}
        
    def flip(self) -> List[int]:
        # after flipping, there must be a 0 to be changed to 1
        self.remain -= 1
        index = random.randint(0, self.remain)  # return a random index from [0, self.remain], valid range
        actualIndex = index  # actual index based on matrix
        # if there is a swap operation happened at this index, find the exact index element on this index now
        if index in self.swap:
            actualIndex = self.swap[index]
        tail = self.remain
        # if there is a swap operation happened at this tail index, find the exact index element on this tail index now
        if tail in self.swap: 
            tail = self.swap[tail]
        self.swap[index] = tail  # swap this index with actual tail index
        return [actualIndex // self.cols, actualIndex % self.cols]

    def reset(self) -> None:
        self.swap = {}
        self.remain = self.rows*self.cols


# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()
```

**Solution 2: (Random)**
```
Runtime: 18 ms
Memory: 19.10 MB
```
```c++
class Solution {
    unordered_map<int, int> m;
    int r, c, sz;
public:
    Solution(int m, int n) {
        r = m;
        c = n;
        sz = r*c;
    }
    
    vector<int> flip() {
        int i = rand()%(sz);
        sz -= 1;
        int ni = i;
        if (m.count(ni)) {
            ni = m[i];
        }
        int tail = sz;
        if (m.count(tail)) {
            tail = m[tail];
        }
        m[i] = tail;
        return {ni/c, ni%c};
    }
    
    void reset() {
        m.clear();
        sz = r*c;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(m, n);
 * vector<int> param_1 = obj->flip();
 * obj->reset();
 */
```
