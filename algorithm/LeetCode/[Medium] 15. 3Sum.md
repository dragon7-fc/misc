15. 3Sum

Given an array `nums` of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

**Example:**
```
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
```

# Submissions
---
**Solution : (Hash Table)**
```
Runtime: 668 ms
Memory Usage: 24.2 MB
```
```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dic = collections.defaultdict(int)
        soln = []

        #creates a dictionary and counts the array
        for x in nums:
            dic[x] += 1
        
        #gets a list of keys and the length
        keys = list(dic.keys())
        length_k = len(keys)
        
        #for each key
        for i in range(length_k):
            x = keys[i]
            
            # case: [x, x, -2*x]
            #if the negative sum exists, add it to the solution
            if dic[x]>1:
                if -2*x in dic:
                    soln.append([x, x,-2*x])
                    
            # case: [x, y, -(x+y)
            for j in range(i+1,length_k):
                y = keys[j]
                #ensures we dont double count
                if -(x+y) in dic and -(x+y) not in [x,y]:
                    soln.append([x, y, -(x+y)])
        
        #special case of 0
        if 0 in dic:
            if dic[0] == 2:
                soln.remove([0,0,0])
        
        #returns unique solution sets
        soln=[list(x) for x in set(tuple(sorted(x)) for x in soln)]
        
        return soln
```

**Solution 2: (Two Pointers)**
```
Runtime: 728 ms
Memory Usage: 17.3 MB
```
```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        
        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, n - 1
            while j < k:                
                cur = nums[i] + nums[j] + nums[k] 
                if cur < 0:
                    j += 1
                elif cur > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    while j + 1 < k and nums[j] == nums[j + 1]:
                        j += 1
                    while k - 1 > j and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
        return res
```

**Solution 3: (Binary Search)**
```
Runtime: 216 ms
Memory Usage: 17.9 MB
```
```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        counter = collections.Counter(nums)
        nums = sorted(counter)
        ret = []
        for i, num in enumerate(nums):
            # case i. three numbers are the same - [0,0,0]
            if num==0:
                if counter[num] > 2:
                    ret.append([0, 0, 0])
            # case ii. two numbers are the same
            elif counter[num] > 1 and -2 * num in counter:
                ret.append([num, num, -2 * num])
            # case iii. not any of the three numbers are the same
            if num < 0:
                opposite = -num
                left = bisect_left(nums, opposite - nums[-1], i + 1)
                right = bisect_right(nums, opposite / 2, left)
                for a in nums[left:right]:
                    b = opposite - a
                    if b in counter and a!=b:
                        ret.append([num, a, b])
        return ret
```