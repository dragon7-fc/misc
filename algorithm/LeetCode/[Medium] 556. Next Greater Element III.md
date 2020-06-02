556. Next Greater Element III

Given a positive **32-bit** integer **n**, you need to find the smallest **32-bit** integer which has exactly the same digits existing in the integer **n** and is greater in value than **n**. If no such positive **32-bit** integer exists, you need to return `-1`.

**Example 1:**
```
Input: 12
Output: 21
```

**Example 2:**
```
Input: 21
Output: -1
```

# Submissions
---
**Solution 1: (String)**
```
Runtime: 20 ms
Memory Usage: 12.6 MB
```
```python
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        if n == 0:
            return -1

        nums = list(str(n))
        ln = len(nums)
        i = ln-1
        # find the first non increasing sequence from the right
        while i > 0:
            if nums[i-1] < nums[i]:
                break
            i -= 1

        #this is the number to be replaced as it is smaller
        # than any other element on the right of it
        i -= 1  

        if i < 0:
            return -1

        # look for the min largest number greater than nums[i]
        # and swap it and sort the rest
        temp = ln-1
        while temp > i:
            if nums[i] < nums[temp]:
                break
            temp -= 1

        nums[i], nums[temp] = nums[temp], nums[i]

        #sort rest of the stuff from [i+1, ln-1]
        nums[i+1:] = sorted(nums[i+1:]) 
        res = int("".join(nums))
        return  res if (res > n and res <= (2**31-1)) else -1
```