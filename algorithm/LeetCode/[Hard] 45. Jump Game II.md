45. Jump Game II

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

**Example:**
```
Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

**Note:**

* You can assume that you can always reach the last index.

# Submissions
---
**Solution 1:**

There are 2 basic ideas:

1. If we look at the index `i`, the longest jump from here would reach out index `i + nums[i]`. For example, given `[2,3,1,1,4]`, from element 0 we can get to `0+2=2`, from element `1` to `1+3=4`, from `2` to `2+1=3`, from `3` to `3+1=4`, from `4` to `4+4=8`
1. Now let's use two pointers. First one moves from `0` and gets increased by `1` on every iteration. The second pointer would would tell the highest index we could reach at the previous step.

Now we just look at every element within that sliding window and see if we can push the high pointer up. And if the high pointer reaches the end of the array, we return number of jumps.

```
Runtime: 104 ms
Memory Usage: 14.8 MB
```
```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps, high = 0, 0
        
        # since we will be using the index of the last element, let's just store it in max_n
        max_n = len(nums)-1
        
        for i in range(0, max_n):
            jumps += 1
            
            # we are looking at the elements from the low pointer i to either high pointer or the end of the list
            for j in range(i,min(high + 1, max_n)):
                
                # can we go higher from this element?
                high = max(high,j + nums[j])

                # can we reach the end?
                if high >= max_n: 
                    return(jumps) 
        return(0)
```

**Solution 2:**
```
Runtime: 96 ms
Memory Usage: 14.9 MB
```
```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        tmp = [i + v for i, v in enumerate(nums)]
        left = right = res = 0
        while right < len(nums)-1:
            left, right, res = right, max(tmp[left:right+1]), res + 1
        return res
```