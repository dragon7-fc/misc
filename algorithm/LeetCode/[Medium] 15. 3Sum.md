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
**Solution :**
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
