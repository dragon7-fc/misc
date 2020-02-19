1040. Moving Stones Until Consecutive II

On an infinite number line, the position of the `i`-th stone is given by `stones[i]`.  Call a stone an endpoint stone if it has the smallest or largest position.

Each turn, you pick up an endpoint stone and move it to an unoccupied position so that it is no longer an endpoint stone.

In particular, if the stones are at say, `stones = [1,2,5]`, you cannot move the endpoint stone at position `5`, since moving it to any position (such as `0`, or `3`) will still keep that stone as an endpoint stone.

The game ends when you cannot make any more moves, ie. the stones are in consecutive positions.

When the game ends, what is the minimum and maximum number of moves that you could have made?  Return the answer as an length `2` array: `answer = [minimum_moves, maximum_moves]`

 

**Example 1:**
```
Input: [7,4,9]
Output: [1,2]
Explanation: 
We can move 4 -> 8 for one move to finish the game.
Or, we can move 9 -> 5, 4 -> 6 for two moves to finish the game.
```

**Example 2:**
```
Input: [6,5,4,3,10]
Output: [2,3]
We can move 3 -> 8 then 10 -> 7 to finish the game.
Or, we can move 3 -> 7, 4 -> 8, 5 -> 9 to finish the game.
Notice we cannot move 10 -> 2 to finish the game, because that would be an illegal move.
```

**Example 3:**
```
Input: [100,101,104,102,103]
Output: [0,0]
```

**Note:**

1. `3 <= stones.length <= 10^4`
1. `1 <= stones[i] <= 10^9`
1. `stones[i]` have distinct values.

# Submissions
---
**Solution 1: (Sliding Window)**
```
Runtime: 136 ms
Memory Usage: 14.8 MB
```
```python
class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        A = sorted(stones)
        n = len(stones)
        
        # either keep moving the stone at right endpoint to the left interval between A[0] ... A[n - 2]
        # basically each empty spot can consume 1 move, so total moves = total # of empty spots inside A[0] .. A[n - 2]
        # A[n - 2] - A[0] + 1 -    2           - (n - 3)
        # -------------------      -           ---------
        # interval length     A[0], A[n-2]    stones already inside
        #
        # similar idea for keeping moving the stone at left endpoint to the right interval between A[1] ... A[n - 1]
        # total # of empty spots = A[n - 1] - stone[1] + 1 - 2 - (n - 3)
        # we take the maximum of these two moves
        max_moves = max(A[-1] - A[1] + 1 - 2 - (n - 3), A[-2] - A[0] + 1 - 2 - (n - 3))
        
        # for min moves, use a sliding window
        # idea: https://leetcode.com/problems/moving-stones-until-consecutive-ii/discuss/286886/No-code-just-chinese-explanation
        # https://leetcode.com/problems/moving-stones-until-consecutive-ii/discuss/289357/c++-with-picture
        l, min_moves = 0, n
        
        for r in range(n):
            # in case current window can hold more than n stones, shrink the window
            while A[r] - A[l] + 1 > n:
                l += 1
            
            # a special case: A[l] ... A[r] currently is consecutive and there is only one stone (endpoint) outside
            # in this case we only need 2 move
            if A[r] - A[l] == r - l and r - l + 1 == n - 1:
                min_moves = min(min_moves, 2)
            else:
                # refer: leetcode.com/problems/moving-stones-until-consecutive-ii/discuss/286886/No-code-just-chinese-explanation/275066
                min_moves = min(min_moves, n - (r - l + 1))
        
        return [min_moves, max_moves]
```