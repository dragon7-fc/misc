1820. Maximum Number of Accepted Invitations

There are `m` boys and `n` girls in a class attending an upcoming party.

You are given an `m x n` integer matrix `grid`, where `grid[i][j]` equals `0` or `1`. If `grid[i][j] == 1`, then that means the `i`th boy can invite the `j`th girl to the party. A boy can invite at most **one girl**, and a girl can accept at most **one invitation** from a boy.

Return the **maximum** possible number of accepted invitations.

 

**Example 1:**
```
Input: grid = [[1,1,1],
               [1,0,1],
               [0,0,1]]
Output: 3
Explanation: The invitations are sent as follows:
- The 1st boy invites the 2nd girl.
- The 2nd boy invites the 1st girl.
- The 3rd boy invites the 3rd girl.
```

**Example 2:**
```
Input: grid = [[1,0,1,0],
               [1,0,0,0],
               [0,0,1,0],
               [1,1,1,0]]
Output: 3
Explanation: The invitations are sent as follows:
-The 1st boy invites the 3rd girl.
-The 2nd boy invites the 1st girl.
-The 3rd boy invites no one.
-The 4th boy invites the 2nd girl.
```

**Constraints:**

* `grid.length == m`
* `grid[i].length == n`
* `1 <= m, n <= 200`
* `grid[i][j]` is either `0` or `1`.

# Submissions
---
**Solution 1: (maximum bipartite matching)**
```
Runtime: 1460 ms
Memory Usage: 16.1 MB
```
```python
class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        match = [-1] * n
        
        def fn(i): 
            """Look up match for ith boy."""
            for j in range(n):
                if grid[i][j] and not seen[j]: 
                    seen[j] = True
                    if match[j] == -1 or fn(match[j]): 
                        match[j] = i
                        return True 
            return False 
        
        for i in range(m):
            seen = [False] * n
            if fn(i): ans += 1
        return ans 
```
