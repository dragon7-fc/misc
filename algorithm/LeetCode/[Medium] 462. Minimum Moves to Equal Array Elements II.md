462. Minimum Moves to Equal Array Elements II

Given a **non-empty** integer array, find the minimum number of moves required to make all array elements equal, where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

You may assume the array's length is at most 10,000.

**Example:**
```
Input:
[1,2,3]

Output:
2

Explanation:
Only two moves are needed (remember each move increments or decrements one element):

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
```

# Submissions
---
**Solution 1:**
```
Runtime: 88 ms
Memory Usage: 14.1 MB
```
```python
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        mid = nums[len(nums)//2]       
        return sum(abs(n - mid) for n in nums)
```