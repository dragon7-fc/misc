457. Circular Array Loop

You are given a **circular** array `nums` of positive and negative integers. If a number k at an index is positive, then move forward k steps. Conversely, if it's negative (-k), move backward k steps. Since the array is circular, you may assume that the last element's next element is the first element, and the first element's previous element is the last element.

Determine if there is a loop (or a cycle) in `nums`. A cycle must start and end at the same index and the cycle's length > 1. Furthermore, movements in a cycle must all follow a single direction. In other words, a cycle must not consist of both forward and backward movements.

**Example 1:**
```
Input: [2,-1,1,2,2]
Output: true
Explanation: There is a cycle, from index 0 -> 2 -> 3 -> 0. The cycle's length is 3.
```
**Example 2:**
```
Input: [-1,2]
Output: false
Explanation: The movement from index 1 -> 1 -> 1 ... is not a cycle, because the cycle's length is 1. By definition the cycle's length must be greater than 1.
```
**Example 3:**
```
Input: [-2,1,-1,-2,-2]
Output: false
Explanation: The movement from index 1 -> 2 -> 1 -> ... is not a cycle, because movement from index 1 -> 2 is a forward movement, but movement from index 2 -> 1 is a backward movement. All movements in a cycle must follow a single direction.
``` 

**Note:**

1. `-1000 ≤ nums[i] ≤ 1000
1. nums[i] ≠ 0
1. 1 ≤ nums.length ≤ 5000
 

**Follow up:**

Could you solve it in $O(n)$ time complexity and $O(1)$ extra space complexity?

# Submissions
---
**Solution 1**
```
Runtime: 412 ms
Memory Usage: 14.2 MB
```
```python
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        N = len(nums)
        forward, backward = [], []
        
        for i in range(N):
            if nums[i] > 0:
                forward.append(i)
            else:
                backward.append(i)
                
        for i in forward:
            seen = set([i])
            nex = (i + nums[i]) % N
            while nums[nex] > 0 and nex not in seen:    
                seen.add(nex)
                nex = (nex + nums[nex]) % N
            
            if nums[nex] < 0:
                continue
            if nex in seen and (nex + nums[nex]) % N != nex:
                return True
            
        for i in backward:
            seen = set([i])
            nex = (i + nums[i]) % N
            while nums[nex] < 0 and nex not in seen:    
                seen.add(nex)
                nex = (nex + nums[nex]) % N
            
            if nums[nex] > 0:
                continue
            if nex in seen and (nex + nums[nex]) % N != nex:
                return True
            
        return False
```

**Solution 2:**
```
Runtime: 40 ms
Memory Usage: 14.1 MB
```
```python
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        searched = set()
        for idx, step in enumerate(nums):
            if idx in searched:
                continue
            pos = True if step > 0 else False
            cir = set()
            curIdx = idx
            curStep = step
            while curStep > 0 and pos or curStep < 0 and not pos:
                if curIdx in cir:
                    if len(cir) > 1 and abs(curStep) != len(nums):
                        return True
                    else:
                        break
                else:
                    cir.add(curIdx)
                    curIdx = (curIdx + curStep) % len(nums) 
                    curStep = nums[curIdx]
                    searched.add(curIdx)
        return False
```
