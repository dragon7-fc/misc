1049. Last Stone Weight II

We have a collection of rocks, each rock has a positive integer weight.

Each turn, we choose any two rocks and smash them together.  Suppose the stones have weights `x` and `y` with `x <= y`.  The result of this smash is:

* If `x == y`, both stones are totally destroyed;
* If `x != y`, the stone of weight `x` is totally destroyed, and the stone of weight `y` has new weight `y-x`.

At the end, there is at most 1 stone left.  Return the smallest possible weight of this stone (the weight is `0` if there are no stones left.)

 

**Example 1:**

```
Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We can combine 2 and 4 to get 2 so the array converts to [2,7,1,8,1] then,
we can combine 7 and 8 to get 1 so the array converts to [2,1,1,1] then,
we can combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we can combine 1 and 1 to get 0 so the array converts to [1] then that's the optimal value.
```

**Note:**

1. `1 <= stones.length <= 30`
1. `1 <= stones[i] <= 100`

# Submissions
---
**Solution 1: (0-1 Knapsack)**

The value of the final rock would be a summation of all values with +/- signs. As we are trying to minimize the size of the final rock, we need to find a partition of numbers in the array into two subsets, which have the least amount of differenc in their summations.
We can reformulate this as a 0-1 Knapsack, i.e. collecting some rocks, where the weights of the rocks is maximized and their total weight does not exceed half of the total weight of the rocks.

```
Runtime: 52 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        
        Max_weight = int(total/2)
        
        current = (Max_weight+1)*[0]
        
        for v in stones:
            for w in range(Max_weight, -1, -1):
                if w-v >= 0:
                    current[w] = max(v + current[w-v], current[w])
            
           
        return total-2*current[-1]
```