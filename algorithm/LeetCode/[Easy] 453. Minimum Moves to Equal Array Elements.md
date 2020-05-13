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
**Solution 1: (Math)**

Increase n-1 numbers by 1 is equal to decrease 1 number by 1. Just need to decrease all the numbers to the smallest one

Lets take an example [ 0 , 5 , -3 , 7 ]
initally moves=0
Note: We can only increment values (all values except 1)
So we know that at the all numbers will be equal to or more than 7 (max in this list)

Step 1:
We find the max number ie 7 and the min number -3
The diiference between them is 7 -(-3) = 10
So we increment all the numbers except 7 by 10
new array = [10 , 15 , 7 , 7 ]

Step 2:
Array isnt equal
Max now = 15 , min =7 , difference = 8
So we incrment all numbers except 15 by 8
new array = [18 , 15 , 15, 15 ]

Step 3:
Array isnt equal
Max now = 18 , min =15 , difference = 3
So we incrment all numbers except 18 by 3
new array = [18 , 18 , 18 , 18 ]
We have increment by 10 (step 1) +8 (step 2) +3 (step 3) = 21 times in total

If we observe carefully that the lowest element always got incremented

if we subract the lowest element from every element in from original array we get
[ 3 , 8 , 0 , 10 ] -> sum =21 ( Same as what we get following Steps )

```
Runtime: 264 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums)-len(nums)*min(nums)
```