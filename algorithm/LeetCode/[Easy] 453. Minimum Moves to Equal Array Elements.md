453. Minimum Moves to Equal Array Elements

Given a **non-empty** integer array of size `n`, find the minimum number of moves required to make all array elements equal, where a move is incrementing `n - 1` elements by `1`.

**Example:**
```
Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
```

# Submissions
---
**Solution 1:**

Increase n-1 numbers by 1 is equal to decrease 1 number by 1. Just need to decrease all the numbers to the smallest one

```
Runtime: 264 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums)-len(nums)*min(nums)
```