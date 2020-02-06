260. Single Number III

Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

**Example:**
```
Input:  [1,2,1,3,2,5]
Output: [3,5]
```

**Note:**

* The order of the result is not important. So in the above example, [5, 3] is also correct.
* Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

# Submissions
---
**Solution 1: (Set)**
```
Runtime: 56 ms
Memory Usage: 14.5 MB
```
```python
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans = set()
        for x in nums:
            if x in ans:
                ans.remove(x)
            else:
                ans.add(x)
        return list(ans)
```

**Solution 2: (Bit Manipulation)**
```
Runtime: 60 ms
Memory Usage: 14.6 MB
```
```python
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        m = 0
        for i in nums: m ^= i
        #get masking, the "last set bit" (right most 1 bit)
        m &= -m  #just remember it, I cannot explain
        rst = [0, 0]
        for i in nums:
            #the masking help separate the result two unique num into different group
            #because they differs in the masking bit
            if m & i: rst[0] ^= i
            else: rst[1] ^= i
        return rst
```